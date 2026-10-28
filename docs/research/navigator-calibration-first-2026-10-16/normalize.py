import os
from pathlib import Path
"""Normalize private extracted signals to anonymous20Hz analysis-only tables."""
from pathlib import Path
import json, datetime
import numpy as np, zstandard as z
from dataset import align_past
from cache_provenance import cache_valid, digest
P = Path(__file__).parent
CACHE = Path(str(Path(os.environ['NAVIGATOR_PRIVATE_CACHE']) / 'navigator-calibration-first-cache'))

def load_bound_signal(path, binding):
    if not cache_valid(path, binding):
        raise ValueError('cache provenance mismatch: ' + path.name)
    d = json.loads(z.ZstdDecompressor().decompress(path.read_bytes()))
    if d.get('drive') != binding['drive']:
        raise ValueError('cache provenance label mismatch')
    return d

def normalize_one(d):
    s = d['streams']
    end = (d['last_monotonic_ns'] - d['first_monotonic_ns']) / 1000000000.0
    t = np.arange(0, end, 0.05)
    cs, ca = align_past([x[:13] + [int(x[13] == 'drive')] for x in s['cs']], t)
    cc, cca = align_past(s['cc'], t)
    tx, ta = align_past(s['tx'], t)
    mo, ma = align_past(s['motion'], t)
    pa, paa = align_past(s['parameters'], t)
    ctx, cta = align_past(s['context'], t)
    panda, pana = align_past(s['panda'], t)
    pressed = np.asarray([x[0] for x in s['cs'] if x[4]])
    idx = np.searchsorted(pressed, t, side='right') - 1
    since = np.where(idx >= 0, t - pressed[np.maximum(idx, 0)], np.inf) if len(pressed) else np.full(len(t), np.inf)
    guards = {'fresh_state': ca < 0.08, 'fresh_control': cca < 0.08, 'fresh_wire': ta < 0.075, 'fresh_motion': ma < 0.12, 'fresh_parameters': paa < 0.12, 'fresh_model': cta < 0.15, 'fresh_panda': pana < 0.25, 'can_valid': cs[:, 11] > 0, 'no_steer_fault': (cs[:, 8] == 0) & (cs[:, 9] == 0), 'no_override': (cs[:, 4] == 0) & (since > 1), 'no_brake': cs[:, 6] == 0, 'driving_gear': cs[:, 13] > 0, 'lateral_active': (cc[:, 1] > 0) & (tx[:, 2] == 1), 'control_valid': cc[:, 4] > 0, 'motion_valid': (mo[:, 3] > 0) & (mo[:, 4] > 0) & (mo[:, 5] > 0), 'parameters_valid': pa[:, 1] > 0, 'lane_keeping': (ctx[:, 1] == 0) & (ctx[:, 2] > 0) & (cs[:, 12] == 0), 'panda_healthy': (panda[:, 3] == 0) & (panda[:, 5] == 0) & (panda[:, 7] == 0) & (panda[:, 8] == 0), 'minimum_speed': cs[:, 1] >= 5 * 0.44704}
    eligible = np.logical_and.reduce(list(guards.values()))
    mph = cs[:, 1] / 0.44704
    commits = sorted({x['git_commit'] for x in d['software']})
    if len(commits) != 1:
        eligible[:] = False
    table = dict(t=t, u=tx[:, 1], y=mo[:, 1], mph=mph, reference=cc[:, 2] * cs[:, 1], requested_curvature=cc[:, 2], raw_CAN_yaw=cs[:, 2], wheel_angle_deg=cs[:, 3], roll=pa[:, 2], learned_ratio=pa[:, 3], stiffness=pa[:, 4], angle_offset_deg=pa[:, 5], motion_yaw_std=mo[:, 2], eligible=eligible, lat_active=cc[:, 1] > 0, wire_mode=tx[:, 2], driver_pressed=cs[:, 4] > 0, motion_valid=guards['motion_valid'], fresh_motion=guards['fresh_motion'])
    for name in ['u', 'y', 'reference', 'mph']:
        if np.any(eligible & ~np.isfinite(table[name])):
            raise ValueError('eligible nonfinite ' + name)
    stopped = (cs[:, 1] < 0.05) & guards['fresh_state'] & guards['fresh_motion'] & guards['motion_valid']
    baseline = float(np.median(cs[stopped, 2])) if stopped.any() else None
    table['diagnostic_debiased_CAN_yaw'] = -(cs[:, 2] - baseline) if baseline is not None else np.full(len(t), np.nan)
    clocks = np.asarray(d['clocks'], float)
    start = None
    if len(clocks):
        offset = clocks[:, 1] - clocks[:, 2]
        near = abs(offset - offset[-1]) < 100000000
        start = datetime.datetime.fromtimestamp((d['first_monotonic_ns'] + float(np.median(offset[near]))) / 1000000000.0, datetime.timezone.utc).isoformat()
    metadata = dict(segments=d['segments'], start_utc_from_stable_clocks=start, duration_s=end, source_commits=commits, configuration=d['configuration'], settings=[x['settings'] for x in d['software']], max_mph=float(max((x[1] for x in s['cs'])) / 0.44704), grid_max_mph=float(np.nanmax(mph)), eligible_seconds=float(eligible.sum() * 0.05), stationary_CAN_bias_rad_s=baseline, stationary_samples=int(stopped.sum()), excluded_by_guard={k: int(np.sum(~v)) for k, v in guards.items()}, samples=len(t))
    return (table, metadata)
if __name__ == '__main__':
    out = []
    bindings = {x['drive']: x['inputs'] for x in json.loads((P / 'cache-provenance.json').read_text())}
    for f in sorted(CACHE.glob('*-signals.json.zst')):
        label = f.name.split('-signals')[0]
        d = load_bound_signal(f, bindings[label])
        table, metadata = normalize_one(d)
        metadata['signal_cache_sha256'] = digest(f)
        np.savez_compressed(P / (label + '-normalized.npz'), **table)
        out.append({'drive': label, **metadata})
        print(label, metadata['max_mph'], 'eligible', metadata['eligible_seconds'], flush=True)
    (P / 'normalized-manifest.json').write_text(json.dumps(out, indent=2) + '\n')
