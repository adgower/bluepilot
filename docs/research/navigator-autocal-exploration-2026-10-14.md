<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# BluePilot Ford auto-calibration exploration — 2026-10-14

Read-only primary-source review. No Comma changes, implementation, or Navigator replay of this proposed feature was performed.

## Exact provenance and what the linked PR contains

GitHub API returned PR #172 open, draft, unmerged, head `1cdbd4b29939c455c20debea98f290bb20c712d7`, base `faf135c68f36cd752f858c1886aaa8c79f9976d9`, updated `<private wall-clock timestamp>`. Its three-commit patch includes auto-calibration (`1b8caa2`), anti-weave smoothing (`332e75b`), and gauges (`1cdbd4b`). The top gauges change is display-only; the full PR diff includes control changes through the stacked work. [PR172](https://github.com/BluePilotDev/bluepilot/pull/172), [live API](https://api.github.com/repos/BluePilotDev/bluepilot/pulls/172), [exact head](https://github.com/ghbarker/bluepilot/tree/1cdbd4b29939c455c20debea98f290bb20c712d7).

The underlying auto-calibration is [PR161](https://github.com/BluePilotDev/bluepilot/pull/161); smoothing is [PR171](https://github.com/BluePilotDev/bluepilot/pull/171). Evidence in their descriptions is author-reported reference-car evidence, not Navigator validation.

## What is calibrated

The estimator learns the two Ford angle-mode speed-factor knobs, `FordLowSpeedFactor_ang` and `FordHighSpeedFactor_ang`. It fits weighted steady-curve and matched-apex observations, using applied gain divided by measured/requested curvature ratio. This tunes commanded angle conversion; it does not calibrate camera pose, physical wheelbase, mass, steering ratio, the RCM yaw zero, or a new yaw sensor. Lifecycle code writes factors, persists evidence, detects manual edits, and publishes status. [estimator](https://github.com/ghbarker/bluepilot/blob/1cdbd4b29939c455c20debea98f290bb20c712d7/opendbc_repo/opendbc/sunnypilot/car/ford/angle_autocal.py), [controller](https://github.com/ghbarker/bluepilot/blob/1cdbd4b29939c455c20debea98f290bb20c712d7/opendbc_repo/opendbc/sunnypilot/car/ford/angle_autocal_controller.py).

Actual feedback enters via `current_curvature` from `get_current_curvature`: default is negative RCM yaw divided by speed; pinion option uses VehicleModel curvature from steering angle, learned angle offset and roll. The estimator calls this measured curvature, but it is not independent IMU ground truth. Model geometry/offset errors can appear as gain errors. Our Navigator implementation intentionally has fixed Python/Panda geometry, so blindly substituting this learned-parameter feedback would violate the existing paired-measurement design. [feedback source](https://github.com/ghbarker/bluepilot/blob/1cdbd4b29939c455c20debea98f290bb20c712d7/opendbc_repo/opendbc/sunnypilot/car/ford/lateral_curv_ext.py), [strategy wiring](https://github.com/ghbarker/bluepilot/blob/1cdbd4b29939c455c20debea98f290bb20c712d7/opendbc_repo/opendbc/sunnypilot/car/ford/lateral_angle_ext.py).

## Bounds and material limitations checked in exact code

- Evidence requires speed at least **9.5 m/s / 21.25 mph**, curvature at least **0.001 /m** (apex minimum 0.0012), same-sign response, ratio 0.4–2.5, estimated liveDelay, and sufficiently quiet tracking.
- Delay alignment clamps estimated delay to 0.10–0.42 seconds. Limiter/saturation, light driver torque >=0.5 Nm, pressed history, disturbances, roughness, and excessive acceleration reject evidence. Lateral acceleration cutoff is 2.5 m/s².
- Factors remain 0.5–1.5; changes quantize to 0.01, damp at 0.7 of remaining fit error, cap at 0.05 per nudge, and occur no more often than each 20 seconds of collection. No separate cumulative per-drive movement cap exists.
- Each factor change requires fresh post-step verification. **Failed verification holds the changed factor, without rollback**; after extra evidence it may move again. This matches the PR's documented unresolved drift concern. Missing pre-step baseline can mark verification successful in code.
- Default lock freezes after sufficient evidence plus 300 seconds stability; disabling lock permits ongoing adaptation. Erase Calibration Memory resets both factors to 1.00, which would discard preserved 1.20/0.97 values if copied unchanged.

These bounds come from the exact estimator/controller sources linked above, not inferred tuning recommendations.

## Compatibility with Navigator trial

Our two intervention examples around 19.6 and 15.6 mph are below this estimator's admission floor. Auto-calibration therefore cannot directly identify or fit those frames. It might help qualifying higher-speed steady under-delivery, but is not evidence of a fix for sharp low-speed zigzags.

The PR fits the original curvature gain knee ending at 0.001 /m and speed anchors 13.5/26.82 m/s. Our trial broadens the transition to 0.00025–0.00125 /m and adds speed-dependent endpoint multipliers fading through 30–45 mph. Thus samples between 0.001 and 0.00125 no longer represent a fully high-curvature branch; its two-anchor regression is not the trial's actual gain model. Moreover its BOF platform gains are 0.95/0.95, different from our preserved angle mapping. The estimator must consume the exact deployed effective gain model, rather than importing its `values_ext.py` and overwriting ours. [PR gain model](https://github.com/ghbarker/bluepilot/blob/1cdbd4b29939c455c20debea98f290bb20c712d7/opendbc_repo/opendbc/sunnypilot/car/ford/values_ext.py), [our trial report](navigator-low-speed-prototype-2026-10-14/REPORT.md).

Smoothing is a separate candidate for rhythmic hunting: input-side gain-schedule filtering, prediction low-pass, exit-blend slew, entering hysteresis, and one-LSB outgoing wire hold. Neutral menu strength 1.0 is intended to preserve stock behavior. This warrants separate local analysis before coupling with calibration; the new trial already changes the gain transition that its principal filter targets. No evidence yet establishes this filter fixes our observed wheel tracking excursions. [exact smoothing source](https://github.com/ghbarker/bluepilot/blob/1cdbd4b29939c455c20debea98f290bb20c712d7/opendbc_repo/opendbc/sunnypilot/car/ford/angle_smoothing.py).

Port dependencies include estimator/controller, exact gain model, liveDelay subscriber and estimator status, limiter/saturation telemetry, parameters and persistence, custom cereal/CarState publishing, both device UI paths, and optional sunnylink. Gauges additionally depend on the BluePilot custom onroad debug overlay. Vanilla openpilot has a different controller organization and no equivalent BluePilot telemetry surface; this is a scoped port, not a clean standalone cherry-pick.

## Suggested next local investigation

Start in recommendation-only/offline mode, preserving 1.20/0.97 and current Python/Panda model. First compare pinion model response against independent calibrated device yaw on quiet segments; then audit sample admission, delay alignment, effective gain and confidence for each speed/turn direction. Evaluate smoothing separately on the existing hunting windows. Require rollback/preservation semantics before considering live factor writes.

The latest complete compact export contains carState, carControl, motion, liveParameters, wire TX, Panda and status streams, but no liveDelay stream; its carState tuple lacks per-wheel speed spread and acceleration. It is adequate for initial screening but insufficient to reproduce all original admission gates honestly. Earlier raw saved rlogs can be checked for those fields locally; absence must be reported, never treated as a valid estimated delay or zero disturbance. [post-trial evidence](navigator-post-trial-analysis-2026-10-14/REPORT.md).
