<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator yaw baseline and low-speed steering investigation

2026-10-14. Read-only saved-recording analysis. No Comma files, parameters, services, safety modes, or vehicle configuration were changed. No active CAN reads or ECU queries were performed.

## What is now established

The decoded vehicle CAN yaw has a nonzero baseline while the vehicle is stopped. This baseline is visible in the saved raw message bytes, passes through CarState, and then affects angle-controller curvature feedback. Comma's separately calibrated device-motion estimate is near zero in those same stopped intervals. This is stronger evidence than the prior comparison against a learned steering model.

The software location is established: raw message 0x91 / Yaw_Data_FD1 -> DBC VehYaw_W_Actl -> CarState.yawRate -> LateralAngle.get_current_curvature. The exact underlying OEM cause (module zero-point/calibration, expected raw-signal bias, or Navigator-specific encoding) is NOT established. Do not call it a defective sensor or change the universal Ford DBC offset solely on these recordings.

## Stationary evidence

Saved rlogs were read with calibrated DeviceMotion and ExtrinsicsCalibration through the installed pure in-memory Pose/PoseCalibrator helpers. Stationary selection requires vEgoRaw<0.05 m/s, standstill=true, valid calibrated motion/sensor flags, and motion timestamp matching within 120 ms.

| Drive | Selected stopped samples | Median CAN yaw rad/s | Median independent yaw rad/s | Median raw CAN yaw value |
|---|---:|---:|---:|---:|
| Newer drive-1 | 71 | -0.0160 | +0.000247 | 32420 |
| Newer drive-2 | 844 | -0.0158 | +0.000053 | 32421 |
| Earlier selected segments | 119 | -0.0174 | +0.000186 | 32413 |

The installed DBC converts the raw yaw field using `raw*0.0002-6.5`. It gives zero at raw=32500. For raw=32420 the decoded value is exactly -0.016 rad/s. The saved signal quality code is 3 throughout the extracted raw frames; quality does not establish calibration correctness.

Stopped selection is strong zero-motion evidence, although small vibrations, timestamp matching, and Comma motion-estimator validity are not laboratory ground truth. The modest baseline variation between drives argues against treating one captured value as an immutable universal calibration constant.

## Moving comparison and sign convention

Calibrated DeviceMotion z yaw and Ford CAN yaw use opposite signs in these recordings. Moving fits show CAN yaw approximately equals `-independent_yaw - 0.016`. Controller-sign independent curvature is therefore `+calibrated_device_yaw/vEgoRaw`; controller-sign CAN curvature is `-CarState.yawRate/vEgoRaw`. This was verified from the fitted sign, code's road-frame observation convention, and turn comparisons; subtracting identically signed signals without this correction would be misleading.

Exploratory robust linear fits (outlier trimming, speed>5 m/s, no driver steeringPressed, valid calibrated motion):

| Drive | CAN-vs-independent slope | Intercept rad/s | Median absolute residual rad/s |
|---|---:|---:|---:|
| Newer drive-1 | -0.972 | -0.01574 | 0.000722 |
| Newer drive-2 | -0.997 | -0.01595 | 0.000788 |
| Earlier selected segments | -1.002 | -0.01682 | 0.000756 |

Near-unity magnitude slopes support compatible units and broadly correct dynamic scaling. Nonzero intercepts, also seen stopped, isolate a baseline mismatch rather than merely a learned steering-ratio discrepancy. They do not distinguish a manufacturer's intended signal baseline from module calibration bias.

The learned parameters are marked valid in these selected drives. Median learned steer ratios are about 22.48, 22.45, and 22.54; stiffness is about 1.00–1.02; steering angle offsets and road-roll estimates vary. Validity flags alone do not prove geometry accuracy. Learned-model comparisons understate independent response on some low-speed data, so the motion estimate supplies a useful additional cross-check.

## Source chain and safety implications

Remote installed files read directly:

- `/data/openpilot/opendbc/dbc/ford_lincoln_base_pt.dbc:3169`: message 145 (0x91), Yaw_Data_FD1; VehYaw_W_Actl is big-endian 16-bit starting bit 23, scale 0.0002 rad/s, offset -6.5.
- `/data/openpilot/opendbc/car/ford/carstate.py:36`: assigns the decoded signal directly to yawRate.
- `/data/openpilot/opendbc/car/ford/lateral_angle.py`: current curvature is -yawRate/max(vEgoRaw,0.1); +/-0.002 /m demand-deviation clip begins above 9 m/s.
- `/data/openpilot/opendbc/safety/modes/ford.h`: independently converts the SAME raw bytes with scale 0.0002 and offset -6.5 and uses this curvature for its shadow-curvature checks above its speed threshold.
- `/data/openpilot/openpilot/selfdrive/locationd/paramsd.py`: learned vehicle parameters observe calibrated DeviceMotion, not the raw Ford yaw field directly.

A Python-only yaw correction must NOT be assumed compatible with the existing Panda feedback check. Fix planning must preserve coherent feedback interpretation across controller and safety without bypassing or widening safeguards. A shared, verified change requires offline controller/safety replay and review; no such implementation was applied here.

## How the baseline affects low-speed control

A 0.016 rad/s zero-point mismatch corresponds to about 0.00179 /m curvature at 20 mph, 0.00119 /m at 30 mph, and 0.00080 /m at 45 mph. The same bias therefore occupies much more of the +/-0.002 /m feedback band at low speeds. It also makes feedback asymmetrical between opposite turn directions.

A held-input counterfactual in `feedback_counterfactual.py` removes each drive's observed stationary baseline from CAN yaw, keeps the existing +/-0.002 limit and recorded demands, and recomputes potential clipping. This is NOT a closed-loop simulation, an approved calibration, or a tested fix.

| Drive/speed | Original potential clip | Baseline-corrected potential clip |
|---|---:|---:|
| Newer drive-1, 20–30 mph | 6.25% | 1.21% |
| Newer drive-2, 20–30 mph | 5.40% | 0.235% |
| Newer drive-2, 30–40 mph | 12.07% | 1.724% |
| Earlier selected segments, 40–50 mph | 0% | 0% |

Selection here omits the earlier model lane-change mask, so percentages differ slightly from the prior screen. Newer 30–40 mph coverage is limited (58 selected samples in drive-2). Clipping reconstruction does not count actual safety rejections or reproduce every controller frame.

## Low-speed undertracking is also present independently

| Selected sustained turn | Mean mph | Median independent/requested curvature ratio |
|---|---:|---:|
| Newer drive-2, tighter turn (107.5–112.7 s) | 27.66 | 0.605 |
| Newer drive-2, gentler turn (162.0–168.2 s) | 28.01 | 0.716 |
| Earlier faster turn (50.7–57.2 s relative to extracted segments) | 42.59 | 1.075 |

This supports actual motion undertracking in the selected low-speed windows, beyond a learned-model artifact. Different road turns, demand magnitudes, direction, acceleration, and timing prevent treating ratios as a pure speed-response curve or converting them directly into a tuning multiplier. No direct lane-deviation or closed-loop stability conclusion follows.

Neither low-speed window was clipped in the original sustained-turn analysis. Correcting the yaw baseline therefore does not change their static command through that limiter. It cannot by itself explain or repair all the undertracking.

## Recorded PSCM limit status

Decoded recorded message 0x3CC / Lane_Assist_Data3_FD1 using installed DBC bits:

- Selected newer low-speed segments: 933 active/no-driver-press frames at 20–30 mph show steering_status=2 (ContLatControlInProgress), limit_status=0 (LimitNotReached), capability=2.
- Selected earlier segments: 1,396 frames at 40–50 mph show limit_status=0; 3 show limit_status=1 (LimitClose). 96 selected 30–40 mph frames show limit_status=0.

This does not support a continuously reported PSCM limit ceiling as the low-speed cause in these selected frames. It does not prove every possible internal constraint absent or that all commands were accepted.

## What needs to change, and in what order

1. Establish the proper yaw zero-point policy for this Navigator. Check applicable OEM signal/calibration information or qualified read-only service evidence to distinguish an encoding mismatch from module calibration. The raw/signal boundary is identified; manufacturer intent is not. Do not globally alter the Ford DBC or hardcode +0.016 from one drive as a permanent fix.
2. Prepare a consistent feedback correction or verified alternative in an isolated local checkout. The pending pinion-curvature branch is a candidate to evaluate because it replaces yaw-derived feedback, but it also changes the safety path and uses fixed geometry. It is not automatically validated by this diagnosis and should not be installed incidentally.
3. Replay the controller/safety combination against the saved raw CAN and independent motion, including left/right curves, stopped/rolling transitions, driver overrides, and recorded safety-block timestamps. Preserve the existing safety limits. Baseline correction should eliminate the observed stationary/moving mismatch without creating incompatible safety feedback.
4. After feedback is understood, address the separate low-speed command-response map. Installed low-curvature gain remains 1.0 below about 30 mph, whereas the 1.20 factor boosts only the high-curvature arm. A low-speed calibration must cover BOTH gentle and tighter turns while retaining the satisfactory high-speed behavior. Do not derive a "best" multiplier directly from the two non-matched turn ratios.
5. Validate any candidate offline first, then separately arrange parked/device and controlled vehicle validation. Saved logs cannot establish the response or stability of a new controller in the actual vehicle.

The 1.20->1.25 change is a high-curvature-only command increase of up to 4.17%; it neither corrects the yaw baseline nor changes the gentle low-curvature arm. It is not a comprehensive fix for the identified issues.

## Artifacts and limits

`extract.py`, `analyze.py`, `feedback_counterfactual.py`, and `extract_status.py` document reproducible read-only calculations. `signals.json` contains selected numeric signals without GPS, VIN, device serials, images, or credentials. `analysis.json`, `counterfactual.json`, and `status.json` contain results. Stationary-baseline and sign assertions are recorded in verification output; checksums are in manifest.json.

Exact manufacturer-level calibration/encoding cause and the best low-speed tuning remain unresolved. The investigation has established a vehicle-CAN decoded baseline mismatch, independent low-speed undertracking in selected turns, and useful repair boundaries. It has NOT established a deployable fix, changed steering, or reproduced a new controller on the road.
