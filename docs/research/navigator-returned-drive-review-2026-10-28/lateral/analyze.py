import os
from pathlib import Path
from pathlib import Path
import sys, json, hashlib, datetime, csv
import numpy as np, zstandard as z
P = Path(__file__).resolve().parent
ROOT = Path(str(Path(os.environ['OPENPILOT_ROOT'])))
sys.path[:0] = [str(ROOT), str(ROOT / 'opendbc_repo'), str(P.parent.parent / 'navigator-calibration-first-2026-10-16')]
from normalize import normalize_one
from dataset import align_past
from opendbc.car.vehicle_model import VehicleModel
from opendbc.car.ford.interface import CarInterface
from opendbc.car.ford.values import CAR
CAND = 'e05e42f43d2907a4f02915a924cfd95a46197e79'
vm = VehicleModel(CarInterface.get_non_essential_params(CAR.FORD_EXPEDITION_MK4))

def pct(x):
    return np.percentile(x, [10, 50, 90]).tolist() if len(x) else None

def intervals(m, n=10):
    e = np.diff(np.r_[False, m, False].astype(int))
    return [(a, b) for a, b in zip(np.flatnonzero(e == 1), np.flatnonzero(e == -1)) if b - a >= n]

def stats(d, m):
    if not m.any():
        return {'seconds': 0.0}
    q = d['req'][m]
    b = d['body'][m]
    w = d['wheel'][m]
    u = d['wire'][m]
    sg = np.sign(q)
    return dict(seconds=round(float(m.sum() * 0.05), 3), mph=pct(d['mph'][m]), request_accel=pct(q), body_accel=pct(b), wire_accel=pct(u), wheel_accel=pct(w), body_excess_accel=pct((b - q) * sg), wheel_excess_accel=pct((w - q) * sg), wire_excess_accel=pct((u - q) * sg), body_ratio=pct(b / q), wheel_ratio=pct(w / q), wire_ratio=pct(u / q), wheel_over_wire=pct(w / u), body_over_wire=pct(b / u), yaw_std_rad_s=pct(d['motion_yaw_std'][m]), wheel_rate_deg_s=pct(d['wheel_rate'][m]), roll_rad=pct(d['roll'][m]))
sessions = []
bands = []
events = []
windows = []
hashes = []
for f in sorted(P.glob('*-signals.json.zst')):
    raw = json.loads(z.ZstdDecompressor().decompress(f.read_bytes()))
    missing = []
    for key, n in [('motion', 6), ('parameters', 6), ('context', 3), ('panda', 9), ('tx', 3), ('cc', 5)]:
        if not raw['streams'][key]:
            missing.append(key)
            raw['streams'][key] = [[-1000000000000.0] + [0] * (n - 1)]
    d, meta = normalize_one(raw)
    meta['absent_streams'] = missing
    s = raw['streams']
    t = d['t']
    cs, age = align_past([x[:13] for x in s['cs']], t)
    cc, cca = align_past(s['cc'], t)
    active = np.convolve(d['lat_active'].astype(int), np.ones(41, dtype=int), 'full')[:len(t)] == 41
    ok = d['eligible'] & (cs[:, 7] == 0) & active
    v = d['mph'] * 0.44704
    d['req'] = d['reference'] * v
    d['body'] = d['y'] * v
    d['wire'] = d['u'] * v
    wheel = []
    for a, sp, ro, ra, st, off in zip(d['wheel_angle_deg'], v, d['roll'], d['learned_ratio'], d['stiffness'], d['angle_offset_deg']):
        if np.isfinite([a, sp, ro, ra, st, off]).all() and ra > 0:
            vm.update_params(st, ra)
            wheel.append(-vm.calc_curvature(np.radians(a - off), sp, ro) * sp * sp)
        else:
            wheel.append(np.nan)
    d['wheel'] = np.array(wheel)
    d['wheel_rate'] = np.r_[np.nan, np.diff(d['wheel_angle_deg']) / 0.05]
    meaningful = (abs(d['req']) >= 0.25) & ((d['mph'] >= 50) | (abs(d['requested_curvature']) > 0.001))
    clean = ok & meaningful & np.isfinite(d['wheel'])
    phase = np.full(len(t), 'transition', dtype='<U12')
    for i in np.flatnonzero(clean):
        if i < 20:
            continue
        a = d['requested_curvature'][i - 20:i + 1]
        m = clean[i - 20:i + 1]
        if not m.all() or np.ptp(d['mph'][i - 20:i + 1]) > 3 or np.any(a * a[-1] <= 0):
            continue
        scale = max(np.median(abs(a)), 1e-05)
        delta = (abs(a[-1]) - abs(a[0])) / scale
        if np.ptp(abs(a)) <= 0.1 * scale:
            phase[i] = 'steady'
        elif delta > 0.1:
            phase[i] = 'rising'
        elif delta < -0.1:
            phase[i] = 'unwinding'
    for a in range(0, len(t) - 99, 100):
        sl = slice(a, a + 100)
        if ok[sl].all() and d['mph'][sl].min() >= 55 and (np.percentile(abs(d['req'][sl]), 95) < 0.25):
            windows.append(dict(drive=raw['drive'], type='quiet_demand_5s', start_s=float(t[a]), end_s=float(t[a + 99]), mph=pct(d['mph'][sl]), body_accel=pct(d['body'][sl]), body_accel_peak_to_peak=float(np.ptp(d['body'][sl])), wire_accel=pct(d['wire'][sl]), wheel_rate_deg_s=pct(d['wheel_rate'][sl]), roll_rad=pct(d['roll'][sl])))
    cohort = 'candidate' if meta['source_commits'] == [CAND] else 'pre-update'
    label = raw['drive']
    sessions.append(dict(drive=label, cohort=cohort, **meta, clean=stats(d, clean), active_seconds=float(d['lat_active'].sum() * 0.05), no_gas_active_2s_seconds=float(ok.sum() * 0.05)))
    for lo in range(0, 90, 5):
        band = (d['mph'] >= lo) & (d['mph'] < lo + 5)
        bands.append(dict(drive=label, cohort=cohort, lo=lo, hi=lo + 5, recorded_seconds=float(band.sum() * 0.05), active_seconds=float((band & d['lat_active']).sum() * 0.05), eligible_seconds=float((band & ok).sum() * 0.05), all=stats(d, band & clean), steady=stats(d, band & clean & (phase == 'steady')), rising=stats(d, band & clean & (phase == 'rising')), unwinding=stats(d, band & clean & (phase == 'unwinding'))))
    ratio = np.divide(d['body'], d['req'], out=np.zeros(len(t)), where=meaningful)
    err = (d['body'] - d['req']) * np.sign(d['req'])
    for kind, mask in [('body_excess', clean & (ratio > 1.2) & (err > 0.2)), ('body_shortfall', clean & (ratio < 0.7) & (err < -0.2)), ('coherent_excess', clean & (ratio > 1.2) & (err > np.maximum(0.2, 2 * d['motion_yaw_std'] * v)) & ((d['wheel'] - d['req']) * np.sign(d['req']) > 0.2))]:
        for a, b in intervals(mask):
            m = np.zeros(len(t), bool)
            m[a:b] = 1
            windows.append(dict(drive=label, cohort=cohort, type=kind, start_s=float(t[a]), end_s=float(t[b - 1]), phase_counts={x: int(np.sum(phase[m] == x)) for x in set(phase[m])}, **stats(d, m)))
    candidates = []
    for a, b in intervals(cs[:, 4] > 0, 1):
        if d['mph'][a] >= 5 and d['lat_active'][max(0, a - 20):a + 1].any():
            candidates.append((a, b, 'steering-pressure'))
    for a in np.flatnonzero(d['lat_active'][:-1] & ~d['lat_active'][1:]) + 1:
        if d['mph'][a] >= 5:
            candidates.append((a, a + 1, 'lateral-disengagement'))
    grouped = []
    for a, b, kind in sorted(candidates):
        if grouped and t[a] - t[grouped[-1][1] - 1] < 1:
            grouped[-1][1] = max(b, grouped[-1][1])
            grouped[-1][2].append(kind)
        else:
            grouped.append([a, b, [kind]])
    for a, b, kinds in grouped:
        pre = (t >= t[a] - 3) & (t < t[a] - 0.2) & clean
        near = (t >= t[a] - 0.7) & (t <= t[min(b - 1, len(t) - 1)] + 0.5)
        events.append(dict(drive=label, cohort=cohort, start_s=float(t[a]), end_s=float(t[b - 1]), mph=float(d['mph'][a]), types=kinds, pre_3s=stats(d, pre), brake_associated=bool((cs[near, 6] > 0).any()), gas_associated=bool((cs[near, 7] > 0).any()), signal_associated=bool((cs[near, 12] > 0).any()), onroad_events=sorted({x for row in s['events'] if abs(row[0] - t[a]) < 1 for x in row[1]}), alerts=sorted({x for row in s['selfdrive'] if abs(row[0] - t[a]) < 1 for x in row[3:5] if x})))
    np.savez_compressed(P / (label + '-normalized.npz'), **d, eligible_final=ok, meaningful=meaningful, phase=phase)
    hashes.append(dict(file=f.name, sha256=hashlib.sha256(f.read_bytes()).hexdigest(), normalized_sha256=hashlib.sha256((P / (label + '-normalized.npz')).read_bytes()).hexdigest()))
    print(label, cohort, meta['max_mph'], flush=True)
(P / 'analysis.json').write_text(json.dumps(dict(sessions=sessions, bands=bands, windows=windows, takeovers=events, hashes=hashes), indent=2) + '\n')
with (P / 'bands.csv').open('w') as f:
    w = csv.writer(f)
    w.writerow(['drive', 'cohort', 'mph_low', 'mph_high', 'recorded_s', 'active_s', 'eligible_s', 'meaningful_s', 'steady_s', 'body_ratio_p50', 'body_excess_p50_m_s2'])
    for b in bands:
        w.writerow([b['drive'], b['cohort'], b['lo'], b['hi'], b['recorded_seconds'], b['active_seconds'], b['eligible_seconds'], b['all']['seconds'], b['steady']['seconds'], (b['all'].get('body_ratio') or [None] * 3)[1], (b['all'].get('body_excess_accel') or [None] * 3)[1]])
