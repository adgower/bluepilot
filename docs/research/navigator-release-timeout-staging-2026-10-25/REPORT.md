<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
**Latest status:** activated after explicit authorization; see [activation report](ACTIVATION_REPORT.md). The staging history below is retained.

# Brake-release timeout staging — October 25, 2026

Status: published, backed up, cleaned, ARM-validated and finalized as an inactive candidate. Powered Park check passed. Candidate remains inactive. No firmware or OS update, reboot or live source switch is authorized by this staging task.

Verified remote parent `ead00c30e0f3e174130f475847b1f4a2a76e8902` pins child `d4a201251d184a446cb2db383f4bd024c93e75cb` on the existing `codex/navigator-tracking-release` branches in adgower/openpilot and adgower/opendbc. Current device pair is `74eaa6a60d344f141d06da16f4dbe10d3de49c0e` / `3a5fe9fe5a296d44b7f898b580c2d3afafe6bfd1`.

Fresh private backup: `/data/navigator-backups/<private timestamp identifier>-pre-release-timeout`. Verified Mac copy: `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-release-timeout`. Archive 821,950,347 bytes, all 147 manifest files verified and nested source archives read to EOF. Alpha, preferences, learned calibration, 1.20/0.97, OS 20.1 and firmware are retained.

Cleanup targets only old source archive files with freshly hash-verified Mac copies. Current install, recent rollback copies and drive recordings are excluded. Receipts are in cleanup-verified-copies.json and cleanup-result.json.

Candidate stage: `/data/navigator-validation/<private timestamp identifier>-ead00c30e`. Validation uses private mount/network namespaces, parameters and caches, read-only live /data, blocked USB/CAN/serial/GPIO access, unprivileged workers, no new privileges and monitored ignition/memory/disk guards. Local helper acceptance tests passed (10 cases), as did 75 retained contract tests. ARM build, current-source native regression coverage and passive parked results will be added after completion. Powered parked checks observe the still-current stack; an inactive candidate has no physical actuator proof.

## Cleanup completed

Removed 30 redundant old source archives (12,651,070,171 bytes), preserving their verified Mac copies. Device free space increased to 22,128,349,184 bytes immediately after cleanup (about 20.6 GiB). No drive recordings, current install or recent rollback install were deleted. New staging will consume some of this free space.

## Ignition-off parked check

The unchanged current stack passed a 55-second passive ignition-off check: 551 Panda samples, no faults, no unexpected stopped processes, and no increase over the historical blocked-TX total of 13. Alpha remained ON. This is current-stack evidence, not staged-candidate physical actuation proof.

## ARM acceptance and final audit

Full isolated ARM SCons build passed. The native Ford/controller/context suite passed 1,105 tests and 12,083 subtests (79 platform skips); all 11 new release-progress cases passed on ARM. The 75 retained contracts, 14 parent smoke tests (six parameterized base-class skips) and one calibration regression passed. Total isolated duration was 1,146.9 seconds. Isolation and live-source/settings/manager/service preservation gates passed.

The finalized stage has self-contained Git objects, verified clean exact paired heads, preserved installed signed firmware/prebuilt behavior, unchanged preferences and learned calibration, and exact steering 1.20/0.97. Final read-only audit passed. Only runtime UptimeOffroad and LastAthenaPingTime parameter hashes changed. AGNOS 20.1 and slot _b remain unchanged. No activation or current service restart occurred. Powered Park observation also passed; it assesses the current stack, because the candidate is inactive.

## Powered Park acceptance and terminal status

After owner-confirmed ignition ON, stationary Park and disengaged assistance, a 55-second passive current-stack check passed: 550 Panda samples, 5,496 car-state samples, 5,486 control samples, 19.999 Hz model output, zero dropped frames, 1,100/1,100 healthy observed pose samples (maximum observed age 45.7 ms), no faults, no unexpected stopped processes and no new blocked transmissions. The blocked counter reset from historical 13 to 0 across the normal ignition transition; no increase occurred in either capture. Alpha remained ON. No control/diagnostic messages were sent by this check.

Published heads were reverified after validation. Final staged free space was about 19.3 GiB, after reclaiming 11.8 GiB and retaining the new stage. Both parked checks concern the still-current software; the new correction remains inactive. No live service restart, reboot, OS/firmware update or activation occurred. Device activation and subsequent candidate parked/road checks are separate next steps. See completion-receipt.json.
