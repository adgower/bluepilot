<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Earlier unwind pair installed: powered parked acceptance passed

Installed exact published pair on branch `codex/navigator-tracking-release`:

- openpilot `f7b0c47d23de697b73f1247cd5d32021b37e19bc`
- opendbc `8ccc6cf0ee123afddddbf6e0a0ea3d3316669a5e`, pinned by parent

**Powered stationary checks passed; road performance remains unproved.** User readiness was confirmed before activation; ignition-off checks passed. The complete previous install is retained at `/data/navigator-previous-earlier-unwind-<private timestamp identifier>` for whole-tree rollback.

## Preservation and backup

Fresh device/Mac backup verified:843,669,110bytes,143manifestmembers,66parameters,both nested source archives read successfully. Private Mac copy: `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-earlier-unwind`.

All selected settings remain equal, including DisableUpdates and all existing steering opt-ins. Owner1.20/0.97,geometry,learned calibration hashes,launchers and installed firmware preserved. AGNOS19.9 unchanged; no OS/firmware updates. The installer field new_trial_enabled confirms the already-enabled opt-in; no new preference was introduced or changed. Candidate parent/child trees are clean and self-contained, with correct child pin. Whole-pair atomic exchange used with automatic rollback on acceptance failure; rollback was not needed.

## Validation

Fresh isolated full ARM build passed. Ford/native750passed,79skipped,12,063subtests. Retained320/480/714transition matrices and128abort cases passed. New714case/228,480frame onset transitions and128abort cases passed, with zero added neutral command tail. All8Card preference combinations and IPC/calibration/stale-snapshot pipeline checks passed. Vehicle devices/network/private parameters were isolated; live source was read-only. Across validation, active source/settings/manager/service matched; only LastAthenaPingTime and UptimeOffroad parameter hashes changed.

Offroad acceptance:201passivePanda samples,NO_OUTPUT,controls disallowed,no reported faults or unexpected stopped processes; TX-blocked counter stable at0 after service restart. All five preserved calibration/cache hashes match the backup. [Activation receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md) and [final preservation](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The validation took about118minutes. Ruling: the original1h allowance was too small for ARM matrices; only this isolated unit's runtime allowance was extended first to2h then3h. 3GiB/zero-swap/150%CPU and every offroad/device/network/source guard remained. Cost: longer isolated compute and installation delay. Direct set-property was unsupported; an owned volatile per-unit override was used and has now been removed. The math-thread microbenchmark showed no material difference; harness/controller source was not changed for speed. I over-scoped the repeated installation matrices and should have measured their duration before starting.

The accepted819segment host replay evidence remains carried by the exact source port/factory equivalence, not a fresh ARM819segment replay. Native and command tests do not prove physical vehicle tracking.

## Powered stationary acceptance and next drive

User confirmed ignition on, stationary in Park, assistance disengaged. The55second passive powered check passed: correct clean pair, calibrated, stable~20fps big model with zero dropped frames, no sampled CAN/steering/vehicle faults, healthy Chestnut supply, Ford safety parameter10, controls disallowed, assistance inactive. Atomic calibration schema/provenance and settings checks passed. This observes stationary runtime; it does not prove active mapping or physical steering behavior.

Read-only learned comparison passed: steering ratio, average angle offset, lateral delay, profile/geometry/flags/safety, CalibrationParams and LiveTorqueParameters payload retained. The torque-cache event timestamp changed during normal startup; no cached settings were restored. [Powered acceptance](../../navigator-reference/PRIVATE_ARTIFACTS.md), [learned preservation](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Installation is complete. Next: ordinary supervised driving within posted limits; assess unwind through familiar bends, record approximate times of shortfalls or takeovers, then download and compare logs. Physical60–70mph improvement remains unproved;28mph deviation issue remains open.

[Deployment status](../../navigator-reference/PRIVATE_ARTIFACTS.md), [backup](../../navigator-reference/PRIVATE_ARTIFACTS.md), [publication](../../navigator-reference/PRIVATE_ARTIFACTS.md), [ARM acceptance](../../navigator-reference/PRIVATE_ARTIFACTS.md), [independent review](REVIEW.md).
