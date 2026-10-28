<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator steering: latest-drive evidence, 2026-10-14

## Finding

Two latest saved drives contain sustained 20–30 mph turns. Two full-rate segments from the earlier drive supply a 40–50 mph comparison. The selected windows support the owner's description of weaker low-speed tracking in steering-model estimates, but are not matched turns and do not establish a speed-only root cause or validate a tuning change.

A repeated yaw-versus-steering-model offset is the strongest additional diagnostic finding. Existing angle control estimates current curvature as -raw yawRate/vEgoRaw. A fitted yaw-rate offset of roughly 0.015–0.017 rad/s (0.9 degrees/s) appears across three drives. Its effect in curvature units increases as speed falls. This is disagreement between estimators, not proof that the yaw sensor is defective or that the learned steering model is correct.

No tuning, parameters, source files, services, safety modes, or vehicle configuration were changed during this analysis. No active ECU queries or live CAN reads were performed.

## Source and extraction

`extract_saved.py` reads saved rlogs using installed Cap'n Proto definitions and zstandard, at low CPU priority and with bytecode writes disabled. It emits selected numeric signals only to Mac artifacts. Two drives are anonymized as drive-1 and drive-2. `extract_earlier.py` screens the earlier qlogs; `extract_fast.py` reads earlier full-rate segments 26 and 29 selected for 40–50 mph coverage. No GPS, VIN, device serial, camera imagery, or wall-clock identity data was exported.

`selected-signals.json`, `earlier-signals.json`, and `fast-signals.json` preserve extracted signals. `analysis.json` holds results and `manifest.json` hashes the artifacts. Relative time is derived from the first exported event, not clock dates, because prior investigation found device clock resets.

carState/carControl/controlsState were sampled at about 10 Hz from rlogs. Recorded sendcan angle messages were retained at their available rate. This is analysis of saved messages, not active access to vehicle interfaces.

## Time matching and sign checks

`analyze.py` matches carControl with nearest carState, controlsState, and sendcan within 80 ms, and modelV2 within 150 ms. Primary newer-drive analysis requires lateral active, driver steeringPressed false, no model lane change, encoded steering request mode 1, and requested curvature >=0.00015 /m. These are filtering criteria, not proof of absence of every external disturbance.

Signed curvature conventions follow installed code: controlsState.curvature is negative vehicle-model curvature, and current angle-controller curvature is -yawRate/vEgoRaw. Encoded LatCtlPath_An_Actl is inverted by the controller on transmission, so decoded messages were negated back into controller sign.

The DBC defines the path-angle signal as an 11-bit unsigned value with scale 0.0005 rad and offset -0.5 rad. Message 0x3D6 on bus 0 was decoded using the corresponding installed safety bit layout. sendcan is evidence of messages queued for Panda, not independent proof of PSCM reception or acceptance.

carOutput.actuatorsOutput.curvature must not be treated as actual angle-mode steering demand: installed controller sets apply_curvature to zero in angle mode. This analysis uses encoded path-angle messages instead.

## Recorded command agreement

Median absolute discrepancy between the reconstructed static command formula and encoded commands:

| Dataset/speed | Median discrepancy (rad) |
|---|---:|
| Newer drive-1, 20–30 mph | 0.000143 |
| Newer drive-2, 20–30 mph | 0.000229 |
| Earlier full-rate segments, 40–50 mph | 0.000165 |

These are comparable to half a 0.0005 rad encoding step. They support that the recorded commands broadly follow the installed formula. Reconstruction does not reproduce every controller frame, rate-limiter state, or raw source time exactly.

## Sustained-turn comparison

Windows require >=4 seconds continuous selected samples, constant request sign, requested magnitude >=0.0003 /m, and request coefficient of variation <=0.5. Four candidate response delays (0, 0.2, 0.5, 1 second) were examined for yaw; this is screening, not vehicle-dynamics identification.

| Selected window | Mean speed | Median request (/m) | Median model curvature (/m) | Median model/request sample ratio | Potential deviation clip |
|---|---:|---:|---:|---:|---:|
| Newer drive-2, 107.52–112.64 s | 27.66 mph | 0.002851 | 0.001864 | 0.648 | 0% |
| Earlier fast segments, 50.74–57.15 s | 42.59 mph | -0.000870 | -0.001007 | 1.081 | 0% |

Ratios are median of individual time-matched sample ratios, not ratios of column medians. A model/request ratio below one is consistent with undertracking relative to the requested curvature estimate. It is not a direct lane-deviation measurement, a physical steering-authority percentage, or proof the model geometry/calibration is correct. The opposite-sign turn directions and different curve magnitudes mean these windows are not a controlled speed comparison.

## Yaw/model disagreement

Fit controller-sign yaw rate (-yawRate) against controlsState.curvature*vEgoRaw using active, hands-not-pressing data above 20 mph with time matching. Three residual-trimming iterations reduce transient/outlier influence. This exploratory linear fit has no independent ground-truth validation.

| Drive | Fitted slope | Offset rad/s | Offset degrees/s | Selected fit samples |
|---|---:|---:|---:|---:|
| Newer drive-1 | 0.958 | 0.01517 | 0.869 | 556 |
| Newer drive-2 | 0.973 | 0.01556 | 0.892 | 498 |
| Earlier drive qlogs | 0.991 | 0.01679 | 0.962 | 2,819 |

Approximate curvature offset from 0.0155 rad/s would be 0.00173 /m at 20 mph, 0.00116 /m at 30 mph, and 0.00077 /m at 45 mph. These values are substantial relative to the controller's +/-0.002 /m curvature band.

In the newer drive-2 sustained gentle-turn window 162.01–168.15 s (28.01 mph), requested curvature is negative (median -0.000662 /m) and steering-model curvature is negative (-0.000438 /m), while raw-yaw curvature is positive (+0.000817 /m). A simple same-time measured/requested ratio would therefore mislabel the response. The earlier coarse screen correctly withheld conclusions from these ratios; this analysis identifies a repeated offset as a plausible explanation.

Possible causes still include yaw zero-point/decoding/calibration differences and steering-model parameter errors. The fits do not establish which estimator reflects actual road curvature. Independent motion estimates, learned-model parameters, raw yaw encoding, and straight-road behavior must be checked before selecting a feedback correction.

## Clipping and safety observations

Potential software deviation clipping reconstructed from the saved input values was around 5–6% of selected 20–30 mph samples in the two newer drives. The sustained tighter-turn example and selected faster comparison had none. This does not support clipping as a universal explanation for the weak low-speed turn.

Recorded Panda blocked-counter maxima were 7 and 10 in the newer drives, and up to 15 in the selected older data. No recorded safetyRxChecksInvalid samples appeared. Counter totals alone do not identify blocked message types or prove continuous steering acceptance; a block-timestamp investigation would be needed to attribute them. Safety configurations vary around transitions; no safety mode was changed by the analysis.

## Offline sensitivity of 1.20 -> 1.25

Held-recording-input evaluation changes only the high-curvature gain endpoint. It does not simulate vehicle response, planner reaction, driver reaction, or resulting lane tracking.

- At or below 13.5 m/s (30.2 mph), the high-curvature gain endpoint goes from 1.30*1.20=1.56 to 1.30*1.25=1.625, a 4.17% increase.
- Low-curvature gain is unchanged. Blended responses change by less than 4.17%.
- At or above 26.82 m/s (60 mph), the high-speed endpoint remains 1.425*0.97; this constant change has no effect there.
- 70.35% and 68.78% of the selected 20–30 mph samples in the two newer drives would be unchanged.
- The selected tighter low-speed turn would get about 4.17% more static path-angle demand. The gentle-turn sign-disagreement example would get no gain change.
- The selected 42.6 mph window's median static-command increase would be about 1.53%.

Thus 1.25 is a small high-curvature sensitivity change, not a demonstrated cure for most observed low-speed/gentle-turn behavior. Nothing here proves that it is safe or unsafe in the actual vehicle. No value was changed or road-tested.

## Next evidence

Focus on the persistent yaw/model offset and distinguish planner demand from physical response on matched left/right steady curves. Inspect saved model parameters and independently derived motion before selecting a correction. Preserve the current source and do not incidentally install the pending pinion/safety update as a tuning fix.

This is a saved-drive diagnosis with explicit limits. It is not a validated retrofit, a road test, a closed-loop simulation, or approval of a steering change.
