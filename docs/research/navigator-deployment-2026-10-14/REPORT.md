<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator pinion + low-speed trial — installed

2026-10-14. User explicitly authorized backup and installation on the Comma. Installation completed over SSH while offroad. No vehicle ECU query was sent. Fresh direct Panda health confirmed ignition off and controls disabled before flashing and activation.

## Installed and enabled

- `FordPrefSteerAngleCurvature=true`: fixed pinion-model feedback with paired Panda safety parameter bit 8.
- `FordPrefLowSpeedGain=true`: explicitly selected Navigator low-speed trial. It activates only with supported pinion configuration and both controller flags; it adds no safety-mode bit or wider safety limit.
- Owner coefficients remain **1.20/0.97**.
- Trial gain effect fades from 30 to 45 mph; original gain calculation is used at ≥45 mph. Full recorded replay matched the pinion baseline at/above 45 mph on all **12,425** compared generated messages.
- All **85 original model files** were copied unchanged and hash-verified before activation.
- `DisableUpdates=true` retained.

Offroad Settings → Toggles now contains **Use Pinion Yaw Sensor** and **Navigator Low-speed Steering Trial**. Changes are blocked onroad and apply at the next vehicle start. The low-speed trial requires the pinion setting.

## Backup and recovery copies

Complete source, Git state, pre-existing changes, firmware/build artifacts and parameters were archived before installation:

- On Comma: `/data/navigator-backups/20261014-pinion-low-speed-preinstall/`
- Full prior working installation retained: `/data/navigator-previous-20261014/`
- Second private Mac copy: `${PRIVATE_CACHE}`

Both Mac archives matched the device manifest SHA256. `openpilot.tgz` is 2,729,735,326 bytes; `params.tgz` is 8,506 bytes. Archives contain private configuration; do not publish them. The Mac copy is in temporary storage, so the device archive and retained prior installation are the durable recovery copies.

To return to previous **controller steering behavior**, turn both trial toggles off with the vehicle off, then start the next vehicle session. Coefficients remain 1.20/0.97. A full code/firmware rollback can use the retained prior directory and its original signed Panda image; it must be performed offroad with ignition off and controls disabled. Do not restore all backed-up parameters blindly over later unrelated changes.

## Build and deployment evidence

Local activation wiring commits: opendbc `6c17a0af`; openpilot `07761dfa1`, atop the tested prototype and paired pinion commits. Device files were installed via a checksummed 15-file overlay on a copy of the existing installation. Installed Git metadata remains the prior branch/base with local changes; the source manifest records the exact deployed files. No remote branch was pushed and no upstream update was pulled.

- Real constructor/setting selection was replayed against all **45** saved segments. It generated exactly the same stream as the reviewed prototype: **252,406 controller updates, 10,082,330 RX frames, 148,765 accepted TX messages, zero TX rejections**. Pre-Ford initialization exclusions and warmup ticks remain documented in replay JSON.
- **181 targeted tests passed**, **77 skipped**, **12,000 subtests passed**; three UI contract tests also passed. Ruff and whitespace checks passed. Independent activation review found no blocking issue.
- On-device targeted build of `panda_h7.bin.signed` and `libparams_c.so` succeeded. Native Params recognized both new keys. Static installed controller construction selects `LowSpeedGainPrototype`, CP flags 7, safety param 10, with the geometry guard and 1.20/0.97 preserved.
- Panda app was flashed and its actual firmware signature verified against the staged image, and reverified after activation.
- All installed overlay source hashes verified after activation.
- Offroad startup process check found manager, UI, and pandad running. Direct post-install health reported ignition off, controls disabled, safety mode 19/no-output as expected offroad. The onroad safety parameter has **not** been observed live; param 10 is static constructor/configuration evidence until the next vehicle start.

A published parked-telemetry check returned no fresh messages, so direct board health was used before activation. One initial flash attempt stopped before flashing because this Panda API has no `get_mcu_type`; the supported API subsequently flashed and verified successfully. An initial activation guard stopped before source/settings changes because this version has no registered `IsOnroad` Params key; the corrected guard checks its optional file and fresh board health.

## Build limitation and startup handling

A broader isolated full build first failed because its model compiler hardcodes CPU 7 while only CPUs 0–3 were online. A temporary build-only affinity wrapper resolved that, but an unrelated model capture/replay check then stalled and was stopped. **The full device build did not pass.** Both changed native targets were subsequently rebuilt/reverified successfully.

Original model artifacts were restored and hash-verified, rather than deploying the partial model build. A standard `prebuilt` marker skips automatic startup recompilation; this is intentional for the frozen trial. A staging-path symlink retains any build-time path references. Updates remain paused. Before resuming source updates/builds later, remove/reassess the prebuilt marker and build environment deliberately so updates do not overwrite the trial or reproduce the offline-core compilation failure.

## What is and is not validated

Installed files, persistent settings, the selected controller constructor, paired firmware signature, and offroad service startup are verified. Saved-input replay validates recorded command/safety compatibility. The next vehicle session will read the enabled settings.

No road test or new physical response measurement was performed. The trial gives a ~20% larger command in the prior gentle example and ~5% in the stronger example; maximum blended-map uplift is ~35.75%. Those are command changes, not proven handling improvements. ≥45 mph parity is recorded-stream evidence, not a guarantee of every possible stateful transition.

## Inspectable files

`source-manifest.json`, `post-install-verification.json`, `source-overlay.tgz`, `full_replay.py`, replay JSON/console, and guarded `activate.py`/`verify_device.py` accompany this report. Private backups and device-side verification logs include checksums, activation record, firmware verification, and preserved-model hashes.

## Comma 4 settings-screen correction

After a device reboot, the user reported both controls missing. Inspection confirmed both settings remained enabled and the source/firmware were present. The original deployment exposed controls only in the larger-screen `TogglesLayout`, while Comma 4 routes to `TogglesLayoutMici`.

Fixed the actual MICI screen with two visible BigToggle controls, checked-state refresh from persistent parameters, supported-vehicle/offroad enabled predicates, and callback guards that prevent onroad writes. Both labels remain visible even if cached vehicle eligibility is unavailable. The controls appear after driving personality/experimental mode: **use pinion yaw sensor** and **navigator low-speed trial**. Regression tests instantiate the complete class constructor against graphics/parameter stubs; all three failed before the fix and passed afterward. Together with existing generic UI contracts: six tests passed. Ruff/whitespace checks passed. This is constructor/wiring evidence, not a pixel screenshot.

Local fix commit `c1bf21f3d`. The previous MICI file was backed up on the device before atomic replacement; source checksum manifest updated. Offroad manager/UI restarted to reload imports. Steering source, calibration, persistent option values, native libraries and flashed firmware were not changed by this UI correction.
