<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator budgeted tracking pair activation

Status: backed up, activated, ignition-off and powered parked acceptance passed. Road response remains untested.

## Installed pair and preserved configuration

- Parent `0cc74c94f3c6dafa3790c303be9ef345878bd792`.
- opendbc `d64ffcfa4e4a7556151962ca304d223a0a323375`.
- Branch `codex/navigator-tracking-release` in both repositories, active path `/data/openpilot`.
- Existing opt-in selects `BudgetedTrackingPrototype`; disabled selects the original `VeryLowSpeedGainPrototype`. Exact Car constructor tested with in-memory Params and stubbed IPC before app startup.
- Owner factors **1.20/0.97**, Navigator wheelbase **3.1115 m**, ratio **19.6**, existing pinion/low-speed/tracking options, update pause, Alpha/Experimental state and persistent calibration preserved.
- AGNOS remains **19.9**. Signed Panda image remains SHA-256 `5a10a6119110b3c41a03d381c4bdd3bea4e05c3a7164bef515b42df7054c466e`, identical to both original and separately built candidate. No OS/firmware updater or flasher was invoked by this activation.

The candidate previously passed [isolated device build and full offline replay](../navigator-device-staged-build-2026-10-15/REPORT.md). The active repositories were fast-forwarded to those exact commits; the borrowed-object staging directory was not substituted for the active path. Native code/dependency pins remain unchanged. Normal app startup completed successfully.

## Fresh backup and rollback

Fresh private Mac backup: `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-budgeted-activation`.

Device backup: `/data/navigator-backups/<private timestamp identifier>-pre-budgeted-activation`.

Read all archived file contents to EOF and recorded byte counts and SHA-256: 1,261 parent source files (929,372,160-byte archive), 479 child source files (7,055,360-byte archive), all 66 parameter files, plus launcher/firmware/inventory and candidate delta bundles. Saved selected settings and persistent calibration hashes before/after. Detailed private evidence includes guarded scripts and first-attempt diagnostics. This is source/settings recovery material, not a full OS image or a rehearsed full restoration.

Original heads retained in **both** repositories under `codex/navigator-pre-budgeted-20261015-123129`:

- Original parent `74f66e7a0bf1dc0718431532948ece2c4fb0041c`.
- Original child `1b965caadd4a6aea4d09985532bf7cca6c0873ca`.

A source rollback was exercised by the first stopped acceptance attempt. It restored both original heads; the guard deliberately left the application stopped while the parameter classification was investigated. The successful retry switched back to the existing candidate branches without advancing these rollback references. No reset/clean/forced overwrite was used.

## Ignition-off acceptance

[Acceptance receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md) and [prestart verification](../../navigator-reference/PRIVATE_ARTIFACTS.md):

- Both exact active heads and clean source; all protected preference comparisons pass.
- CalibrationParams, CarParamsPersistent, LiveParametersV2, LiveTorqueParameters and LiveDelay match the captured hashes.
- 1.20/0.97, geometry, launcher and signed Panda-image hashes preserved.
- 201 Panda samples: noOutput, ignition off, controls disallowed, no RX-invalid/fault/heartbeat issues; TX-blocked count stayed **0**.
- Required runtime topics alive/valid; no unexpectedly stopped required process (intentionally paused updater excluded).

## Startup-state investigation

The first acceptance attempt treated live `CarParams` as persistent calibration and compared all parameter files too strictly. Manager startup explicitly clears CarParams, cached control/route state, driver-preview state and lockout state; boot logging increments BootCount. These caused the expected mismatch, despite unchanged owner options and persistent calibration. Verified against `params_keys.h`, manager `clear_all(CLEAR_ON_MANAGER_START)` and boot logger code. The guard stopped the app and restored the original source before correction.

The final check protects all captured persistent settings/calibration and separately records documented startup state, Git metadata, heartbeat/uptime and live cache differences. It does not restore stale live CarParams or alter driver lockouts. Known upstream initialization of an absent ExperimentalMode was restored to the captured absent/off state only. See [recorded parameter differences](../../navigator-reference/PRIVATE_ARTIFACTS.md) and the final receipt. No steering algorithm or safety limit was changed during installation.

## Powered parked acceptance completed

After the owner confirmed ignition on and staying in Park, a 55.01-second passive check passed. [Powered summary](../../navigator-reference/PRIVATE_ARTIFACTS.md):

- All 12 observed topics alive/valid; vehicle 0 m/s, gear Park, assistance disabled/inactive, no alerts or detected vehicle/CAN/steering faults.
- Exact new source pair, both repositories clean. Live forced Expedition profile retains Navigator wheelbase3.1115m/ratio19.6, flags15, pinion/low-speed options, stock longitudinal and Ford safety10. Tracking enabled; update pause preserved; Alpha/Experimental off.
- 1,101 big-model samples at20.001fps,39.72ms mean execution, zero reported frame drops; Chestnut reports no supply fault.
- 550 Panda samples: Ford safety10, controls disallowed, zero RX-invalid/TX-blocked, no heartbeat loss/SPI errors/faults.
- Camera calibration reports calibrated. Owner1.20/.97 and all captured owner preferences match the pre-activation backup.

The additional [configuration preservation check](../../navigator-reference/PRIVATE_ARTIFACTS.md) compared decoded learned data rather than requiring stale serialized cache hashes. Ignition-on normally refreshes these files: learned steer ratio21.8716946 and average angle offset−0.8440931deg were retained; learned lateral delay0.2621531s and torque-parameter payload were unchanged. Existing upstream paramsd policy resets stiffness to1 each real drive and initializes transient state/uncertainties; no verification command restored or changed these caches. CarParamsPersistent differed only in its firmware-identification list, while live vehicle geometry/profile/flags/safety matched the previous drive. This is identification metadata refresh, not evidence of a firmware flash. Original extrinsic CalibrationParams remained byte-identical. [Decoded comparison](../../navigator-reference/PRIVATE_ARTIFACTS.md).

An optional initial comparison attempted the removed CarParams.mass field, then used a raw cache-hash equality assertion; these verification helpers failed without writing settings. The corrected semantic check above passed. Source values.py remained unchanged, and no mass/geometry tuning was performed.

This establishes powered stationary health of the installed revision, not closed-loop steering response, live high-demand metadata timing, road handling or improvement percentage. The passive script did not inject diagnostic/control requests or engage assistance. A supervised road comparison remains.
