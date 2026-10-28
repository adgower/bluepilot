<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Remaining pulsing and midrange tracking — October 27, 2026

**The local investigation and replay are complete, but no prototype is selected for integration.** The bounded longitudinal and body-led steering experiments do not change the problem recordings. A separate angle-led steering experiment acts on the error but fails quantized/delayed-feedback stress tests. The Comma was not accessed or changed. Paired branches remain clean at openpilot `e05e42f43` / opendbc `5097b993`; owner1.20/0.97 remains unchanged.

## Longitudinal: identify the release/reentry boundary

The full recorded moving-drive observations remain14/14/12 brake-request changes in the highlighted53/40–50/58mph windows. Current-source coupled reconstruction gives14/15/12; it is not an exact recording reproduction. The normal selector has0/+0.3m/s² hysteresis, but qualified release can withdraw braking after raw and grade-adjusted demand exceed+0.02 for60ms. Small subsequent negative changes can re-enter braking before measured clearance. This explains a software mechanism consistent with the cycling, without identifying the Ford ECU's internal grade or pressure behavior.

The pending-pressure prototype retains the same signed0.01/0.3-second allowance, measured-clearance requirements, original timeout, strong/stop/FCW bypass and propulsion exclusion. It never opens another account or clears accumulated obligation. Of1,614 positive-raw/positive-target weak full-brake rows in the newest40–70mph drive,1,600 already have a locked account. The remaining14 are not freely eligible entries. The extension has **zero activations and zero command changes** across the entire corpus, so passing compatibility checks does not make it a useful smoothing treatment.

Full coupled comparison covers**316 unique segments / 23 routes**, **903,645 consumer callbacks** and1,725,152 producer steps.304segments have complete active atomic inputs;12historical segments remain explicitly diagnostic. Brake-bit changes remain2,463→2,463 and brake exposure4,519.896→4,519.896s. Consumed raw/I/gas/fault/activity and complete wire streams are unchanged; the comparison does not independently prove equality at every unconsumed producer step. The two historical release-timeout histories remain unchanged.

Fresh native replay covers**903,463 ACC replacement slots** with205existing rejections per variant, zero added rejections, zero relay faults and no forced permission.11focused checks and1,033Ford tests/75subtests pass with unsanitized hooks. Initial macOS UBSan loading failures and the separate zero-active startup-recording resume are retained and disclosed; the full result is not mislabelled a single uninterrupted exit-zero execution.

[Longitudinal report](../navigator-remaining-pulsing-prototype-2026-10-27/REPORT.md) · [Local prototype](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Verification](../navigator-remaining-pulsing-prototype-2026-10-27/PUBLIC_VERIFICATION.json)

## Lateral: a coverage gap, with insufficient independent confidence

The40–45mph result remains25.25s of selected steady turning at median body/request1.1472 and wheel/request1.1526. Calibrated target computation is consistent: median target mismatch about−0.00046degrees. Extending roll mapping alone accounts for roughly1.7% median target difference, rather than explaining the entire response excess. Existing earned midrange admission often activates, but controls a small roll-map adjustment; it supplies no independent sustained-error trim in this band.

The local prototype adds a bounded, earned trim with unchanged owner factors, coherent wheel/body history, current calibration/target provenance and an additional2×reported yaw-uncertainty guard. That new guard is a conservative engineering choice, not a factory threshold, Gaussian confidence guarantee, or proof the error is noise. None of the505steady40–45mph observations clears even its current-sample2×threshold. Median yaw error is0.01148rad/s versus reported standard deviation0.01314rad/s. Consequently the prototype leaves **all116,072 newest-drive controller updates unchanged**. It does not correct this drive's apparent excess.

Wheel/body agreement is not fully independent calibration proof: paramsd learns ratio/stiffness/offset/roll using the same calibrated deviceMotion yaw and roll estimates used by this comparison.25.25s comprises three steady clusters, dominated by one turn; it is not25independent seconds of calibrated evidence. Better uncertainty interpretation and independent calibration evidence are needed before using a response ratio as a gain correction.

The driver-confirmed49mph movement into the newly added rightmost lane for the upcoming exit remains excluded as problem-takeover evidence, with±6/±10s exclusion sensitivities retained. No new-source70–85mph coverage is invented.

Full fresh steering/controller/native replay covers**737unique segments /42routes /4,244,330 controller updates**. Across the whole corpus, recorded-context changed updates=0; separately labelled causal-calibration-fixture changed updates=0. These are distinct comparisons, not additive road exposure. Default-off equality and zero added native rejections are verified per route.165synthetic checks pass. Abrupt synthetic speed jumps after earned trim require bounded inherited unwind rather than impossible immediate parity; max residual0.005904rad, at most0.60s in the42→85mph jump fixture. Actual full-corpus per-band outcomes, inherited-policy counters versus new-feedback activations, initial overstrict test failures and source provenance are disclosed in the domain report.

[Lateral report](../navigator-remaining-tracking-prototype-2026-10-27/REPORT.md) · [Local prototype](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Full summary](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Angle-led alternatives: useful activity, failed stability gate

A separate wheel-angle-led prototype retains earned coherent admission, atomic target/calibration guards, the owner factors and bounded correction limits, using body response as a shortfall veto rather than requiring a positive2×body residual. It does not assert independent physical-gain identification or introduce unlogged parameter covariance.

Its fresh21-segment newest-drive controller/native comparison produces177 command reductions and zero increases per recorded/fixture stream, with zero added native rejections. With the planned exit interval excluded,144reductions occur among422qualified40–45mph steady angle slots; the other33changes are separately retained. These are command changes, not measured improved steering. However, hypothetical lag/quantization stress cases expose persistent one-wire-increment cycling, so this version is rejected.

A correction-only hold was then tested. Diagnosis showed a0.1degree measured step becoming0.25degree variation after prediction, defeating the original hold. Anchoring update hysteresis to measured amplitude clears that original case without widening its threshold, but the complete32-case sweep exposes a different delayed/quantized case:0.0015rad peak-to-peak output,57transitions in the20-second tail.227unit tests pass, yet the dynamic quality gate fails. These are invented scalar stress fixtures, not a validated Navigator plant; their counterexamples still demonstrate an unresolved algorithm problem.

**No full corpus replay is claimed for either rejected angle-led version.** The first has the focused21-segment comparison; the hold revision has unit/stress evidence only and was stopped before a focused/full drive run. Full737-segment results above belong to the unchanged body-led candidate. No candidate was selected by silently relaxing confidence, gains, clearance, timeout or stability gates.

[Angle-led experiment and retained failures](../navigator-remaining-tracking-prototype-2026-10-27/REPORT.md) · [Final failed quality gate](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Next local work

1. For pulsing, build on the [existing OEM/Alpha response investigation](../navigator-gear-grade-coast-2026-10-25/REPORT.md), not another gear table or the rejected valid-propulsion bridge. The missing capability is validated dynamic mode/authority transitions with integral recovery and explicitly unsupported Alpha inactive-propulsion/no-brake regimes. Validate the response-state model against observed brake/precharge/propulsion status and torque transitions, holding out entire episodes by gear and grade. Record unsupported counterfactual coast responses explicitly. Use actual acceleration error and cumulative speed error alongside grade and actuator state in one revised producer/allocator contract; retain necessary braking and independent measured clearance. Reopening the existing account simply to obtain fewer edges is not a demonstrated fix.
2. For tracking, design explicit feedback state for delayed, quantized angle response, retaining calibration uncertainty, target-change release, driver aborts and bounded output. The angle-led hypothesis remains viable in principle, but proportional trim plus amplitude hold is not a demonstrated stable implementation. Resolve that quality gate before another full candidate replay; preserve1.20/0.97 and high-speed behavior. Do not turn a shared-input response ratio into a gain cut.

No paired-source integration, branch publication, device staging, service restart, setting write, ECU query or CAN transmission occurred. Full saved-input/native checks establish software behavior and compatibility only; they do not establish closed-loop physical comfort, tracking, braking, fuel efficiency or installation readiness.

[Independent review](REVIEW.md) · [Combined verification](PUBLIC_VERIFICATION.json) · [Work scope](PLAN.md)
