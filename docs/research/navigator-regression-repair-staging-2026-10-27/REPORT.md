<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Regression repair staging complete — October 27, 2026

**Published, backed up, separately staged and validated; candidate remains inactive.** Full ARM build/recheck and1,304 tests plus12,083 subtests passed (79skipped, one existing capnp repeated-write test warning). Final source/settings/calibration/firmware/service audit and passive active-install offroad check passed. No activation, active-service restart, reboot, OS/firmware update, active ECU request or CAN transmission occurred.

## Exact identities and recovery material

- Candidate parent `e05e42f43d2907a4f02915a924cfd95a46197e79` pins child `5097b993965b2b65ea3fcca7e3769cfa9403d49c` on `codex/navigator-tracking-release`. Both adgower remote heads were rechecked and match.
- Separate candidate: `/data/navigator-validation/<private timestamp identifier>-e05e42f43/source`. Both candidate repositories are clean, track the published pair, and have self-contained Git objects; all submodule connectivity checks passed. Only immutable Git objects share hardlinks; working files are separate.
- Active pair remains `df788e02719c05595dab2f980e6fd9fb9e464006` / `1d29e6e78abcbf5c6a80eb397d80b349c6cca960`. Its manager PIDs, service start timestamp and source hashes did not change during validation.
- Original full private backup: `/data/navigator-backups/<private timestamp identifier>-pre-regression-repair` on device and `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-regression-repair` on Mac. SHA256,821,973,108archive bytes,145manifest entries and both nested source archives verified.
- Fresh post-drive private checkpoint: `/data/navigator-backups/<private timestamp identifier>-pre-regression-repair/return-checkpoints/<private timestamp identifier>` on device, `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-regression-repair/return-checkpoints/<private timestamp identifier>` on Mac; all138manifest entries verified. Preservation checks use this current checkpoint so learned values from the intervening drive are retained rather than restored to the older backup.

## Completed verification

The first full SCons ARM compilation passed before departure. Its test run was intentionally stopped when the owner needed to drive; the entire interrupted evidence directory was retained on device and copied to `evidence-departure/` on Mac. On return, the exact source/assets were reverified, private test parameters were recreated, and the same full SCons command passed again with the completed build cache. No old partial test result was counted as a completed suite.

Fresh isolated Ford/native/context/clock/engagement run: **1,304 passed,79skipped,12,083subtests**, zero failures/errors. Hooks were compiled from the candidate source on ARM, without sanitizer claims. Isolation receipts verify active data read-only, private params/cache/log/home, blocked vehicle devices, network interfaces down/no routes, dropped privileges and no capabilities. The supervisor monitored ignition-off state and resource limits. Minimum available memory stayed above2.3GB and free data storage above9.5GB during this run. See `evidence/runner-status.json`, `native-junit.xml`, `replay.log` and `isolation-*.json`.

All253committed LFS assets were hash-verified. Candidate manifests and exact gitlink were checked; installed signed firmware and launch behavior were preserved. The prebuilt marker was carried only after the complete ARM build. Candidate branch/remote-tracking metadata was finalized without switching the active tree.

Final audit retained **Alpha ON,1.20/0.97**, current selected settings, calibration hashes, geometry, AGNOS20.1/slotB, firmware, launchers and the active service. During the test interval only `UptimeOffroad` and `LastAthenaPingTime` changed among parameter hashes; selected/protected values were unchanged. Passive existing telemetry yielded81board samples with ignition off, noOutput and no reported board/receive/heartbeat faults. Existing blocked-TX counter values remained[10]; this is no observed increase, not a claim that the historical counter was zero. About9.52GB data space remained at final audit.

## Limits and next boundary

The [local integration report](../navigator-regression-repair-integration-2026-10-27/REPORT.md) documents237segment longitudinal production parity and658segment scheduled steering parity. Those are distinct from this ARM test suite. There was no fresh full route-native replay, candidate powered acceptance or road validation here. The two historical release-timeout faults and current-install sub40mph pulsing remain open evidence; physical comfort/tracking improvement is unproved.

**Activation was explicitly excluded and has not occurred.** The current installation remains usable. Candidate offroad/powered acceptance must follow a separately authorized activation; this report does not claim that the candidate was tested as the running vehicle stack.

Initial candidate indexing needed the device's Git LFS runtime on PATH; the corrected verification passed. A resume-helper quoting error was rejected by Python before any device action, then corrected and syntax-checked. Original failure logs are retained. No production source or settings were weakened to accommodate these helper issues.

`VERIFICATION.json` binds final receipts, exact pair, backup/checkpoint archive hashes and evidence files. `final-audit.json` is the read-only final source/settings/telemetry result.
