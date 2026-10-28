<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Post-calibration-fix drive review — October 23, 2026

**The calibration-only validity bug did not recur in these recordings, but Controls Mismatch is not fully resolved. Alpha still cycles braking and propulsion, and its end-to-end planner usually limits speed well below the selected cruise speed. Lateral work also remains. No device changes were made.**

## Evidence and scope

Downloaded all37completed unseen segments across three sessions (321,115,156bytes), verified their source hashes remotely before/after and again locally. No open segments deferred. Session01 is four pre-update parked segments on e9ddc7668 with no active driving; exclude it from post-fix performance. Sessions02/03 contain33segments on exact parent fe08ede1a / child d2e8d040, roughly22.4minutes of as-of longitudinal-active coverage including stops. Source remained clean and settings/protected files/service unchanged during acquisition. Owner1.20/0.97 retained. Raw identities/GPS remain in the private download cache.

Full-rate health and exact first-fault packet inspection are separate from20Hz performance alignment. Past-only joins reject stale topic data; performance metrics exclude driver pedals where stated. Descriptive windows are correlated, not independent trials. These roads and lead situations differ from the first Alpha trial, so this is not a causal before/after smoothness score.

## Controls Mismatch: one remaining freshness-timing failure

At **<private clock time> CDT, approximately64.2mph**, coordination latched `invalid_pose_or_accel` and disengaged, with no driver pedal/steering input at the onset. There were no other coordination fault transitions in the new-source sessions and no active invalid-CAN samples in the20Hz review.

Across129,779recorded longitudinal-active control packets, **zero carried poseValid=false**. The earlier calibration-only false-validity mechanism was not observed. For the exact failed sequence84867:

- Pose validity and reference validity were true, request finite (+0.08863m/s²), and surrounding motion health flags were true.
- Motion age at request production was81.521ms. The controller consumed that request22.847ms later, making it104.368ms old—past the unchanged100ms safety limit.
- A newer healthy motion message was timestamped23.399ms before the fault, just0.552ms before that request's producer timestamp. It was not reflected in the consumed request. A control packet containing the newer pose was published6.112ms after the fault, too late to avoid it.
- Surrounding motion publications continue at roughly20Hz with about19–30ms source-to-publication age. This does not look like another calibration-only invalidation. Logging timestamps do not establish exact IPC receipt/order, so the precise producer/subscriber scheduling cause remains unproved.

**Next local investigation:** coherent producer/consumer snapshot timing, age headroom and delivery/polling behavior. Reproduce this exact boundary and ensure a fresh coherent request reaches the consumer while retaining the100ms guard and genuine fault latching. Do not mark this solved by accepting stale motion, forcing validity, or merely increasing a timeout. [Exact timing evidence](../../navigator-reference/PRIVATE_ARTIFACTS.md), [full-rate health](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Why the85mph setting did not produce85mph

The cruise setting really reached85mph; this is not an mph/kph misunderstanding. The new recordings' maximum actual speed was about65.9mph (66.0mph raw-wheel estimate), and maximum actual speed during eligible85mph-setting samples was63.7mph.

With85mph selected, no detected lead and actual speed already above45mph, there are **126.39seconds** of eligible data. The recorded plan source is end-to-end (`e2e`) for126.34seconds. Median actual speed is55.8mph, maximum58.4mph, median planner acceleration only+0.017m/s², and the recorded acceleration boost is zero. Including slower scenes, no-lead85mph-setting coverage is160.92seconds, with e2e selected for160.82seconds.

The installed planner explicitly chooses the minimum acceleration candidate among lead/MPC, cruise and the end-to-end model; it also permits stopping when any candidate requests it. Cruise setting is therefore a ceiling rather than a promise to accelerate to that speed. The inspected selection path uses no dedicated posted-speed-limit input. This is evidence for **model-limited speed policy**, not proof the model is reading/following speed-limit signs. Leads account for additional limited periods. The cruise maximum constant is145km/h (~90mph), so the constant itself does not explain this shortfall.

Source: local paired `openpilot/selfdrive/controls/lib/longitudinal_planner.py` lines100–114 and `openpilot/selfdrive/car/cruise.py` lines8–14. [Recorded no-lead case](../../navigator-reference/PRIVATE_ARTIFACTS.md).

**Next policy decision:** separate the desired OEM-like cruise/lead-following behavior from always-on end-to-end speed selection before treating this as an actuator-gain problem. Preserve lead/stop constraints; any alternate policy needs design and regression testing. No mode or planner change was made.

## Braking, acceleration, coasting and grade

Your report of continued cycling is supported. Examples with at least95% eligible active coverage:

| Start CDT | Median speed | Brake-command transitions in20s | Observation |
|---|---:|---:|---|
|<private clock time>|58mph|29|Downhill-indicated, lead present; reported brake torque above4Nm for48% of samples|
|<private clock time>|56mph|26|Downhill-indicated, lead present; brake torque above4Nm for51%|
|<private clock time>|61mph|22|Mostly no detected lead|
|<private clock time>|27mph|17|Near-level proxy, not exclusively downhill|
|<private clock time>|22mph|21|Lead-following, downhill-indicated|

These are command transitions, not a claim that every edge produced a separate physical brake application. Reported brake torque nevertheless confirms that the concern is more than a display artifact. The first Alpha drive's worst examined highway window had33edges/20s; this drive's29 is only an unmatched descriptive comparison, not a demonstrated percentage improvement.

For942.48seconds of main-drive eligible moving Alpha control (no driver pedals), brake requests occupy31.8% of samples, reported brake torque>4Nm27.7%, and strict brake/precharge-free inactive-propulsion coast commands only4.0%. In the slower drive, corresponding fractions are40.4%,38.2% and3.0%. Low strict-coast fraction does not mean every other sample is braking: ordinary propulsion can maintain speed smoothly.

The grade proxy is the calibrated pitch gravity term plus the controller's relative OEM-derived offset. In the main drive, braking requests occupy56.4% of downhill-indicated samples,23.6% near-level and16.0% uphill-indicated; actual reported braking torque follows the same direction. This supports a grade association but not surveyed road-slope accuracy or causality. Pitch contains dynamics/reference uncertainty, and lead/planner demand differs between groups.

Even in146.52seconds with no lead and planner acceleration between−0.1and+0.1m/s², brake requests appear32.3% of samples and reported torque>4Nm25.7%. Some downhill braking is necessary to hold the planner's selected speed, but the model's reluctance to accelerate plus grade-sensitive brake allocation gives a plausible path to the sensation of braking instead of coasting. Separate planner demand, gravity compensation, integral/feedback and actual release behavior before changing thresholds. The current logs do not justify disabling necessary braking or promise better fuel economy. [Detailed contexts](../../navigator-reference/PRIVATE_ARTIFACTS.md), [worst windows and bands](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Five recorded active stops subsequently crossed3mph with longitudinal still active and no intervening driver pedal. Four crossed3mph about1.2–1.4seconds after their final<0.8mph sample; one took5.8seconds. That interval includes creeping and is not a measured lead-move-to-launch delay. This is useful restart evidence, not comprehensive stop/grade safety or ride-quality proof. [Stop records](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Lateral review across speed ranges

These are calibrated body-yaw estimates relative to requested turning, excluding stale data, driver override and lane changes. They are not independent ground-truth wheel calibration, and transient under-response cannot simply be inverted into a gain multiplier.

| mph | Evidence |
|---|---|
|0–15|No sufficient clean meaningful-turn pool for a calibration conclusion|
|15–20|5.85s transient pool; median response53%. Sharp19mph episode overlaps driver input and “turn exceeds limit”|
|20–25|15.55s transient pool; median66%; shortfall episodes remain|
|25–30|14.05s pooled median76%; only1.35s steady (median93%), so do not conclude a fixed gain error|
|30–35|6.05s pooled; delayed entry/shortfall example around30–31mph; no adequate steady pool|
|35–40|Only1.5s meaningful pool; insufficient evidence|
|40–45|19.4s steady, median114% response, p10–p90 108–119%|
|45–50|25.45s steady, median116%, p10–p90 110–126%; turning directions imbalanced|
|50–55|7.15s steady, median115%, p10–p90 101–126%; thin evidence|
|55–60|35.75s steady, median102%, p10–p90 91–115%|
|60–65|10.2s steady, median101%, p10–p90 89–118%; mainly one turn direction|
|65–70|Brief travel only, no adequate qualifying-turn pool|
|70–85|Not driven in these recordings;85mph set speed supplies no85mph steering validation|

The body-yaw uncertainty is material; road/roll, direction, path choice and wheel/body mapping remain possible contributors. Especially at40–50mph, the observed error and propagated yaw uncertainty can be comparable. Do not apply a universal gain reduction from these medians.

There are29grouped steering-pressure/disengagement events:28include steering input, eight include turn signals, two include brake input; categories overlap. They are **not29 proven unsafe takeovers**. Six longitudinal deactivations comprise the one Controls Mismatch and five pedal-associated events. Full times, alerts and pre-input response are in [the intervention table](INTERVENTIONS.md).

Priority lateral episodes:

- **<private clock time>,57.9mph:** no turn signal; preceding clean body-response median155% of request. Investigate requested-path withdrawal, calibrated wheel target/unwind and lane context.
- **<private clock time>,50.1mph:** preceding median123% before steering input.
- **<private clock time>,19.1mph**, and **<private clock time>,24.8mph:** preceding response about49%/58%, “turn exceeds limit” and steering input. Treat as turn-entry/authority evidence, not permission to increase gain past the deviation/vehicle limits.
- **<private clock time>,64.2mph:** automatic mismatch disengagement, separate from a confirmed driver lateral correction.

## Recommended order

1. Resolve the exact coherent-snapshot freshness/timing mismatch locally, preserving the guard and latched disengagement.
2. Decide the desired model-versus-cruise speed policy; the85mph symptom is mainly upstream planning in this recording.
3. Replay the marked cycling/coasting/grade windows through the actual integrated planner/controller/actuator path, including release/feedback and conservative stopping.
4. Investigate40–55mph excess turning and the marked58mph unwind/input episode, then low-speed bounded turn-entry limits. Continue balanced turn evidence; no conclusion about80–85mph stability.

OEM ACC remains the sensible baseline while Alpha has an unexpected-disengagement case and unwanted cycling. No code, settings, OS, firmware, services or CAN/ECU requests were changed during this review.
