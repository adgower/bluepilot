<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator calibration-first implementation and speed audit

October16,2026. Approved design implemented locally, using all335 retained segments/19 sessions. No Comma changes, controller integration, firmware changes or new steering gain map.

## Result

The offline estimator is implemented and tested. It fits gain, yaw bias and response dynamics separately from actually transmitted steering commands, checks whole held-out drives, and abstains where evidence is inadequate. **The physical15mph steering problem is not fixed by this deliverable.** No new low-speed command map clears the validation requirements, so none was added to the paired release.

Your1.20/.97 source factors, native fixed pinion safety interpretation, and existing higher-speed controller remain unchanged. The implementation is a reusable local analysis tool, not onboard automatic calibration. [Run it](README.md), inspect the [code](estimator.py), or review the [verification](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Higher-speed findings

Speed bands are center±2.5mph. The table uses recordings on release9da98d0c9, separately from older-source training data. Eligibility requires valid/fresh aligned control/state/body motion/model/parameters/Panda, active lateral control and mode1, Drive, no brake/override/recent steering input/fault/lane change/blinker. Meaningful bends require absolute requested curvature above0.001/m. Counts are20Hz sample exposure, not independent trials.

| Focus band | Eligible active exposure on release9da | Meaningful bend exposure | Median body/request response | Interpretation |
| --- | ---: | ---: | ---: | --- |
| 55mph:52.5–57.5 | 166.45s | 18.95s | 112.2% | Response tends above request in this subset; no broad gain increase supported |
| 65mph:62.5–67.5 | 1,062.10s | 96.15s | 110.1% | Both turn directions present; no sustained below70% response window in this band |
| 75mph:72.5–77.5 | 15.40s | 0 | Not estimable | Only72.5–about74mph captured in the band; no meaningful bend exposure |
| 85mph:82.5–87.5 | 0 | 0 | Not estimable | No recordings in this speed range |

Maximum recorded raw speed is74.005mph. The75mph band must not be represented as a completed75mph road test, and nothing here establishes85mph performance.

The10th–90th sample response percentiles are101.2–128.8% at55mph and91.2–129.6% at65mph. Median absolute lateral-acceleration discrepancies are0.154 and0.135m/s²;95th percentiles0.323 and0.410. Diagnostic stationary-debiased OEM CAN yaw gives median request ratios113.2% and110.7%, broadly corroborating the body-motion result. These ratios include delay, road/banking, request evolution and calibration effects; they are neither lane-position error nor proof of persistent oversteer. They do not justify inverting the medians into a speed gain.

[Private/local visualization omitted](../../navigator-reference/PRIVATE_ARTIFACTS.md)

### The brief high-response window near65mph

At about11:02:32CDT in newest-drive-01, speed64.6mph, a0.55s clean window has body/request ratio138.9%. Requested turning falls approximately19.8% across it. The same earlier requests compared with body response0.25s later give122.9%;0.5s later gives102.6%. This supports a timing/request-withdrawal contribution and does not establish a steady gain error or an exact0.5s actuator delay. It is a post-hoc physical observation, not a new control policy. No sustained below70% response episode lasting at least0.5s was found in the eligible55/65focus bands. [Window detail](../../navigator-reference/PRIVATE_ARTIFACTS.md), [all scanned windows](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## What was implemented

The fitted first-order model has positive gainG, steady yaw biasB, delayd and time constantτ. Actual path angleu is its input; body yaw is its output. The discrete update is equivalent to a stable first-order response toward `G*u(t-d)+B`. Each episode uses its initial measured yaw as a rollout state, then predicts freely; it does not feed subsequent measured output back as a regressor. The first1.25s are excluded from scoring. Gain and bias are solved separately, with robust residual weighting, over a delay/time-constant grid plus a local refinement. Near-best profile ranges retain losses within `best + max(10% of best,0.00005 rad/s)`. Validation gates include normalized held-out error0.25, absolute residual/input-reference correlation0.35, held-out gain shift25%, and relative route-bootstrap gain width30%; these were established and tested before the final data run. They are estimator acceptance rules, not vehicle safety limits.

Why actual transmitted commands matter: planner curvature is a desired outcome and may be clipped, filtered or corrected before transmission. Fitting request as though it were the actuator input would mix existing tuning with vehicle response. Planner-derived requested yaw remains a diagnostic/reference and residual-dependence check.

The implementation explicitly separates:

- **Predictive support:** held-out prediction error, gain shift, residual/input-reference dependence and per-drive consistency.
- **Steady gain support across modeled dynamics:** whether gain remains reasonably stable across the near-best dynamics and route bootstrap.
- **Dynamics identification:** whether delay/time-constant sensitivity ranges are sufficiently narrow. Predictive accuracy alone does not identify those parameters.
- **Causality/controller validation:** neither is established from these observational closed-loop logs. There is no automatic application path, and every controller-map recommendation remains null.

Episode selection uses contiguous4–12s data,20Hz cadence, at most3mph speed spread, and minimum command variation. Source/version labels stay attached. The newest four sessions are held out in full; older sessions train the models. Additional historical low-speed cross-validation leaves out whole routes rather than random adjacent frames. Inputs/outputs from the same route never appear on both sides of a fold.

## Calibration results and abstentions

| Band | Training/held-out episodes | Finding |
| --- | ---: | --- |
| 13–17mph | 10/0 | Older data provide candidates, but latest routes have no uninterrupted qualifying4s episodes; historical coverage has only3 qualifying routes |
| 17–20mph | 16/0 | Historical route-held-out fits fail or lack support; no latest qualifying episode |
| 20–25mph | 15/0 | Historical folds inconsistent; no validated current low-speed map |
| 55focus | 6/8 | Gain varies across training routes, held-out residuals depend on input/reference, and per-drive checks fail |
| 65focus | 45/47 | Pooled prediction is fairly close, but one drive has too little turning variation for the per-route normalized-error gate; delay remains ambiguous |
| 75focus | 0/2 | Too few independent routes/episodes, with no training support |
| 85focus | 0/0 | No data |

The broader60–70mph model passes held-out predictive checks, including each of its three latest moving drives, but delay/time-constant identification remains ambiguous. Its exploratory yaw-rate gain is0.823/s, conditional gain interval0.793–0.857/s; this is a transfer-model coefficient, not an input multiplier recommendation.

For the narrower65focus band, exploratory gain is0.804/s and held-out gain0.816/s. Conditional gain interval is approximately0.780–0.881/s. Best-fit delay0.15s and time constant0.10s are **not identified settings**: near-equivalent fits span delay0–0.4s and time constant0.05–0.6s. One held-out drive's normalized prediction error is0.283, above the predefined0.25 gate, although absolute yaw error is modest. The estimator therefore withholds precise calibration. This is a model-support limitation, not a steering fault alert.

The55focus estimate is less stable; the conditional gain interval extends roughly0.806–1.387/s, and strong residual dependence remains in a held-out turn. A single highway gain number would conceal that discrepancy. These checks are intentionally capable of rejecting an estimate even when a pooled chart looks plausible.

[Private/local visualization omitted](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Why this does not yet produce a15mph fix

Earlier work established real low-speed deficits and identified fixed pinion versus calibrated-body interpretation differences. This implementation does not erase those observations. It finds that the latest relevant turns do not meet the duration/excitation conditions needed to identify a replacement steady map and distinguish delay from gain. Older low-speed episodes also do not consistently generalize across held-out routes. Taking an inverse response percentage and installing it as a multiplier would skip the central calibration-first requirement.

The design's controller-change step was conditional on a justified exact bounded map. That condition is not met. No additional steering prototype was integrated, no firmware limits were widened, and no claim of improved road handling is made. Existing≥25mph behavior is preserved by leaving the controller source untouched. No new controller/native build or safety replay was necessary for this pure offline implementation; the earlier335segment native replay belongs to the preceding feedback prototype and is not claimed as a new calibration result.

## Validation and review

- 31 tests pass: known gain/bias/delay recovery; separate bias fitting; closed-loop synthetic references without causal claims; rank/one-direction/sparse support; stale/future/gapped data; route leakage; held-out gain shift; correlated observations; conditional-uncertainty consistency; source-cache integrity; and discrepancy-window handling.
- A synthetic regression demonstrates that opposite held-out-route errors can cancel into a pooled pass. Per-route error/dependence gates now prevent that failure.
- A second regression caught a robust-point/unweighted-bootstrap mismatch. Bootstrap estimates now use the same robust estimator as the point fit.
- All335 raw input hashes match the prior verified inventory. All19 signals were freshly regenerated after the cache-provenance review finding, then bound to ordered raw hashes, extraction code/schema dependencies, anonymous route identity and payload digest. Normalization rechecks those bindings. Staging accepts only exact expected raw links.
- An independent reviewer confirmed the core tests, identified the cache-provenance gap, and re-reviewed its repair plus per-route validation/staging guards with no remaining material findings. The reviewed core suite has28 tests; the additional3 tracking-window tests make31 total. [Review record](REVIEW.md).
- Final pipeline status and verification are saved separately from this prose. [Run journal](../../navigator-reference/PRIVATE_ARTIFACTS.md), [verification](../../navigator-reference/PRIVATE_ARTIFACTS.md).

### Practical limits

This is an observational, finite model. It does not prove a causal actuator transfer function, capture every nonlinear EPS constraint, or establish lane stability. Gain/bias bootstrap intervals condition on selected dynamics and finite route blocks; they exclude dynamics-selection and unmodeled-system uncertainty. Delay/time-constant profile bounds are sensitivity ranges at a stated loss tolerance, **not confidence intervals**. Body-motion validity/uncertainty is not laboratory ground truth. The independent CAN cross-check removes a stationary baseline for diagnosis only; no Ford DBC, raw-yaw setting or safety conversion changes.

Alignment uses physical measurement timestamps in offline logs. It is not evidence that an online controller received each body observation by the corresponding timestamp; online integration would need arrival-time freshness validation separately. The corpus contains no85mph coverage. Raw logs and private signal caches contain location/device data; public normalized arrays exclude those fields.

## Durable evidence and unchanged source

All335 recordings, totaling2,788,299,892 logical bytes, were verified into `${USER_HOME}/CommaBackups/<private timestamp identifier>-calibration-first` using335 APFS clones, with independent file contents and no full raw-data duplication. Private bound signal caches are retained there. The code, reports and normalized outputs are also preserved with that backup. [Corpus backup receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md), [input hashes](../../navigator-reference/PRIVATE_ARTIFACTS.md), [cache bindings](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Paired dependencies remain clean at parent9da98d0c91f0559efa976e3ffb221f2584fd0b88 and child18175406d0cc5af8233afde70a5d121aedf8de44; source factors remain1.20/.97. No SSH was needed for this implementation. No Comma source/settings writes, restarts, ECU queries, firmware actions, Git switches/resets, pushes or installations occurred.
