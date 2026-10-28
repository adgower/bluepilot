<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Calibration update continuity implementation plan

Goal: repair the diagnosed calibration-only pose-validity gap locally, preserving motion timestamps, invalid-input rejection and all steering/longitudinal safety limits.
Spec: ../navigator-coordination-engagement-failure-2026-10-23/REPORT.md (Required local repair and release gates), authorized by owner to implement and replay.
Isolation: existing paired codex/navigator-tracking-release worktree, parent e9ddc7668 / child d2e8d040, initially clean. No Comma access, device writes, push, install or preference changes. Keep 1.20/0.97. Child control/safety source remains unchanged unless evidence demands otherwise.

Design: rebuild calibrated pose and its validity on motion updates, and also calibration updates when coordination is enabled and a motion sample has been seen. Feed calibration before transforming pose. Preserve original sample timestamp. Baseline disabled path retains its existing update cadence; no validity override, grace period or age-limit increase.
Alternatives rejected: retaining validity blindly can pair old orientation with changed calibration; extending timeouts or masking the fault would weaken genuine stale/unhealthy rejection.

## Tasks
- [x] Add production update/publish→schema→controller engagement regressions. Prove unchanged/changed calibration-only failures before production edits. Cover simultaneous input, no motion startup, invalid calibration/sensor health, stale/future/reversed input, disabled parity and real fault latching.
- [x] Minimal controlsd change; run RED→GREEN and existing coordination/producer tests. Use real PoseCalibrator/schema/controller; stub only IPC/Params/thread setup.
- [x] Replay new saved sensor chronology and all five first-fault snapshots without fabricated validity; retain health/freshness failures. Run full retained longitudinal slot/release/response/native replay and lateral safety corpus, documenting exact coverage and recorded boundary rejects separately.
- [x] Run relevant broad parent/Ford/native suites, lint/type/build where applicable; review complete diff, preserve owner source hashes, update report/roadmap. No publication or activation.

Review focus: calibration-only update without prior motion; invalid input must stay invalid; original timestamp and frame pairing; independent 4Hz/20Hz/100Hz cadence across engagement; fault must remain latched until owner reset. Every input class gets an explicit assertion.
Ruling: execute the already authorized design directly in the existing isolated worktree. Additional design/permission questions would duplicate the owner's explicit request.

Progress: first two tasks complete; native/sensor/longitudinal/model replays and final suites/build passed. Full71-session/1,015-segment lateral replay running, no errors so far. Independent review identified a missing real-card assertion; closed with production Card/Interface/schema, parent latch/rearm and nonfinite cases. Production patch remains six lines; no device access.

Completion: all71sessions/1,015segments passed freshly. Final receipt/source hashes verified. Local patch retained; no commit, push or device change.
