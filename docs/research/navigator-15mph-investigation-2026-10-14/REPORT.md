<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator ~15 mph steering: local diagnosis and repair boundary

October 14, 2026 local time. Investigation only, using saved recordings. No SSH, ECU query, device write, controller-source change, parameter change, firmware change or deployment. Owner factors remain **1.20/0.97**. The isolated paired master-integration repositories remain clean at openpilot `6ae31161b73de2ce5043f708569759ac5f55f283` and opendbc `c09baff5c2cdd7c887e25c2d88b671f403e1ed9d`.

## What needs to change

The evidence points to the **very-low-speed curvature-to-path-angle response calibration**, separately from the yaw/pinion feedback option. The next local controller experiment should be a Navigator-scoped extra compensation below about 20 mph, with a smooth fade to zero by 25 mph. Apply it in the trial strategy's curvature factor, retaining the existing 1.20/0.97 constants and existing trial map above that range. This isolates it from the satisfactory ~45 mph behavior rather than retuning all speeds or changing the main factors.

This identifies the repair location and experiment shape, **not a proven numeric fix**. Evaluate gentle and tight turns separately, both signs, and rising/falling demand. Existing recordings establish the shortfall but do not supply how the vehicle would respond to a stronger command. Do not choose a 2–3× gain from the reciprocal of a transient tracking ratio. A concrete handling fix cannot be certified offline from this recording alone.

First evaluate a separate feedforward correction. If a persistent residual remains, separately assess a bounded, damped wheel/pinion tracking-error term; do not add an integrator or raw-CAN-yaw correction as part of the first experiment. The current application only reports wheel tracking error; it does not feed that error continuously into the Ford path-angle command. Changing desired wheel-angle reporting or the saturation threshold therefore will not create the missing correction.

Preserve DBC ranges, rate bounds, human override and paired safety behavior. No evidence in the selected turn justifies widening them. Any implementation would still need paired full controller/native safety replay, default/OFF regression, both turn directions, reversal behavior, and byte-identical high-speed command checks. The speed-isolation calculation here is arithmetic only, not that complete replay.

## Evidence and hypothesis discrimination

`investigate.py` executes the actual installed-revision `LowSpeedGainPrototype.update` locally at recorded send timestamps, holding saved input requests/vehicle states fixed. Its pinion-mode path output matches recorded wire commands in the selected late interval to median **0.000138 rad**, p95 **0.000337 rad**, below the 0.0005 rad wire encoding step. Nearest-topic timestamps and downsampling prevent an exact original internal-state reconstruction.

The repeatable observational check reproduces 176 selected frames at 927–938.03 s with median actual/requested curvature **0.312**. This is a diagnostic fixture, **not a closed-loop failing test that can prove a new command fixes the vehicle**. The real vehicle/EPS response is the missing test seam for that claim.

| Hypothesis | Prediction | Local result |
| --- | --- | --- |
| Low-speed conversion provides insufficient effective command | A valid request and transmitted command coexist with insufficient actual wheel/IMU response, without local clip/limit activity | Supported in the selected episode; conversion map is the primary experiment target. Exact EPS response law remains unidentified |
| Pure response delay explains the discrepancy | Shifting measured response later should largely recover requested motion before driver input | Delay helps but up to 1 s does not remove the gap; insufficient to attribute it solely to delay |
| CAN yaw bias is causing the 15 mph command deficit | Switching yaw/pinion in the actual strategy should alter commands there | Falsified for this episode: zero command difference |
| Existing low-speed trial excludes 15 mph or a controller limit caps it | Trial weighting should be absent or a limiter active before intervention | Not supported: full trial weight; no curvature-deviation clamp below 9 m/s; previous report found path/rate headroom, no EPS reached-limit indication or local safety blocks |

For 935–937 s, the same 40 base frames remain eligible in every fixed-delay probe, and future samples stop before detected intervention. Median actual/requested curvature is **0.356** with no shift, **0.483** at +0.5 s, and **0.638** at +1 s. Median paired wheel error falls from **10.18°** to **8.55°** and **6.26°**, respectively. This is a narrow observational probe, not an identified actuator delay; longer delays cannot be cleanly evaluated before the driver intervenes. Do not change the global actuator-delay setting from these numbers.

Exploratory first-order models were also fit to connected selected samples. Their feedback-correlated inputs, changing sample admission with delay, limited steady-state excitation, and persistence-dominated one-step fits do not justify selecting a gain or delay. They are retained in `analysis.json` as exploratory evidence, not used to certify a tuning value.

## Concrete local experiment shape

Modify only the Navigator trial strategy's `get_curvature_factor`, with a separate very-low-speed coefficient. Keep all current base factors and the existing 30–45 mph fade. A proposed extra weighting is full through 15 mph, smoothly decreasing over 15–25 mph, exactly zero at/above 25 mph. This could strengthen the selected 15 mph case while leaving current 25–45+ mph feedforward unchanged.

For sensitivity illustration only, a nominal extra 10% would yield 10% more unclipped command at 15 mph, 5% at 20 mph, and 0% at/above 25 mph. **10% is not a selected calibration and is not predicted to cure the observed deficit.** The analysis verifies only this isolation arithmetic; no new controller class, flag or toggle was implemented. The selected episode is already beyond the trial's tight-curvature blend endpoint, so broadening the gentle/tight blend again would not address its strongest portion.

Adding correction before the existing rate/range limits keeps those limits authoritative. State-dependent replay is still necessary: unchanged feedforward above 25 mph alone does not guarantee identical outputs immediately after a lower-speed history if a limiter/override state differs. Require both high-speed steady input equivalence and transition coverage before claiming preservation.

## Is the yaw/pinion issue resolved?

**The biased-CAN-yaw dependency is bypassed in the installed selected controller/safety mode; the raw yaw offset itself is not repaired.** Pinion is a steering-angle-derived estimate, not another physical yaw sensor or an OEM recalibration.

The new drive still contains a stationary raw CAN yaw median of **−0.01620 rad/s**, versus calibrated Comma IMU **−0.000202 rad/s** (9,943 matched selected samples). This is consistent with the earlier baseline mismatch. It does not establish whether factory signal encoding, module calibration or another manufacturer-level cause explains it. Do not globally patch the DBC from this observation.

Against calibrated Comma motion, selected no-detected-driver-input moving samples show:

| Speed | Matched frames | Raw CAN feedback median absolute yaw-equivalent error | Fixed pinion median absolute error |
| --- | --- | --- | --- |
| 10–15 mph | 618 | 0.01711 rad/s | 0.00254 rad/s |
| 15–20 mph | 1,713 | 0.01711 rad/s | 0.00278 rad/s |
| 20–30 mph | 3,061 | 0.01713 rad/s | 0.00352 rad/s |
| 30–40 mph | 760 | 0.01719 rad/s | 0.00554 rad/s |

Thus the new 20–30 mph samples again show about **79.5% lower median feedback error** with fixed pinion. This is estimator agreement, not 79.5% more steering or a handling-improvement percentage. Residual fixed-geometry/zero-point errors remain; Comma motion is a comparison reference, not independently certified ground truth.

In selected 10–20 mph replay, switching pinion back to yaw changes **0 of 1,016** commands by more than one wire step; all 176 selected late-turn commands are exactly equal between the two calculations. In 20–30 mph it changes 143/969 selected commands; in 30–40 mph, 6/142. This is expected because feedback mainly affects the deviation bound above 9 m/s. Pinion can remove a biased-feedback influence there without solving the lower-speed response map.

Current flags 15 and safety parameter 10 in the saved drive confirm selection of the paired pinion path. Earlier source/build/firmware and native tests support its installation. The first master-drive recorded replay still has three lateral transition-time rejections elsewhere, documented separately; do not call the entire implementation fault-free or claim all wandering resolved.

## Verification and sources

Run from this directory using the master-integration virtualenv:

```
python investigate.py /path/to/private/segment-00/rlog.zst
python verify.py
```

The anonymous signal export and prepared numeric matrix are the outputs from the [first master-drive analysis](../navigator-master-drive-analysis-2026-10-14/REPORT.md); the analysis script currently reads them at their existing `/private/tmp` and report paths. Private raw recordings remain backed up outside Git. `verify.py` passed and checks the observational claims, replay agreement, zero pinion/yaw difference at 15 mph, residual after fixed-delay probes, speed-isolation arithmetic and unchanged 1.20/0.97 constants. It does not test new vehicle behavior.

Sources: actual paired local source at the pinned revisions; the 17 saved, checksum-verified rlogs; calibrated DeviceMotion, carState/carControl, recorded path commands and saved vehicle parameters. Previous yaw and pinion evaluations are linked for context: [yaw baseline investigation](../navigator-yaw-root-cause-2026-10-14/REPORT.md), [pinion evaluation](../navigator-pinion-evaluation-2026-10-14/REPORT.md). No web or OEM claims were required for this local diagnosis.
