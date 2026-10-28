<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# 50–70 mph wheel/roll/route investigation

October17,2026. Local saved-data investigation only. No Comma connection, controller changes, new gain, branch integration or installation. Existing1.20/0.97 remain unchanged; expected paired source9da98d0c9/18175406 and dependency hashes still verify clean.

## Outcome

The strongest supported next change is **a calibration- and roll-aware application command mapping**, not a blanket speed gain adjustment. The standard angle controller already creates a desired wheel-angle target using learned steering ratio, stiffness, angle offset and roll. The Ford path-angle strategy instead constructs PSCM commands from requested curvature × speed × provisional factor; it does not use that desired wheel-angle channel. Current application feedback uses fixed nominal pinion geometry, and its corrective term is disabled above25mph.

The data supports investigating this integration gap: at50–70mph, learned wheel-only prediction is about101% of request while body response is112%. Recorded roll explains much of their difference in the measurement model. This is **not** a completed steering fix, proof of causal road banking, or permission to send a steering-wheel angle as a Ford path angle.

## Measurement-model result

The unchanged eligibility/steady-request rules select3,244samples,162.2seconds, across10sessions. Both requested turn signs are represented in the pooled cohort. It remains a selected observational cohort: steady request does not ensure a settled vehicle or an independent flat-road experiment.

| Band | Body / request median | Learned wheel / request without roll | Learned wheel + roll / request |
| --- | ---: | ---: | ---: |
| 50–55 mph | 109.7% | 103.4% | 111.7% |
| 55–60 mph | 113.8% | 103.2% | 115.5% |
| 60–65 mph | 112.2% | 97.9% | 113.6% |
| 65–70 mph | 111.2% | 95.6% | 114.1% |
| Pooled50–70 | **112.1%** | **100.6%** | **113.8%** |

Using the fixed physics roll term, average absolute wheel-to-body yaw prediction error falls **0.005399→0.002848rad/s**, a **47.2% reduction**, and improves in every one of the10sessions. **47.2% refers to measurement-model prediction error, not improved steering or road performance.** No new controller was driven.

The signed mean tracking-error decomposition is exact algebra, not independent causal identification:

`body − request = (wheel_without_roll − request) + roll_effect + model_residual`

Projected along the desired turn, pooled means are approximately0.005209rad/s total excess =0.000446wheel-only excess +0.005455modeled roll contribution −0.000692residual. This suggests broad gain reduction would conflate wheel-command response with roll/model effects. The model's roll/request fraction spans roughly4.1–24.8% at the10th–90th sample percentiles, median12.9%; a single12% reduction would not account for that variation. These sample percentiles are not uncertainty intervals.

Recorded roll and learned ratio/offset/stiffness are estimates, partly identified from the same vehicle motion. Agreement with body yaw can therefore reflect estimator coupling/model structure. It is not independent proof of true road banking. The earlier OEM yaw cross-check corroborates body motion but does not identify its cause.

## Route differences

The steady cohort's per-session body/request medians range approximately107.5–114.0%. Session median learned steering ratios range22.25–22.90; angle offsets range roughly−0.70°to−3.49°. These estimates differ materially from the application's fixed19.6/zero-offset proxy, especially on gentle turns where a few degrees are a substantial share of wheel angle.

The fixed, unfitted roll term improves wheel/body measurement MAE in10of10sessions, so the pooled improvement is not confined to the longest session. An exploratory no-intercept roll scale fitted on all other sessions ranges0.859–0.910 in leave-one-session-out checks. It is not a control multiplier: fitting uses correlated samples and learned parameters, and no causal uncertainty or actuator policy is established. The fixed physics result is retained separately from that fitted diagnostic.

The previous55–60command-to-body model's close aggregate predictions and one-route residual dependence are consistent with a model missing relevant speed/roll/directional structure. They are not evidence that all highway tracking is correct, or that more highway data alone would solve the mismatch. Current evidence is sufficient to build an offline bounded mapping prototype; road validation remains a later step.

## Source/data trace: the calibrated target exists but is not used by this map

1. [controlsd.py](../../navigator-reference/PRIVATE_ARTIFACTS.md) updates its VehicleModel from learned ratio/stiffness and estimates current curvature using angle offset and roll.
2. [LatControlAngle.update](../../navigator-reference/PRIVATE_ARTIFACTS.md) converts desired curvature to wheel angle with roll, then adds learned angle offset.
3. [controlsd actuator assignment](../../navigator-reference/PRIVATE_ARTIFACTS.md) carries desired curvature and desired steeringAngleDeg as distinct actuator fields for this angle-control platform.
4. The Ford [path-angle map](../../navigator-reference/PRIVATE_ARTIFACTS.md) starts from `actuators.curvature`, maps it with speed and provisional factors, then applies correction/range/slew constraints. It does not consume `actuators.steeringAngleDeg` or live vehicleParameters.
5. [card.py](../../navigator-reference/PRIVATE_ARTIFACTS.md) currently subscribes to Panda/control/events/model topics, not vehicleParameters; its tracking-context bridge does not carry learned vehicle calibration.

Reading the private saved control streams confirms that the existing angle target matches reconstruction from recorded learned parameters: per-session median target-versus-reconstruction differences are within0.003°, with10th–90th differences generally within about0.03°. The minor raw/filtered-speed and alignment differences prevent claiming bit-exact target reconstruction. Median absolute recorded target-versus-actual wheel-angle errors range approximately0.89–1.56° across the10sessions. These are different stages of the control path, not evidence that the PSCM was asked to track that wheel-angle value.

Roll is **already used by the upstream curvature limiter**, but that shifts acceleration bounds; it is not equivalent to carrying the model's roll-aware desired wheel target through the Ford path-angle conversion. Do not add compensation to both the target and mapper independently.

## What should change next

### First prototype: restore an explicit calibration-aware mapping seam

- Keep requested body curvature and the existing learned desired wheel angle as distinct, inspectable targets. Use the existing calibrated angle target as a diagnostic reference rather than discarding it silently.
- Build an application-side conversion into Ford path angle that accounts for the roll-aware steering component and learned calibration, preserving1.20/0.97 as the baseline coefficients. One equivalent model relation is `wheel_component_target = desired_body_curvature − modeled_roll_effect`, under the verified sign conventions. That relation alone is not a validated path-angle command policy.
- If vehicleParameters are consumed at the strategy seam, pass them with explicit validity/timestamps and isolate a dynamic application VehicleModel. Do not mutate the fixed native-safety/pinion model or overwrite CP safety geometry with learned values.
- Start as an opt-in, bounded/smooth50–70mph correction around the existing feedforward. Stale/invalid parameters must fall back to the unchanged map. Bound absolute/relative changes, onset, release and slew behavior; do not remove original driver/permission/safety guards.
- Preserve truthful planner intent/shadow metadata and fixed firmware limits. Do not alter intent markers simply to admit a different command. Verify both turn directions and zero/near-zero demand, where dividing by requested curvature is unreliable.

**Do not directly place `steeringAngleDeg` into PSCM `path_angle`.** The units/semantics and actuator response differ. Likewise, do not invert the native fixed19.6 model to retrofit live learned values into safety. The desired-wheel-to-path-angle conversion must be identified and validated as an application mapping.

### Only then consider residual feedback

First determine whether the bounded feedforward mapping reduces route/directional error in held-out replay/model tests. If a persistent measured deficit remains, evaluate calibrated wheel/body feedback separately, with identified dynamics and freshness; avoid counting the same roll correction twice. The existing below25mph tracking term and budget cannot improve50–70mph because their speed weight is zero there. A rearm change is therefore not the highway fix.

### Required evidence before installation

Use the complete515segment retained corpus for candidate-generated/native safety replay, with trackingOFF parity and defined scope/blending checks. Add data-flow sign/unit/stale-parameter tests, measured-versus-target decomposition, both-direction/zero-demand cases and abort/withdrawal/entry timing screens. Independently review the mapping and its fallback behavior. Native replay cannot prove physical tracking improvement; a later supervised road comparison would be required after separate deployment authorization.

45mph remains objectively in scope for the broader project, not assumed perfect. An initial50–70prototype would have an explicit evaluated scope, rather than freezing45mph calibration permanently.

## Evidence and verification

`decomposition.json`, `route-check.json`, `steady-rows.json`, `target-check.json` and private-cache SHA receipts retain the analysis. `verification.json` checks the signed decomposition identity, ten-session improvement of fixed physics roll prediction and angle-target reconstruction. The mean identity is a calculation QA check, not proof of causal roll attribution. Expected paired source/dependencies remain clean. No new controller/native replay, build, setting change or road test occurred in this investigation.
