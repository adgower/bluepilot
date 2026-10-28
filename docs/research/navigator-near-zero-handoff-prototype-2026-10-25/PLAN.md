<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Near-zero handoff prototype implementation plan

Goal: test the authorized bounded coast-state/integral-settling experiment against actual saved drive inputs.
Architecture: separate research-only policy and actual-controller/producer overlays, causal paired feedback replay, immutable input hashes and baseline controls.
Tech stack: existing paired Python/CAN parser/native hooks; no Comma access.

- [x] Write RED synthetic contracts for bounded state, debt rearming, stale/lead/stop/strong-demand fallback and feedback recovery.
- [x] Implement policy.py and in-memory experiment.py; verify fallback identity and physical clearance.
- [x] Extract exact serialized state/control/pose/consumed plan/PID and actual/arbitrated torque from the three active newly downloaded routes.
- [x] Run installed baseline, admission-only and combined candidates through full chronological producer/consumer replay. Include prior 61-segment corpus.
- [x] Inspect failure cases, resolve routine implementation defects, retain rejected variants, and run broader/native checks if a candidate qualifies.
- [x] Save numerical comparisons, limitations, source-preservation proof and roadmap status. No device changes.

Outcome: local spike complete and rejected for integration. Native packet acceptance passes, but the coupled comfort/regression criteria do not. No device or paired-source changes.
