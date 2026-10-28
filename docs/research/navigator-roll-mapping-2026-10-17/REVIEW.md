<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent review

Read-only reviewer `/root/review_roll_mapping` reviewed the mapping, replay seam and transition screen separately from implementation. No Comma connection or changes.

- Found a requested-reversal gap when measured pinion curvature keeps the deviation-clipped feedforward sign unchanged. Fixed by tracking requested curvature sign rather than clipped feedforward sign. A new regression reproduces the failure against an isolated pre-fix copy (`clipped-reversal-red.txt`); current source passes.
- Confirmed native fixed pinion model, inherited command limits and truthful shadow intent remain unchanged. No remaining concrete mapping/native-hook defect reported after re-review. Reviewer independently ran the then-current 26 tests successfully.
- Identified a counting ambiguity: raw route receipts count held mapping status on every 100Hz controller update. Final `verification.json` deliberately counts only actual steering-TX evaluations, not held status.
- Requested explicit cadence/stale-state/stale-control/invalid-model abort assertions. Added six focused established-mapping abort cases; main agent ran the expanded 35-test suite, including three zero-roll calibration consistency cases. The transition matrix's cadence scenario remains an injected transition; its explicit clearance assertion is in the focused suite.
- Confirmed a scope limitation: using the same learned vehicle model for the desired-angle forward/inverse transform cancels ratio/offset effects at zero roll. This prototype is roll-compensation sensitivity with calibration consistency gating; it is not an independently identified learned-ratio or actuator-gain remap.

Review and native replay are local evidence only, not hardware or road validation.
