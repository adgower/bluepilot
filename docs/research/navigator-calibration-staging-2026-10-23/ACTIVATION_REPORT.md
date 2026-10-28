<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Calibration fix activation — October 23, 2026

Activated exact published pair **openpilot `fe08ede1af29a9c37b0c8b3550ce66cbd9392348` / opendbc `d2e8d0404143da0f2685c2ff4932b9b9f702951f`** on `codex/navigator-tracking-release`. User confirmed responsive home screen after installation and Alpha ON while offroad, then ignition ON/stationary Park/assistance disengaged. AGNOS20.1 slot B and the existing firmware remain unchanged.

## Preservation and recovery

Fresh activation snapshot: 69 parameter files, independently checksum-verified on device and private Mac backup `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-calibration-fix` before the switch. Whole original install retained at `/data/openpilot.pre-calibration-fix-<private timestamp identifier>`. Atomic rename exchange succeeded. Active and rollback parent/child repositories are clean; exact gitlink and calibration-fix controlsd SHA256 verified. Seven protected source/firmware/launcher files match. Owner steering **1.20/0.97**, geometry, pinion/tracking opt-ins and preferences retained. No OS update, firmware flash, reboot or manual CAN/ECU request. The running app was restarted only with ignition off.

First attempt automatically restored the original installation because the whole-parameter guard flagged `OnroadCycleRequested`. All source/preferences/calibration checks passed. Source declares this boolean CLEAR_ON_MANAGER_START; the activation checker was corrected to classify only this documented transient flag as runtime state. The unchanged candidate then passed activation. The first attempt log is retained; stale device rollback/error receipts describe that historical attempt, not the final successful state.

During the successful offroad swap all five learned/calibration binary hashes matched the fresh snapshot. After owner ignition-on, LiveParametersV2, LiveTorqueParameters, LiveDelay and CarParamsPersistent hashes changed in the running stack; no manual cache write/reset/restoration was performed. CalibrationParams still matches. Alpha and coordination are ON by owner confirmation; assistance stayed disengaged throughout powered acceptance.

## Completed acceptance

Full ARM build and offline validation passed before activation: 979 native/integration tests,12,083subtests,14 parent smoke tests, subprocess-isolated19-case calibration engagement regression, real pipeline and default/stall contracts. See [staging report](REPORT.md) for provenance and limits.

Ignition-off acceptance passed:201Panda samples, no reported faults or blocked-TX increments. Powered Alpha/Park acceptance passed for **55.04seconds**: all16topics alive/valid,551Panda samples, zero RX-invalid/blockedTX/transport faults, correct Ford Alpha safety parameter11 and controlsAllowed=false. Big model ran20.003fps, zero reported frame drops. All1,101atomic calibration snapshots were valid; all1,101coordination request poses were valid, producer maximum observed age20.75ms,1,101inactive feedback packets and zero coordination faults. No vehicle/steering/radar/Chestnut supply fault or unexpected stopped process. Assistance remained disengaged and the vehicle stationary in Park.

## Road evidence still required

Activation and parked checks are complete. This does not yet prove moving engagement, disappearance of Controls Mismatch in driving, physical brake-release/grade/restart behavior, reduced brake/accel cycling or fuel efficiency. Next is a short supervised low/moderate-speed trial and log review before highway expansion. Stop the trial if Controls Mismatch or unsafe behavior recurs. Keep the whole original rollback and both private backup snapshots.
