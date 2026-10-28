<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# OEM/Alpha pitch-reference investigation and local mapping

October23,2026. Local saved-data investigation only. No Comma contact, ECU queries, CAN transmission, paired-source edits, calibration reset, push or activation. Owner1.20/0.97 unchanged.

## Finding and resolution scope

There is a repeatable **relative longitudinal zero-reference gap** between the Ford motion/wheel reference and Comma's calibrated pitch reference. It appears during OEM ACC, Alpha and stops. A wrong pitch transport sign, wheel differentiation lag alone, or the inferred location filter bias does not explain most of it.

An OEM-only, route-balanced fit gives **+0.149913m/s²**, equivalent to approximately0.876° at level attitude. Applying that mapping to the held-out Alpha data reduces the moving median relative residual from **+0.164045 to+0.014132m/s²**. GNSS grade-proxy RMSE improves on each moving route, including Alpha. This resolves most of the *relative zero discrepancy in these saved data* and provides a report-local mapping prototype. It does not uniquely establish which physical sensor/body/calibration reference is wrong. The fit must not be written into global calibration or represented as measured road slope.

The prototype's frozen-input Alpha replay reduces eligible brake edges **213→79**, worst highway20s **33→4**, low-speed20s **24→2**. **These are command changes, not observed comfort, following-distance, stopping or fuel-economy gains.** Remaining cycling, upstream integral/actuator response and physical validation are unresolved. Not an installation candidate.

## Evidence and provenance

`extract.py` freshly hash-verifies58existing rlogs:35OEM segments/five routes plus23Alpha segments/one drive. Four OEM routes have moving qualification; the fifth provides stationary evidence only. All selected raw IMU, Ford motion/vertical channels, carState/carControl, pose, calibration and GNSS data are extracted into a separate private cache. Measurement and publish timestamps are retained. No coordinates or private route identifiers are exported. Manifest/source revisions and column definitions: `inputs.json`.

Profiles include older parent0171b8972/f750d756c and Alpha parentffebc4349. The PoseCalibrator matrix composition was checked at both older parent commits and the current source; it matches. No saved parameters were changed. Analysis excludes Ford fault/no-data numerical ranges, invalid poses/calibration/IMU, stale or future observations; moving comparisons exclude pedals and large yaw rate. Source channels are selected around25Hz; full Alpha command replay remains at actual50Hz send slots.

Past-only diagnostic alignment is driven by carState timestamps with pose/IMU/Ford/control age<=100ms, calibration<=2s and GNSS<=300ms. Twenty-second fit windows require >=300state samples, >=90%eligible moving coverage and no state gap>120ms. No centered filter or gap interpolation is used in this fit.

## Tracing the discrepancy

The source path is:

1. `openpilot/selfdrive/locationd/locationd.py` converts sensor axes to device axes as`[-v[2],-v[1],-v[0]]`.
2. `models/pose_kf.py` models accelerometer observations as device-frame gravity + acceleration + angular-velocity-cross-velocity + accelerometer bias.
3. `helpers.py` rotates device measurements into the calibrated frame and composes calibrated NED orientation.
4. `controlsd.publish()` copies that calibrated orientation into CarControl. The Ford controller uses`9.81*sin(pitch)` for brake-bit decisions; its comment says PCM itself applies pitch compensation to acceleration requests.

The cross-check compares Ford119 with`aEgo+9.81*sin(CC.pitch)`. Reconstructing calibrated pitch from recorded pose/extrinsics gives approximately zero median transport difference across routes. The sign is consistent with the NED/GNSS vertical-velocity convention. No transport/sign fix is supported.

To separate sensor-zero and filtering effects, raw IMU acceleration is rotated into the same calibrated frame. The inferred observation-equation residual is:

`raw_specific_force - (pose_acceleration + omega_cross_velocity + calibrated_gravity)`.

This is **not a logged exact bias state**: debug bias states are absent, and measurement/filter lag and vibration contribute. Its moving medians are about-0.006/-0.008/-0.038/-0.044m/s² across moving OEM routes and-0.043m/s² in Alpha. These do not explain the positive~0.15–0.20gap. Median Ford-minus-raw-calibrated-force differences remain about0.16–0.21moving and0.15–0.25stopped. The stopped difference rules out acceleration differentiation lag as the sole explanation. Body-frame mounting/sensor zero/compensation semantics remain possible physical owners.

Wheel/GNSS speed ratios are approximately0.9994/0.9996/0.9988/1.0012 across the moving OEM routes and1.0034in Alpha. This and the stopped evidence argue against wheel-speed scaling as the main constant offset. They do not identify absolute acceleration scale under every condition.

## OEM-only fit and independent checks

`fit.py` computes a median residual per eligible20s window, a median per OEM route, then the median of those four route medians. There are15training windows:1/1/9/4per route. Alpha does not participate in fit or offset selection. Two routes have only one eligible window, so route uncertainty remains material; this is not a large independent calibration corpus.

| Route | Moving median residual before | After OEM mapping | Steady GNSS grade-proxy RMSE before→after |
|---|---:|---:|---:|
| OEM01 |+0.168|+0.018|0.193→0.089|
| OEM02 |+0.204|+0.054|0.321→0.212|
| OEM04 |+0.135|-0.015|0.269→0.222|
| OEM05 |+0.135|-0.015|0.223→0.172|
| **Alpha held out** |**+0.164**|**+0.014**|**0.232→0.176**|

All unitsm/s². Leave-one-OEM-route-out median residuals are+0.022,+0.061,-0.022,-0.036. The~0.06held-out route discrepancy is larger than the installed0.02release margin, so this fit is **not instantaneous precision sufficient to certify that threshold**. The research qualification flag checks >=3moving routes, >=12windows, bounded offset and <=0.08route-holdout median residual; those are diagnostic screening criteria, not an established vehicle safety standard.

GNSS is not fit data. Its check uses no-pedal, low-yaw, near-steady samples with valid fixes, speed accuracy<0.5m/s and horizontal speed>10m/s. Vertical velocity still has substantial noise/lag, especially in individual20s windows. Improved aggregate GNSS agreement supports the correction direction, not a ground-truth road-angle certificate. Full results: `analysis.json`, `calibration.json`.

## Local mapping prototype

`mapping.py` is **default off**. It accepts the separately qualified OEM-derived offset; no0.18constant, brake-edge optimization or calibration reset. It slews the learned relative term in at0.005m/s³, fades it from zero at3m/s to full at5m/s, and uses only PID/active/fresh/valid pose context with no driver pedals. Stopping/starting, creep, disengagement or invalid context returns installed gravity. Only the brake decision term changes; brake acceleration requests, global pose/calibration, planner/PID implementation and steering remain unchanged.

The in-memory controller adapter requires saved pose timestamps because current CarControl does not carry the full atomic provenance needed for a deployment. During testing, the first adapter used a secondary state-aligned pose cache and unnecessarily declared a fresh pose stale. It now selects the newest past raw pose/calibration event directly. A failing regression contract covers this. The initial hard speed cutoff was also reproduced and replaced with a continuous3–5m/s fade. First-pass results remain under`first-pass/`.

There are no active/no-pedal/>=5m/s correction-reset drops in the final saved Alpha replay. Fade-related offset changes remain, and six reset drops>0.001occur outside that envelope. Invalid-context/disengagement fallback can still withdraw the correction abruptly. No claim of arbitrary-transition or physical bumplessness is made.

## Final Alpha replay and verification

Same SHA-verified328,469-event full-rate cache as earlier work;65,736actual ACC send slots per variant. The reconstructed baseline retains96.04%recorded-byte agreement. Unknown internal receive ordering/frame phase remains; comparisons are candidate-versus-reconstructed-baseline, not exact counterfactual vehicle behavior.

| Measure | Baseline | Mapping prototype |
|---|---:|---:|
| Eligible active/no-pedal/>5mph brake edges |213|79|
| Eligible actual-brake slots |13,411|8,809|
| Worst highway20s brake edges |33|4|
| Low-speed20s brake edges |24|2|

7,524packets change, only propulsion/precharge/actual-brake fields. No inactive, stopping/starting or below3m/s packet changes in this saved drive; brake acceleration is identical at every slot. No simultaneous actual-brake/valid-propulsion requests. All non-ACC hashes match, and the default-off variant has exact wire parity over all65,736slots. `comparison.json` contains results, including an overlapping highway window24→0; overlapping windows are not independent trials.

-11focused mapping/context contracts pass after observed RED failures, including slew, invalid/future/stale data, default off, stop/restart, speed fade and direct pose chronology (`mapping-tests.log`).
-Fresh Ford/native regression:886tests and12,083subtests pass,79skips. Candidate controller enabled with explicit fresh synthetic pose context for this suite; it is not merely testing a fallback that never activates (`ford-tests.log`, `ford-tests.xml`).
-Fresh recorded-RX native ACC-hook replay:5,260,361RX packets/variant and65,728TX slots after logged Ford11configuration. Recorded/baseline/candidate share the same three pedal/permission-boundary rejections; zero added candidate rejects and no relay fault. No forced permission. Uses retained debug Mac native library; only ACC TX hooks, no physical hardware or full lateral/forwarding/heartbeat replay (`rx-results.json`). Eight preconfiguration slots are excluded.

No new full paired build, ARM/device validation or closed-loop road/plant proof is claimed. Source hashes and clean exact paired heads are checked separately in`acceptance.json`.

## Remaining work before integration or another Alpha trial

The **relative mapping is now supported by independent OEM-to-Alpha evidence**; physical zero ownership remains non-identifiable from these recordings alone. Do not change camera/global steering calibration to force agreement. Stationary physical incline or an independent calibrated reference would be needed to distinguish mounting, raw sensor offset and Ford compensation ownership conclusively.

The next local work is a coherent default-off integration design with atomic pose/reference validity, safe withdrawal/re-entry and upstream integral/actuator feedback consistency. Existing LongControl integrates acceleration error; this replay freezes its recorded output. Removing brake edges can change subsequent engine torque, acceleration and integral demand, so the79-edge result does not prove that the closed loop will stay smooth. Validate grades, urgent braking, release/restart, stale contexts and the original highway cycling with a justified response model before preparing any installation. No additional Alpha road collection is needed for the current local work.
