<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Live inventory and private backup — 2026-10-14

Authorized scope: SSH inventory and backups only. No OS/firmware update, candidate launch, source switch, preference change, service stop or reboot was performed. No active ECU queries were made.

## Live installation

- AGNOS 19.7; boot slot `_a`, unchanged after backup.
- Installed parent `f35e6e5eb11ca9cddad3ed945d44d8f191679240`; child `eb70bef4f56d2e9e91cb5a0a8374890a6acfaf51`, with the existing uncommitted Navigator overlay. Git HEAD alone does not describe the running source.
- Forced/staging layout and old prebuilt marker remain intact; `/data/pythonpath` and `/data/navigator-stage-20261014` resolve to `/data/openpilot`.
- Read-only USB product inventory reports Chestnut `custom ed4e39b7-CLEAN`. New candidate expects 8516b768; no flash was attempted. Actual Panda firmware was not actively queried.
- Device reported offroad. No application-updater process or finalized staged overlay was found. Old backups/previous installation remain untouched.
- Both Ford trial preferences remain 1; DisableUpdates remains 1; alpha longitudinal remains 0; ExperimentalMode remains absent/off; confirmation flag and OpenpilotEnabledToggle remain 1; DisengageOnAccelerator remains 0.
- Installed steering source asserts owner 1.20/0.97. Critical source hashes and selected settings match before/after the backup.

## Private backup locations

- Comma: `/data/navigator-backups/<private timestamp identifier>-pre-master-migration/`.
- Mac: `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-master-migration/` (outside Git repositories; owner-only parent directory and files).

The complete application archive contains source overlay/untracked files, native artifacts/models and parent/submodule Git metadata. Separate archives preserve complete parameter storage including symlink layout, calibration, private network configuration and launcher/service configuration. Working-tree patches, source/settings inventory, checksum manifest and post-backup checks accompany them. Private archives and full parameter data are not committed or published.

## Verification

All copied files match the device-side SHA256 and byte counts. Every compressed archive was streamed/read and its gzip CRC checked. Critical source hashes match inventory; parent/child Git metadata are present; selected archived parameter values match the inventory and calibration is present. Saved CalibrationParams, CarParamsPersistent, LiveParametersV2 and LiveTorqueParameters were compared with live files after backup and match.

This is archive/content integrity evidence, not a restoration, recovery boot, OS image or firmware backup. Services remained running; this is not a transactionally frozen snapshot of all ephemeral parameters. Critical settings/source and the listed calibration/learned files were explicitly checked for consistency.

## Remaining installation work

No candidate staging or migration was started. Recheck parked/power/network and available capacity before downloading another installation. Establish supported OS/firmware recovery before the deliberate AGNOS 19.9 migration. Do not treat the application backup as a proven OS downgrade path, copy the old prebuilt marker, enable alpha/experimental longitudinal, or launch the new branch during read-only preparation.
