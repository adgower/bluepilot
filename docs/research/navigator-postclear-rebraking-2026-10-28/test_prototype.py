import os
from pathlib import Path
"""Adapter checks against actual GradeLease and request-validity contract."""
import unittest
from types import SimpleNamespace as N
from prototype import scope, DiagnosticGradeLease
from opendbc.car.ford.longitudinal_coordination import GradeLease
from opendbc.car.ford.longitudinal_precharge import PRECHARGE_PROTOCOL_VERSION

def context():
    q = N(allocatorVersion=PRECHARGE_PROTOCOL_VERSION, targetValid=True, targetAcceleration=0.1, targetMonoTime=1000000000, producerMonoTime=1000000000, poseValid=True, referenceValid=True)
    cc = N(navigatorLongitudinal=q, enabled=True, longActive=True, actuators=N(accel=0.2, longControlState='pid'), hudControl=N(visualAlert='none'))
    cs = N(out=N(vEgo=50 / 2.236936, canValid=True, gasPressed=False, brakePressed=False))
    return (cc, cs)

class AdapterTests(unittest.TestCase):

    def test_active_weak_context_qualifies(self):
        cc, cs = context()
        self.assertEqual(scope(cc, cs, 1000000000), 1.0)

    def test_negative_or_strong_target_is_unfiltered(self):
        for target in [-1.0, -0.01, 0.51]:
            cc, cs = context()
            cc.navigatorLongitudinal.targetAcceleration = target
            self.assertEqual(scope(cc, cs, 1000000000), 0.0)

    def test_pedals_fcw_stop_and_invalid_reference_are_unfiltered(self):
        cases = ['gas', 'brake', 'fcw', 'stopping', 'reference', 'can', 'stale']
        for case in cases:
            cc, cs = context()
            now = 1000000000
            if case == 'gas':
                cs.out.gasPressed = True
            if case == 'brake':
                cs.out.brakePressed = True
            if case == 'fcw':
                cc.hudControl.visualAlert = 'fcw'
            if case == 'stopping':
                cc.actuators.longControlState = 'stopping'
            if case == 'reference':
                cc.navigatorLongitudinal.referenceValid = False
            if case == 'can':
                cs.out.canValid = False
            if case == 'stale':
                now += 110000000
            self.assertEqual(scope(cc, cs, now), 0.0, case)

    def test_outside_speed_band_is_unfiltered(self):
        for mph in [0.0, 15.0, 25.0, 35.0, 75.0, 85.0]:
            cc, cs = context()
            cs.out.vEgo = mph / 2.236936
            self.assertAlmostEqual(scope(cc, cs, 1000000000), 0.0, places=12)

    def test_preserves_grade_offset_and_caps_selected_correction(self):
        base = GradeLease(True)
        candidate = DiagnosticGradeLease(True)
        candidate.weight = 1.0
        for t, g in [(1.0, -0.2), (1.02, -0.1)]:
            b = base.update(t, g, t, True, True, 20.0, 'pid')
            c = candidate.update(t, g, t, True, True, 20.0, 'pid')
            self.assertEqual(b.offset, c.offset)
            self.assertEqual(b.reason, c.reason)
            self.assertLessEqual(abs(b.gravity - c.gravity), 0.05 + 1e-12)
        self.assertNotEqual(b.gravity, c.gravity)

    def test_disabled_weight_has_exact_native_parity(self):
        b = GradeLease(True)
        c = DiagnosticGradeLease(True)
        for i in range(100):
            t = 1.0 + i * 0.02
            g = -0.2 + (0.04 if i % 2 else -0.04)
            self.assertEqual(b.update(t, g, t, True, True, 20.0, 'pid'), c.update(t, g, t, True, True, 20.0, 'pid'))

    def test_invalid_pose_remains_native_invalid(self):
        b = GradeLease(True)
        c = DiagnosticGradeLease(True)
        c.weight = 1.0
        self.assertEqual(b.update(1.0, -0.1, 0.7, True, True, 20.0, 'pid'), c.update(1.0, -0.1, 0.7, True, True, 20.0, 'pid'))
if __name__ == '__main__':
    unittest.main()
