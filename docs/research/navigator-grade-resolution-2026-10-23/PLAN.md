<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local pitch/grade discrepancy investigation

Authorized scope: resolve the saved-data discrepancy locally; no device access, active queries, paired integration or steering/settings changes.

1. Reproduce the relative Ford119 minus wheel acceleration minus Comma gravity offset across independent OEM routes and Alpha, with validity/sentinel/timing gates and source/version hashes.
2. Trace PoseCalibrator, locationd sensor axes and estimated accelerometer bias. Separate road grade, body attitude, specific force, calibrated acceleration and wheel acceleration; test sign/scale/delay and sensor-zero hypotheses separately. Include stops and GNSS grade proxies; do not assume the Ford channel is calibrated ground truth.
3. If evidence identifies a correction, write a report-local implementation and failing regression contracts first, then replay held-out routes/Alpha. Separate a discrepancy correction from a longitudinal controller cure; frozen requests cannot establish closed-loop comfort.
4. Preserve exact source pair, owner1.20/0.97, cached learned parameters and device. Record unresolved identifiability/coverage rather than fit a hard-coded offset to edge counts. Update report/roadmap with concrete findings and checks.

Potential approaches: fix a proved transport/axis bug; correct a proved sensor-zero mismatch with fresh validity-gated runtime context; otherwise quarantine non-identifiable calibration and keep controller unchanged. Independent data decides between them. No arbitrary one-degree reset.
