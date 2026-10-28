import os
from pathlib import Path
"""Past-only <=100ms CAN-anchored on-road descriptive analysis; no simulation."""
from pathlib import Path
import json, hashlib, csv, numpy as np
P = Path(__file__).resolve().parent
BANDS = [(i, i + 5) for i in range(0, 85, 5)] + [(85, 90), (90, 1000)]

def asof(a, t, maxage=0.1):
    if not len(a):
        return (np.zeros((len(t), a.shape[1])), np.zeros(len(t), bool))
    ix = np.searchsorted(a[:, 0], t, side='right') - 1
    q = a[np.maximum(ix, 0)]
    age = t - q[:, 0]
    return (q, (ix >= 0) & (age >= 0) & (age <= maxage) & (q[:, 1] == 1))

def safe(v):
    v = np.asarray(v)
    v = v[np.isfinite(v)]
    return dict(min=float(v.min()), p05=float(np.quantile(v, 0.05)), median=float(np.median(v)), p95=float(np.quantile(v, 0.95)), max=float(v.max())) if len(v) else None

def changes(value, continuity):
    return continuity & np.r_[False, np.diff(value.astype(int)) != 0]

def summary(mask, dt, speed, br, pre, bt, pt, ct, rapid, raw, target, accel, jerk, tor, torok, ecu, ecuok, deficit, lead, leadok, gas):
    sec = float(dt[mask].sum())
    b = int(bt[mask].sum())
    p = int(pt[mask].sum())
    c = int(ct[mask].sum())
    h = mask & torok
    ec = mask & ecuok
    return dict(active_s=sec, full_brake_changes=b, precharge_changes=p, combined_changes=c, full_brake_changes_per_active_min=b * 60 / sec if sec else None, precharge_changes_per_active_min=p * 60 / sec if sec else None, combined_changes_per_active_min=c * 60 / sec if sec else None, rapid_full_brake_reversals=int(rapid[mask].sum()), full_brake_s=float(dt[mask & br].sum()), precharge_s=float(dt[mask & pre].sum()), combined_s=float(dt[mask & (br | pre)].sum()), brake_precharge_clear_s=float(dt[mask & ~br & ~pre].sum()), inactive_propulsion_requests_clear_s=float(dt[mask & ~br & ~pre & (np.abs(gas + 5) < 1e-06)].sum()), reported_brake_clear_inactive_propulsion_s=float(dt[mask & ~br & ~pre & (np.abs(gas + 5) < 1e-06) & torok & ecuok & (tor[:, 3] >= 0) & (tor[:, 3] <= 4) & (tor[:, 2] >= 0) & (tor[:, 2] <= 4) & (ecu[:, 5] == 0) & (ecu[:, 2] == 0)].sum()), valid_engine_request_clear_s=float(dt[mask & ~br & ~pre & (gas >= -0.5)].sum()), raw_gt_point1_full_brake_s=float(dt[mask & br & (raw > 0.1)].sum()), target_abs_lt_point2_full_brake_s=float(dt[mask & br & (np.abs(target) < 0.2)].sum()), speed_mph=safe(speed[mask]), raw_accel=safe(raw[mask]), plan_accel=safe(target[mask]), actual_accel=safe(accel[mask]), abs_jerk_200ms=safe(np.abs(jerk[mask])), torque_fresh_s=float(dt[h].sum()), brake_torque_Nm=safe(tor[h, 3]), torque_gt50Nm_s=float(dt[h & (tor[:, 3] > 50)].sum()), ecu_fresh_s=float(dt[ec].sum()), ecu_brake_active_s=float(dt[ec & (ecu[:, 5] == 1)].sum()), ecu_precharge_active_s=float(dt[ec & (ecu[:, 2] == 1)].sum()), speed_deficit_known_s=float(dt[mask & np.isfinite(deficit)].sum()), speed_deficit_gt2mph_s=float(dt[mask & (deficit > 2)].sum()), lead_known_s=float(dt[mask & leadok].sum()), lead_present_s=float(dt[mask & leadok & lead].sum()))
results = []
for label in ['baseline', 'new']:
    path = P / (label + '-inputs.json')
    if not path.exists():
        continue
    meta = json.loads(path.read_text())
    for m in meta['sessions']:
        f = Path(m['private_arrays'])
        with f.open('rb') as stream:
            assert hashlib.file_digest(stream, 'sha256').hexdigest() == m['sha256']
        a = dict(np.load(f))
        can = a['390']
        t = can[:, 0]
        for key in ['state', 'output', 'control', 'pid', 'plan', 'radar', '125', '531', '516', '357']:
            if not len(a[key]):
                a[key] = np.zeros((1, a[key].shape[1]))
        if not len(t):
            continue
        state, sv = asof(a['state'], t)
        out, ov = asof(a['output'], t)
        cc = a['control']
        lookup = {(r[11], r[12]): i for i, r in enumerate(cc)}
        ix = np.array([lookup.get((r[7], r[8]), -1) for r in out])
        ctrl = cc[np.maximum(ix, 0)]
        cv = (ix >= 0) & (ctrl[:, 0] <= t) & (t - ctrl[:, 0] <= 0.1) & (ctrl[:, 1] == 1)
        pi, pv = asof(a['pid'], ctrl[:, 0])
        pl = a['plan']
        px = np.searchsorted(pl[:, 0], pi[:, 6])
        px = np.minimum(px, len(pl) - 1)
        plan = pl[px]
        plv = (plan[:, 0] <= t) & (t - plan[:, 0] <= 0.1) & (np.abs(plan[:, 0] - pi[:, 6]) < 1e-07) & (plan[:, 1] == 1)
        tor, tv = asof(a['125'], t)
        ecu, ev = asof(a['531'], t)
        rpm, rv = asof(a['516'], t)
        eng, engv = asof(a['357'], t)
        rad, rav = asof(a['radar'], t)
        lead = rad[:, 2] == 1
        assert np.all(np.abs(out[cv, 2] - ctrl[cv, 4]) < 1e-05), 'Consumed request identity mismatch'
        active = (ctrl[:, 2] == 1) & (ctrl[:, 3] == 1)
        nooverride = (state[:, 5] == 0) & (state[:, 6] == 0) & (state[:, 7] == 0)
        ok = (can[:, 1] == 1) & sv & ov & cv & pv & plv & active & nooverride & (state[:, 8] == 1) & (out[:, 6] == 0) & (out[:, 11] == 1)
        if m['is_maneuver']:
            ok[:] = False
        speed = np.maximum(0, state[:, 2] / 0.44704)
        raw = ctrl[:, 4]
        target = plan[:, 2]
        br = can[:, 3] == 1
        pre = can[:, 4] == 1
        comb = br | pre
        deficit = np.where((state[:, 4] > 0) & (state[:, 4] < 250), state[:, 4] / 1.609344 - speed, np.nan)
        dt = np.r_[np.diff(t), 0]
        dt = np.where((dt >= 0) & (dt <= 0.1), dt, 0)
        cont = ok & np.r_[False, ok[:-1] & (np.diff(t) <= 0.1) & (np.diff(t) > 0)]
        bt = changes(br, cont)
        pt = changes(pre, cont)
        ct = changes(comb, cont)
        rapid = np.zeros(len(t), bool)
        indices = np.flatnonzero(bt)
        for x, y in zip(indices[:-1], indices[1:]):
            if t[y] - t[x] < 0.6 and np.all(cont[x + 1:y + 1]):
                rapid[y] = True
        st = a['state']
        stt = st[:, 0]
        cs = np.r_[0, np.cumsum(st[:, 3])]
        lo = np.searchsorted(stt, stt - 0.2, side='left')
        sm = (cs[1:] - cs[lo]) / (np.arange(len(st)) + 1 - lo)
        pastix = np.searchsorted(stt, stt - 0.2, side='right') - 1
        jer = np.full(len(st), np.nan)
        valid = pastix >= 0
        jer[valid] = (sm[valid] - sm[pastix[valid]]) / (stt[valid] - stt[pastix[valid]])
        ji = np.searchsorted(stt, t, side='right') - 1
        jerk = jer[np.maximum(ji, 0)]
        versions = sorted(set((int(v) for v in out[ok, 12])))
        commits = sorted(set((q['commit'] for q in m['startup'])))
        clean = all((not q['dirty'] for q in m['startup'])) and len(m['startup']) >= len(m['segment_spans'])
        cohort = 'installed_V3' if clean and commits == ['e05e42f43d2907a4f02915a924cfd95a46197e79'] and (versions in ([3], [])) else 'prior_V1' if clean and commits == ['df788e02719c05595dab2f980e6fd9fb9e464006'] and (versions in ([1], [])) else 'other_or_mixed'

        def stats(mask):
            return summary(mask, dt, speed, br, pre, bt, pt, ct, rapid, raw, target, state[:, 3], jerk, tor, tv, ecu, ev, deficit, lead, rav, can[:, 5])
        bands = [dict(mph=[lo, hi if hi < 1000 else None], **stats(ok & (speed >= lo) & (speed < hi))) for lo, hi in BANDS]
        splits = {}
        for nam, mask in [('below40', speed < 40), ('40to85', (speed >= 40) & (speed < 85)), ('85plus', speed >= 85)]:
            for ln, lm in [('lead', rav & lead), ('no_lead', rav & ~lead), ('deficit_gt2mph', deficit > 2), ('deficit_lte2mph', deficit <= 2), ('neutral_request_plan', (speed >= 5) & (raw >= -0.1) & (raw <= 0.3) & (np.abs(target) <= 0.2))]:
                splits[nam + '_' + ln] = stats(ok & mask & lm)
        windows = []
        for below in [True, False]:
            candidates = []
            for center in np.flatnonzero(bt | pt)[::2]:
                start = t[center] - 3
                ii = np.flatnonzero((t >= start) & (t < start + 15))
                if len(ii) < 500 or np.mean(ok[ii]) < 0.95 or (not np.all(np.diff(t[ii]) <= 0.1)) or (not np.all((active & nooverride & (out[:, 6] == 0))[ii])):
                    continue
                if below and np.max(speed[ii]) >= 40:
                    continue
                if not below and (np.min(speed[ii]) < 40 or np.max(speed[ii]) >= 85):
                    continue
                score = int(bt[ii].sum() + pt[ii].sum())
                candidates.append((score, ii))
            selected = []
            for score, ii in sorted(candidates, key=lambda q: -q[0]):
                if any((abs(t[ii[0]] - q) < 20 for q in selected)):
                    continue
                selected.append(t[ii[0]])
                z = dict(below40=below, start_relative_s=float(t[ii[0]] - m['start_mono']), end_relative_s=float(t[ii[-1]] - m['start_mono']), qualified_fraction=float(np.mean(ok[ii])), excluded_samples=int((~ok[ii]).sum()), **stats(ok & np.isin(np.arange(len(t)), ii)), integral=safe(pi[ii, 3]), pitch_degrees=safe(ctrl[ii, 6] * 180 / np.pi), grade_offset=safe(out[ii, 18]), rpm=safe(rpm[ii[rv[ii]], 4]), engine_status=safe(eng[ii[engv[ii]], 4]), raw_zero_crossings=int(changes(raw > 0, cont)[ii].sum()), plan_zero_crossings=int(changes(target > 0, cont)[ii].sum()), lead_distance_m=safe(rad[ii[rav[ii] & lead[ii]], 3]), lead_vrel_mps=safe(rad[ii[rav[ii] & lead[ii]], 4]))
                name = f"{label}-{m['drive']}-{('below40' if below else 'highway')}-{len(selected)}.csv"
                z['csv'] = name
                with (P / name).open('w') as stream:
                    w = csv.writer(stream)
                    w.writerow(['relative_s', 'mph', 'cruise_mph', 'deficit_mph', 'plan_accel', 'raw_accel', 'integral', 'pitch_deg', 'grade_offset', 'actual_accel', 'jerk_200ms', 'brake_request', 'precharge_request', 'propulsion_request', 'brake_accel_request', 'ecu_brake_active', 'ecu_precharge_active', 'actual_brake_torque_Nm', 'requested_brake_torque_Nm', 'rpm', 'engine_status', 'lead', 'distance_m', 'vrel_mps', 'state_age', 'output_age'])
                    for i in ii[::5]:
                        w.writerow([t[i] - m['start_mono'], speed[i], state[i, 4] / 1.609344, deficit[i], target[i], raw[i], pi[i, 3], ctrl[i, 6] * 180 / np.pi, out[i, 18], state[i, 3], jerk[i], int(br[i]), int(pre[i]), can[i, 5], can[i, 6], ecu[i, 5] if ev[i] else '', ecu[i, 2] if ev[i] else '', tor[i, 3] if tv[i] else '', tor[i, 2] if tv[i] else '', rpm[i, 4] if rv[i] else '', eng[i, 4] if engv[i] else '', int(lead[i]) if rav[i] else '', rad[i, 3] if rav[i] else '', rad[i, 4] if rav[i] else '', t[i] - state[i, 0], t[i] - out[i, 0]])
                windows.append(z)
                if len(selected) >= 3:
                    break
        restarts = []
        off = None
        running = True
        for i in range(len(t)):
            if not rv[i]:
                continue
            n = rpm[i, 4]
            if n < 100:
                off = i
                running = False
            if n > 400 and (not running):
                if off is not None and t[i] - t[off] <= 10 and ok[i]:
                    ii = np.flatnonzero((t >= t[i] - 2) & (t < t[i] + 3) & ok)
                    restarts.append(dict(relative_s=float(t[i] - m['start_mono']), mph=float(speed[i]), rpm=float(n), last_off_age=float(t[i] - t[off]), brake=bool(br[i]), precharge=bool(pre[i]), target=float(target[i]), raw=float(raw[i]), actual_accel_5s=safe(state[ii, 3]), jerk_200ms_5s=safe(jerk[ii]), integral_5s=safe(pi[ii, 3])))
                running = True
        coast = ok & ~comb & (speed >= 5) & (np.abs(can[:, 5] + 5) < 1e-06)
        runs = []
        start = None
        for i in range(len(t) + 1):
            here = i < len(t) and coast[i] and (i == 0 or start is None or cont[i])
            if here and start is None:
                start = i
            if start is not None and (not here):
                jj = np.arange(start, i)
                runs.append(dict(start_relative_s=float(t[start] - m['start_mono']), duration_s=float(dt[jj].sum()), speed_range_mph=[float(speed[jj].min()), float(speed[jj].max())], raw_range=[float(raw[jj].min()), float(raw[jj].max())], plan_range=[float(target[jj].min()), float(target[jj].max())], lead_fraction=float(np.mean(lead[jj] & rav[jj]))))
                start = None
        coast_runs = dict(count=len(runs), duration_s=safe([q['duration_s'] for q in runs]), under_point3_s=sum((q['duration_s'] <= 0.3 for q in runs)), under1_s=sum((q['duration_s'] < 1 for q in runs)), runs=runs)
        reason_metrics = {name: stats(ok & (out[:, 10] == ri)) for ri, name in enumerate(m['reasons'])}
        boundid = m['reasons'].index('bounded_coast_pending') if 'bounded_coast_pending' in m['reasons'] else -100
        marker = (out[:, 15] == 3) & (out[:, 14] == 1) & (out[:, 4] == 0) & (out[:, 13] == 0) & (out[:, 3] == -5) & (out[:, 5] == 1) & (out[:, 12] == 3) & np.isfinite(out[:, 16]) & np.isfinite(out[:, 17]) & (out[:, 16] >= 0) & (out[:, 16] < 0.300000001) & (out[:, 17] > 0) & (out[:, 17] <= 0.01)
        boundmask = ok & (out[:, 10] == boundid) & marker
        boundout = a['output'][a['output'][:, 10] == boundid]
        odt = np.r_[np.diff(a['output'][:, 0]), 0]
        odt = np.where((odt >= 0) & (odt <= 0.1), odt, 0)
        boundduration = float(odt[a['output'][:, 10] == boundid].sum())
        bounded = dict(feedback_duration_s=boundduration, qualified=stats(boundmask), feedback_rows=len(boundout), feedback_all_full_precharge_clear=bool(len(boundout) and np.all((boundout[:, 4] == 0) & (boundout[:, 13] == 0))), sample_relative_s=[float(t[i] - m['start_mono']) for i in np.flatnonzero(boundmask)], integral=safe(pi[boundmask, 3]), grade_offset=safe(out[boundmask, 18]))
        fo = a['output']
        fm = (fo[:, 10] == boundid) & (fo[:, 15] == 3) & (fo[:, 14] == 1) & (fo[:, 4] == 0) & (fo[:, 13] == 0) & (fo[:, 3] == -5) & (fo[:, 5] == 1) & (fo[:, 12] == 3) & (fo[:, 1] == 1) & (fo[:, 11] == 1) & (fo[:, 6] == 0) & np.isfinite(fo[:, 16]) & np.isfinite(fo[:, 17]) & (fo[:, 16] >= 0) & (fo[:, 16] < 0.300000001) & (fo[:, 17] > 0) & (fo[:, 17] <= 0.01)
        bounded.update(marker_rows=int(fm.sum()), marker_duration_s=float(odt[fm].sum()), marker_runs=int(np.sum(fm & np.r_[True, ~fm[:-1]])), marker_unique_consumed_requests=len(np.unique(fo[fm, 7:9], axis=0)), precharge_age_s=safe(fo[fm, 16]), budget_remaining=safe(fo[fm, 17]))
        if np.any(boundmask):
            near = np.zeros(len(t), bool)
            for k in np.flatnonzero(boundmask):
                near |= np.abs(t - t[k]) <= 0.5
            name = f"{label}-{m['drive']}-bounded-coast.csv"
            bounded['csv'] = name
            with (P / name).open('w') as stream:
                w = csv.writer(stream)
                w.writerow(['relative_s', 'qualified', 'mph', 'full_brake', 'precharge', 'past_feedback_reason', 'feedback_full_brake', 'feedback_precharge', 'output_age_s', 'raw', 'plan', 'actual_accel', 'integral', 'actual_brake_torque_Nm', 'ecu_active', 'ecu_precharge'])
                for i in np.flatnonzero(near):
                    w.writerow([t[i] - m['start_mono'], int(ok[i]), speed[i], int(br[i]), int(pre[i]), m['reasons'][int(out[i, 10])], int(out[i, 4]), int(out[i, 13]), t[i] - out[i, 0], raw[i], target[i], state[i, 3], pi[i, 3], tor[i, 3] if tv[i] else '', ecu[i, 5] if ev[i] else '', ecu[i, 2] if ev[i] else ''])
        result = dict(reason_metrics=reason_metrics, bounded_coast=bounded, inactive_propulsion_command_runs=coast_runs, label=label, drive=m['drive'], cohort=cohort, commits=commits, allocator_versions=versions, recorded_s=m['duration_s'], eligibility_exposure=dict(active_nooverride_s=float(dt[active & nooverride & sv & cv].sum()), excluded_from_active_nooverride_s=float(dt[active & nooverride & sv & cv & ~ok].sum()), active_nooverride_feedback_fault_s=float(dt[active & nooverride & sv & cv & ov & (out[:, 6] == 1)].sum()), inactive_or_override_s=float(dt[~(active & nooverride)].sum())), start_mono=m['start_mono'], qualification_counts=dict(can=len(t), state_fresh=int(sv.sum()), output_fresh=int(ov.sum()), matched_control=int(cv.sum()), pid_fresh=int(pv.sum()), exact_plan_fresh=int(plv.sum()), active=int(active.sum()), nooverride=int(nooverride.sum()), qualified=int(ok.sum())), overall=stats(ok), bands=bands, splits=splits, windows=windows, restarts=restarts)
        results.append(result)
        (P / 'metrics.json').write_text(json.dumps(results, indent=2, allow_nan=False) + '\n')
        print(label, m['drive'], cohort, result['qualification_counts'], 'ACTIVE', result['overall']['active_s'], flush=True)
