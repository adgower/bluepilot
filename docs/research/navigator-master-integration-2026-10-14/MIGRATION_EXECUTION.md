<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator device migration — execution record

**Installed; normal offroad reboot and powered stationary ignition-on checks verified. Road evaluation remains pending.** User authorized the update and confirmed being beside the parked, powered device with recovery cables available on October 14, 2026 (America/Chicago).

## Completed before OS reboot

- Fresh offroad/source/settings check matched the verified private backup; staged parent remains `6ae31161b73de2ce5043f708569759ac5f55f283` and child `c09baff5c2cdd7c887e25c2d88b671f403e1ed9d`.
- Stopped `comma.service` and confirmed runtime processes stopped.
- Saved the original `/data/continue.sh` to the private device and Mac backups; installed an explicit maintenance hold. It prevents old-source automatic OS/firmware actions after the OS reboot.
- Preserved the missing 256-byte Chestnut configuration using three identical reads. The narrowly scoped reader permits SPI READ only and forbids write-enable, erase, programming and firmware activation. Bridge controller/driver access was a deliberate authorized hardware operation, not passive inventory.
- Saved the configuration at the official flasher's hostname-dependent path and copied it privately to the Mac; size/hash/archive readability checks passed. Raw bytes and hostname remain private.
- Started the pinned supported AGNOS updater as a detached service, targeting inactive slot B. Runner logs/status are in `/data/navigator-backups/<private timestamp identifier>-pre-master-migration/`. It verifies and selects B on success, but does not reboot automatically.

Current source and parameter backups remain available. Owner 1.20/0.97 constants and selected settings are to be verified again before activation. Subsequent OS boot, target-native build, firmware activation and parked runtime acceptance are not yet recorded as complete.

## Verified OS boot and source transition

AGNOS update completed with return code 0 and successful target-slot selection after its built-in retry. Device rebooted and reconnected on **AGNOS 19.9 / slot B** with maintenance hold intact. Boot success was marked after checking OS, slot and preferences. Preserved the complete old source at `/data/navigator-before-master-20261015`; moved new source to `/data/openpilot` while runtime remained stopped. This allows native artifacts to be built at their final path. Started `scons -j4` through a detached service; completion is not yet established. No firmware flash has yet been started.

## Completed native build, firmware and activation

- Clean `scons -j4` native device build passed on AGNOS 19.9 (<private clock time>–<private clock time> UTC / October 14 evening local time). No prebuilt bypass or Mac native artifacts were used. Build occurred at the final `/data/openpilot` path; the new installation does not depend on a staging symlink.
- Device lacks pytest. Equivalent four isolated Params-to-Ford startup combinations passed using temporary Params storage, real native libraries and stubbed fingerprint I/O. This is not a full on-device pytest suite.
- Important preference migration: old absent ExperimentalMode meant off; new master defaults it to true. Explicitly stored `ExperimentalMode=0` before manager initialization to preserve disabled behavior. Alpha remains 0. The removed legacy ExperimentalModeConfirmed marker remains in the backup; current upstream no longer uses/registers it.
- Chestnut programmed and full-image verification passed, then its VBUS activation completed. Actual USB product is now `custom 8516b768-CLEAN`. Configuration preservation prerequisite was met before programming and a verified private Mac copy exists.
- Matching Panda check/update passed using the standard recovery/check helpers. Native H7 signed image SHA256 is `5a10a6119110b3c41a03d381c4bdd3bea4e05c3a7164bef515b42df7054c466e`, identical to the earlier validated artifact.
- Restored the exact original boot entrypoint, now launching the new source at `/data/openpilot`; removed the temporary maintenance hold. Root-created Python cache ownership was corrected for normal-user access. No tracked source modifications were needed.

## Final normal boot acceptance

Normal reboot returned on AGNOS **19.9 / slot B**. Both Git and the live manager identify parent **6ae31161b73de2ce5043f708569759ac5f55f283**, branch **codex/navigator-master-integration**, with pinned child **c09baff5c2cdd7c887e25c2d88b671f403e1ed9d**. Parent and child working trees are clean. User confirmed normal home screen before the final reboot; after final reboot the manager/device/Panda/Chestnut topics are alive and valid, with no offroad alerts or unexpectedly stopped required processes.

`updated` intentionally exits successfully because DisableUpdates=1; it is excluded from unexpected process failures. Initial early probes preceded completed startup and are superseded by the final live checks. Startup diagnostics contained a caught uploader file-disappearance race and a NetworkManager profile-info lookup warning; uploader remained running and network/SSH worked through both reboots. No unrelated source patch was introduced.

Verified after final boot: DisableUpdates=1; both Ford options=1; AlphaLongitudinalEnabled=0; ExperimentalMode=0; OpenpilotEnabledToggle=1; DisengageOnAccelerator=0. Owner 1.20/0.97 source constants remain unchanged. Calibration matches the private pre-migration backup. Panda is in offroad noOutput, controls disallowed, ignition flags false.

Vehicle remained parked with ignition off. Chestnut bridge firmware/telemetry are established, but full GPU power, big-model inference, actual onroad CarParams and driving behavior are not established by this offroad check. No active vehicle ECU queries or road test were performed. Next acceptance is a deliberately scoped parked ignition/full-power check, followed separately by road evaluation.

## Preserved recovery and evidence

Old complete source remains `/data/navigator-before-master-20261015`; earlier backups/previous installation remain. Private Mac backup is `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-master-migration/`; completed evidence bundle contains 20 checked records/scripts/logs, plus the independently verified Chestnut configuration archive. Public reports contain no raw credentials, full parameters or hostname-dependent configuration bytes.

Application restoration does not automatically restore OS or firmware. Original slot A was retained by the inactive-slot update design, but exact rollback/recovery has not been boot-tested. Official Mac factory recovery erases userdata; preserve the private Mac backup.

## Subsequent parked ignition-on acceptance

User authorized and performed ignition-on while parked in the driveway. [Powered stationary checks](PARKED_IGNITION_ACCEPTANCE.md) pass: live geometry/options/safety10, valid CAN/no reported faults, calibration and full big-model inference ~20fps with zero sampled reported drops over one minute. Panda RX-invalid/TX-blocked counters remain zero in the observed window. No tuning, ECU diagnostic injection, engagement or steering-command tests were performed. This supersedes the earlier pending-full-power status for stationary operation only; road behavior and sustained reliability remain unverified.
