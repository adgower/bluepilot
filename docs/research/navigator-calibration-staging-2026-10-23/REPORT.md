<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Calibration fix publication and staging — October 23, 2026

**Historical staging snapshot:** activation and candidate powered acceptance subsequently passed. See the [current activation report](ACTIVATION_REPORT.md). Inactive/pending statements below describe the earlier staging phase.

## Exact pair and backup

Published and remote-verified `codex/navigator-tracking-release`: openpilot `fe08ede1af29a9c37b0c8b3550ce66cbd9392348`, opendbc `d2e8d0404143da0f2685c2ff4932b9b9f702951f`. Separate device candidate: `/data/navigator-validation/<private timestamp identifier>-fe08ede1a/source`. Current active installation remains `e9ddc7668eb996f8c0912004facd66aed9206072` / `d2e8d0404143da0f2685c2ff4932b9b9f702951f`.

Fresh backup `/data/navigator-backups/<private timestamp identifier>-pre-calibration-fix` and private Mac copy `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-calibration-fix` verified: 843,618,686-byte archive, complete SHA256 plus all 145 manifest entries and nested source archives read back successfully. All 68 parameters, parent/child sources, firmware image and launchers included. Fresh device rollback refs retained. Backup copies contain private settings and are not publication artifacts.

## Completed candidate checks

Full ARM `scons -j1` build passed in the separate checkout. Hardware/USB/SPI blocked, no network, private parameters/cache/logs, live source mounted read-only, unprivileged process with no new privileges and resource limits. All three probe/build/replay phases passed in 1,134.89 seconds. This is a native debug safety build, not a UBSan claim.

- 979 Ford/native and integration tests passed; 79 skips; 12,083 passing subtests.
- 14 parent smoke tests passed; six parameterized base-case skips.
- Subprocess-isolated calibration continuity/engagement regression passed on ARM (one wrapper exercising the 19-case module).
- Actual card/startup pipeline, stall/default settings and protected-child identity checks passed.
- All 253 LFS assets verified; exact child and protected steering/safety files unchanged.
- Source/settings/manager/service preservation audit passed. Only routine `UptimeOffroad` and `LastAthenaPingTime` parameters changed during validation; learned calibration unchanged.

Finalized candidate has independent Git object availability, both repositories clean, the backup's exact firmware image and launch behavior, and preserved prebuilt marker after the full build. Candidate remains inactive. Existing1.20/0.97 unchanged; no OS/firmware update, active settings write, restart or activation performed.

## Parked checks

Passive current-install ignition-off acceptance passed: 55 seconds, 551 Panda samples, no new blocked transmissions or reported faults. Recorded historical blocked count is retained rather than described as zero.

Powered stationary Park observation passed after owner confirmation with Alpha OFF: 55.00 seconds, all nine required topics alive/valid, 550 Panda samples, 5,496 car-state samples and 5,494 control samples, zero new blocked transmissions or faults, ~20 Hz big model with zero reported frame drops, and 1,100 healthy motion samples (maximum observed age35.54ms). Assistance remained disengaged. The old active installation still contains the calibration bug; the staged fix is not running. These checks and offline replays do not prove moving engagement, brake release/grades/restart or ride smoothness. Candidate activation and subsequent candidate powered acceptance remain separate steps.


## Final preservation audit and next step

Current install remains clean at the original e9ddc7668/d2e8d040 pair, AGNOS20.1 slot B. Seven protected source/firmware/launcher hashes and all 13 other selected settings match the backup; owner-selected Alpha OFF and ignition ON are the expected changes.1.20/0.97 remains unchanged. After ignition-on, binary hashes for LiveTorqueParameters, LiveDelay and CarParamsPersistent differ from the offroad snapshot; the running stack updated these caches, and no values were restored or manually written. CalibrationParams and LiveParametersV2 hashes still match. Earlier during isolated validation, all learned hashes remained unchanged, as documented in the preservation receipt.

Publication, backup, separate staging, ARM/offline validation and passive current-install parked checks are complete. The fix is NOT active and these are not candidate live or road checks. Next is separately authorized ignition-off activation with retained rollback, followed by responsive-screen and candidate powered acceptance before a drive. Keep Alpha off on the old installed version.
