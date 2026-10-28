<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Original steering identification: predictive value, insufficient trim separation

**The original applied-request prefix improves held-out steering-response retrodiction, but this model cannot supply a validated moving-reference null/responsive provider for a ≤5% trim.** Its empirical error envelopes are wider than its predicted trim effect. No G/delay is certified, no controller is changed, and no new physical response to a proposed trim is claimed.

## Original dataset and strict sensor recovery

Targeted extraction covers **100 unique original segments / ten sessions**: the nine newly saved captures (79 segments), plus the previously extracted coordinated-coast session05 (21). The latter supplies independent 35–50 mph calibration coverage absent in the short low-speed new04 session. Training uses new01–04, calibration uses prior coordinated-coast05, and new05/06 plus installed08 are whole-session tests. New07/09 have no eligible moving assisted examples; they are not scored as stationary successes. Old training/calibration use parent df788e027; installed08 records e05e42f43. Vehicle is unchanged; source control tuning differs and is disclosed.

The response is **original receive-CAN0x7e StePinComp_An_Est**, an ECU compensated pinion-angle estimate with 0.1-degree DBC resolution, not independent physical steering truth. The targeted raw extraction retains its host receive-event clock and quality flag; QF must equal3. Decoder angle/QF fields are checked against the installed DBC parser. It recovers 535,962 distinct-time raw sensor frames and original CS envelope/vehicleSensorsInvalid flags, without parsing the full737-segment corpus.

Inputs are the original published sendcan0x3d6 path-angle/mode and original atomic producer target. Sendcan publication is an applied-command **request**, not proof of ECU receipt. Known active-mode rejection neighborhoods are censored; controlsAllowed alone is not treated as acceptance. The atomic target equals valid navigatorCalibration.targetAngleDeg and precedes final Ford clipping/roll/trim mapping. It is not an identified physical feedforward gain.

Qualification requires original mode1/active-valid CC/valid atomic target, drive gear, fresh state/control/target/Panda and raw angle sources, QF3/CS sensor validity/no faults, healthy CAN/Panda, and no steer pressure/raw torque over the installed allowance, pedals or turn signal in preceding1s. Response windows and initial history remain continuously qualified. The declared planned maneuver in08 is excluded ±10s. No body-yaw-derived wheel curvature is used as a label.

For the representative 0.6s/20ms retrodiction, training35–40/40–45/45–50 support is **216 / 157 / 336 anchors**; nearly all comes from one session(new02), with only59 additional45–50 anchors from new01. Calibration has **62 / 341 / 742**, held-out08 **86 / 296 / 396**. These are overlapping 100ms forecast/retrodiction anchors, not independent maneuvers. New05/06 test only lower-speed exposure. Midrange transport therefore depends heavily on one training session and one calibration session.

## What was fit, and what was not

The transparent regularized response model predicts angle change from initial raw angle/rate/earlier rate/speed, original nominal-target/speed prefix, and optionally the **actual original CAN path prefix**. Path, path/v and path×v are empirical speed bases; no degrees/radian plant gain is assumed and no wheel/body ratio sets G. Train-only scaling/imputation, calibration-only ridge selection/residual envelopes and training-session jackknife are retained in inspectable parameter files.

Two timing questions are separate:

- **Ordinary forecast:** only information before forecast origin minus source margin predicts future angle. It does not know future commands or speed. Moving35–50 held-out08 at0.6s/20ms improves state+target RMSE2.467→2.007deg when past CAN history is added, still with a3.050deg calibration q90 error.
- **Association-time retrodiction:** at label time t, initial angle/rate come from t−H and earlier; the entire known original command/target/speed prefix through t−20ms or t−50ms is legitimate. No angle after the window start is used in this response-kernel model. Commands that were future at trial start are past at association; this is not a future-prefix oracle relative to inference time.

A separate recent-angle/rate baseline uses angle already observed during the response. It predicts current angle much better (about0.16deg error in the moving35–50 0.6s/20ms subset) but has already absorbed the response to the action. It cannot be relabelled an untrimmed/null counterfactual or used to cancel the trim's response in the association test.

## Held-out moving-reference result

Moving-target means the original atomic-target prefix changes faster than1degree/s, a known-input definition. Held-out08,35–50mph:

|Window s|Source margin ms|Anchors|State + nominal target RMSE°|With actual CAN prefix RMSE°|Calibration q90 error°|≤5% probe effect median / p90°|
|---:|---:|---:|---:|---:|---:|---:|
|0.3|20|428|1.391|1.050|1.617|0.384 / 0.465|
|0.3|50|442|1.379|0.970|1.538|0.647 / 0.787|
|0.6|20|335|1.878|1.014|1.688|0.900 / 1.094|
|0.6|50|348|1.870|1.019|1.711|0.869 / 1.069|

At0.6s/20ms, the335 anchors form five qualified continuous-control islands and13 ten-second blocks. The paired block95% interval for added-command minus baseline MSE is approximately **[−3.29,−1.49]deg²**. Actual prefix information has predictive value. This is conditional on one held-out session, not a cross-vehicle or causal confidence interval.

The moving-subset calibration envelope uses380 anchors/eight qualified islands in one calibration session; held-out coverage is about90.4%. Some other speed/direction subsets have limited calibration support. These are empirical observed-input residual bands, not hard sensor/plant bounds or calibrated coverage for a hypothetical new input.

## Bounded trim sensitivity and dual-prefix failure

The offline probe reduces the recorded prefix toward zero by at most5%, quantized to realizable0.0005rad steps, retaining the initial/pre-action point, initial state and original nominal target. It is a sensitivity exercise—not a packet sent to the vehicle, a generated command treated as observed plant input, or observed trim truth. Forecast-only examples do not invent future probe commands.

For moving35–50 at0.6s/20ms,302/335 probes change at least one command quantum. All four leave-training-session-out models agree on the nonzero probe effect direction in these302 cases. That stability does **not** validate a causal G. The predicted effect is about0.900deg median and1.094deg p90, while the empirical q90 angle error is1.688deg. At0.3s the typical effect is only0.384deg against1.617deg error. At0.1s typical predicted effects are below the0.1deg sensor quantum.

**No held-out08 35–50 or50–70mph probe exceeds even one corresponding empirical q90 half-width. Across all eligible08 speeds, zero equal-width null/corrected q90 bands become nonoverlapping.** At lower speeds,109/79 pooled-band probes at0.6s with20/50ms margins exceed one half-width, but none clears the two-band separation requirement. This remains true at20ms and50ms margins and all tested window sizes. Assigning the same observed-data band to both hypothetical prefixes is only an illustrative exercise: a joint counterfactual envelope has not been validated. A better shared-error/conditional model might narrow it; this result is not a theorem that all models or all retained data are incapable of doing so.

The last command coordinate alone would falsely look well supported. A full21-dimensional prefix-innovation check conditions actual command features on initial state/target. In the moving35–50 0.6s/20ms subset, about94.6% of actual prefixes and86.6% of probed prefixes lie within its training empirical q99 score; only290/335 pairs are jointly inside. This heuristic is not a domain/safety certificate, and proposed-prefix uncertainty outside it may be larger. Closed-loop command/state/target collinearity remains: the original controller's commands already react to intermediate angle, although those intermediate angles are not response-model features.

## Timing evidence and remaining source-age limit

For89,245 available active CS publications in08, the latest raw receive-CAN frame precedes publication by median3.59ms, p9914.27ms and maximum21.05ms. The latest frame differs from published CS angle by more than half an LSB in672 cases. A valid value match exists within the preceding100ms for every such publication, but69,066 publications(77.4%) have multiple matching frames; repeated values cannot identify which one the hidden consumer used. The most recent matching frame's maximum observed age is23.65ms.

The100ms search limit is **not** an upper bound on actual measurement/consumer latency, and CAN receive time is not the internal ECU measurement clock. The targeted extraction supplies real QF/time/value events; it does not certify the original CS's exact consumed packet or internal sensor delay. The20/50ms source margins are explicit host-clock modeling assumptions, not an identified actuator delay or a manufacturer timing bound.

## Consequence for the moving-reference blocker

This is a useful original-data response assessment: known past actual commands improve angle retrodiction beyond initial state and nominal target, and raw QF/time observations are now recoverable. It does not yet discriminate a small responsive trim from a moving null with validated envelopes. The delayed-feedback contract should continue to wait/expire when no validated dual-prefix provider is available. No fitted G, source margin, gain/delay or covariance from this study is installed or consumed by the controller.

The missing evidence scope is a validated **two-prefix response envelope** under the relevant source/age/35–50mph domain, with errors narrow enough for the bounded trim, and with trustworthy actual-command and sensor-source timing. Existing original maneuver/command-innovation records may help if their ownership, QF and independent excitation can be demonstrated; this assessment is not exhaustive of all737 originals or all possible identification models. A future local model must retain pre-action state, known nominal and actual prefixes, whole-session uncertainty, conditional full-prefix support and explicit correlated/model-error behavior. It must not adapt its null using an angle that already contains the trial response.

If the retained data cannot establish that support, controlled excitation would require a separate validated and explicitly authorized plan. No new test commands, driving maneuver, device connection or calibration are requested or authorized here. Raw compensated angle/QF is still not independent physical ground truth; body-yaw-derived wheel ratios cannot fill the missing actuator evidence.

## Artifacts and preservation

[Source/sensor extraction](../../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Prior source sensor receipt](../../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Strict cases](../../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Models](../../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Per-session/subset scores](../../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Full-prefix support](../../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Dual-band exercise](../../../navigator-reference/PRIVATE_ARTIFACTS.md) · [CAN/CS timing audit](../../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Support counts](../../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Verification](PUBLIC_VERIFICATION.json).

Only this steering-identification directory and its task-specific private caches were written. Earlier longitudinal/controller receipts and the other steering worker's files are untouched. Paired source remains clean at e05e42f43/5097b993;1.20/.97 unchanged. No controller change, network/device interaction, CAN transmission, integration, commit, push or fresh full/native controller replay occurred.
