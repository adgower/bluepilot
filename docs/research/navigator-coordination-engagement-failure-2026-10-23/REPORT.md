<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Coordination road trial: controls mismatch — October 23, 2026

**Road trial blocked.** The new coordination path spuriously invalidates pose during calibration-only updates. Owner reported repeated red/beeping Controls Mismatch and inability to stay engaged. All18completed new segments downloaded/hash-verified, three sessions,144,141,615bytes. Installed pair e9ddc7668/d2e8d040 and owner steering preferences/1.20/0.97 unchanged; acquisition read-only with zero device mutations. Alpha and coordination were both1 at acquisition. Recommend owner select Alpha off while parked and use OEM ACC pending a validated repair. [Acquisition](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Recorded failure

Five distinct first-fault occurrences at approximately15.4,15.9,20.0,24.1and24.6mph. Each reported `invalid_pose_or_accel` in carOutput and immediately became `controlsMismatch/immediateDisable`. Approximately1.50seconds total longitudinal-active time across the attempted engagements; no meaningful evaluation of ride smoothness, grade compensation or brake/propulsion coordination is possible. [Fault transitions](../../navigator-reference/PRIVATE_ARTIFACTS.md), [captured inputs](../../navigator-reference/PRIVATE_ARTIFACTS.md), [engagement/health](../../navigator-reference/PRIVATE_ARTIFACTS.md).

All five first-fault controls had finite acceleration/orientation, fresh producer context and pose ages72.01–81.47ms, below the unchanged100ms ceiling, but `poseValid=false`. Neighboring controls with the same sensor timestamp had `poseValid=true`. Nearby motion samples reported healthy sensors/inputs/posenet/orientation and valid calibrated extrinsics. Publication timestamps are not exact consumer arrival times; they are not treated as proof that a just-published motion message was already consumed. [Pose provenance](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Root cause and local reproduction

Production `Controls.update` clears `coordination_pose_valid` whenever extrinsicsCalibration updates, and only restores it inside the separate deviceMotion-updated branch. A calibration-only publication therefore creates a false-validity gap even when the calibration is unchanged and the existing motion is healthy/fresh. Production `CarController` treats that gap as an invalid pose during active PID above3m/s, latches `invalid_pose_or_accel`, and the parent maps it to the existing immediate-disable/no-entry Controls Mismatch alert.

Two independent offline reproductions:

1. `reproduce_calibration_update.py`: real production Controls.update + PoseCalibrator, recorded calibrated extrinsics, healthy schema motion. Motion+calibration update givesvalid=true; unchanged calibration-only update givesvalid=false with unchanged motion timestamp. Assertion intentionally fails on the installed source. [Result](../../navigator-reference/PRIVATE_ARTIFACTS.md), [red log](../../navigator-reference/PRIVATE_ARTIFACTS.md).
2. `reproduce.py`: real production Ford controller and alert mapper, five captured pose/demand/request snapshots. Auxiliary speed fixed8m/s, CAN valid and fresh synthetic zero-torque feedback isolate the pose path; these auxiliary values are explicitly not claimed to reproduce actual physical release. All five produce `invalid_pose_or_accel` + Controls Mismatch. Changing only the pose-valid flag in a diagnostic counterfactual removes all five faults. This counterfactual is **not** an implementable safety fix or proof that a blind flag override is acceptable. [Red result](../../navigator-reference/PRIVATE_ARTIFACTS.md), [counterfactual](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Run with the existing paired worktree `.venv/bin/python`; see scripts for the exact local paths. Neither reproduction creates vehicle I/O. No installed or paired production source changed.

## Additional boundary evidence

No Panda RX invalidity/board faults, no permanent steering fault or ACC fault. Temporary steering-fault samples occur at startup/shutdown, outside these first coordination faults. There are14Ford blocked-TX increments following the five coordination faults (roughly80–130ms after the first fault); startup diagnostic-mode counters are tracked separately. Recorded chronology supports the coordination fault preceding those increments, but exact rejected frames still require native RX/TX replay. Do not claim zero road safety rejections or that these increments are already resolved. [Boundary timing](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Required local repair and release gates

Recompute the calibrated pose and validity atomically from the latest actual motion sample when either calibration or motion changes. Preserve the motion sample's original timestamp; do not relabel old motion as new. Retain calibrated/health/validity checks, the100ms age ceiling, non-finite/reversed-time rejection and latched real-fault disengagement. An unchanged valid calibration publication alone must not create a gap. Changed calibration must apply consistently to the published orientation and validity; uncalibrated/invalid input must continue to reject.

Add production-update/publish→schema→card→controller tests with independent calibration/motion cadence, including calibration-only updates, changed calibration, simultaneous updates, startup without motion, actual unhealthy/stale/future/reversed motion and engagement in each boundary. Replay the actual saved sensor/engagement chronology and native RX/TX boundaries before broad controller replay/build checks and any subsequent activation. Keep steering1.20/0.97 and existing longitudinal safety limits intact.

## Why parked checks missed it

The parked pass proved source selection, live transport and healthy inactive telemetry. It recorded occasional pose-invalid requests but did not activate moving PID; the controller's invalid-pose latch is conditional on active longitudinal PID and speed>=3m/s. Existing integration tests did not cover calibration-only message ordering during engagement. The road evidence supersedes the prior parked acceptance as a trial-readiness result. **No additional Alpha road testing until repaired and revalidated.**
