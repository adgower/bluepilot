<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent review

Reviewer `/root/review_highspeed_trial` examined the bounded prototype, tests, replay harness, calibration data flow, source snapshots and scene replay without editing files or accessing the device.

Initial important findings resolved before the accepted full replay:

1. Preserve carState event-envelope validity rather than relying solely on payload CAN validity. The new correction now has a separate `input_state_valid` gate; both raw-event harnesses populate it, and synthetic calibration validity also incorporates it. Added active-to-invalid transition test. Production integration would need an equivalent producer/consumer contract; this package is deliberately not integrated.
2. Capture source hashes at worker startup, verify unchanged at completion, and require identical snapshots across all workers. Includes both installed HEADs, all Ford Python sources, VM/context helpers, native library and experiment/harness sources. Early exploratory runs were stopped; only the restarted verified-snapshot full run counts as acceptance evidence.

Re-review found no additional concrete blocker by inspection. Qualifications retained:

- Withdrawal means more than 10% retreat within the six-frame window. Slow continuous unwind can remain eligible. Added explicit slow-unwind characterization; all outputs remain reduction-only and bounded. No claim of universal unwind suppression.
- Scene reference fidelity must be checked before interpreting counterfactual changes; the final evidence verifier asserts exact all-active half-wire-step coverage. Scene replay alone merely reports fidelity.

Inspection and native replay do not establish physical vehicle response or road readiness.
