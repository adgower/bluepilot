<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator Alpha pitch/grade and actuator feedback investigation

October 23, 2026. Saved drive only; no device contact or paired-source changes.

## Finding

The leading remaining issue is a **relative gravity/pitch calibration or compensation mismatch interacting with repeated propulsion withdrawal/resumption**. This is stronger evidence than the earlier brief-dip hypothesis, but it does **not** uniquely identify Comma's physical pitch as wrong or establish a road-ready correction.

A Ford motion signal already present in received CAN closely matches `wheel-derived acceleration + Comma pitch gravity term + approximately 0.18 m/s²` after diagnostic low-frequency filtering. The residual is similar in highway and low-speed windows; GNSS comparisons point in the same direction. A report-local **+0.18 m/s² adjustment to only the brake-decision gravity term** reduces reconstructed brake transitions **213 → 56**. This is **fewer reconstructed command transitions, not a measured 74% improvement in comfort, braking or vehicle tracking**. The unchanged recorded vehicle response is not a simulation of the adjusted controller.

Neither saved calibration nor any on-device setting was adjusted. Owner steering **1.20/0.97** and clean paired heads remain unchanged.

## Source and provenance

All 23 Alpha-drive segments from the already verified acquisition are used. Private raw/cache directory: `${PRIVATE_CACHE}`. Raw segment hashes are checked when extracting pose data. No additional download, ECU query, CAN transmission, reboot, install, source integration or commit.

Exact local pair: parent `ffebc43497f8015c37be5927800832f2719c7dca`, child `0ac9618972dd580281c5e933c7990f186522fbd4`.

- [Pose inputs/columns and hash](../../navigator-reference/PRIVATE_ARTIFACTS.md), [pose/grade diagnostics](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [ECU release/overlap observations](../../navigator-reference/PRIVATE_ARTIFACTS.md), [feedback-state review](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Ford motion cross-check](../../navigator-reference/PRIVATE_ARTIFACTS.md), [low-frequency alignment](../../navigator-reference/PRIVATE_ARTIFACTS.md), [additional-window offset check](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Full-drive diagnostic comparisons](../../navigator-reference/PRIVATE_ARTIFACTS.md), [verification](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Pitch transport and grade estimates

`controlsd.publish()` copies calibrated pose orientation into CarControl; the Ford controller computes `g·sin(pitch)` and uses it for brake/precharge admission. Reconstructing PoseCalibrator from saved deviceMotion/extrinsics gives essentially identical pitch terms for most aligned samples: p05/p95 error about ±1.6e−8 m/s². Maximum discrepancy is 0.0804 m/s² (standard deviation 0.0030), so asynchronous samples are not an unconditional exact match. There is no demonstrated sign/transport bug in this path; physical calibration correctness remains separate.

The first-order **diagonal-covariance pitch uncertainty proxy** has median gravity-equivalent magnitude about 0.080 m/s², versus the 0.020 positive-release margin. This is not measured noise or calibrated grade uncertainty: it assumes independent device orientation components and fixed extrinsics, omits correlations/calibration uncertainty, and cannot prove threshold noise crossings.

GNSS vertical velocity and centered 20-second altitude-versus-distance regression suggest Comma's slow pitch term is more negative than their grade proxies by roughly **0.15–0.17 m/s²** in eligible high-speed samples. GNSS speed/altitude uncertainty is material, particularly at low speed. No fixed correction can be justified from GNSS alone. Validity gating is applied; two invalid GNSS samples in active moving coverage are excluded. Smoothed estimates interpolate gaps before filtering, so neighboring values remain influenced by that diagnostic interpolation.

All four focused windows have zero invalid pose or GNSS observations; largest state gap is about 56 ms. Lag-correlation calculations reject missing samples rather than compressing gaps. Centered decompositions are diagnostic only, not proposed causal runtime filters.

## A second Ford motion channel strengthens the mismatch hypothesis

Decoded **66,278 received bus-0 frames** of `BrakeSnData_3` / address119, DBC signal `VehLongComp_A_Actl`. No diagnostic request was sent. Ford coverage is complete on the aligned timeline; the channel's largest raw interval is about33 ms. Its name alone does not establish physical compensation/offset semantics for this Navigator.

At low frequencies (centered 0.6 Hz low-pass), the descriptive relationship is:

`Ford channel ≈ aEgo + g·sin(Comma pitch) + offset`

| Window | Relative offset | Correlation | Centered residual RMS |
|---|---:|---:|---:|
| Highway <private clock time>–<private clock time> CDT | +0.181 m/s² | 0.962 | 0.068 m/s² |
| Low speed <private clock time>–<private clock time> CDT | +0.177 m/s² | 0.994 | 0.040 m/s² |

The highway descriptive alignment uses50 ms lag; low speed's best same-window fit uses zero lag. Even zero-lag highway correlation is0.957. These are optimized descriptive associations, not uniquely identified sensor latencies.

Thirteen additional **nonoverlapping 20-second windows from this same drive**, excluding the highway selection interval, have median window offset **+0.157 m/s²**, with p05/p95 **+0.113/+0.204**. Centered filtering spans boundaries and operating conditions are shared; this is not a strictly isolated or independent validation set. The equivalent angle for0.18 m/s² is approximately **1.05°**.

Agreement across imperfect Ford, wheel/pose and GNSS observations supports a relative calibration/compensation mismatch. It does not tell us whether Comma's reference frame, the Ford channel's zero/compensation, suspension attitude, or a combination owns that mismatch. **Do not reset calibration or hard-code a one-degree adjustment on the device.**

## Actuator response: large propulsion changes, not proof of widespread brake riding

The ECU-reported torque response follows command changes with measurable lag. Across51 selected moving releases (preceding brake bit on≥0.2s, following off≥0.5s, prior reported brake torque>24Nm), reported brake torque reaches≤4Nm for three continuous samples at median **103 ms** after the bit clears (p05/p95 81/152 ms). First positive propulsion request appears at median **55 ms**. Episodes with driver pedals/disengagement during follow-up or missing cadence are excluded. These are log-event intervals, not exact hydraulic release times.

Engine request/actual torque associations show their own lag (roughly100–150 ms from propulsion request to ECU requested torque, then around50 ms to reported actual torque in the focused bands). Correlation maxima can select periodic phases; these are not causal latency calibrations. Starting a positive request before the brake-torque channel clears does **not** establish simultaneous physical actuation, because the engine responds later too.

In the worst highway window, after150 ms in each command state:

- Brake-request state: median ECU propulsion torque **28Nm**, median reported brake torque **0Nm**, median wheel-derived acceleration **−0.138m/s²**.
- Valid-propulsion state: median propulsion torque **498Nm**, median brake torque **0Nm**, median acceleration **+0.257m/s²**.

At low speed, corresponding propulsion medians are **−216Nm vs +406Nm**, with brake torque **56Nm vs0Nm**. Different instantaneous demands/grades remain confounders; this is a descriptive contrast, not a causal force decomposition.

Reported overlap above24Nm braking and100Nm propulsion occupies only **0.25%** of the worst highway window and **2.25%** of the low-speed window. Those thresholds/whole-window denominators are explicit. This does not prove continuous heavy brake/throttle conflict, brake pressure, opposing wheel forces, or fuel waste. The installed software already removed concurrent active brake/valid-propulsion requests; the remaining modulation and request/response mismatch are a different issue.

The source explains the sensitivity: a brake request withdraws propulsion and resets ramp history; clear requalifies and ramps from zero at0.5m/s³. The packer also ties precharge and deceleration bits together and comments that toggling these bits can produce an initial jerk. Its comment is supporting source context, not proof of this vehicle's physical cause.

## The acceleration oscillation is corroborated beyond one counter

In the0.2–0.6Hz band, wheel-derived and IMU-derived acceleration correlate **0.973 highway /0.990 low speed**. Highway RMS is about0.193/0.191m/s², while planner-target RMS is about0.040. This supports genuine slow vehicle-motion cycling alongside command modulation. The IMU estimate is filtered/fused and shares localization inputs; it is not an independent calibrated acceleration instrument. Faster-frequency disagreement remains and should not all be labeled physical jerk.

LongControl has zero P gain and an integral acceleration-error term (FordKi0.5). The highway slow integral term is strongly associated with the opposite of slow pitch. Feedback therefore cannot be treated as a fixed open-loop gas request: changing grade arbitration will also change future integral demand. A correction replay that freezes recorded I/planner/vehicle signals does not predict the final closed loop.

## Local diagnostic experiments

All variants use the same65,736 actual ACC slots and full-rate recorded state/control chronology as the prior reconstruction. Baseline matches96.04% of recorded messages; its213 eligible brake edges differ from209 recorded. Internal receive ordering/call time/frame phase are reconstructed. Same caveats carry forward.

| Diagnostic intervention | Reconstructed edges | Worst highway20s | Low-speed20s |
|---|---:|---:|---:|
| Installed logic reconstruction | 213 | 33 | 24 |
| Causal pitch LPFτ0.5s | 159 | 19 | 12 |
| Causal pitch LPFτ2s | 151 | 19 | 10 |
| Response-aware weak-entry test | 205 | 33 | 22 |
| Decision gravity term+0.18m/s² | 56 | 2 | 2 |

The response-aware test uses fresh, past-only planner target/shouldStop/validity plus actual acceleration. Existing holds, stopping, low speed, stronger negative net and requested deceleration bypass suppression. It barely helps. Its signed tracking-error budget is not a physical speed-error guarantee; recorded planner context is selected at ACC send time and may not be the exact plan used by the original control producer. A real integration would require atomic timestamped context in CarControl.

The0.18 adjustment is a **sensitivity test derived from the relative-sensor relationship**, not an accepted calibration. It changes the brake-decision term only, not logged calibration or braking acceleration. Fewer edges can result directly from shifting the decision threshold, even if the hypothetical vehicle would behave worse. It also affects low-speed commands; no stop/grade/restart preservation claim for that variant. The smoothing variants likewise change356/358 below3m/s slots and cannot be promoted as safe local fixes.

Across these frozen-input comparisons, braking-acceleration values and reconstructed non-ACC hashes remain equal, no inactive/stopping slots change, and zero active brake+valid-propulsion overlaps occur. These limited properties are not physical stopping/grade validation. Eight new response-gate contracts pass; initial behavior and fallback failures were observed and retained before corrections. **No new full native replay, paired build, ARM or hardware acceptance is claimed for these diagnostic interventions.** Earlier886-test/ACC-hook receipts belong to the prior bounded-admission prototype, not these variants.

## Resolution path justified by this investigation

The next implementation should be **calibration-first and feedback-aware**, rather than a larger deadband or arbitrary PID gain change:

1. Establish a timestamped, validity-gated relative gravity/acceleration calibration using the already broadcast Ford motion, wheel and pose signals. Treat the estimated offset as a hypothesis with confidence/limits, not a permanent learned constant from this single Alpha drive. Cross-check across independent routes/OEM operation and grade changes before enabling compensation.
2. Apply any accepted estimate smoothly and consistently with upstream integral demand; prevent a sudden propulsion increase from the existing integral offset. Retain original learned steering/calibration and make the experiment default-off/reversible.
3. Add explicit fresh actuator-state observation from already recorded/broadcast brake and propulsion torque. Distinguish requested brake mode from observed torque response. A larger fixed release delay alone would worsen propulsion interruption; a blind ramp restart or blind reuse of old gas is not justified either.
4. Validate a coherent propulsion/coast/brake allocation and resumption policy against calibration uncertainty, genuine deceleration, new/existing grade holds, stop/restart, stale/future data, overrides and the original historical conflict. Recorded-input command checks must be complemented by a justified response model/closed-loop evidence before another physical trial.

This turn narrows the mechanism substantially and provides runnable local experiments. **The cycling is not yet physically resolved and there is no installation candidate.** No additional Alpha drive is requested; OEM ACC remains the recommendation for ordinary driving while this work continues.
