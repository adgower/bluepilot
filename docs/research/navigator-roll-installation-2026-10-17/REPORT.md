<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator calibration/roll pair deployment — 2026-10-17

User authorized paired publication, backup and installation, and confirmed parked ignition-off state, stable power/Wi-Fi, accessible screen and recovery cables. OS and firmware updates are excluded.

## Published pair

- openpilot `99645f2222ea2ba1fd4124808774bcd6381f8154`
- opendbc `8cbc834fe534a248a3bc6d56ce964106c0f49503`
- Both `codex/navigator-tracking-release` branches pushed without force and exact remote refs verified: [publication receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md).
- Prior local build/replay provenance: [paired build report](../navigator-paired-roll-build-2026-10-17/REPORT.md).

## Backup and preservation

[Backup verification](../../navigator-reference/PRIVATE_ARTIFACTS.md): 843,567,098-byte archive verified by SHA-256, 141 extracted member hashes checked and both nested source archives read to EOF. Private Mac copy: `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-roll-mapping`. Device copy: `/data/navigator-backups/<private timestamp identifier>-pre-roll-mapping`.

Backups include parameters, committed source, exact signed Panda image, launchers and inventory. They are not an OS image or model backup. Whole original installation will additionally be retained at `/data/navigator-previous-roll-<private timestamp identifier>` during activation.

Owner factors 1.20/0.97, native geometry, firmware image, existing preferences and calibration must pass preservation guards. The single intentional additional preference is `FordPrefRollAwareMapping=True`. Its bounded roll mapping applies inside 50–70 mph; this does not introduce a new low-speed correction or establish physical tracking improvement.

## Current status

**Installed; ignition-off and powered stationary Park acceptance passed. Road tracking improvement remains unverified.**

Both exact published heads are active and clean. All captured selected preferences match except the intentional new roll flag. CalibrationParams, LiveParametersV2, LiveTorqueParameters, LiveDelay and CarParamsPersistent hashes match the backup. Owner factors 1.20/0.97 and protected geometry/launchers/signed firmware hashes match. AGNOS remains 19.9. Passive200-sample offroad check: NO_OUTPUT, no ignition or controls allowed, no safety/RX/heartbeat fault, TX-blocked0 and no unexpectedly stopped process. [Activation receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md), [final preservation](../../navigator-reference/PRIVATE_ARTIFACTS.md).


Installer review fixed two findings: receipt-write failures cannot bypass rollback, and all preservation/paired-head checks repeat after service shutdown immediately before swap. Atomic exchange is preferred; guarded renames retain whole-install rollback when exchange is unsupported. No firmware flashing is part of activation.

## Completed ARM validation and installation progress

Full ARM SCons build passed. Native suite: 338 passed, 79 skipped, 12,063 subtests. Transition screen: 320 cases / 115,200 frames, final bounds and baseline rejoin passed. Actual Controls→serialized local msgq→Card test passed. Initial IPC attempt failed because the private prefixed shared-memory directory was absent; fixed only the harness and reran offline validation successfully, retaining failed-attempt receipts. No candidate source change. [Runner](../../navigator-reference/PRIVATE_ARTIFACTS.md), [preservation](../../navigator-reference/PRIVATE_ARTIFACTS.md), [transitions](../../navigator-reference/PRIVATE_ARTIFACTS.md), [pipeline](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Candidate preparation passed after preserving partial-clone metadata and normalizing verified LFS index entries; no committed asset changes. Whole-directory swap and controller constructor checks passed. The standard startup wrapper entered its tap-reset UI; only the verified UI process was terminated to resume normal launch. No reset, erase or reboot command was called. Standard application startup rebuilt path-dependent native targets successfully. A strict final guard then triggered automatic whole-original rollback because it did not classify the startup-generated Offroad_DriverMonitoringUncertain alert as runtime state. Source, firmware and calibration matched. Classified only that identified alert as runtime state, restored the captured absent/off ExperimentalMode after original-app startup recreated1, and retried successfully. Final checks confirm the captured ExperimentalMode is absent/off. The failed activation and rollback receipts remain in the private backup. Powered stationary acceptance subsequently passed; see results below.

## Powered stationary acceptance — passed

User confirmed ignition on, stationary in Park. Passive55.01s screen: all12topics alive/valid, zero speed, assistance disengaged, no steering/CAN/safety fault, Ford safety parameter10,550Panda samples with zeroRX-invalid/TX-blocked/SPI errors and no heartbeat loss/faults. Chestnut supply healthy. Large model1101frames at19.998fps, zero frame drops, mean execution40.10ms. All1101CarControl calibration snapshots valid, matched target/provenance checks. This verifies live snapshot delivery while stationary; active mapping and physical tracking remain road tests. [Powered receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Published source clean at exact paired heads. Updates remain paused; pinion, low-speed gain, persistent tracking and roll mapping enabled; AlphaLongitudinal and ExperimentalMode remain off. Owner1.20/0.97 and protected geometry/firmware retained from installation checks.

[Learned-value check](../../navigator-reference/PRIVATE_ARTIFACTS.md) passed: learned ratio22.7516822815, average angle offset−1.6242322922deg and delay0.2682819366s retained, along with profile/geometry/flags/safety, CalibrationParams and torque-cache payload. Stiffness reset0.990940392→1.0 during normal estimator startup; torque Event timestamp advanced. No stale estimator cache was restored. Results also copied alongside the private Mac backup.

Next: ordinary supervised driving on familiar roads, recording approximate times/speeds for understeer, overshoot or interventions. The new mapping applies within50–70mph; existing low-speed behavior and owner factors are retained. Parked checks do not establish road improvement.
