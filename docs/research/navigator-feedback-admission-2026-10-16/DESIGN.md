<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Proposed next design: separate calibration and transient tracking

Status: concrete review proposal, not implemented in the paired branches or installed. The three report-local experiments do not establish a physical low-speed fix.

## Problem and intended result

The fixed pinion proxy can differ materially from measured turning because it intentionally omits learned angle offset, steering ratio and roll. The existing correction waits for a stable deficit and has only modest extra authority. It cannot reliably compensate for a larger steady command/response discrepancy in short changing turns.

Preserve owner's1.20/.97, existing native safety interpretation and high-speed behavior. Improve the supported below25mph region only after calibration and transient dynamics have been distinguished; do not infer a universal multiplier from inverse observed ratios.

## Approaches

1. **Recommended: identify calibration first, then revise transient control.** Use existing saved raw logs to evaluate command-to-physical-response gain, bias and delay separately, with source/version labels, left/right support, uncertainty and held-out-route prediction. Produce recommendations only. Where observations cannot identify a speed band, explicitly abstain. A local tracking-feedback seam uses calibrated body motion with freshness/validity while preserving the fixed native proxy. This takes more work but gives evidence for the actual command-map change rather than another persistence tweak.
2. **Earlier small proportional correction.** The local three-frame variants already show a0.15s earlier pulse; they do not resolve the deficit, and have small additional modeled peak excess. Not selected as a fix.
3. **Replace paired fixed geometry with learned geometry everywhere.** Broad safety/protocol implications and changes beyond the target range; not recommended for this task. Raw yaw baseline also remains unresolved at the OEM boundary.

## Proposed implementation scope

- A pure offline calibration/identifiability module consumes saved controller request, actually transmitted path angle, physical yaw and validity, speed, wheel angle, learned ratio/offset/roll, and driver/engagement state. Keep GPS/device identifiers private.
- Establish pass/fail synthetic recovery tests with known delay/gain/offset before fitting. Include correlated closed-loop inputs, sparse/one-sided turns, ramps, dropouts and latency so the estimator abstains instead of assigning spurious speed gains.
- Evaluate retained historical sessions, including older low-speed logs. Validate held-out contiguous episodes/routes, not random adjacent frames; report uncertainty and insufficient coverage. Body-motion and learned-model agreement is not independent evidence, so retain diagnostic stationary-debiased OEM yaw cross-checks.
- Only if identification supports a bounded speed/demand correction, propose the exact gain/transition map and its limits. Do not write recommendations to device settings automatically. Keep additions fading out by25mph and preserve≥25mph actuation byte parity.
- For a justified controller candidate, implement the narrow change in isolated paired local source, with fresh calibrated feedback passed through the existing context seam; preserve original default-OFF behavior. Do not replace native safety feedback, widen limits, alter signed firmware or reinterpret the Ford DBC.
- Replay all cached raw physical RX plus generated TX against native safety; test sensor mismatch/delay, abort, reversal, stale context, driver override, budget and final-limiter residuals. Separate these from actual vehicle validation. A lack of relevant held-out data is a result, not permission to tune anyway.

## Acceptance and deliberate limits

The offline estimator must recover known synthetic parameters with defensible uncertainty or abstain, and must not confuse offset with a speed multiplier. Any proposed controller must pass actual emitted-command and native safety tests, retain1.20/.97 and exact higher-speed behavior, and document remaining modeled overshoot/residual. Frozen-input replay cannot show improved physical steering. Installation and new road evaluation remain separate user requests.

This design does not authorize automatic calibration, integral stall rescue, expanded firmware permissions, MADS, longitudinal changes or on-device writes. No architecture changes have been applied while this proposal is under review.
