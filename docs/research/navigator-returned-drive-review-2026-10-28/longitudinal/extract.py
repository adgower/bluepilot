import os
from pathlib import Path
"""Offline streaming numerical telemetry and CAN extraction. No vehicle I/O."""
from pathlib import Path
import sys, json, hashlib, collections, numpy as np
R = Path(str(Path(os.environ['OPENPILOT_ROOT'])))
sys.path[:0] = [str(R / 'opendbc_repo'), str(R / 'msgq_repo'), str(R)]
from openpilot.tools.lib.logreader import LogReader
from opendbc.can import CANParser
P = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else P.parent
LABEL = sys.argv[2] if len(sys.argv) > 2 else 'new'
A = json.loads((ROOT / 'acquisition-provenance.json').read_text())
assert A['segment_hashes_verified']
B = Path(A['private_backup'])
out = B / 'longitudinal'
out.mkdir(exist_ok=True)
results = []
fields = json.loads((ROOT.parent / 'navigator-highway-pulsing-prototype-2026-10-24/protocol-fields.json').read_text())
mapping = {int(k.split(':')[0]): (k.split(':')[1], v) for k, v in fields.items() if v}
mapping[390] = ('ACCDATA', ['Cmbb_B_Enbl', 'AccBrkDecel_B_Rq', 'AccBrkPrchg_B_Rq', 'AccPrpl_A_Rq', 'AccBrkTot_A_Rq', 'AccStopStat_B_Rq', 'AccResumEnbl_B_Rq'])
manifest = json.loads((ROOT / 'input-manifest.json').read_text())
phase = {'off': 0, 'pid': 1, 'stopping': 2, 'starting': 3}
columns = {'state': ['t', 'valid', 'speed', 'a', 'vcruise', 'brake', 'gas', 'steer', 'can', 'standstill', 'yaw', 'steering_angle'], 'control': ['t', 'valid', 'enabled', 'active', 'raw', 'phase', 'pitch', 'producer_t', 'pose_t', 'pose_valid', 'reference_valid', 'epoch', 'sequence', 'allocator_version', 'target', 'target_t', 'target_valid'], 'output': ['t', 'valid', 'raw', 'gas', 'brake', 'limited', 'fault', 'epoch', 'sequence', 'producer_t', 'reason', 'feedback_valid', 'allocator_version', 'precharge', 'reference_brake', 'allocator_phase', 'precharge_age', 'budget_remaining', 'grade_offset'], 'plan': ['t', 'valid', 'target', 'stop', 'lead', 'allow_brake', 'allow_throttle', 'source', 'model_t'], 'pid': ['t', 'valid', 'p', 'i', 'f', 'phase', 'plan_t'], 'radar': ['t', 'valid', 'status', 'distance', 'vrel', 'arel', 'vlead', 'alead', 'probability'], 'motion': ['t', 'valid', 'pitch', 'orientation_valid', 'ax', 'vx', 'inputs', 'posenet', 'sensors', 'timestamp']}
for drive in sorted({x['drive'] for x in manifest}):
    groups = collections.defaultdict(list)
    reasons = []
    sources = []
    startup = []
    segment_spans = []
    first = None
    last = None
    canrows = collections.defaultdict(list)
    maneuver = False
    parser = CANParser('ford_lincoln_base_pt', [(n, 0) for n, c in mapping.values()], 0)

    def code(seq, value):
        if value not in seq:
            seq.append(value)
        return seq.index(value)
    for m in sorted([x for x in manifest if x['drive'] == drive], key=lambda x: x['segment']):
        path = B / 'recordings' / drive / f"segment-{m['segment']:03d}" / 'rlog.zst'
        with path.open('rb') as f:
            assert hashlib.file_digest(f, 'sha256').hexdigest() == m['sha256']
        segstart = None
        for e in LogReader(str(path)):
            k = e.which()
            t = e.logMonoTime / 1000000000.0
            v = bool(e.valid)
            if first is None:
                first = t
            if segstart is None:
                segstart = t
            last = t
            if k == 'initData':
                q = e.initData
                startup.append(dict(segment=m['segment'], commit=q.gitCommit, dirty=q.dirty))
                continue
            if k in ['can', 'sendcan']:
                for msg in getattr(e, k):
                    addr = int(msg.address)
                    if msg.src != 0 or addr not in mapping or (addr == 390) != (k == 'sendcan'):
                        continue
                    name, cols = mapping[addr]
                    parser.update([(e.logMonoTime, [(addr, bytes(msg.dat), 0)])])
                    vals = parser.vl[name]
                    canrows[str(addr)].append([t, v, *[vals[x] for x in cols]])
                continue
            if k not in ['carState', 'carControl', 'carOutput', 'longitudinalPlan', 'controlsState', 'radarState', 'deviceMotion', 'alertDebug']:
                continue
            d = getattr(e, k).to_dict()
            if k == 'alertDebug' and ('Maneuver Active' in str(d) or 'Maneuvers Finished' in str(d)):
                maneuver = True
            if k == 'carState':
                groups['state'].append([t, v, d['vEgo'], d['aEgo'], d.get('vCruise', np.nan), d['brakePressed'], d['gasPressed'], d['steeringPressed'], d['canValid'], d['standstill'], d['yawRate'], d['steeringAngleDeg']])
            elif k == 'carControl':
                q = d.get('navigatorLongitudinal', {})
                ori = d.get('orientationNED', [])
                groups['control'].append([t, v, d['enabled'], d['longActive'], d['actuators']['accel'], phase[d['actuators']['longControlState']], ori[1] if len(ori) == 3 else np.nan, q.get('producerMonoTime', 0) / 1000000000.0, q.get('poseMonoTime', 0) / 1000000000.0, q.get('poseValid', False), q.get('referenceValid', False), q.get('epoch', 0), q.get('sequence', 0), q.get('allocatorVersion', 0), q.get('targetAcceleration', 0), q.get('targetMonoTime', 0) / 1000000000.0, q.get('targetValid', False)])
            elif k == 'carOutput':
                q = d['actuatorsOutput'].get('navigatorLongitudinal')
                if q:
                    groups['output'].append([t, v, q.get('requested', 0), q.get('gas', 0), q.get('brake', False), q.get('limited', False), q.get('fault', False), q.get('epoch', 0), q.get('sequence', 0), q.get('producerMonoTime', 0) / 1000000000.0, code(reasons, q.get('reason', '')), q.get('valid', False), q.get('allocatorVersion', 0), q.get('precharge', False), q.get('referenceBrake', False), {'inactive': 0, 'brake': 1, 'precharge': 2, 'release': 3, 'engineRamp': 4, 'drive': 5, 'fault': 6}.get(q.get('allocatorPhase', 'inactive'), -1), q.get('prechargeAge', 0), q.get('budgetRemaining', 0), q.get('gradeOffset', 0)])
            elif k == 'longitudinalPlan':
                groups['plan'].append([t, v, d['aTarget'], d['shouldStop'], d['hasLead'], d['allowBrake'], d['allowThrottle'], code(sources, d['longitudinalPlanSource']), d.get('modelMonoTime', 0) / 1000000000.0])
            elif k == 'controlsState':
                groups['pid'].append([t, v, d['upAccelCmd'], d['uiAccelCmd'], d['ufAccelCmd'], phase[d['longControlState']], d['longitudinalPlanMonoTime'] / 1000000000.0])
            elif k == 'radarState':
                q = d.get('leadOne', {})
                groups['radar'].append([t, v and bool(q), q.get('present', q.get('status', False)), q.get('dRel', np.nan), q.get('vRel', np.nan), q.get('aRel', np.nan), q.get('vLead', np.nan), q.get('aLeadK', np.nan), q.get('modelProb', np.nan)])
            elif k == 'deviceMotion':
                o = d['orientationNED']
                groups['motion'].append([t, v, o['y'], o['valid'], d['accelerationDevice']['x'], d['velocityDevice']['x'], d['inputsOK'], d['posenetOK'], d['sensorsOK'], d['timestamp'] / 1000000000.0])
        segment_spans.append(dict(segment=m['segment'], start=segstart, end=last))
        print(drive, m['segment'], flush=True)
    target = out / (drive + '.npz')
    np.savez_compressed(target, **{k: np.array(groups[k], float).reshape(-1, len(cols)) for k, cols in columns.items()}, **{k: np.array(canrows[k], float).reshape(-1, len(cols) + 2) for k, (_, cols) in [(str(a), b) for a, b in mapping.items()]})
    results.append(dict(drive=drive, start_mono=first, end_mono=last, duration_s=last - first, private_arrays=str(target), sha256=hashlib.sha256(target.read_bytes()).hexdigest(), reasons=reasons, sources=sources, counts={k: len(groups[k]) for k in columns}, can_counts={k: len(v) for k, v in canrows.items()}, is_maneuver=maneuver, startup=startup, segment_spans=segment_spans))
    (P / (LABEL + '-inputs.json')).write_text(json.dumps(dict(columns=columns, can_columns={str(a): ['t', 'valid', *cols] for a, (_, cols) in mapping.items()}, sessions=results), indent=2) + '\n')
