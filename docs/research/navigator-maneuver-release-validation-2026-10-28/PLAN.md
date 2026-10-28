<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Source-bound brake-release validation and local pulsing investigation

Offline research only. Preserve paired sources e05e42f43 / 5097b993 and owner 1.20/0.97. No device, network, CAN, integration or installation operations.

1. Verify recovered original NPZ hashes and source versions. Replay the installed ReleaseBarrier against original command, actual torque receive and post-update mode clocks. Separate clean PID brake steps from stopping and interrupted setup.
2. Establish a red-capable regression: command/status-only clearance must not grant propulsion before the existing <=4 Nm / distinct-sample / 40 ms measured qualification. Preserve actual faults and censorship instead of fitting them away.
3. Prototype an observation-only release-state tracker, failing closed on stale/reversed/invalid samples, preserving source timestamps and identifying requested release versus measured clearance. Test the actual installed guard, not merely a duplicate of its policy.
4. Evaluate the recovered tests' support for optional coast/integral changes. Test an actionable controller change only if its physical premise is supported; reject extrapolation from low-speed braking to highway quiet-coast authority. Retain all prior weaker-braking/city/highway regressions.
5. Record fresh evidence, run meaningful local checks and update roadmap. Artifact/test success is not resolution of physical pulsing.
