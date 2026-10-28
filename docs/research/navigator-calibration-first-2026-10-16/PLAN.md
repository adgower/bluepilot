<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Calibration-first implementation plan

> Execute inline with superpowers:executing-plans; use test-first development and one final independent review. The user approved the preceding design and explicitly authorized implementation, so no repeated design/plan approval is needed.

Goal: a pure offline estimator and speed audit that separates predictive gain, yaw bias and dynamics, abstains on inadequate evidence, and never writes vehicle calibration.
Architecture: normalize retained raw logs to anonymous fixed-cadence episodes; fit a delayed first-order input/output model using actually transmitted path angle and calibrated physical yaw; validate on held-out routes/episodes and output recommendation-only JSON.
Tech: existing paired Python3.12 environment, numpy/scipy/pytest; no dependency changes.
Spec: ../navigator-feedback-admission-2026-10-16/DESIGN.md (approved).

Constraints: preserve1.20/.97; no device changes; no safety/DBC/native geometry changes; preserve≥25mph control path; no random adjacent-frame validation; keep GPS/identity private. No controller change unless identification justifies an exact bounded map. Recommendations cannot be applied automatically.

Review focus: correlated closed-loop inputs; rank-deficient gain/bias separation; unidentifiable latency on steady input; missing/future samples and segment gaps; no85mph exposure. Each gets an explicit synthetic or dataset test.

## Task1: estimator and synthetic contract
Files: estimator.py,test_estimator.py. Interfaces: Episode(route,t,u,y,mph,reference); fit(episodes)->FitResult; diagnose(train,test)->recommendation-only result. Model physical yaw follows delayed transmitted path angle with first-order response plus bias. Tests recover known gain/bias/delay/tau, respect turn-sign reversal, reject constant/one-sided/short/sparse inputs, refuse incompatible held-out dynamics and residual/input dependence. Derive confidence from whole-episode fits, not frame counts.
- [x] Write/run failing functional tests against an unimplemented fit stub.
- [x] Implement minimal grid/delay + free-rollout robust linear fit and diagnostics.
- [x] Run synthetic recovery/abstention tests; record red/green evidence.

## Task2: normalize/segment original logs
Files: routes.py,normalize.py,test_dataset.py. Interfaces: local raw paths -> per-route NPZ and anonymous manifest; eligibility -> contiguous uniformly resampled episodes. Use prior hash-verified335segment corpus. Keep actual TX, requested curvature, body yaw/time/validity, CS, learned params and raw CAN yaw; never export GPS/IDs. Handle fresh clocks independently from stale init RTC. Segment at invalid data/engagement/source transitions; require warmup and past-only alignment.
- [x] Test gaps/staleness/turn and route identity invariants before implementation.
- [x] Normalize all historical sessions; verify hashes and source/config metadata.
- [x] Check coverage,95th/max speed, eligibility and exact55/65/75/85mph bands.

## Task3: held-out speed audit and recommendations
Files: evaluate.py,REPORT.md,verification.json. Train/test separated by whole routes; if only one route or insufficient sign/excitation/support, abstain. Report descriptive tracking separately from transfer fit. Report gain/bias/delay uncertainty, held-out gain stability, residual dependence and model ambiguity. Do not infer per-speed multipliers from median response alone.
- [x] Run complete corpus evaluation and synthetic negative controls.
- [x] Generate independent OEM-yaw diagnostic cross-check and inspect all specified speed bands including explicit no-data85 status.
- [x] If evidence supports a local command-map candidate, implement/test the exact narrow change and native-replay it; otherwise record why no controller change is justified without fabricating a fix.
- [x] Run final tests and independent review, resolve material issues, update roadmap, preserve artifacts/private evidence and source state.

Ruling: implementation is contained in a new report-local package; paired source is a clean dependency and remains unchanged unless Task3 justifies a controller change. Existing root README/untracked reports are preserved. No Git reset/switch/commit of unrelated work or device operation is needed.

Completion notes: final pipeline verifies335segments/19routes,31tests,19raw/code/payload bindings and exact source state. The conditional controller-change step was evaluated and deliberately not taken: no current low-speed map validates. Historical CV is separate from newest-route validation. Independent review finding repaired and re-reviewed; private durable evidence preserved withAPFSclones. No branch/device modification.
