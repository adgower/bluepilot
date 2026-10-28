import os
from pathlib import Path
"""Streaming route health/cohort and exact producer-sequence fault audit; saved logs only."""
from pathlib import Path
import sys, json, collections, bisect, hashlib, datetime
from zoneinfo import ZoneInfo
R = Path(str(Path(os.environ['OPENPILOT_ROOT'])))
sys.path[:0] = [str(R / 'opendbc_repo'), str(R / 'msgq_repo'), str(R)]
from openpilot.tools.lib.logreader import LogReader
P = Path(__file__).resolve().parent
receipt = json.loads((P / 'acquisition-provenance.json').read_text())
B = Path(receipt['private_backup'])
manifest = json.loads((P / 'input-manifest.json').read_text())
results = []
for drive in sorted({x['drive'] for x in manifest}):
    counts = collections.Counter()
    invalid = collections.Counter()
    starts = []
    cs = []
    cc = []
    co = []
    dm = []
    ps = []
    alerts = []
    cc_lookup = {}
    faults = []
    posebad = []
    model = []
    health = {}
    time0 = None
    time1 = None
    wall_offset = None
    last_fault = False
    last_alert = ''
    versions = collections.Counter()
    for entry in sorted([x for x in manifest if x['drive'] == drive], key=lambda x: x['segment']):
        path = B / 'recordings' / drive / f"segment-{entry['segment']:03d}" / 'rlog.zst'
        with path.open('rb') as f:
            assert hashlib.file_digest(f, 'sha256').hexdigest() == entry['sha256']
        for e in LogReader(str(path)):
            k = e.which()
            t = e.logMonoTime / 1000000000.0
            counts[k] += 1
            if not e.valid:
                invalid[k] += 1
            time0 = t if time0 is None else min(time0, t)
            time1 = t if time1 is None else max(time1, t)
            if k == 'initData':
                x = e.initData
                starts.append({'segment': entry['segment'], 'parent': str(x.gitCommit), 'dirty': bool(x.dirty)})
                if wall_offset is None and x.wallTimeNanos:
                    wall_offset = x.wallTimeNanos / 1000000000.0 - t
            elif k == 'clocks' and wall_offset is None and e.clocks.wallTimeNanos:
                wall_offset = e.clocks.wallTimeNanos / 1000000000.0 - t
            elif k == 'carState':
                x = e.carState
                cs.append((t, bool(e.valid), float(x.vEgo), float(x.aEgo), bool(x.brakePressed), bool(x.gasPressed), bool(x.steeringPressed), bool(x.canValid), str(x.gearShifter), bool(x.canTimeout), bool(x.steerFaultTemporary), bool(x.steerFaultPermanent), bool(x.accFaulted)))
            elif k == 'carControl':
                x = e.carControl
                q = x.navigatorLongitudinal.to_dict()
                row = (t, bool(e.valid), bool(x.enabled), bool(x.latActive), bool(x.longActive), float(x.actuators.accel), q)
                cc.append(row)
                cc_lookup[int(q.get('epoch', 0)), int(q.get('sequence', 0))] = row
                versions[int(q.get('allocatorVersion', 0))] += 1
                if x.longActive and (not q.get('poseValid', False)):
                    posebad.append({'t': t, 'producer': q})
            elif k == 'carOutput':
                q = e.carOutput.actuatorsOutput.navigatorLongitudinal.to_dict()
                co.append((t, bool(e.valid), q))
                fault = bool(q.get('fault', False))
                if fault and (not last_fault or (faults and t - faults[-1]['last_fault_mono'] > 0.2)):
                    faults.append({'mono': t, 'last_fault_mono': t, 'output_valid': bool(e.valid), 'feedback': q, 'fault_samples': 1})
                elif fault and faults:
                    faults[-1]['last_fault_mono'] = t
                    faults[-1]['fault_samples'] += 1
                last_fault = fault
            elif k == 'selfdriveState':
                x = e.selfdriveState
                sig = (str(x.state), str(x.alertType), str(x.alertText1), str(x.alertText2))
                if sig != last_alert:
                    alerts.append({'mono': t, 'event_valid': bool(e.valid), 'state': sig[0], 'alert_type': sig[1], 'text1': sig[2], 'text2': sig[3]})
                    last_alert = sig
            elif k == 'deviceMotion':
                x = e.deviceMotion
                dm.append((t, bool(e.valid), int(x.timestamp), bool(x.orientationNED.valid), bool(x.inputsOK), bool(x.sensorsOK), bool(x.posenetOK)))
            elif k == 'pandaStates':
                ps.append((t, bool(e.valid), [{key: value for key, value in x.to_dict().items() if key in ['controlsAllowed', 'safetyTxBlocked', 'safetyRxInvalid', 'safetyRxChecksInvalid', 'heartbeatLost', 'faults', 'spiErrorCount', 'ignitionLine', 'ignitionCan', 'safetyModel', 'safetyParam']} for x in e.pandaStates]))
            elif k == 'modelV2':
                model.append((t, bool(e.valid), float(e.modelV2.frameDropPerc), bool(e.modelV2.big)))
            elif k == 'deviceState':
                d = e.deviceState.to_dict()
                for name in ['thermalStatus', 'freeSpacePercent', 'memoryUsagePercent', 'cpuTempC', 'gpuTempC']:
                    v = d.get(name)
                    if isinstance(v, list):
                        v = max(v) if v else None
                    if isinstance(v, (int, float)):
                        prior = health.setdefault(name, [v, v])
                        prior[0] = min(prior[0], v)
                        prior[1] = max(prior[1], v)
        print(drive, 'segment', entry['segment'], flush=True)
    cs.sort()
    cc.sort(key=lambda x: x[0])
    co.sort(key=lambda x: x[0])
    dm.sort()
    ps.sort(key=lambda x: x[0])
    alerts.sort(key=lambda x: x['mono'])
    times = [x[0] for x in cs]

    def state(t):
        j = bisect.bisect_right(times, t) - 1
        if j < 0:
            return None
        r = cs[j]
        return {'age_s': t - r[0], 'event_valid': r[1], 'mph': r[2] / 0.44704, 'aEgo': r[3], 'brakePressed': r[4], 'gasPressed': r[5], 'steeringPressed': r[6], 'canValid': r[7], 'gear': r[8], 'canTimeout': r[9], 'steerFaultTemporary': r[10], 'steerFaultPermanent': r[11], 'accFaulted': r[12]}

    def local(t):
        return datetime.datetime.fromtimestamp(t + wall_offset, ZoneInfo('America/Chicago')).isoformat() if wall_offset else None
    mismatch = [x for x in alerts if 'controlsMismatch' in x['alert_type']]
    for f in faults:
        t = f['mono']
        q = f['feedback']
        key = (int(q.get('epoch', 0)), int(q.get('sequence', 0)))
        producer = cc_lookup.get(key)
        f.update(relative_s=t - time0, local_time=local(t), state=state(t), matched_producer=None)
        if producer:
            request = producer[6]
            f['matched_producer'] = {'publication_mono': producer[0], 'publication_minus_fault_ms': (producer[0] - t) * 1000, 'event_valid': producer[1], 'enabled': producer[2], 'latActive': producer[3], 'longActive': producer[4], 'requested': producer[5], 'metadata': request, 'pose_minus_producer_ms': (request.get('poseMonoTime', 0) - request.get('producerMonoTime', 0)) / 1000000.0, 'pose_age_at_feedback_ms': (q.get('producerMonoTime', 0) - request.get('poseMonoTime', 0)) / 1000000.0}
            target = int(request.get('poseMonoTime', 0))
            f['exact_pose_sources'] = [{'publication_mono': r[0], 'event_valid': r[1], 'source_ns': r[2], 'orientation_valid': r[3], 'inputsOK': r[4], 'sensorsOK': r[5], 'posenetOK': r[6]} for r in dm if r[2] == target and abs(r[0] - t) < 1]
        f['panda_context'] = [{'relative_to_fault_s': r[0] - t, 'event_valid': r[1], 'boards': r[2]} for r in ps if t - 0.3 <= r[0] <= t + 0.5]
        f['alert_context'] = [dict(r, relative_to_fault_s=r['mono'] - t) for r in alerts if t - 1 <= r['mono'] <= t + 2]
        f['nearby_controls'] = [{'relative_to_fault_s': r[0] - t, 'event_valid': r[1], 'enabled': r[2], 'latActive': r[3], 'longActive': r[4], 'raw': r[5], 'metadata': r[6]} for r in cc if t - 0.15 <= r[0] <= t + 0.15]
    for m in mismatch:
        m.update(relative_s=m['mono'] - time0, local_time=local(m['mono']), state=state(m['mono']))
    active = {k: 0.0 for k in ['lateral_s', 'longitudinal_s', 'longitudinal_no_override_s']}
    bands = []
    band_acc = collections.defaultdict(lambda: [0.0, 0.0, 0.0])
    for idx, r in enumerate(cc):
        st = state(r[0])
        dt = min(max(cc[idx + 1][0] - r[0] if idx + 1 < len(cc) else 0.01, 0), 0.05)
        if not st or not r[1] or (not st['event_valid']) or (not st['canValid']) or (not 0 <= st['age_s'] <= 0.1):
            continue
        if r[3]:
            active['lateral_s'] += dt
        if r[4]:
            active['longitudinal_s'] += dt
        band = int(st['mph'] // 5) * 5
        z = band_acc[band]
        z[0] += dt if r[3] else 0
        z[1] += dt if r[4] else 0
        if r[4] and (not any((st[k] for k in ['brakePressed', 'gasPressed', 'steeringPressed']))):
            active['longitudinal_no_override_s'] += dt
            z[2] += dt
    for band in sorted(band_acc):
        bands.append({'mph': [band, band + 5], 'lat_active_s': band_acc[band][0], 'long_active_s': band_acc[band][1], 'long_no_override_s': band_acc[band][2]})
    for row in posebad:
        row.update(relative_s=row['t'] - time0, state=state(row['t']), pose_minus_producer_ms=(row['producer'].get('poseMonoTime', 0) - row['producer'].get('producerMonoTime', 0)) / 1000000.0)
    parents = sorted({x['parent'] for x in starts})
    dirty = any((x['dirty'] for x in starts))
    r = {'drive': drive, 'segments': len(starts), 'start_mono': time0, 'duration_s': time1 - time0, 'local_start': local(time0), 'local_end': local(time1), 'parents': parents, 'dirty': dirty, 'candidate_source': parents == [receipt['source']['parent']] and (not dirty), 'segment_startup': starts, 'counts': dict(counts), 'invalid_counts': dict(invalid), 'max_mph': max((r[2] / 0.44704 for r in cs), default=0), 'active_exposure': active, 'speed_bands': bands, 'allocator_versions': dict(versions), 'active_pose_invalid_samples': posebad, 'fault_episodes': faults, 'controls_mismatch_alerts': mismatch, 'model_samples': len(model), 'model_max_drop': max((x[2] for x in model), default=None), 'device_health_ranges': health}
    results.append(r)
    (P / 'health-scan.json').write_text(json.dumps(results, indent=2) + '\n')
    print(drive, 'cohort', parents, 'faults', len(faults), 'mismatch', len(mismatch), 'maxmph', r['max_mph'], flush=True)
