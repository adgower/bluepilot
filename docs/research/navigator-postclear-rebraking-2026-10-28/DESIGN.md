<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local grade-bandwidth diagnostic

The user authorized a local prototype and replay, preserving paired sources and device state. This is a throwaway diagnostic, not a calibration or controller integration.

Recorded request attribution is mixed: five pitch-gravity dominated, four I dominated, three planner dominated, one without an intervening released callback. GradeOffset is constant at all endpoints; the static OEM-fitted zero is not retuned. OEM and Alpha pitch-span distributions overlap, and routes/lead/grades are not identical.

Test one fixed causal 250 ms first-order grade filter with at most 0.05 m/s² decision-reference correction. These are declared diagnostic parameters, not fitted physical constants or a tolerance search. Track only fresh valid data with continuity. Preserve DC, existing GradeLease offset/slew, raw acceleration and numerical brake fields. Fade scope from 35–40 and 70–75 mph; target must be nonnegative and <=0.5, raw request >0.02, active PID, valid pose/reference/CAN, no pedals or FCW. Strong/negative planner demand bypasses immediately. No new integral filter, reset, copied PID, pose calibration, native threshold, handoff or clearance change.

Implement through research-only monkeypatches in the existing source-bound producer/consumer runner. The original shared allocator and observed-clearance classes remain intact. However filtering changes their decision reference: a filter cannot be credited as harmless noise removal or new coast authority. Explicitly audit nominal brake omissions against the original baseline, including locked-account cases. Such cases remain unsupported without an independent grade/coast response model even if edge counts decline. All raw/I/freeze, stronger braking, exposure, faults, retained-torque propulsion and ownership gates remain decisive.

Run focused 21-segment paired replay and city/highway regressions before deciding whether broader replay is justified. Reject fewer transitions achieved through extra braking, weaker strong requests, budget/clearance bypass or unsupported nominal omission. Frozen state/pose/torque cannot establish changed physical comfort or counterfactual grade response. Do not expand parameters if this declared diagnostic fails.
