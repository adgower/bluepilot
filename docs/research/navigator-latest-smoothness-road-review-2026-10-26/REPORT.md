<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Latest drives: below-set speed and smoothness — October 26, 2026

## Result and device state

Downloaded all 14 newly completed segments across two sessions, about 122 MB, with source/settings/service equality before and after acquisition. Separately verified that all 154 completed recordings currently listed on the device have matching local raw copies, so older inventory-only deduplication did not hide an uncopied file. No active ECU query, setting change, source change, reboot or installation.

The new recordings are city drives starting around <private clock time> and <private clock time> Central. They run the same clean installed pair `5b301a944` / `884c9f491`, AGNOS 20.1. Maximum active measured speed is about 29.51 / 30.05 mph; recorded maximum set speed is 30 / 37 mph. These new recordings do not contain an 85 mph setpoint or highway run.

The owner explicitly chose **leave the Comma unchanged for now**. The separate below-6.7mph integral guard remains locally committed in `2ca969e45` / `bcd706d0`. It does not fix the model's road-speed choice or the highway pulsing. The newer coast work is recovered evidence and an unfinished response-model experiment, not a validated runtime patch to install.

## Why MAX does not mean the vehicle must reach that speed

The installed planner always chooses the lowest acceleration candidate from:

1. Radar/lead MPC.
2. The jerk-limited cruise/set-speed controller.
3. Model desired acceleration, including its bounded accelerator-override boost.

The set speed is therefore a **ceiling**, not an unconditional target. Raising MAX does not force acceleration when the road/traffic model or lead controller chooses less. Source inspection confirms the model candidate is unconditional in this branch: it is not gated by the old ExperimentalMode parameter. There is no separate posted-speed-limit controller/toggle in this planner. The code and logs do not establish whether the learned model reacted to a speed-limit sign, road geometry, a vehicle or another visual cue.

The selected source is `e2e` for 5,047/5,320 qualified planner samples (94.9%) in the first drive and 3,448/4,722 (73.0%) in the second. Both recordings report Relaxed personality. Aggressive/Standard/Relaxed affect the following controller; they do not remove the model candidate. Thus changing that setting need not resolve either below-set-speed behavior or Ford brake/coast transitions.

## Specific recorded examples

Times use recorded wall/monotonic clock pairs and America/Chicago, rather than assuming the host timezone.

- **<private clock time>–<private clock time>:** MAX 30 mph, median actual speed 19.24 mph, no detected lead throughout, selected source model. Median selected acceleration is about −0.018 m/s². This shows the effect can occur without a lead; it does not establish that going faster was appropriate for the visible road.
- **<private clock time>–<private clock time>:** MAX 35 mph, median actual speed 25.28 mph. Model selected throughout and the reconstructed boosted/clipped model action matches the published target. A lead is present throughout. Median selected acceleration is about +0.019 m/s², with a 10th–90th percentile range of about −0.310 to +0.570. There are 17 recorded brake-bit changes during the moving episode. This is a useful new combined planner/actuator regression; it is not proof of a hidden 25 mph speed-limit setting or an unnecessary lead restriction.
- **<private clock time>–<private clock time>:** MAX 35 mph, median actual speed 23.52 mph; model selected throughout, with a lead present most of the interval. There are 15 recorded brake-bit changes. Some time within the larger trip also uses the radar/lead candidate.

Model-action reconstruction uses exact model publication references, recorded boost and official acceleration limits. State-dependent boost scaling uses the latest available published state; that is an observational approximation of planner receipt order, not full planner replay. The 35mph example above matches within tolerance throughout; a few lower-speed reconstructed samples elsewhere do not exactly match, so no whole-trip bit-identity claim is made.

## The highway example is separate

The immediately preceding retained highway drives show MAX 70 or 75 mph with substantial below-set exposure. At least-10mph shortfall samples above 50mph include both model and radar-lead selection. In the retained 75mph example, a lead is present for about 92.4% of these samples. These are retained observations, not new highway testing. The specific claimed 85mph setting is not matched in the newly analyzed cohorts; do not treat it as verified 85mph actuation saturation or extend a tune on that basis.

## Smoothness and health

No coordination fault transition, controls-mismatch event or mismatch alert was recorded in either new session. This does not prove the historical fault permanently solved.

Recorded brake-bit changes persist across the city speed ranges:

| Drive | 0–20 mph changes / analyzed active span | 20–40 mph changes / analyzed active span |
|---|---|---|
| First | 13 / 158.43 s | 24 / 92.19 s |
| Second | 11 / 105.52 s | 39 / 109.30 s |

These are software mode changes, not a measured comfort score or a count of hydraulic brake pulses. City stopping, turns and following are included; rates cannot be compared with a highway route as proof of improvement. The 37.5second moving example above is a better fixed regression for joint demand and actuator analysis than a whole-trip switch total.

There are 11 and four recorded steering-input runs lasting at least 0.2seconds while enabled, largely at city speeds. They are retained as review candidates; steeringPressed alone does not establish a failure or driver takeover cause. These drives add no 60–85mph lateral stability evidence. No lateral tune is changed.

## Existing setting and engineering priorities

For conventional set-speed/following behavior on this Navigator, the existing alternative is **Settings → Developer → openpilot Longitudinal Control (Alpha) OFF**, while parked/offroad. Captured CarParams has radarUnavailable true and alphaLongitudinalAvailable true; the installed Ford interface enables openpilot longitudinal for this vehicle through Alpha. Turning it off returns longitudinal ownership to the existing Ford ACC path on the next configuration cycle. This was not changed remotely. It is a choice of longitudinal controller, not a posted-limit override switch.

A new custom stock-like cruise option inside Alpha would be a separate design. Removing model acceleration also affects learned slowing/stopping behavior, including traffic-light/road-context responses; it cannot be represented as a harmless speed-limit-toggle fix. The setpoint remains subordinate to following constraints in either controller.

For actual smoothing, keep two tracks explicit:

- **Planner/behavior:** characterize model demand variability and the desired distinction between model-selected road speed and conventional cruise. Do not try to fix low model demand by increasing vehicle gains.
- **Ford response:** continue the separately versioned coast-response experiment using recovered OEM torque/gear/grade/radar evidence, then coupled mode-selection/integral checks. The new 25mph moving episode joins the existing downhill/highway regressions. Neither track is currently a validated new code package for installation.

## Evidence

`acquisition-provenance.json`, private inventories/local-coverage check, 14-segment `input-manifest.json`, `quick-inventory.json`, `extraction.json`, `speed-and-smoothness.json`, `retained-highway-speed.json`, analysis scripts and verification preserve scope and provenance. Raw routes, full extracted rows and planner traces remain private. No remote source or settings writes were performed; equality was verified during acquisition. Local paired code remains unchanged.
