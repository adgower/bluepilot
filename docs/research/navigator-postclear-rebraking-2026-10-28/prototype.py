import os
from pathlib import Path
"""Research-only grade filter injection. No paired source or transport changes.
This diagnostic has no independent physical grade/coast authority. Its nominal
brake omissions and original-account state must be audited, not called harmless.
"""
import math, collections
from opendbc.car.ford.longitudinal_coordination import GradeLease, GradeResult
from opendbc.car.ford.longitudinal_precharge import allocator_request_valid
from policy import DecisionGrade
RECEIPTS = {}
COUNTS = collections.Counter()

def key(f):
    return (f.epoch, f.sequence, round(f.t * 1000000000.0))

def scope(CC, CS, now):
    q = CC.navigatorLongitudinal
    mph = CS.out.vEgo * 2.236936
    weight = max(0.0, min(1.0, (mph - 35) / 5, (75 - mph) / 5))
    valid = CC.enabled and CC.longActive and CS.out.canValid and (not CS.out.gasPressed) and (not CS.out.brakePressed) and (str(CC.actuators.longControlState) == 'pid') and (str(CC.hudControl.visualAlert) != 'fcw') and q.poseValid and q.referenceValid and allocator_request_valid(q, now) and (0 <= q.targetAcceleration <= 0.5) and (CC.actuators.accel > 0.02)
    return weight if valid else 0.0

class DiagnosticGradeLease(GradeLease):

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.filter = DecisionGrade()
        self.weight = 0.0
        self.diagnostic = {}

    def update(self, now, pitch, pose_t, pose_valid, active, speed, phase, reference_valid=True):
        native = super().update(now, pitch, pose_t, pose_valid, active, speed, phase, reference_valid)
        valid = bool(self.enabled and active and pose_valid and reference_valid and (phase == 'pid') and (native.reason == 'mapped') and all((math.isfinite(x) for x in (now, native.gravity, pose_t))) and (0 <= now - pose_t <= 0.1))
        filtered = self.filter.update(now, native.gravity, valid=valid, enabled=self.weight > 0)
        delta = self.weight * (filtered - native.gravity) if valid else 0.0
        self.diagnostic = {'native_gravity': native.gravity, 'filtered_gravity': filtered, 'selected_delta': delta, 'weight': self.weight, 'valid': valid}
        if abs(delta) > 1e-12:
            COUNTS['changed_grade_callbacks'] += 1
        COUNTS['maximum_abs_grade_delta'] = max(COUNTS['maximum_abs_grade_delta'], abs(delta))
        return GradeResult(native.gravity + delta, native.offset, native.reason)

def install():
    from opendbc.car.ford import carcontroller as cm
    original_update = cm.CarController.update
    cm.GradeLease = DiagnosticGradeLease

    def update(self, CC, CS, now):
        self.grade_map.weight = scope(CC, CS, now)
        return original_update(self, CC, CS, now)
    cm.CarController.update = update
