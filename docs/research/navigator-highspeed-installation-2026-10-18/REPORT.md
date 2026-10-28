<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator body-confirmed high-speed installation — October 18, 2026

User authorized pushing both paired branches to the existing adgower repositories, fresh backup and installation, and confirmed parked ignition-off state, stable power/Wi-Fi, screen access and recovery cables. No OS or firmware update is part of this installation.

## Published and active pair

- openpilot `ff6ff263084a4bc433cf197b44ce3a31f7608851`
- opendbc `9d5a3d485085f36beeb9aff7baf53c0d4ea603ee`
- Both `codex/navigator-tracking-release` branches pushed without force; exact remote heads verified. [Publication](../../navigator-reference/PRIVATE_ARTIFACTS.md), [prior full Mac build/540-segment replay](../navigator-paired-highspeed-build-2026-10-18/REPORT.md).

## Backup and rollback

Fresh private backup: `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-highspeed` on the Mac and `/data/navigator-backups/<private timestamp identifier>-pre-highspeed` on device. Archive **843,575,681 bytes**, SHA256 `850bfbb7da57825ccfab80efba1bdca4c228f8b5068a9a5acd17429d63197efc`; all145 manifest members verified and both nested source archives read to EOF. [Verification](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Whole original installation retained at `/data/navigator-previous-highspeed-<private timestamp identifier>`, plus rollback branches. This is source/settings/launchers/signed-firmware preservation, not an OS or model image or a tested OS recovery procedure.

## Completed validation and activation

Full separate ARM SCons build passed. Isolated native Ford/controller/context tests: **440 passed,79 skipped,12,063 subtests**. Deterministic transition screen: **320 cases /115,200 frames**, bounds and reference rejoin passed. Real producer/local-msgq/card pipeline passed, as did all8 exact constructor/factory combinations. Mount/network/device isolation and live source/settings/service preservation were verified. The Mac540-segment replay is not claimed as a new540-segment device replay.

One retained pipeline helper still asserted the previous isolation-prefix name. Corrected only that helper check, preserved passing native/transition evidence, and resumed the pipeline in the same restricted environment; it passed. Initial failed-attempt receipts remain. Installer review found no blocking issues. A direct evidence download encountered root-owned diagnostic files; privileged read-only tar download preserves their permissions.

The guarded whole-directory swap succeeded. Application normal startup completed and ignition-off acceptance passed: **201 healthy Panda samples**, NO_OUTPUT, no controls/ignition/RX/safety/heartbeat fault, TX-blocked0, no unexpectedly stopped process. Baseline historical TX-blocked4 was stable before restart; this is not a cumulative lifetime count comparison.

Exact active heads and clean source match the published pair. Owner **1.20/0.97**, fixed pinion/geometry, signed firmware, launchers, selected preferences and calibration hashes passed preservation guards. The only intentional new preference is **FordPrefHighSpeedTracking=True**; pinion, low-speed, persistent tracking, roll mapping and DisableUpdates remain enabled. Alpha longitudinal and Experimental Mode remain off. AGNOS remains19.9. [Activation](../../navigator-reference/PRIVATE_ARTIFACTS.md), [preservation](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Acceptance status

**Installed; ignition-off and powered stationary Park acceptance passed. Road handling remains unverified.**

User confirmed ignition on and stationary in Park with assistance disengaged. Passive55.02s acceptance: all12topics alive/valid, zero speed, Ford safety parameter10,550Panda samples with zeroRX-invalid/TX-blocked/SPI errors, no heartbeat loss/faults or unexpectedly stopped process. Large model1101frames at19.999fps, no frame drops, mean39.57ms execution; all1101atomic calibration snapshots valid. [Powered check](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Additional passive35s real-motion adapter check:700motion samples,697valid transformed samples after startup; all four topics alive/valid. Finalsource age31.38ms, receipt age2.69ms, yaw standard deviation0.01338rad/s. This checks an observer using the installed adapter, not internal active-controller instrumentation or high-speed eligibility. [Motion check](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Learned ratio22.7136803, average offset−0.5723621deg and delay0.2542532s retained, along with profile/geometry/flags/safety, CalibrationParams and torque-cache payload. Stiffness0.9977184→1.0 and torque event timestamp advanced during normal estimator startup; no stale estimator cache was restored. [Learned preservation](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Final read-only post-powered checks confirm exact paired clean heads, existing preferences except the intentional new key, protected source/launchers/signed firmware, AGNOS19.9 and whole-original rollback directory. [Final preservation](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The new trial only reduces commands when fresh wheel/body evidence agrees above60mph, with smooth onset to70mph and withdrawal/rearm guards. It preserves below60mph and owner calibration. Replay changes are not measured tracking improvement or proof that the reported bend/lane-cutting issue is fixed. No special high-speed reproduction drive is requested.

For the next ordinary supervised drive, use familiar roads at appropriate legal speeds and note approximate times of understeer, overshoot or intervention. No need to reproduce the85mph event. The option is already enabled; there is no new UI toggle. This is a limited personal trial, not demonstrated lane-clearance or handling improvement.
