<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Frozen pre-action shared-error assessment

Status: proposed, awaiting root/peer review before fit. Read only the frozen original100-segment steering cases, source clocks, split and response models; never change earlier receipts or any controller.

## One predeclared model

Primary: existing association retrodiction H=.6s/sourceMargin=.02s. Keep its initial angle/rate state, original nominal-target/applied-command prefixes, predictions and bounded5% probe unchanged. No new response-kernel family, gain/delay fit or parameter selection on installed08.

For a trial starting at T0=t_label−H, compute the mean of original full-kernel residuals from prior case endpoints in **[T0−1.25s,T0−.25s]**. Every such residual's observed angle and model features must already be available before T0. Require≥8 endpoints, same qualified control island and no gap>150ms. This fixed one-second window ends before the existing model's initial angle/rate history (which reaches .2s before T0); it does not adapt using any post-start angle/torque/residual. Missing prehistory is unavailable, not zero bias.

Remove the part of that history mean linearly predictable from the existing PRE-ACTION initial columns (initial angle/rates/speed, first target error, first original command/speed basis). A train-only standardized ridge(λ=1, fixed nuisance projection) produces one prehistory-innovation scalar z. This prevents describing a reweighting of already-used initial state as new history information.

Fit just one bounded persistence coefficient β=clip(sum(z·e_actual)/sum(z²),0,1), on training35–50mph examples, and freeze c=βz at T0. The same c is added to both prefix predictions. No intercept, alternate history lengths, filter families or08-selected threshold. If β collapses to0 or held-out error does not narrow, retain that negative result.

Training residuals use leave-whole-training-session-out base-kernel predictions, fixed existing regularization, so the bias model is not trained on artificially small in-sample kernel errors. Calibration/test histories use the original frozen full-training kernel. Report that nuisance crossfit shift and sparse midrange training support. A conditioning-coefficient jackknife with fixed nuisance predictions is conditional uncertainty, not a complete physical-model confidence interval.

## Preserve the timing and baseline

Old equal-band negative result is immutable. Compare original kernel and conditioned kernel on EXACTLY the same prehistory-available calibration/test anchors; separately disclose loss of examples. Original01–04 train, priorcoast05 calibrates, new05/06+08 test.08 never selects β, projection, history window, residual band or likelihood threshold. Current100-segment source masks/quality and strict clock checks remain unchanged.

Counterfactual5% point contrast Δμ is unchanged by applying a common c to both prefixes. A narrow coefficient/jackknife Δμ interval cannot delete residual uncertainty about the observed angle. Measure actual observed-prefix residual RMSE, cal-onlyq90 bands, held-out coverage/tail exceedance and equal-band separation after conditioning. Do not claim that an invented trimmed prefix has a physically observed label or a calibrated counterfactual error distribution.

## Conditional likelihood and controls: precise meaning

The data retain an original **atomic-target-only predictor**, not a directly recorded untrimmed feedforward CAN prefix. Compare actual observed y under that target-only predictive alternative and under the actual-CAN-prefix predictor, with the SAME frozen c and a shared working Gaussian error scale estimated from calibration actual-prefix residuals. Report log-likelihood difference as a descriptive conditional forecast score, not a causal null-ignoring-trim posterior or a responder label. If a genuine original nominal-FF prefix becomes available, it requires separate provenance/split review before replacing this alternative.

Controls: exact identical-prefix predictions must have zero contrast/likelihood ratio; stable original-input subsets are defined from known prefix only; natural high/low command variation is not randomized responsiveness truth. Cal-only90% bands have empirical held-out exceedance rates, not a physical false-positive guarantee. No post-start recent-angle baseline may be used in conditioning.

Measure shared residual covariance between the two original predictive models, future-error correlation with the frozen prehistory scalar, and observed-angle residual variance AFTER correction. Separate those from coefficient covariance and hypothetical-prefix Δμ uncertainty. If prediction biases are shared but y remains ambiguous, say so directly.

## Hold-out tests and stop conditions

- Inspect every selected residual endpoint and every conditioning feature clock≤T0; mutate all post-start test angles/targets/commands and show c unchanged.
- Test same correction for actual/probe branches, no missing-history default, no identity-prefix discrimination, and no modification to earlier source/case/model hashes.
- Report moving-target35–50 first, with case/island/10s-block counts. Use paired10s-block error intervals within held-out08 and explicit whole-session split limitations.
- Compare cal-only likelihood/bands and paired prediction contrast on actual held-out data. No observed new-trim ground truth exists; provider remains unsupported unless genuinely demonstrated, not merely because a common-bias term or Δμ confidence interval becomes small.
- One model only. Preserve failure; no controller/runtime/full replay/network/device/CAN changes. New maneuver data are a separate cohort and cannot enter this fit without explicit provenance/split approval.
