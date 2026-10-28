import os
from pathlib import Path
"""Pure offline implementation contract. No vehicle, network or settings access."""
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class Episode:
    route: str
    t: np.ndarray
    u: np.ndarray
    y: np.ndarray
    mph: np.ndarray
    reference: np.ndarray

    def __post_init__(self):
        n = len(self.t)
        if n < 60 or any((np.shape(x) != (n,) for x in [self.u, self.y, self.mph, self.reference])):
            raise ValueError('episode too short or shape mismatch')
        if not all((np.isfinite(x).all() for x in [self.t, self.u, self.y, self.mph, self.reference])):
            raise ValueError('nonfinite episode')
        if not np.all(abs(np.diff(self.t) - 0.05) < 1e-05):
            raise ValueError('episode has gap or wrong cadence')
from scipy.signal import lfilter
DELAYS = np.arange(0.0, 1.001, 0.05)
TAUS = np.array([0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.6, 0.8, 1.0, 1.25])
BURN_S = 1.25

def _basis(e, delay, tau):
    dt = 0.05
    a = np.exp(-dt / tau)
    time = e.t - e.t[0]
    delayed = np.interp(e.t - delay, e.t, e.u, left=e.u[0])
    driven = lfilter([0.0, 1.0 - a], [1.0, -a], delayed)
    initial = a ** np.arange(len(time)) * e.y[0]
    return (np.c_[driven, 1.0 - a ** np.arange(len(time))], initial)

def _solve(x, y, weights, robust=True):
    scale = np.linalg.norm(x, axis=0)
    if np.any(scale < 1e-10) or np.linalg.cond(x / scale) > 100:
        raise ValueError('gain/bias rank deficient')
    w = weights.copy()
    for _ in range(3 if robust else 1):
        coef = np.linalg.lstsq(x * w[:, None], y * w, rcond=None)[0]
        residual = y - x @ coef
        mad = max(5e-05, 1.4826 * float(np.median(abs(residual - np.median(residual)))))
        w = weights * np.sqrt(np.minimum(1.0, 1.5 * mad / np.maximum(abs(residual), 1e-12)))
    return coef

def _design(episodes, delay, tau):
    xs = []
    ys = []
    ws = []
    groups = []
    for n, e in enumerate(episodes):
        x, initial = _basis(e, delay, tau)
        m = e.t - e.t[0] >= BURN_S
        xs.append(x[m])
        ys.append(e.y[m] - initial[m])
        ws.append(np.full(m.sum(), 1 / np.sqrt(m.sum())))
        groups.append(np.full(m.sum(), n))
    return (np.concatenate(xs), np.concatenate(ys), np.concatenate(ws), np.concatenate(groups))

def _support(episodes):
    if len(episodes) < 2:
        raise ValueError('too few episodes')
    u = np.concatenate([e.u for e in episodes])
    if np.ptp(u) < 0.006 or np.std(u) < 0.002:
        raise ValueError('insufficient input variation')
    if np.sum(u > 0.002) < 20 or np.sum(u < -0.002) < 20:
        raise ValueError('one_direction_input')

def fit_model(episodes):
    _support(episodes)
    candidates = []

    def evaluate(delay, tau):
        x, y, w, _ = _design(episodes, float(delay), float(tau))
        try:
            coef = _solve(x, y, w)
        except ValueError:
            return
        if not 0.01 < coef[0] < 10:
            return
        residual = y - x @ coef
        limit = max(0.0001, float(np.percentile(abs(residual), 90)))
        loss = float(np.sqrt(np.mean(np.minimum(residual ** 2, limit ** 2))))
        candidates.append(dict(gain=float(coef[0]), bias=float(coef[1]), delay_s=float(delay), tau_s=float(tau), training_loss=loss))
    for delay in DELAYS:
        for tau in TAUS:
            evaluate(delay, tau)
    if not candidates:
        raise ValueError('no identifiable positive model')
    best = min(candidates, key=lambda x: x['training_loss'])
    for delay in np.arange(max(0.0, best['delay_s'] - 0.05), min(1.0, best['delay_s'] + 0.05) + 0.001, 0.025):
        for tau in np.arange(max(0.025, best['tau_s'] - 0.05), min(1.3, best['tau_s'] + 0.05) + 0.001, 0.025):
            evaluate(delay, tau)
    best = min(candidates, key=lambda x: x['training_loss']).copy()
    near = [c for c in candidates if c['training_loss'] <= best['training_loss'] + max(5e-05, best['training_loss'] * 0.1)]
    best['profile_delay_range_s'] = [min((c['delay_s'] for c in near)), max((c['delay_s'] for c in near))]
    best['profile_tau_range_s'] = [min((c['tau_s'] for c in near)), max((c['tau_s'] for c in near))]
    best['profile_gain_range'] = [min((c['gain'] for c in near)), max((c['gain'] for c in near))]
    return best

def predict(model, episode):
    x, initial = _basis(episode, model['delay_s'], model['tau_s'])
    return initial + x @ np.array([model['gain'], model['bias']])

def _quality(model, episodes):
    errors = []
    ys = []
    refs = []
    inputs = []
    route_errors = {}
    route_series = {}
    for e in episodes:
        m = e.t - e.t[0] >= BURN_S
        error = e.y[m] - predict(model, e)[m]
        errors.append(error)
        ys.append(e.y[m])
        refs.append(e.reference[m])
        inputs.append(e.u[m])
        route_errors.setdefault(e.route, []).append(error)
        route_series.setdefault(e.route, []).append((error, e.y[m], e.u[m], e.reference[m]))
    err = np.concatenate(errors)
    y = np.concatenate(ys)
    ref = np.concatenate(refs)
    u = np.concatenate(inputs)
    rms = float(np.sqrt(np.mean(err ** 2)))
    scale = max(0.001, float(np.percentile(y, 90) - np.percentile(y, 10)))
    corrs = []
    for series in [ref, u]:
        corrs.append(float(np.corrcoef(err, series)[0, 1]) if np.std(series) > 1e-10 and np.std(err) > 1e-10 else 0.0)
    route_metrics = {}
    for route, pieces in route_series.items():
        er, yr, ur, rr = [np.concatenate([x[i] for x in pieces]) for i in range(4)]
        c = [float(abs(np.corrcoef(er, x)[0, 1])) if np.std(x) > 1e-10 and np.std(er) > 1e-10 else 0.0 for x in [ur, rr]]
        route_metrics[route] = dict(normalized_rmse=float(np.sqrt(np.mean(er ** 2)) / max(0.001, float(np.percentile(yr, 90) - np.percentile(yr, 10)))), max_residual_dependence=max(c))
    return dict(route_metrics=route_metrics, rmse_yaw_rad_s=rms, normalized_rmse=rms / scale, max_residual_input_reference_correlation=max((abs(x) for x in corrs)), route_rmse={k: float(np.sqrt(np.mean(np.concatenate(v) ** 2))) for k, v in route_errors.items()})

def assess(train, test):
    train_routes = sorted({e.route for e in train})
    test_routes = sorted({e.route for e in test})
    overlap = sorted(set(train_routes) & set(test_routes))
    if overlap:
        raise ValueError('whole-route validation leakage: ' + ','.join(overlap))
    out = dict(predictive_supported=False, reasons=[], train_routes=len(train_routes), test_routes=len(test_routes), route_overlap=overlap, causal_identified=False, automatic_application=False, controller_map_validated=False, model=None, conditional_gain_interval=None, conditional_bias_interval=None, steady_gain_supported=False, dynamics_identified=False, identification_reasons=['not_fitted'])
    if len(train_routes) < 2 or len(test_routes) < 2 or len(train) < 6 or (len(test) < 3):
        out['reasons'].append('insufficient_independent_route_episodes')
    if sum((e.t[-1] - e.t[0] for e in train)) < 20 or sum((e.t[-1] - e.t[0] for e in test)) < 10:
        out['reasons'].append('insufficient_duration')
    try:
        _support(train)
        _support(test)
    except ValueError as exc:
        out['reasons'].append(str(exc))
        return out
    if out['reasons']:
        return out
    try:
        model = fit_model(train)
    except ValueError as exc:
        out['reasons'].append(str(exc))
        return out
    out['model'] = model
    out['training'] = _quality(model, train)
    out['held_out'] = _quality(model, test)
    if out['held_out']['normalized_rmse'] > 0.25:
        out['reasons'].append('held_out_prediction')
    tx, ty, tw, _ = _design(test, model['delay_s'], model['tau_s'])
    try:
        held_gain = float(_solve(tx, ty, tw)[0])
        out['held_out_gain'] = held_gain
        if abs(held_gain / model['gain'] - 1) > 0.25:
            out['reasons'].append('held_out_gain_shift')
    except ValueError:
        out['reasons'].append('held_out_gain_unidentifiable')
    if out['held_out']['max_residual_input_reference_correlation'] > 0.35:
        out['reasons'].append('residual_input_dependence')
    if any((x['max_residual_dependence'] > 0.35 or x['normalized_rmse'] > 0.25 for x in out['held_out']['route_metrics'].values())):
        out['reasons'].append('held_out_route_dependence')
    out['dynamics_identified'] = not profile_ambiguous(model)
    out['identification_reasons'] = [] if out['dynamics_identified'] else ['dynamics_ambiguous']
    x, y, w, groups = _design(train, model['delay_s'], model['tau_s'])
    rng = np.random.default_rng(73)
    draws = []
    route_masks = [np.isin(groups, [i for i, e in enumerate(train) if e.route == route]) for route in train_routes]
    for _ in range(100):
        ids = np.concatenate([np.flatnonzero(route_masks[i]) for i in rng.integers(0, len(route_masks), len(route_masks))])
        try:
            draws.append(_solve(x[ids], y[ids], w[ids], robust=True).tolist())
        except ValueError:
            pass
    if len(draws) < 50:
        out['reasons'].append('gain_uncertainty_unidentifiable')
    else:
        bounds = np.percentile(draws, [2.5, 97.5], axis=0)
        interval = bounds[:, 0]
        out['conditional_gain_interval'] = interval.tolist()
        out['conditional_bias_interval'] = bounds[:, 1].tolist()
        if (interval[1] - interval[0]) / max(model['gain'], 0.001) > 0.3:
            out['reasons'].append('gain_varies_across_routes')
    out['predictive_supported'] = not out['reasons']
    out['steady_gain_supported'] = bool(out['predictive_supported'] and np.ptp(model['profile_gain_range']) / model['gain'] <= 0.3)
    if not out['steady_gain_supported'] and out['predictive_supported']:
        out['identification_reasons'].append('gain_dynamic_tradeoff')
    return out

def profile_ambiguous(model):
    return np.ptp(model['profile_delay_range_s']) > 0.3 + 1e-09 or np.ptp(model['profile_tau_range_s']) > 0.6 + 1e-09

def cross_validate_routes(episodes):
    routes = sorted({e.route for e in episodes})
    out = dict(routes=len(routes), folds=[], median_gain=None, causal_identified=False, validated=False, reasons=[])
    if len(routes) < 4 or len(episodes) < 10:
        out['reasons'] = ['insufficient_historical_routes_or_episodes']
        return out
    for route in routes:
        train = [e for e in episodes if e.route != route]
        test = [e for e in episodes if e.route == route]
        fold = dict(held_route=route, train_routes=sorted({e.route for e in train}), train_episodes=len(train), test_episodes=len(test))
        if len(train) < 6:
            fold['reason'] = 'insufficient_training_episodes'
            out['folds'].append(fold)
            continue
        try:
            _support(train)
            _support(test)
            model = fit_model(train)
        except ValueError as exc:
            fold['reason'] = str(exc)
            out['folds'].append(fold)
            continue
        quality = _quality(model, test)
        fold.update(model=model, held_out=quality)
        fold['prediction_pass'] = quality['normalized_rmse'] <= 0.25 and quality['max_residual_input_reference_correlation'] <= 0.35
        out['folds'].append(fold)
    models = [x['model'] for x in out['folds'] if 'model' in x]
    if models:
        out['median_gain'] = float(np.median([x['gain'] for x in models]))
    out['validated'] = len(models) == len(routes) and all((x['prediction_pass'] for x in out['folds']))
    if not out['validated']:
        out['reasons'] = ['historical_route_folds_fail_or_lack_support']
    return out
