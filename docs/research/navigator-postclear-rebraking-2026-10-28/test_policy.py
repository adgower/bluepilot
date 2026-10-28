import os
from pathlib import Path
import math
import unittest
from policy import DecisionGrade

class DecisionGradeTests(unittest.TestCase):

    def test_reduces_short_grade_oscillation_without_recalibrating_dc(self):
        p = DecisionGrade()
        p.update(0.0, -0.2)
        filtered = [p.update(i * 0.02, -0.2 + (0.04 if i % 2 else -0.04)) for i in range(1, 30)]
        self.assertLess(max(filtered) - min(filtered), 0.04)
        self.assertLess(abs(sum(filtered) / len(filtered) + 0.2), 0.01)

    def test_constant_input_is_unchanged(self):
        p = DecisionGrade()
        for i in range(100):
            self.assertEqual(p.update(i * 0.02, -0.17), -0.17)

    def test_correction_is_capped(self):
        p = DecisionGrade()
        p.update(0.0, -0.4)
        value = p.update(0.02, 0.4)
        self.assertGreaterEqual(value, 0.35 - 1e-12)
        self.assertLessEqual(value, 0.45 + 1e-12)

    def test_invalid_and_disabled_inputs_pass_through(self):
        for kwargs in ({'valid': False}, {'enabled': False}):
            p = DecisionGrade()
            p.update(0.0, -0.4)
            self.assertEqual(p.update(0.02, 0.4, **kwargs), 0.4)

    def test_duplicate_or_reversed_clock_does_not_invent_filter_history(self):
        for t in (0.0, -0.02):
            p = DecisionGrade()
            p.update(0.0, -0.4)
            self.assertEqual(p.update(t, 0.2), 0.2)

    def test_gap_restarts_at_current_observation(self):
        p = DecisionGrade()
        p.update(0.0, -0.4)
        self.assertEqual(p.update(0.2, 0.2), 0.2)

    def test_no_constant_zero_bias_after_settling(self):
        p = DecisionGrade()
        p.update(0.0, -0.4)
        for i in range(1, 300):
            out = p.update(i * 0.02, -0.1)
        self.assertAlmostEqual(out, -0.1, places=8)
if __name__ == '__main__':
    unittest.main()
