<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Original steering actuator-response data, not reconstructed commands

## New nine-session capture

Directory: `${USER_HOME}/Apps/bluepilot/docs/research/navigator-post-regression-drives-2026-10-27/lateral/`

- `post-regression-session-01-signals.json.zst` through `...-09-signals.json.zst`: original recorded extracted streams; strongest existing detailed source for direct wire/ECUangle work. Extractor: `extract.py` in that directory.
- Matching `...-normalized.npz`: anonymous50ms analysis grids; direct recorded `u` path-angle, `wheel_angle_deg`, `mph`, requested_curvature/reference, roll/learned_ratio/stiffness/angle_offset_deg, wire_mode, lat_active, driver_pressed, and qualification/phase fields. These grids are past-only but decimated; do not treat them as exact command/sensor timestamps for system identification.
- `analysis.json` contains per-session recorded source parents/settings and coverage.01–06are pre-update48segments;07–09record currentparent31segments, but07stationary,08onlymeaningful moving source(21segments),09near-stationary/missing motion/model/calibration streams. Missing data are not valid zeros.
- Original segment hashes: parent directory`input-manifest.json`; acquisition provenance includes private capture root `${PRIVATE_CACHE}<session-label>/segment-NNN/rlog.zst`. Durable archive verification is in`durable-archive-verification.json`.

Detailed compressed JSON schema:

- top-level`first_monotonic_ns`: add to relative seconds to recover original event clock; software/configuration retain original source cohorts, not generated-current-source assumptions.
- `streams.tx`: `[relative_sendcan_event_s, decoded_original_path_angle_rad, original_mode]`. These are ORIGINAL recorded sendcan0x3d6/bus0packets, decoded as `-((((d[3]&31)<<6)|(d[4]>>2))*.0005-.5)`. Sendcan publication is not proof of ECUreceipt/acceptance.
- `streams.cs`: `[carState_publication_s, vEgoRaw_m_s, raw_CAN_yaw, steeringAngleDeg, steeringPressed, steeringTorque, brakePressed, gasPressed, steerFaultTemporary, steerFaultPermanent, cruise_enabled, canValid, turn_signal, gear_string]`. steeringAngleDeg is original ECU compensated pinion-angle estimate. This extraction did not retain its quality flag or exact last-CAN-frame sample age; re-extract original carState.vehicleSensorsInvalid and/or raw CAN for those.
- `streams.calibration`: `[carControl_publication_s, navigatorCalibration_dict]`. Fields include valid/sourceMonoTime/stateMonoTime/computedMonoTime/targetSpeed/roll/steerRatio/stiffnessFactor/angleOffsetDeg/requestedCurvature/targetAngleDeg. Exact producer snapshot, not later latest-parameter substitution.
- `streams.parameters`: `[vehicleParameters_publication_s,valid,roll,steerRatio,stiffnessFactor,angleOffsetDeg]`. Original publication/source event; not automatically atomic with a control record.
- `streams.cc`: `[carControl_publication_s,latActive,requestedCurvature,atomicSteeringAngleDeg,envelopeValid]`.

Source-age caution: carState time is a publication time, not necessarily the ECUangle's physical CANsample. The model must preserve past-only lookup and explicit command/state age and, if necessary, decode original raw CAN. The signal is `SteeringPinion_Data.StePinComp_An_Est`, nominal0.1degDBC resolution; its quality signal is `StePinCompAnEst_D_Qf`(carstate expects3). Raw bus0message address0x7e is defined by the exact installed Ford DBC; validate through the parser/DBC. No independent actuator/sensor covariance bound exists just from quantization.

## Prior original cohorts already extracted

- `${PRIVATE_CACHE}`: `coordinated-coast-road-session-*-signals.json.zst` and matching normalized arrays, including prior21segment session05. Same extractor-style schema, inspect metadata/cohorts before pooling.
- `${USER_HOME}/Apps/bluepilot/docs/research/navigator-calibration-first-2026-10-16/`: retained original normalized arrays for earlier named drives; normalization implementation `normalize.py` defines recorded `u` versus measured wheel/body fields.
- Complete original737segment corpus paths: `${USER_HOME}/Apps/bluepilot/docs/research/navigator-remaining-tracking-prototype-2026-10-27/corpus.json`,42anonymous session labels and paths. `manifest-verification.json`/`corpus-deduplication.json` prove737original hashes and737unique segments. This manifest references raw recordings in place; no download/device access is needed.

## Do not fit these as original actuation

`route-replays/*/commands.json(.zst)` in the current/prior prototype directories are GENERATED current-policy installed-reference/candidate commands against frozen input. Even the generated installed-reference column is a replay reconstruction, not the vehicle's recorded original sendcan. Prior`new-commands.npz`/`previous-commands.npz` may also be reconstruction products; use original stream extraction/manifests instead. Never use current proposed correction as if the recorded ECUangle responded to it.
