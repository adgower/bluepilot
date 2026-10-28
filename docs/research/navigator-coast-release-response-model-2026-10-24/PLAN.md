<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Ford coast/release response model improvement

October24,2026. User-authorized local saved-data investigation only. No controller/source integration, device contact, ECU queries or CAN transmission. Preserve owner1.20/0.97.

Reproduce and minimize the existing response model's false-clear signature. Compare original OEM camera-bus requests with Alpha vehicle-bus sent requests, with fresh received arbitration/actual torque and control ownership. Keep inactive(-5), valid negative/coast, precharge-only and actual braking distinct. Identify retained arbitration versus physical tracking delay.

Use whole-route splits frozen before model fitting: trainOEM01/02/03+olderAlpha01; calibrateOEM04+olderAlpha02; final testOEM05+latestAlpha. Deduplicate raw hashes and report sparse/unsupported strata. No future torque or future statuses enter a prediction; only original command prefixes through each predicted horizon may be supplied for known-input replay.

Compare improved nonlinear/direct-horizon response against an autoregressive baseline on exactly the same held-out cases and channels. Include pressure error, propulsion error, time horizon, early/late point-clear predictions, interval coverage/width and abstention. Do not obtain zero errors by declaring everything unknown. Models never grant physical clearance or feed candidate control.

Verify invalid/stale inputs, training/holdout separation and prefix causality. Replay original recorded commands on the held-out OEM and Alpha routes, preserving commands byte-for-byte. Update roadmap with measured improvement, remaining gaps and explicit limits.
