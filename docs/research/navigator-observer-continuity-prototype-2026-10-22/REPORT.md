<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
> **Final broader validation completed:** [71-route / 1,015-segment report](../navigator-observer-continuity-validation-2026-10-22/REPORT.md). Current prototype.py passed 71 focused tests and the corrected broader replay. The initial low-admission design/results below are historical; new low actuation was withdrawn.

> **Superseded during broader validation.** This report describes the initial candidate, preserved as [prototype-initial-continuity.txt](../../navigator-reference/PRIVATE_ARTIFACTS.md) and [test-initial-continuity.txt](../../navigator-reference/PRIVATE_ARTIFACTS.md). Broader replay exposed speed-boundary/history effects. The current prototype.py is an independent highway overlay over untouched installed policy; low-speed observation remains, but new low-speed actuation was withdrawn. See the [validation execution record](../navigator-observer-continuity-validation-2026-10-22/EXECUTION.md) for current status. Initial48segment/67test results are not validation of the revised source.

# Observer continuity prototype — October 22, 2026

**Local prototype completed and tested. Not integrated, pushed, built for the device or installed.** Comma never accessed in this task. Paired source remains26b3416a6/fe59e503, clean; owner1.20/0.97 unchanged. This is a command-space candidate, not proof of improved vehicle response.

## Result

The highway observer can now retain valid source-ordered wheel history across temporary body-excess-margin crossings. Applying trim still requires current sustained body confirmation, current wheel excess, predictive closing checks and existing provenance/driver/fault guards. The existing release envelope withdraws trim on failed current evidence; history continuity is not permission to hold through a fault or stale data.

The low-speed observer now validates the original requested curvature and atomic wheel target independently from the feasible clipped command. Earlier bounded admission can use that already-fresh history. It retains the existing shared exposure budget, brief episode duration and command headroom restrictions. **It does not bypass saturation. Neither saved severe23–24mph shortfall window changes.**

The prototype therefore answers the design question positively for earlier highway admission and original-target observation, but does not establish a low-speed steering fix or physical reduction in highway excess/ping-pong.

## Evidence

### Tests

- Initial current-policy alias run:5failures/23passes, covering missing earlier highway admission and original low-target observation.
- Additional low-admission tests failed for both turn directions before the continuity change.
- Final67focused tests pass:70–79mph admission, original low target under clipping, bounded low early effort, current-evidence guards, predictive trim bounds, driver/fault/stale/lane/target invalidation, reversals, default-off parity, static protected ranges and gradual speed transitions. These are synthetic source tests, not hardware or road proof.

### Native controller replay:48segments, two complete target drives

Production CarController generates TX from recorded RX and original control packets, and separately from clearly labeled causal calibration fixtures. Four independent native safety instances derive permission from recorded RX; controls permission is never forced. Default-off streams remain byte-identical to their installed reference. Existing native debug library reused, without a new sanitizer build or device firmware action.

|Drive|Segments|Controller updates per variant|Recorded candidate changed updates|New native rejections|
|---|---:|---:|---:|---:|
|session10|23|139,885|18|0|
|session11|25|137,180|92|0|

Total277,065updates per variant. Candidate and reference each have the same two0x83rejections in session11 at an inactive/driver transition with controlsAllowed=false. These are not active steering-command rejections; session10 has none. No additional rejection introduced by the prototype. Recorded and separately stamped fixture variants agree on changed-update counts.

Both drives show zero changed updates outside the intended22–25mph/70–80mph bands, including zero40–50mph changes. In this controller-scheduled replay there are no changed low-speed commands;110changed updates are highway commands. No broad878-segment or newer full-corpus replay, full build, fresh ARM validation, or deployment is claimed.

The first native runs completed computation but failed the final source-snapshot gate because the test file was expanded while they ran. Their logs/results are retained as `*-initial` / `*-source-gate.log`. Both complete routes were rerun with source/tests frozen: exit0, provenance gates passed, and results/stream hashes exactly match the initial runs. The failed runs are not counted as successful validation.

### Original send-time replay

This separate strategy replay uses original atomic packets, actual send timestamps and recorded motion/model/state context. Its invocation cadence differs from the full controller replay above, so its counts must not be mixed with controller-scheduled counts.

|Drive|Send-time commands|Changed packed commands|Max packed path-angle difference|
|---|---:|---:|---:|
|session10|27,422|43, all70–75mph|0.0015rad|
|session11|28,948|130:9at70–75,117at75–80,4at23–24|0.0025rad|

In the focused79mph bend,122of284send frames change. These are command differences, not a predicted tracking improvement percentage. All four low-speed changes occur at23.44–23.87mph around session11 relative393.81–394.56s, outside the severe shortfall windows. Their timing sensitivity—absent in controller-scheduled replay—is a remaining integration-validation issue.

The two severe session10 low-speed windows, relative478–484s and509–513s, remain byte-identical after packing. The new original-intent observer is valid on116of183active/unpressed sampled frames across those windows and explicitly identifies55headroom-limited frames; remaining invalid samples mainly fail target magnitude/direction checks. No claim that every invalid inherited feedback sample is repaired or that these183frames equal the91clean meaningful frames from the earlier diagnosis.

Original send-time command comparison can be rerun with `python send-time-harness.txt <label>` then `python summarize-send-times.txt` using the documented integration virtual environment. These files contain the exact executable harness text; raw logs remain in the private acquisition folder referenced by the prior drive report.

## Corrected selector attribution

A test initially showed no output change at76/79mph despite updating the nearby upper observer. The final selector above75mph actually passes through `unchanged.stock.upper_reference`, one level deeper than the prior diagnostic trace attributed. The candidate now modifies that selected predecessor as well. Earlier adjacent-policy reason-frequency claims were withdrawn in the diagnosis report; actual command and physical-response measurements remain separate. This is why testing final packed output matters.

## Limits and next gates

- 1.20/0.97, geometry, application deviation/range/slew limits, native safety source and exposure caps remain unchanged. No additional cumulative low-speed allowance or persistent integral is introduced. High additional admission fades in70–71mph and out79–80mph; low additional admission fades in22–23 and out24–25mph.
- The severe low-speed request remains infeasible under the unchanged current-command envelope. Observation continuity alone cannot produce the missing steering authority. Further work must separate earlier feasible entry from fully clipped demand, rather than silently widening the clamp or refunding spent budgets.
- The highway candidate needs a full current-corpus replay, additional gentle-curve/rapid-abort/boundary stress coverage and final timing integration review before paired integration. The67tests and48segments do not replace those release gates.
- This is frozen-input/open-loop replay. Measured physical yaw/wheel response is unchanged in the recordings; counterfactual commands cannot establish actual road benefit or damping. Meaningful80–85mph data remains absent. Synthetic85mph parity is not85mph road validation.

Artifacts: [design](DESIGN.md), [prototype](../../navigator-reference/PRIVATE_ARTIFACTS.md), [tests](../../navigator-reference/PRIVATE_ARTIFACTS.md), [guard/transition result](../../navigator-reference/PRIVATE_ARTIFACTS.md), [send-time comparison](../../navigator-reference/PRIVATE_ARTIFACTS.md), native route receipts under [replay/route-replays](../../navigator-reference/PRIVATE_ARTIFACTS.md).
