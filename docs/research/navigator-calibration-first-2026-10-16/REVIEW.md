<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent review record

Review scope: estimator/data pipeline/tests versus approved calibration-first design. Read-only reviewer, fresh context, no device access or file mutations.

Initial review:20 tests passed. OneP2 finding: verified raw hashes were not bound to reused extracted caches. Fixed with ordered raw input/code/schema fingerprints, payload digest, embedded anonymous label verification and full fresh extraction. Three cache tests failed before repair; swapped-cache normalization integration test added.

Repair review:24 tests passed; no new material findings. Optional staging hardening identified; exact-link/segment validation added with regression tests.

Final bounded review:28 core tests passed. No new material findings. Reviewer checked staging validation, per-held-out-route error gates that prevent cancellation of opposite errors, and the evidence-status flag `controller_map_validated`. Three additional tracking-window tests bring the final full suite to31.

Reported limitations: intervals are conditional; profile ranges are sensitivity bounds, not confidence intervals; no physical steering fix follows from the model. Bias now has a conditional bootstrap interval, with no causal interpretation.
