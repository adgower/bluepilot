<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Coordinated coast/brake inactive staging — October 27, 2026

**Published, backed up and staged; candidate remains inactive.** The ARM build/offline checks and final preservation audit passed. No app restart, activation, reboot, OS/firmware update or CAN transmission was performed.

- Published openpilot `df788e02719c05595dab2f980e6fd9fb9e464006` /opendbc `1d29e6e78abcbf5c6a80eb397d80b349c6cca960` to both adgower `codex/navigator-tracking-release` branches. Remote heads reverified.
- Inactive source: `/data/navigator-validation/<private timestamp identifier>-df788e027/source`.
- Active source at the final audit: **`1dbbc0189` /`beb10c25`**, unchanged. Both staged repositories are clean, exactly pinned and have self-contained Git objects. Installed firmware image and prebuilt behavior were retained after the full ARM build.
- Private Mac backup: `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-coordinated-coast`. Archive821,970,076bytes, SHA-256 and all145manifest members verified;68parameter files captured. This is source/settings/calibration/launch/firmware recovery material, not an OS disk image.

## Validation

- Full isolated ARM SCons build, including model targets: pass.
- Fresh ARM native/Ford/transport suite: **1,252passed,79skipped,12,083passing subtests**.
- Retained controller/clearance regressions: **75passed**.
- Parent smoke: **14passed,6parameterized-base skips**; calibration continuity: **1passed**.
- Current-stack passive ignition-off check:55seconds /551Panda samples, historical blocked counter11 with **zero new increments**, no unexpected stopped processes. This observed the existing installation, not candidate hardware behavior.
- Isolation receipts verify read-only active data, private params/cache/log/home, network down, USB/SPI/GPIO/serial vehicle nodes blocked, dropped UID/capabilities and resource limits. Initial passive raw ignition was checked; ongoing guard monitors offroad state plus memory/disk limits.

## Corrected staging-harness assertion

The initial attempt passed the full ARM build,1,252native tests and75retained tests. A later pipeline check then failed because its private-prefix assertion still named the previous stage namespace. That staging-only assertion was corrected to the current namespace; no production source changed.

The failed attempt is retained in `evidence-attempt1`. The corrected validation reran isolation/build and the remaining tests, reusing the passed native XML/binary only after verifying **3,796bound source/binary/XML files**, exact candidate heads and clean source. The final acceptance passed every required phase. This is explicit hash-bound reuse of the fresh native run, not a claim that the native suite ran twice.

## Preservation and departure

The final read-only audit passed before the user left to drive. Selected preferences, binary calibration, additional personality/upgrade preferences and steering **1.20/0.97** match backup. Alpha stayed **ON**. Firmware,AGNOS20.1/slot_b,active service and `/data/continue.sh` are unchanged. Only ordinary `LastAthenaPingTime` and `UptimeOffroad` parameter counters changed.

Validation is complete and its background unit inactive. The user was told the previous install remains active and to drive manually with assistance disengaged given unresolved Alpha pulsing. No further device/network work was performed after that departure request; remaining documentation/verification was local.

## Limits

The new code is **not activated or road-validated**. Current-stack offroad observations do not establish candidate powered-Park behavior. The selected saved-replay benefit remains modest: fewer brief full-brake requests across the corpus, unchanged gas/combined brake-precharge timing, and14/12/10changes in the three new highway windows. Physical highway pulsing, RPM/fuel/comfort improvement remains unproved.

[Final audit](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [ARM acceptance](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Backup verification](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Final verification](PUBLIC_VERIFICATION.json)


Subsequent activation completed with powered-Park acceptance; see [ACTIVATION_REPORT.md](ACTIVATION_REPORT.md). Historical staging results above describe the earlier inactive state.
