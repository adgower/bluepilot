<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator installation preparation — 2026-10-14

This is a preparation plan, not a record of device installation. The Comma has not been connected to or changed during publication. The target is a pinned master snapshot, not an automatically moving latest-master deployment.

## Published target

- [openpilot branch](https://github.com/adgower/openpilot/tree/codex/navigator-master-integration): `6ae31161b73de2ce5043f708569759ac5f55f283`.
- [opendbc branch](https://github.com/adgower/opendbc/tree/codex/navigator-master-integration): `c09baff5c2cdd7c887e25c2d88b671f403e1ed9d`, pinned by the parent.
- Expected AGNOS: 19.9. Expected Chestnut firmware product revision: `8516b768`.
- Vehicle code preserves 1.20/0.97, forced Expedition identity, Navigator geometry, pinion feedback, low-speed trial and its 45 mph fade.

## Important startup boundary

`launch_chffrplus.sh` calls `agnos_init` before manager startup. When `/VERSION` differs from 19.9 it invokes the AGNOS verifier/updater and can reboot. The verifier's `--verify` CLI is **not read-only**: a successful check invokes `swap()` and changes the active slot. Do not run it during a read-only inventory.

After startup, `hardwared` can automatically flash mismatched Chestnut firmware while offroad; `pandad` can flash Panda. `DisableUpdates=1` stops the application updater but does not suppress these compatibility operations. Therefore booting or manually launching the new checkout is already an OS/firmware migration action. An unattended branch switch/reboot is inappropriate before the checks below.

## Stage A — parked inventory and private backups

Before device writes, confirm the vehicle is parked, ignition off, Comma powered reliably, stable Wi-Fi available, and owner can access the screen. Re-establish SSH using the existing private setup; never put credentials in this report. No active ECU queries are needed.

Read current OS, available disk space, current boot slot (`abctl --boot_slot` only), current source/child revisions and modifications, `/data/openpilot` path/symlink identity, startup mechanism, staging/overlay state, current selected settings and actual USB firmware products. Read-only USB inventory is distinct from a firmware updater. Check for an external AGNOS_VERSION override. Reconcile against the saved inventory rather than assuming it is still current.

Create a fresh private backup of the complete installed application including uncommitted overlay, symlink targets, source hashes, logs needed for recovery, complete parameter storage (including symlink layout), calibration, and firmware/boot-slot provenance. Preserve the earlier known-good backups. Copy the new backup off the Comma to private Mac storage and verify archive checksums/readability. Complete parameter backups contain credentials and device identity: keep them private and out of Git. Check capacity before copying; do not remove driving logs to make room without a separate decision.

Known settings to preserve and recheck:

| Setting | Last inventoried value |
|---|---|
| DisableUpdates | 1 |
| FordPrefSteerAngleCurvature | 1 |
| FordPrefLowSpeedGain | 1 |
| AlphaLongitudinalEnabled | 0 |
| ExperimentalMode | absent/off |
| ExperimentalModeConfirmed | 1 |
| OpenpilotEnabledToggle | 1 |
| DisengageOnAccelerator | 0 |

Keep current persistent storage wherever compatible, rather than constructing a fresh Params store that defaults the Ford options off. Review learned-parameter schema changes; preserve calibration in the backup, but do not blindly restore old serialized CarParams/runtime flags or incompatible learned values. Startup regenerates the changed internal option bits. Do not enable alpha/experimental longitudinal as part of this migration.

## Stage B — separate source staging

Use a new, uniquely named directory under `/data` after checking capacity. Do not switch/reset/clean the working installation or reuse the old staging symlink. Clone the published parent and initialize all pinned submodules; verify exact parent/child SHAs against this document. Fetch the Git LFS objects needed for the target build, including real models, firmware and assets, and verify pointer sizes/hashes. A successful Git clone alone does not establish complete model downloads.

Do not run `launch_openpilot.sh`, `launch_chffrplus.sh`, manager, hardwared, pandad or the AGNOS updater merely to test the staged clone. Do not copy Mac native binaries or its build cache onto AGNOS. Do not copy the old `prebuilt` marker. The target's supported AGNOS environment and clean native build are required.

## Stage C — establish recovery, then migrate

The candidate's AGNOS manifest targets the inactive A/B slot for every listed partition. This supports an update mechanism, but is not proof that this device can recover through an arbitrary old-slot switch. Record the initial slot and preserve it; establish a supported recovery route and access before migration. Do not prescribe `abctl --set_active` or an OS downgrade based solely on an application backup. Chestnut and Panda firmware recovery must also be considered; swapping application directories does not restore those components.

Once recovery and backups are verified, stop the existing runtime while parked using the verified on-device service/launcher mechanism. Deliberately perform the supported AGNOS 19.9 update, retaining its logs. Reconnect and verify `/VERSION`, boot slot and network access. Complete a clean target-native build in the supported environment and identify matching firmware/model artifacts. Only then make the preserved old installation and staged new installation available for a controlled launcher transition. Choose exact directory/service commands from the fresh inventory, so symlinks and automatic service restarts cannot race the swap.

No ready-to-paste destructive swap or flash commands are included before those device facts and recovery checks are known.

## Stage D — acceptance while parked

1. Confirm parent/child SHAs, actual firmware products, OS, complete LFS artifacts and clean target build.
2. Verify the selected settings above, forced vehicle identity, geometry and 1.20/0.97 constants; confirm both trial toggles and startup option wiring. Do not transplant old CarParams option bits.
3. Confirm no model/firmware/build errors, normal startup and shutdown, and no updater/hotspot/reboot loop. Check a subsequent offline startup once provisioning is complete; keep stable network during downloads/OS updates.
4. With the vehicle stationary, verify ordinary ignition transitions and correct recognition through passive data. No active ECU interrogation is required.
5. Keep the old installation and private backups. Record actual installation and acceptance evidence separately from later road evaluation. Driving remains a separate cautious evaluation after parked checks; replay does not guarantee unchanged closed-loop handling.

## Recovery decision

If source staging or download fails, keep the current runtime untouched. If target-native build fails, retain the old source and logs; do not bypass the build with `prebuilt`. If OS/firmware has already changed, stop and use the verified recovery procedure for the actual installed versions. An application-directory rollback alone is not presumed sufficient.

## Inventory/backup execution record

Stage A inventory and private backups completed October 14; see [DEVICE_BACKUP.md](DEVICE_BACKUP.md). Application/parameter backups were copied to the Mac and integrity checked. OS/firmware recovery feasibility remains unproven, and no staging, update, flash or installation was started.

## Separate staging and recovery review

Completed separate source staging and verified all 262 LFS assets, paired SHAs and submodules; see [STAGING_STATUS.md](STAGING_STATUS.md). OS/firmware remain unchanged. [Recovery review](RECOVERY_OPTIONS.md) documents Mac factory recovery, untested A/B rollback and the missing pre-flash Chestnut configuration backup. No target-native build, activation or update was started.

## Executed migration

The user subsequently authorized updates with physical readiness confirmed. Installation, native build, matching firmware and final normal offroad boot are complete; see [MIGRATION_EXECUTION.md](MIGRATION_EXECUTION.md). Current source is `/data/openpilot`, old source `/data/navigator-before-master-20261015`; the temporary separate staging directory was moved to the final path before native build. The maintenance hold is removed. Chestnut configuration is now preserved and privately verified on the Mac. Full-power/onroad acceptance and road evaluation remain separate.
