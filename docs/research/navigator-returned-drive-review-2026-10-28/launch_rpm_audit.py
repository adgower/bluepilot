import os
from pathlib import Path
"""Saved-log propulsion/RPM and vehicle-launch audit; RPM quality retained."""
from pathlib import Path
import json, hashlib, numpy as np
P = Path(__file__).resolve().parent
meta = json.loads((P / 'longitudinal/new-inputs.json').read_text())
results = []

def prior(a, t, age=0.1):
    j = np.searchsorted(a[:, 0], t, 'right') - 1
    ii = np.maximum(j, 0)
    q = a[ii]
    return (q, (j >= 0) & (t - q[:, 0] >= 0) & (t - q[:, 0] <= age) & (q[:, 1] == 1))

def runs(mask, t):
    good = mask.copy()
    starts = []
    a = None
    for i in range(len(mask) + 1):
        if i < len(mask) and mask[i] and (a is None or i == 0 or t[i] - t[i - 1] <= 0.1):
            if a is None:
                a = i
        else:
            if a is not None:
                starts.append(np.arange(a, i))
                a = None
            if i < len(mask) and mask[i]:
                a = i
    return starts
for m in meta['sessions']:
    f = Path(m['private_arrays'])
    with f.open('rb') as z:
        assert hashlib.file_digest(z, 'sha256').hexdigest() == m['sha256']
    a = dict(np.load(f))
    can = a['390']
    t = can[:, 0]
    s, sv = prior(a['state'], t)
    out, ov = prior(a['output'], t)
    rpm, rv = prior(a['516'], t)
    gear, gv = prior(a['374'], t, 0.5)
    cc = a['control']
    bykey = {(r[11], r[12]): i for i, r in enumerate(cc)}
    idx = np.array([bykey.get((r[7], r[8]), -1) for r in out])
    c = cc[np.maximum(idx, 0)]
    cv = (idx >= 0) & (c[:, 0] <= t) & (t - c[:, 0] <= 0.1) & (c[:, 1] == 1)
    good = sv & ov & cv & (can[:, 1] == 1) & (can[:, 2] == 1) & (c[:, 2] == 1) & (c[:, 3] == 1) & (s[:, 5] == 0) & (s[:, 6] == 0) & (s[:, 8] == 1) & (out[:, 6] == 0) & (out[:, 11] == 1)
    high = good & rv & gv & (rpm[:, 4] > 3200)
    episodes = []
    for ii in runs(high, t):
        duration = t[ii[-1]] - t[ii[0]]
        if duration < 0.2:
            continue
        episodes.append(dict(start_relative_s=float(t[ii[0]] - m['start_mono']), duration_s=float(duration), max_decoded_rpm=float(rpm[ii, 4].max()), qf_codes=sorted(set(map(int, rpm[ii, 2]))), speed_range_mph=[float(s[ii, 2].min() * 2.236936), float(s[ii, 2].max() * 2.236936)], actual_gears=sorted(set(map(int, gear[ii, 4]))), target_gears=sorted(set(map(int, gear[ii, 3]))), gas_request_range=[float(can[ii, 5].min()), float(can[ii, 5].max())], brake_samples=int((can[ii, 3] > 0.5).sum()), precharge_samples=int((can[ii, 4] > 0.5).sum()), rpm_independently_qualified=False))
    launches = []
    stopped_since = None
    armed = False
    for i in range(len(t)):
        if not good[i]:
            stopped_since = None
            armed = False
            continue
        speed = s[i, 2]
        if speed < 0.15:
            if stopped_since is None:
                stopped_since = t[i]
            if t[i] - stopped_since >= 1.0:
                armed = True
        elif speed >= 0.3 and armed:
            stop_duration = t[i] - stopped_since
            armed = False
            stopped_since = None
            end = i + 1
            while end < len(t) and t[end] - t[i] <= 15 and good[end] and (t[end] - t[end - 1] <= 0.1):
                end += 1
            ii = np.arange(i, end)
            reached = lambda v: next((float(t[j] - t[i]) for j in ii if s[j, 2] >= v), None)
            launches.append(dict(start_relative_s=float(t[i] - m['start_mono']), preceding_stop_s=float(stop_duration), observed_until_s=float(t[ii[-1]] - t[i]), time_to_6p7mph_s=reached(6.7 / 2.236936), time_to_10mph_s=reached(10 / 2.236936), max_raw=float(c[ii, 4].max()), max_aego=float(s[ii, 3].max()), censored_before15s=bool(t[ii[-1]] - t[i] < 14.9)))
    selected = rpm[good & rv, 4]
    results.append(dict(drive=m['drive'], max_decoded_active_nopedal_rpm=float(selected.max()) if len(selected) else None, active_rpm_qf_codes=sorted(set(map(int, rpm[good & rv, 2]))), high_decoded_rpm_episodes=episodes, observed_vehicle_launches=launches, limits='RPM QF=0 is labeled Faulty by current DBC; decoded RPM remains unqualified. Launch times start at first speed>=0.3m/s after >=1s near-stop; they are not traffic-light reaction or lead-response delays. Missing/censored crossings are not successful starts.'))
(P / 'launch-rpm-audit.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
