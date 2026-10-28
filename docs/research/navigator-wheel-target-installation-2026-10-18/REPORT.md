<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Calibrated wheel-target trial installation — October 18, 2026

Status: paired branches published and activated; full device validation and ignition-off acceptance passed. Powered stationary acceptance passed after user confirmation of ignition on in Park.

The user authorized publication, backup and installation, and confirmed parked ignition off, stable power/Wi-Fi, screen access and recovery cables. No OS/firmware update or active ECU diagnostics are part of this installation.

## Exact pair

Both `codex/navigator-tracking-release` branches were pushed without force to the existing adgower origins, child first, with remote heads verified:

- openpilot `50baa6fd6acf9d37b7e0768e5736efab2a357ddc`
- opendbc `0e65f296260ec16da3c3b814c10ac5f36f8b2e4c`

Previous active pair: `ff6ff263084a4bc433cf197b44ce3a31f7608851` / `9d5a3d485085f36beeb9aff7baf53c0d4ea603ee`. AGNOS19.9; clean tracked source. Existing high-speed preference already enabled; no new preference is required.

## Backup and validation

Fresh device backup: `/data/navigator-backups/<private timestamp identifier>-pre-wheel-target`; archive SHA256 `086f2747f5275663612274301905a471471096e29565e99b9320e5b8e309ad51`,843,586,700bytes. Captures66parameters, both source archives, signed firmware and launchers. Private Mac copy target: `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-wheel-target`. Mac archive hash,143manifest members and both nested source archives verified. Raw settings stay private.

Stage: `/data/navigator-validation/<private timestamp identifier>-50baa6fd6`. Dedicated validation unit masks vehicle interfaces, isolates networking and parameters, and mounts active source read-only. Device ARM build and native tests precede preparation/activation. Local additional280transition cases/100,800frames pass bounds/slew/settling checks; these are in-memory tests, not physical handling proof.

The installation helper review found no material installation/isolation/rollback issue. The historical `resume-replay` path contains an obsolete exact test count and is not used; fresh validation must complete normally.

## Preservation and limits

Preserve owner1.20/0.97, geometry, fixed pinion, native safety, all existing preferences, learned calibration and signed installed firmware. `DisableUpdates=1`, Alpha longitudinal off and ExperimentalMode absent/off remain. Guarded whole-directory activation retains the previous binary/source install and automatically restores it if acceptance fails.

Frozen saved-input replay and parked checks do not establish improved physical handling. The requested model path near the lane edge remains a separate issue. No dedicated high-speed reproduction drive is requested.

## Device acceptance

Full isolated ARM SCons build passed. Ford/native-safety suite:477passed,79skipped,12,063subtests passed. Existing roll-mapping320transition cases/115,200frames and wheel-target280cases/100,800frames passed. Eight actual Card factory combinations and Controls/Card/Cap’n Proto IPC screen passed. Validation duration1,046.86seconds. Live heads/source/preferences/manager/service preserved during validation.

Atomic directory exchange activated the exact new pair. Twenty-second passive ignition-off acceptance passed: normal processes, NO_OUTPUT, no ignition/control permissions, no new faults or blocked-transmission increments. All selected preferences and five learned/calibration hashes equal the backup; protected1.20/0.97/source/firmware/launchers match. No new preference was written (historical receipt field names still call the existing preference a new trial).

Retained whole previous install: `/data/navigator-previous-wheel-target-<private timestamp identifier>`. Installer rollback restores this whole tree and restarts the service on acceptance failure. For any later rollback, stop the service only while parked ignition off, inventory/back up intervening settings first, and restore the retained whole install; do not mix parent/child or restore stale learned parameters blindly.

## Powered stationary acceptance — complete

55-second passive check passed with ignition on, stationary Park and assistance disengaged. All monitored topics alive/valid, no sampled vehicle/steering/CAN faults, correct Ford safety configuration10 and no blocked-transmission increments, no Chestnut supply fault. Big model sustained approximately20fps with zero reported frame drops. Exact installed parent/child and clean source verified. Existing preferences and geometry match. Learned steer ratio, average offset, delay, extrinsics calibration and torque payload retained. Stiffness reset from0.995896to1.0 and torque-cache timestamp changed during normal upstream startup; no stale cache was restored. See powered-parked-check.json and learned-preservation.json.

Installation and parked acceptance are complete. Physical improvement remains unproved. Start with ordinary supervised driving on familiar roads at legal speeds; take over immediately if tracking is uncomfortable, and note approximate time/location for review. No deliberate lane-edge or85mph reproduction is needed.
