<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Sustained tracking / unwind installation — October 19, 2026

Status: exact paired branches published, backed up and activated. Fresh isolated ARM/native validation, ignition-off acceptance and user-confirmed powered stationary acceptance all pass. Installation and parked checks are complete; physical tracking improvement remains to be evaluated during ordinary supervised driving.

## Pair and backup

Published without force to the existing adgower origins, child first, with both remote heads verified:

- openpilot `0171b897289be53fd62f330935c55825b86c3c3a`
- opendbc `4167433e5c575f620a9dedf8144a0bc7cba14291`

Replaced clean pair `50baa6fd6acf9d37b7e0768e5736efab2a357ddc` / `0e65f296260ec16da3c3b814c10ac5f36f8b2e4c`. AGNOS remains 19.9.

Fresh private backup: `/data/navigator-backups/<private timestamp identifier>-pre-sustained`, with an independently verified Mac copy at `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-sustained`. Archive 843,590,766 bytes; 66 parameters, source archives, launchers and signed firmware. Archive SHA-256, all 143 manifest members and both nested source archives verified. Raw parameter values stay in the private backup.

## Device validation

Separate stage `/data/navigator-validation/<private timestamp identifier>-0171b8972` used verified exact-pair bundles and 262 hash-verified LFS files. Its dedicated unit masked vehicle interfaces, isolated network/parameters/cache, mounted the active source read-only and dropped child privileges. Full ARM SCons build passed.

- Ford/native suite: **599 passed, 79 skipped, 12,063 subtests passed**.
- Retained roll screen: **320 cases / 115,200 frames**.
- New sustained/unwind screen: **480 cases / 172,800 frames**, actual-output bounds/slew/settlement pass.
- All eight actual Card factory combinations pass; enabled selection is `SustainedErrorUnwind`.
- Controls/Card/Cap'n Proto IPC, atomic calibration and stale-snapshot withdrawal checks pass.

Validation took 1,609 seconds. Live source heads/files, selected settings, manager PID and service timestamp remained unchanged. Only ordinary runtime parameter hashes `UptimeOffroad` and `LastAthenaPingTime` changed during validation. Independent installer review found no material issue.

## Activation and preservation

The prepared candidate has self-contained Git objects, clean paired source, preserved launchers and the exact existing signed firmware image. Startup/prebuilt behavior was preserved. A guarded atomic whole-directory exchange retained the entire previous install at `/data/navigator-previous-sustained-<private timestamp identifier>`; the installer restores that tree automatically if offroad acceptance fails.

Twenty-second passive ignition-off acceptance passed: healthy expected processes, NO_OUTPUT, no ignition/control permission, no sampled faults or blocked-transmission increments. All selected preferences and all five captured learned/calibration hashes equal the fresh backup. **1.20/0.97**, geometry, pinion and safety sources remain unchanged. `DisableUpdates=1`, Alpha longitudinal off and ExperimentalMode absent/off remain. No new preference was introduced; existing prerequisites were already enabled. No OS/firmware update or active ECU diagnostics were requested or performed by these helpers.

Retain both the stage and previous install. A later rollback must happen parked with ignition off, after preserving intervening settings; restore the whole pair rather than mixing trees or blindly restoring stale learned parameters.

Frozen-input/native checks and stationary acceptance do not establish physical tracking improvement. Powered acceptance and ordinary supervised road evidence are separate stages.

[Publication](../../navigator-reference/PRIVATE_ARTIFACTS.md), [backup verification](../../navigator-reference/PRIVATE_ARTIFACTS.md), [isolated acceptance](../../navigator-reference/PRIVATE_ARTIFACTS.md), [offroad acceptance](../../navigator-reference/PRIVATE_ARTIFACTS.md), [preservation](../../navigator-reference/PRIVATE_ARTIFACTS.md), [installer review](REVIEW.md).

## Powered stationary acceptance — complete

After the user confirmed ignition on, stationary Park and assistance disengaged, the55-second passive check passed. All monitored topics were alive/valid. No sampled steering, CAN or vehicle fault, unexpected stopped process, Chestnut supply fault or blocked-transmission increment was observed. Correct Ford safety parameter10, unchanged profile/geometry/pinion flags and clean exact paired source were verified. Big model sustained approximately20fps with zero reported frame drops.

Core learned steer ratio, average offset, lateral delay, extrinsics calibration and torque payload remain preserved. Normal upstream startup reset stiffness from1.000095to1.0 and refreshed a torque-cache timestamp; no stale learned cache was restored. Updates remain paused; Alpha and Experimental longitudinal remain off. Existing preferences already enable the new policy; no extra toggle is needed.

[Powered check](../../navigator-reference/PRIVATE_ARTIFACTS.md), [learned preservation](../../navigator-reference/PRIVATE_ARTIFACTS.md), [completion](../../navigator-reference/PRIVATE_ARTIFACTS.md). This confirms stationary startup/health, not active mapping performance or improved physical tracking. Start with ordinary supervised driving on familiar roads at legal speeds, taking over whenever needed and noting approximate takeover times for later review. No deliberate high-speed or lane-edge reproduction is required.
