<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Ford coast and brake-release response model

October 24, 2026. Local original-recording analysis only.

## Outcome

**The local response forecaster improved on both evaluation routes.** It models reported propulsion torque, reported brake torque and measured acceleration at 40, 100, 200, 400, 600 and 1,000 ms using the initial received state and known original command prefixes. It does not grant brake clearance, supply actuator feedback or change control logic.

Whole-route evaluation, one-second horizon, lower RMSE is better:

| Evaluation source | Channel | Same-split legacy model | Improved forecaster |
|---|---|---:|---:|
| OEM ACC | Propulsion torque | 281.9 Nm | 179.4 Nm |
| OEM ACC | Brake torque | 127.4 Nm | 67.9 Nm |
| Alpha | Propulsion torque | 179.0 Nm | 87.6 Nm |
| Alpha | Brake torque | 91.2 Nm | 60.3 Nm |
| OEM ACC | Acceleration | 0.391 m/s² | 0.293 m/s² |
| Alpha | Acceleration | 0.298 m/s² | 0.263 m/s² |

These are prediction-error reductions, **not measured driving, comfort, fuel-economy or stopping improvements**. The Comma and paired branches remain unchanged, with owner steering constants 1.20/0.97 preserved.

The same-split legacy baseline is refitted on the new training pool and evaluated on whole separate routes using original wire requests. Its numbers are not directly comparable to the prior single-session result (~45 Nm brake error), which used different training, evaluation coverage and clock/input construction. Use the paired columns above for this round's comparison.

## Original data and fixed roles

Re-read and SHA-256 verified **96 raw segments**: 35 OEM across five cached routes and 61 Alpha across three sessions. No duplicate raw segment hash is allowed across roles. OEM carParams confirm openpilot longitudinal disabled. OEM requests come from received camera-bus ACCDATA; Alpha requests come from original vehicle-bus sendcan ACCDATA. Original received bus-zero torque, arbitration, drivetrain and status fields are retained.

| Role | Cached routes | Model cases |
|---|---|---:|
| Fit | OEM01, OEM02, older Alpha01 | 4,587 |
| Calibration/model-method selection | OEM04, older Alpha02 | 7,367 |
| Evaluation excluded from fitting/calibration | OEM05, latest Alpha | 839 + 5,150 |

OEM03 contains no eligible ACC model cases and contributes no training examples. Cases overlap in time, so counts are not independent maneuvers. The latest Alpha recording had already been examined in preceding investigations. Development diagnostics, including initial evaluation errors, were inspected while refining the forecast heads; **this is not a blind prospective test**.

Selection requires fresh state/control, CAN-valid state, active original command ownership, no driver pedals, valid numerical torque and uninterrupted command coverage. Targets affected by pedals/invalid state are excluded. Commands are never rewritten. Original extracted command/RX cache hashes match after replay.

Input-only feature history is causal: initial state/torque/arbitration/status, past commands through 400 ms, and known original commands only through the predicted horizon. A regression caught a one-nanosecond tolerance that could include a later command; integer-nanosecond cutoff now excludes it. No future torque, RPM, gear, arbitration or status measurement enters a prediction.

Alpha sendcan is a requested packet, not an ECU delivery acknowledgment. The resulting model includes observed scheduling/transport/control effects and cannot isolate hydraulic dynamics from these logs alone.

## OEM versus Alpha response findings

The data distinguish six input regimes:

1. Actual brake request.
2. Precharge-only request.
3. Propulsion inactive (-5), without requested brake/precharge.
4. Valid negative propulsion request without brake/precharge.
5. Near-zero valid propulsion request without brake/precharge.
6. Positive propulsion request without brake/precharge.

Inactive propulsion does not establish neutral, fuel cut or zero wheel torque. A valid negative request is a different ECU input. Precharge is also an input that may produce torque; it is not equivalent to no braking.

Completed release timing is broadly similar in the original recordings. Across the eligible OEM routes, median command-to-reported distinct-sample clearance is about 152–169 ms; the Alpha sessions are about 163–168 ms. Reapplication, override, gaps and observation limits censor other episodes. Sample timing includes transport/filtering and is not isolated ECU delay.

Reported torque can remain above 4 Nm after both host brake/precharge bits are off. In the two early OEM routes, approximately 96.5% and 89.0% of those samples also have an arbitrated brake-torque request above 4 Nm. The Alpha fractions are approximately 56–59%. This supports including arbitration state and command history instead of fitting only an undifferentiated decay. It does **not** identify the owner of every arbitration request or prove causality between the two reported estimates.

These are ECU-reported torque quantities, not direct hydraulic-pressure readings or independently calibrated pad-force measurements. The existing 4 Nm/three-distinct-sample clearance rule was not changed or physically revalidated here.

## Model changes

The same-split benchmark retains the preceding four-mode autoregressive form and advances it under original known commands. The improved forecaster combines:

- Initial reported actual and arbitrated brake torque, propulsion actual/requested torque, motion and available drivetrain/status context.
- Causal command history and command-prefix timing, keeping valid coast, inactive propulsion, precharge and braking separate.
- Separate direct-horizon forecasts to avoid accumulating a small one-step error over an entire second.
- Regularized regression plus a local analogue residual model; the choice uses calibration routes only.
- A separate low-torque probability and positive-torque magnitude head for release/coast. A mixed average of zero and nonzero torque was producing spurious retained-torque predictions. The new head models those regimes separately.
- Empirical residual intervals and a numerical training-support flag. Neither is safety certification.

The forecaster never substitutes predicted torque for received CAN feedback. It has no method that grants actuation or clearance. No controller imports it, and no new CAN packets are constructed or sent.

## Low-torque forecast checks

For analysis only, “low torque” means the reported torque is at most the existing 4 Nm benchmark. A high-confidence forecast is a calibrated empirical probability at least 0.99, within the model's numerical support, with no brake/precharge requested at the prediction horizon.

One-second evaluation results:

| Source | Eligible release/coast cases | High-confidence forecasts | Erroneous early-clear forecasts | Initially retained-torque forecasts |
|---|---:|---:|---:|---:|
| OEM | 674 | 617 (91.5%) | 0 | 9 |
| Alpha | 3,634 | 3,306 (91.0%) | 0 | 341 |

The initially retained column starts with reported torque above 4 Nm, so this result is not obtained solely by forecasting already-zero states. It also does not obtain zero errors by declaring everything unknown. The same-split legacy probability forecast made 11 erroneous high-confidence forecasts in the Alpha one-second set; the improved model made none in this finite sample.

A minimized same-case replay is retained: the legacy model predicts approximately zero with probability 0.9978 while received torque is 60 Nm. The improved model's average is still badly wrong for that case (~1.6 Nm), but its low-torque probability is only 0.84, so it correctly avoids the high-confidence claim. This is an uncertainty-handling improvement, **not proof the torque estimate or physical release has been solved**.

Across shorter Alpha horizons there are still **11 erroneous high-confidence samples**: 3 at 40 ms, 3 at 200 ms, 2 at 400 ms and 3 at 600 ms; zero at 100 ms. These counts may share physical episodes. Even the one-second result supplies no physical-clearance guarantee.

The mean forecast itself must not be thresholded as clearance. At one second its Alpha point estimate still produces 12 early-low predictions, versus 11 for the legacy point model, although late/retained predictions drop from 351 to 142. For OEM, early-low point errors remain zero and late/retained errors drop from 98 to 48.

One-second empirical brake-interval coverage is about 98.1% OEM and 97.0% Alpha, with median widths around 85 Nm. OEM propulsion-interval coverage is only about 91.5%, below the nominal residual interval target; Alpha propulsion coverage is about 98.7%. These are diagnostics, not calibrated safety bounds.

## Coast and speed gaps remain visible

Stratified results are in `stratified-replay.json`; they are not all uniformly better.

- In valid-negative/no-brake one-second Alpha cases (144 cases), propulsion error improves from 82.3 to 46.0 Nm, and brake-torque error from 7.27 to 1.49 Nm.
- The equivalent OEM propulsion stratum (69 cases) regresses from 90.4 to 106.9 Nm, although brake-torque prediction improves. Do not claim a universally improved coasting model.
- There are only four uninterrupted inactive-propulsion/no-brake one-second cases in the OEM evaluation route and one in Alpha. Those sparse cases perform worse and do not validate prolonged inactive coasting. Training contains more examples, but that does not substitute for held-out coverage.
- The held-out Alpha route covers 0–70 mph, with sparse individual bands. The held-out OEM route has no cases below 15 mph. The older Alpha training/calibration data reach the low 70s, but neither evaluation route supplies 70–85 mph validation. Previous Alpha audit found no active 75–85 mph data.

No interpolation into unsupported speed ranges is labeled validated. No stop/restart, highway acceleration or steering tune was changed.

## Replay and verification

- Seven focused contracts pass: horizon-prefix causality (including +1 ns), stale/missing inputs, split-role protection, no actuation-permission output, model serialization/immutability and unsupported one-class training.
- The prior response-model fixture remains red, documenting the old failure. The same-split forecast fixture is red with the legacy model and green with the improved forecaster; the global one-second coverage check also passes.
- Original-command held-out replay covers all six horizons on both evaluation routes. The primary one-second propulsion/brake RMSE improves on both routes. Short-horizon, regime and coverage regressions are retained.
- Original source data caches are unchanged. Paired parent/child remain clean at `74eaa6a60d344f141d06da16f4dbe10d3de49c0e` / `3a5fe9fe5a296d44b7f898b580c2d3afafe6bfd1`; 1.20/0.97 remain present.
- This round changes only a forecasting research tool. No native controller safety rerun, ARM/product build, physical test, device staging or installation was performed. Packet-generation/control paths were not changed.

## Appropriate next use

Use the model for local original-command response analysis and uncertainty-aware stress cases in supported regimes. It is not yet a validated closed-loop vehicle simulator for arbitrary controller changes. Known future command prefixes are available in these replays; an altered controller would generate its own future commands from changed vehicle feedback, and its motion/gear/ECU-state evolution has not been established by this test.

Next priorities are rare retained-arbitration/hold episodes, low-speed drivetrain transitions, OEM valid-negative coast response, prolonged inactive coast coverage and validation on additional unseen routes. Keep real received feedback authoritative and keep uncertain response cases in controller acceptance tests. This model improvement does not authorize installation or establish that highway pulsing is fixed.

## Artifacts and reproduction

- `split-manifest.json`, `case-manifest.json`: whole-route roles, original hashes and exposure.
- `fit-provenance.json`: train/calibration counts and selected forecast method.
- `protocol-response-analysis.json`: original OEM/Alpha modes, arbitration and censored release timing.
- `heldout-replay.json`, `stratified-replay.json`: full horizon/speed/regime metrics.
- `validation-status.json`: preservation and primary research checks.
- `features.py`, `response_model.py`, `probability.py`: forecasting-only implementation.
- `legacy_arx.py`, `train_evaluate.py`: same-input benchmark and held-out replay.
- `replay_fixture.py --baseline`: expected red; default `--assert-useful`: expected green.
- Use the paired checkout's `.venv/bin/python`; pytest needs `-o addopts=''` and this folder as `--confcutdir` to avoid ancestor configuration.

Raw arrays, fitted models, forecast cases and recorded route identities remain under `${PRIVATE_CACHE}`. Derived caches are local research artifacts, not permanent backups. Model-development variants are retained as separate JSON results where applicable. Nothing was pushed or published.

### Durable local model copy

The fitted models, matching prediction source, version metadata and minimized fixture are also retained in the Git-ignored local directory `${USER_HOME}/Apps/bluepilot/.navigator-response-models/20261024-coast-release-v1`. Checksums are in `model-archive.json`. This preserves the trained forecaster beyond temporary-cache cleanup without adding a large model binary to the repository or publishing it. Full original-recording/derived-array caches remain separate as described above.
