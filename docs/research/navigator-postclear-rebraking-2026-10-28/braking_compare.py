import os
from pathlib import Path
"""Encoded demand is checked independently of the producer's raw ordering."""

def strong_pair(target, baseline_raw, candidate_raw, baseline_data, candidate_data):

    def value(data):
        raw = (data[0] & 31) << 8 | data[1]
        return raw * 0.0039 - 20.0
    delta = value(candidate_data) - value(baseline_data)
    strong = target <= -0.5
    return {'weaker_raw': bool(strong and candidate_raw > baseline_raw + 1e-06), 'weaker_encoded': bool(strong and delta > 1e-09), 'encoded_delta': delta}
