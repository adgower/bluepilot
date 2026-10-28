import os
from pathlib import Path
"""Extract read-only saved logs. Raw GNSS and identities stay in private cache."""
from pathlib import Path
import sys, json, zstandard as z
from collections import Counter
ROOT = Path(str(Path(os.environ['OPENPILOT_ROOT'])))
sys.path[:0] = [str(ROOT), str(ROOT / 'opendbc_repo')]
from openpilot.cereal import log
from openpilot.selfdrive.locationd.helpers import Pose, PoseCalibrator
D = Path(sys.argv[1])
label = sys.argv[2]
OUT = Path(sys.argv[3])
cal = PoseCalibrator()
first = None
last_event = None
pending = []
last_sample = {}
cal_envelope_valid = False
metadata = []
startup = []
clocks = []
counts = Counter()
status = (0, 0, 0)
status_t = -1000000000000.0
S = {k: [] for k in ['cs', 'cc', 'motion', 'parameters', 'tx', 'panda', 'status', 'model', 'selfdrive', 'chestnut', 'context', 'calibration', 'buttons', 'events', 'lanes', 'controls', 'rejections']}
paths = sorted(D.glob('segment-*/rlog.zst'))

def chunks():
    global first, pending
    for p in paths:
        print(label, p.parent.name, file=sys.stderr, flush=True)
        with p.open('rb') as f:
            raw = z.ZstdDecompressor().stream_reader(f).read()
        events = list(log.Event.read_multiple_bytes(raw))
        if first is None:
            first = min((e.logMonoTime for e in events))
        for e in events:
            k = e.which()
            if k == 'initData':
                c = e.initData
                wanted = {}
                for entry in c.params.entries:
                    if entry.key in ['FordPrefHighSpeedTracking', 'FordPrefRollAwareMapping', 'FordPrefPersistentTracking', 'FordPrefSteerAngleCurvature', 'FordPrefLowSpeedGain', 'AlphaLongitudinalEnabled', 'ExperimentalMode', 'DisableUpdates']:
                        wanted[entry.key] = bytes(entry.value).decode(errors='replace')
                row = {'git_commit': c.gitCommit, 'git_branch': c.gitBranch, 'dirty': c.dirty, 'wall_time_ns': c.wallTimeNanos, 'mono_time_ns': e.logMonoTime, 'settings': wanted}
                if row not in startup:
                    startup.append(row)
            elif k == 'carParams':
                c = e.carParams
                row = {'flags': int(c.flags), 'safety_params': [x.safetyParam for x in c.safetyConfigs], 'steer_ratio': c.steerRatio, 'wheelbase': c.wheelbase, 'fingerprint': c.carFingerprint}
                if row not in metadata:
                    metadata.append(row)
        kinds = {'can', 'sendcan', 'extrinsicsCalibration', 'carState', 'carControl', 'modelV2', 'drivingModelData', 'deviceMotion', 'vehicleParameters', 'pandaStates', 'chestnutState', 'selfdriveState', 'gpsLocation', 'gpsLocationExternal', 'clocks', 'onroadEvents', 'controlsState'}
        batch = sorted(pending + [e for e in events if e.which() in kinds], key=lambda e: e.logMonoTime)
        if not batch:
            continue
        cut = batch[-1].logMonoTime - 5000000000
        split = next((i for i, e in enumerate(batch) if e.logMonoTime > cut), len(batch))
        pending = batch[split:]
        yield batch[:split]
    yield pending
for events in chunks():
    for e in events:
        k = e.which()
        t = e.logMonoTime / 1000000000.0
        at = (e.logMonoTime - first) / 1000000000.0
        if last_event is not None:
            assert e.logMonoTime >= last_event, 'Nonmonotonic merged segments'
        last_event = e.logMonoTime
        counts[k] += 1
        if k == 'clocks':
            clocks.append([at, int(e.clocks.wallTimeNanos), int(e.logMonoTime)])
        if k not in ['can', 'sendcan', 'extrinsicsCalibration', 'carState', 'carControl'] and t - last_sample.get(k, -1) < 0.045:
            continue
        last_sample[k] = t
        if k == 'extrinsicsCalibration':
            cal.feed_extrinsics_calibration(e.extrinsicsCalibration)
            cal_envelope_valid = bool(e.valid)
        elif k == 'modelV2':
            c = e.modelV2
            import numpy as np
            ll = c.laneLines
            pr = c.laneLineProbs
            if len(ll) >= 3 and len(pr) >= 3 and len(ll[1].x) and len(ll[2].x):
                left = float(np.interp(0, list(ll[1].x), list(ll[1].y)))
                right = float(np.interp(0, list(ll[2].x), list(ll[2].y)))
                S['lanes'].append([at, left, right, min(pr[1], pr[2]), (left + right) / 2, int(e.valid)])
            S['context'].append([at, int(str(c.meta.laneChangeState) != 'off'), int(e.valid)])
            S['model'].append([at, c.modelExecutionTime, c.frameDropPerc, int(c.big)])
        elif k == 'deviceMotion':
            dm = e.deviceMotion
            p = cal.build_calibrated_pose(Pose.from_device_motion(dm))
            S['motion'].append([dm.timestamp / 1000000000.0 - first / 1000000000.0, p.angular_velocity.z, p.angular_velocity.z_std, int(e.valid and cal_envelope_valid and dm.angularVelocityDevice.valid and dm.sensorsOK and cal.calib_valid), int(dm.inputsOK), int(dm.posenetOK), at])
        elif k == 'chestnutState':
            c = e.chestnutState
            S['chestnut'].append([at, c.tempC, c.memoryTempC, c.supplyVoltage, int(c.supplyFault)])
        elif k == 'selfdriveState':
            c = e.selfdriveState
            S['selfdrive'].append([at, int(c.active), str(c.state), c.alertText1, c.alertText2, int(c.enabled)])
        elif k == 'onroadEvents':
            S['events'].append([at, [str(x.name) for x in e.onroadEvents]])
        elif k == 'carState':
            c = e.carState
            for b in c.buttonEvents:
                S['buttons'].append([at, str(b.type), bool(b.pressed)])
            S['cs'].append([at, c.vEgoRaw, c.yawRate, c.steeringAngleDeg, int(c.steeringPressed), c.steeringTorque, int(c.brakePressed), int(c.gasPressed), int(c.steerFaultTemporary), int(c.steerFaultPermanent), int(c.cruiseState.enabled), int(c.canValid), int(c.leftBlinker or c.rightBlinker), str(c.gearShifter)])
        elif k == 'carControl':
            c = e.carControl
            S['cc'].append([at, int(c.latActive), c.actuators.curvature, c.actuators.steeringAngleDeg, int(e.valid)])
            S['calibration'].append([at, c.navigatorCalibration.to_dict()])
        elif k == 'controlsState':
            c = e.controlsState
            S['controls'].append([at, c.curvature, c.desiredCurvature, int(e.valid)])
        elif k == 'vehicleParameters':
            c = e.vehicleParameters
            S['parameters'].append([at, int(c.valid), c.roll, c.steerRatio, c.stiffnessFactor, c.angleOffsetDeg])
        elif k == 'pandaStates':
            for c in e.pandaStates:
                S['panda'].append([at, c.safetyParam, c.safetyTxBlocked, int(c.safetyRxChecksInvalid), int(c.controlsAllowed), c.safetyRxInvalid, int(c.ignitionLine or c.ignitionCan), int(bool(c.faults)), int(c.heartbeatLost)])
        elif False:
            c = getattr(e, k)
            if c.hasFix:
                S['gps'].append([at, c.latitude, c.longitude, c.bearingDeg, c.horizontalAccuracy, c.speed])
        elif k == 'can':
            for c in e.can:
                if c.src >= 192:
                    d = c.dat
                    S['rejections'].append([at, c.address, c.src - 192, d[0] >> 4 & 7 if c.address == 982 and len(d) == 8 else -1])
                if c.src == 0 and c.address == 972 and (len(c.dat) == 8):
                    status = (c.dat[2] & 7, c.dat[4] & 3, c.dat[4] >> 6 & 3)
                    status_t = at
        elif k == 'sendcan':
            for c in e.sendcan:
                if c.src == 0 and c.address == 982 and (len(c.dat) == 8):
                    d = c.dat
                    wire = -(((d[3] & 31) << 6 | d[4] >> 2) * 0.0005 - 0.5)
                    S['tx'].append([at, wire, d[0] >> 4 & 7])
                    S['status'].append([at, *status, at - status_t])
for k, v in S.items():
    v.sort(key=lambda x: x[0])
r = {'drive': label, 'segments': len(paths), 'first_monotonic_ns': first, 'last_monotonic_ns': last_event, 'software': startup, 'configuration': metadata, 'event_counts': dict(counts), 'clocks': clocks, 'streams': S}
OUT.write_bytes(z.ZstdCompressor(level=3).compress(json.dumps(r, separators=(',', ':')).encode()))
print(json.dumps({'drive': label, 'segments': len(paths), 'duration_s': (last_event - first) / 1000000000.0, 'software': startup, 'configuration': metadata, 'stream_rows': {k: len(v) for k, v in S.items()}}, indent=2), file=sys.stderr)
