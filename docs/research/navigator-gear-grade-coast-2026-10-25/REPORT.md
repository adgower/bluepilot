<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Ford coast, engine-braking and gear/grade investigation

**Local experiment completed; not an installation candidate.** The saved data identify useful input/response distinctions but do not identify a complete causal engine-braking map. The proposed bounded valid-propulsion bridge fails the full controller comparison. Nothing on the Comma or either paired branch was changed; 1.20/0.97 is preserved.

## Data and method

Reused SHA-256-verified original command/RX caches covering 96 OEM/Alpha segments: five OEM routes and three older Alpha routes. OEM commands are original received camera-side requests with openpilot longitudinal disabled; Alpha commands are original transmitted vehicle-side requests with longitudinal enabled. Original extraction and ownership/freshness selection are retained. No external sources or new downloads were needed.

Identification selects 0.6-second windows with continuous eligible original commands, no driver override, actual and arbitrated reported brake torque at most 4 Nm, a constant input mode, command variation at most 0.025 m/s², stable forward gear, and the DBC's **GearEngag_D_Actl = 6, Fwd_Clutch_Fully_Engaged**. It estimates average acceleration from speed change rather than treating every wheel-derived acceleration spike as vehicle response. Low lateral demand is required. Future window stability is a retrospective data selection criterion, never runtime controller information.

There are 2,137 overlapping windows: 866 OEM and 1,271 Alpha. These are not independent maneuvers. Fit/evaluation anchors are thinned to at least one second per route; whole-route fit, calibration and test roles are retained. The existing test routes had already been examined in earlier work; this is not blind prospective validation.

“Grade” below means the recorded vehicle-pitch gravity term: below -0.15 m/s², within ±0.15, or above +0.15. It is **not independently measured road grade** and includes calibration/body-motion uncertainty. The results do not uniquely separate engine drag from rolling resistance, aerodynamics and grade.

## What the response data show

| Original no-brake input | OEM windows | Alpha windows | Observed distinction |
|---|---:|---:|---|
| Inactive propulsion (-5) | 32 | 0 | OEM median acceleration about -0.398 m/s²; not a zero-force state |
| Valid negative propulsion | 194 | 41 | Mild deceleration without reported friction braking is observable |
| Near-zero valid propulsion | 224 | 51 | Often near steady speed while propulsion torque remains positive |
| Positive valid propulsion | 416 | 1,179 | Acceleration authority and response depend on operating context |

These are observational populations with different routes/speeds; their medians are not randomized comparisons of the commands.

A concrete OEM test-route example in 10th gear / near-level pitch band:

- near-zero valid request: median acceleration -0.032 m/s², median reported propulsion torque about 332 Nm;
- valid negative request: median request -0.11 m/s², median acceleration -0.118 m/s², median reported propulsion torque about 209 Nm.

Thus “negative acceleration request” does not necessarily mean negative reported wheel torque, and “zero acceleration request” does not mean zero torque. A controller should not interchange inactive propulsion, valid propulsion and friction braking on that assumption.

## Grade and gear model checks

Compared a net-acceleration request predictor, request plus/minus the recorded gravity term, and a regularized model including initial acceleration, propulsion torque, speed, gravity and gear. On the broad held-out Alpha set the net-request predictor RMSE is 0.0849 m/s²; the added/subtracted-gravity alternatives are 0.2026 / 0.1433, and the learned context model is 0.1124. Additional gear/grade complexity does not win that comparison. This supports the net-acceleration interpretation in these cases; it does **not** prove that all grade compensation in the controller should be deleted.

In the narrower weak-demand held-out set, net-request prediction RMSE is 0.0587 OEM (23 thinned anchors) and 0.0791 Alpha (64). A first-order response grid chooses zero added lag on the selected settled windows. **That is not evidence of instantaneous ECU response:** the selection deliberately requires stable input. Strict isolated-step selection finds zero qualifying steps, so engine-response delay remains unidentifiable under those criteria.

For the prototype's support check, fit and calibration routes are explicitly combined as development data; test routes are excluded. The original fit-only support table is retained separately. Support requires at least 10 thinned anchors and absolute residual 90th percentile at most 0.15 m/s², within observed speed/gravity ranges. These are research admission criteria, not safety confidence bounds.

Only 8th-gear downhill/near-level groups pass the combined-development criteria, covering roughly 31–44 mph. The larger 10th-gear groups have 90th-percentile errors about 0.155 and 0.164 m/s² and fail this chosen criterion. The threshold was not loosened after seeing the replay to manufacture highway coverage. Uphill and other gears are sparse or unsupported. No complete 0–85 mph coast map is established.

## Brake-release timing by gear and pitch band

Examined 277 moving brake-release episodes with initial reported torque above 4 Nm. There are 243 completed observed-clear episodes; others are censored by reapplication, gear change, invalid/gapped data or observation limit. Clearance requires three distinct received samples at most 4 Nm spanning at least 40 ms, preserving the existing benchmark rather than predicting clearance.

Selected larger groups are tabulated in `release-by-gear-grade.json`. For 10th gear, Alpha near-level completed releases have median about 0.148 s; OEM downhill about 0.161 s. These are conditional completed-episode statistics, not a maximum release time. Censored episodes and the separately observed long maneuver releases prevent substituting a fixed 0.2-second timer. Timing includes command/transport/filtering and does not isolate a hydraulic delay.

## Local prototype and failures corrected

Implemented a support-gated valid-propulsion bridge before weak friction-brake entry. It keeps the actual original CarController, measured clearance, gas ramp, fault handling and integral policy. The new selector never predicts brake clearance. It requires fresh independent no-lead radar, stable engaged gear, fresh actual/arbitrated torque at most 4 Nm, small tracking error, weak positive planner/raw request and low lateral demand. It has a fixed 300 ms maximum and a measured 0.04 m/s speed-error budget, with sustained positive recovery before rearming.

Two ordinary defects were caught and fixed:

1. After its deadline, the bridge could fall into the legacy brake qualifier and delay braking again. `budget-red.log` reproduces this; the corrected lock returns the baseline brake decision immediately.
2. An infinite pitch value raised a math-domain exception in the research wrapper. The existing invalid-pitch contract caught it; the wrapper now marks that context invalid and lets original fallback handle it. `nonfinite-pitch-red.log` is retained.

The final source was replayed again after these fixes and the strict gear-engagement check. Its generated wire and producer histories are identical to the preceding native-tested variant, proved in `final-native-identity.json`.

## Full replay result

Actual causal LongControl plus CarController replay processed **137 segments / 401,970 consumer callbacks**, with persistent integral state and returned candidate feedback at recorded publication times. Recorded planner, vehicle response, reported torque, pose and driver actions are frozen. This is not a closed-loop counterfactual vehicle simulation.

| Matched common active samples, five-mph bands | Baseline | Trial |
|---|---:|---:|
| Exposure | 4,210.259 s | 4,210.259 s |
| Brake-bit transitions | 992 | 1,008 |
| Successive transitions less than 0.6 s apart | 218 | 243 |
| Brake-command time | 1,485.477 s | 1,491.508 s |
| Propulsion-inactive time | 1,601.837 s | 1,609.441 s |

Only 30 callbacks report an admitted bridge across the two recent highway routes. Nevertheless its earlier changes to returned authority/feedback alter later integral history. In the second route, **430 strong-planner-deceleration samples have weaker generated wire requests**, maximum brake-acceleration delta **0.1326 m/s²**. This occurs after the new mode has fallen back; preserving the integral algorithm alone does not preserve its trajectory.

There are no added coordination faults or inactive-control differences. The existing reconstructed older-route faults remain. The maneuver route and all older 61 segments are wire-identical to their current-stack baselines because required runtime context keeps the new mode out of scope there. The named 55 mph and highway pulsing windows do not improve; one lower-speed window worsens from eight to ten transitions. No gain is credited from loss of engagement or changed driver behavior.

## Verification

- Nine focused policy/controller tests passed, including actual pressure-clearance and timeout checks under an optimistic admission stub.
- 157 retained Ford tests plus 20 subtests passed after the invalid-pitch fix.
- Fresh plain-debug native replay of all 137 segments: totals and zero-added-rejection assertions are in `RESULT.json`. Original RX, non-ACC TX and timers retained; controls permission never forced. Final wire identity permits applying those native results to the final fixes without claiming another native run.
- Native acceptance is not hardware, ARM, comfort or road validation. No sanitizer run. Original/baseline rejections remain visible; zero added rejections is not zero total rejection.
- The known hidden consumer pose/IPC receipt-order reconstruction limit remains. The separate recorded pose mismatch is not claimed fixed.
- Paired clean source preserved at `ead00c30e` / `d4a20125`; no device connection or settings writes.

## Decision and remaining work

**Reject the bridge for integration.** It neither resolves highway pulsing nor contains later integral effects. Keep the response distinctions, gear/grade support table, release timing and regression fixtures.

The saved drives support useful net-command response estimates, but there are no qualified Alpha inactive-propulsion/no-brake windows and no clean isolated coast steps under the strict criteria. A causal coast/engine-drag model for every gear cannot honestly be recovered from these samples. More complex grade compensation did not improve held-out Alpha prediction, so adding a gear/grade correction table is not justified here.

The next controller design needs an explicit brake/propulsion allocator with integral tracking of actual achieved authority, bounded recovery when returning to lead braking, and a validated dynamic response model. Its first regression must include the later lead-braking divergence, rather than only the instant coast event. Frozen-state replay remains a required CAN/fault regression but cannot prove physical comfort after changed commands. Do not relax measured clearance, force permission, or reset the integral to recorded oracle values to pass it.

No new drive or installation is requested by this report. A future identification test would need a separate controlled plan for the missing input/response regimes; repeating ordinary highway driving alone is not guaranteed to supply them.
