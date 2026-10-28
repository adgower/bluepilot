import os
from pathlib import Path
"""Past-only alignment and whole-episode selection; no fitting or device access."""
import numpy as np
from estimator import Episode

def align_past(rows, t):
    rows = np.asarray(rows, float)
    t = np.asarray(t, float)
    if rows.ndim != 2 or len(rows) == 0:
        raise ValueError('empty or malformed stream')
    if np.any(np.diff(rows[:, 0]) < 0):
        raise ValueError('unsorted stream')
    idx = np.searchsorted(rows[:, 0], t, side='right') - 1
    result = rows[np.maximum(idx, 0)].copy()
    age = t - result[:, 0]
    result[idx < 0] = np.nan
    age[idx < 0] = np.inf
    return (result, age)

def split_episodes(route, data, band):
    t = data['t']
    mph = data['mph']
    bandmask = (mph >= band[0]) & (mph < band[1])
    mask = data['eligible'] & bandmask
    stats = dict(in_band_frames=int(bandmask.sum()), eligible_frames=int(mask.sum()), accepted_episodes=0, rejected_short=0, rejected_unexcited=0, rejected_speed_drift=0)
    edges = np.diff(np.r_[False, mask, False].astype(int))
    starts = np.flatnonzero(edges == 1)
    ends = np.flatnonzero(edges == -1)
    episodes = []
    for start, end in zip(starts, ends):
        for a in range(start, end, 240):
            b = min(a + 240, end)
            if b - a < 80:
                stats['rejected_short'] += 1
                continue
            u = data['u'][a:b]
            if np.ptp(u) < 0.004 or np.std(u) < 0.001:
                stats['rejected_unexcited'] += 1
                continue
            if np.ptp(mph[a:b]) > 3.0:
                stats['rejected_speed_drift'] += 1
                continue
            episodes.append(Episode(route, t[a:b], u, data['y'][a:b], mph[a:b], data['reference'][a:b]))
    stats['accepted_episodes'] = len(episodes)
    return (episodes, stats)
