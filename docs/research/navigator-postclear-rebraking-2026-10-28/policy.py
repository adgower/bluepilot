import os
from pathlib import Path
"""Fixed-parameter causal grade bandwidth diagnostic, not a validated grade model."""
import math

class DecisionGrade:

    def __init__(self, tau=0.25, cap=0.05):
        assert math.isfinite(tau) and tau > 0 and math.isfinite(cap) and (cap > 0)
        self.tau, self.cap = (tau, cap)
        self.last = None
        self.value = None

    def update(self, now, gravity, *, valid=True, enabled=True):
        finite = all((math.isfinite(v) for v in (now, gravity)))
        dt = None if self.last is None else now - self.last
        if not finite or not valid or (not enabled) or (dt is not None and (not 0 < dt <= 0.100000001)):
            self.last = now if finite else None
            self.value = gravity if finite else None
            return gravity
        self.last = now
        if self.value is None or dt is None:
            self.value = gravity
        else:
            alpha = -math.expm1(-dt / self.tau)
            self.value += alpha * (gravity - self.value)
        return gravity + max(-self.cap, min(self.cap, self.value - gravity))
