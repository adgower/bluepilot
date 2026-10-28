<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Allocation/response redesign: causal transaction fixed, controller rejected

**The local longitudinal blocker is diagnosed more precisely, but no acceptable controller fix has been achieved.** The joint diagnostic activates and changes commands; unlike the earlier zero-activation candidate, it is a real test. It fails the first complete focused route by adding brake exposure and weakening later strong requests. It is rejected before broad/full/native replay. No paired source or Comma change occurred.

## Implemented and tested

[Design](DESIGN.md) separates desired net acceleration, numerical actuator request and observed achieved acceleration. The first numerical-only spike passes seven receipt/error tests but fails a synthetic grade-mode counterexample: raw .3000 plus gravity −.2995 is positive .0005; tracking −.001 enters friction at −.0005 despite actual acceleration being above target. That failed source/test is retained; gain was not retuned.

The revised [joint module](../../navigator-reference/PRIVATE_ARTIFACTS.md) and [research adapter](../../navigator-reference/PRIVATE_ARTIFACTS.md) project only an optional negative tracking increment into the current/receipt command-mode feasible interval. They never raise native demand to a floor or override necessary braking. A newer consumer grade can veto only the optional increment. The integral update remains staged until a same-owner, exact issued-branch receipt acknowledges it; then it commits once, subject to current target/phase/urgency/headroom. Veto discards uncommitted work, not committed I. No copied reference I, reset to recorded values, independent weak-demand account or rearm exists. Original clearance and timeout remain authoritative.

The source residual compares decoded ACCDATA propulsion against the candidate's own issued request for the consumed sequence. Its 0.01 m/s² DBC quantum is ignored for residuals at or below one quantum; −5 is never treated as achieved acceleration. Own native/corrected numerical branches are cached. Internal branch receipt does not imply that two tiny numerical proposals produce distinct quantized packets. In particular this is command-authority accounting, not a measurement of the physical effect of a .001 change.

Admission requires actual acceleration at least target and nonpositive accumulated current-ramp measured speed error, so a merely slow acceleration ramp cannot admit negative tracking. It also requires fresh causal ownership/clock/target, valid numerical propulsion, no pedals/stop/FCW/force-decel and no existing CommandRecovery overlay. Target/clock gaps invalidate optional work without forgiving I or the existing sampled .01/.3 account.

**Transport is an offline research sidechannel**, keyed by candidate epoch, sequence and consumer timestamp, carrying actual generated packet decode and causal grade feasibility. It is not integrated cereal negotiation or paired production transport. Seventeen joint tests pass, including NaN/corrupt cache, sequence reuse, timestamp ordering, inactive/stale commit, target changes, reset/new owner, newer-grade veto, existing necessary braking, quantization no-windup and inability to undo a committed derivative. Seven first-spike causal tests pass separately; its deliberately failing grade counterexample remains an expected rejected-design test. This is not a claim that every test under the folder is green.

## Focused real producer/consumer replay

Exact-source saved baseline is reused with its hash disclosed in [baseline reuse](../../navigator-reference/PRIVATE_ARTIFACTS.md). The final candidate freshly runs the entire newest installed session: **21 segments / 60,424 consumer callbacks / 114,018 producer steps**, with no active atomic-input gap. It records **410 nonzero producer proposals and 69 integral commits**; no consumer veto occurs in this route (newer-grade veto is covered synthetically).

| Gate | Baseline → candidate |
|---|---:|
| Full-brake changes | 280 → 278 |
| Full-brake exposure | 389.587054 → 390.475493 s |
| Extra full-brake callbacks | 85 |
| Combined brake/precharge exposure | 397.179772 → 397.961153 s |
| Weaker raw strong-target callbacks | 476 / 4,083 checked |
| Weaker encoded strong-target callbacks | 212; maximum +0.0039 m/s² |
| Changed wire callbacks | 29,626 |
| New fault / lost or gained activity | 0 / 0 |
| New gas under brake/precharge or fresh retained torque | 0 |

Named adverse windows remain **14→14, 15→15, 12→12** full-brake changes. Overall two fewer edges are not a benefit clearance: braking lasts 0.888439 seconds longer and later strong braking is weaker. Encoded differences are one brake-field quantum, but the underlying I/raw difference is real; it is not discarded as propulsion representation noise.

[Complete comparison](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Final replay receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md)

Only this failing focused route was required to reject the hypothesis. Protected city/other restart routes, fresh full316 candidate replay, native replay and hypothetical closed-loop plant comparisons were intentionally **not run after the decisive focused failure**. Earlier full316/native results belong to the earlier unchanged-output candidate and are not reused as validation of this changed controller.

## Exact delayed failure chain

[Failure-chain evidence](../../navigator-reference/PRIVATE_ARTIFACTS.md) preserves preceding callback context. Times below use first-carState route origin, not the previous report's first-log origin.

1. **+128.2796 s:** first optional −.001 proposal while both variants remain in engineRamp; I is still equal.
2. **+128.2990 s:** first acknowledged commit makes candidate I .001 lower. Command feasibility remains valid.
3. **+142.8654 s:** after tracking is already off and target is −.00986, candidate enters friction one callback sooner. Its prior committed I is still .001 lower. Instantaneous projection cannot prevent this later history effect without undoing committed I or changing needed braking.
4. **+150.2800 s:** baseline is release/wait-observed-clear and freezes positive error; candidate remains actual brake and permits positive native integration. At this point target .03639 exceeds measured −.13915.
5. **+150.2986 s:** candidate I crosses above baseline by **.00282732**, despite all experimental commits being negative. Feedback still reflects candidate's preceding actual brake while baseline reflects release.
6. **+157.2651 s:** target −.50708; baseline raw −.316876, candidate raw −.314049. Tracking is off and both physically command braking, but the accumulated difference weakens this later strong request.

This confirms that negative-only correction does not preserve integral ordering across hybrid authority states. The defect in the proposed design is treating instantaneous command feasibility and numerical tracking as sufficient to contain future integral effects. Returning the installed algorithm after a commit means that algorithm runs on a changed state; it does not restore baseline history.

## Required joint authority semantics

Making the freeze decision independent of brake bits is not, by itself, a defensible fix. Under actual braking, increasing raw request can reduce requested friction effort. During a fully withdrawn request with retained pressure, raising raw cannot necessarily remove pressure faster and may only accumulate future propulsion demand. Conversely a blanket positive freeze can trap excessive braking or prolong already-slow acceleration. A sticky freeze or repayment ledger cannot establish the missing directional authority, and previous debt/bridge experiments already failed after their nominal recovery ended.

The appropriate response-state variable is an interval for **how a causal request change can affect future achieved acceleration over the release/ramp horizon**, conditioned on measured pressure-proxy/status history, valid propulsion mode, gear and grade. Integration in a direction should require that the interval identifies useful controllability in that direction; saturation/tracking should refer to physically supported authority, with the independent measured-clearance barrier unchanged. Strong/stop/urgent paths remain authoritative. This can be specified and tested as a module contract, but its numerical transition gain/delay is not identified by present command bits plus current aEgo/125/531 alone. Two systems can share that observed prefix and have different remaining pressure decay or engine-drag response; a bit-only gain is an assumption, not an identified response model.

No third controller hypothesis was added after the two failed spikes. A validated mode/achieved-authority transition model is the missing prerequisite, rather than a new command-floor bandage.

## Exact missing observed regime

The older [gear/grade/coast investigation](../navigator-gear-grade-coast-2026-10-25/REPORT.md) already reviewed 277 releases, found zero strict isolated coast steps and no qualified Alpha settled inactive-propulsion/no-brake windows. Its net-command RMSE .0849 beat added/subtracted gravity .2026/.1433; it does not authorize gravity removal. Its valid-propulsion bridge increased 992→1,008 edges and weakened 430 later strong requests.

Fresh support audits extend that context without pretending generated commands are observed vehicle response:

- **Current-source reconstructed full316/23 baseline:** 1,103 strict healthy weak-positive, fresh-torque-clear, no-brake/precharge, inactive-propulsion runs; maximum observed callback span **0.341893 s**, zero spanning 0.6 s. This is software command-support evidence, not new physical coast identification.
- **Nine newly saved ORIGINAL recorded arrays / 79 segments:** 195 runs under the stated strict source/target/state/torque qualification; maximum **0.181139 s**, zero spanning 0.6 s. Installed session08 supplies 111 runs, same maximum. These are short conditional observations, not independent matched experiments or a complete census of every coast/release event.

[Full reconstructed support audit](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [New original-recording support audit](../../navigator-reference/PRIVATE_ARTIFACTS.md)

### Bounded evidence prerequisite, not a driving instruction

Before attempting another authority-based I law, a separately authorized identification plan must provide observable **clear no-brake/inactive-propulsion response** in the weak-positive 40–70 mph regimes, separated from retained-pressure decay, plus **release→clear→valid-propulsion transitions** with independently variable input timing. Existing ordinary traffic co-switches pressure, propulsion, gear and target; simply collecting more of the same does not guarantee identifiability.

Here 0.6 seconds is the prior research selection criterion, **not** a physical safety constant, maximum release time or runtime timeout. A fit plan must validate an appropriate observation horizon rather than infer one from that selection. A minimum fit attempt needs verified original command ownership (OEM observations remain OEM, Alpha observations remain Alpha), continuous fresh command/status/torque/state and stable engaged-gear/pitch context, a verified torque-clear prefix and at least a 0.6-second clear coast observation interval, followed through valid propulsion or explicit censoring. Matched valid-propulsion observations in the same operating regime and distinct whole sessions reserved for held-out transition tests are necessary; no claim is made that a chosen episode count alone suffices. Received 531/125/359/512 and 374/516 must remain separate from sent requests and the acceleration used for scoring.

Candidate admission would require held-out multi-horizon predictions of acceleration and torque/status transition timing, calibrated uncertainty and explicit unsupported states. The uncertainty plus proposed tracking effect must fit the existing single permitted deficit envelope; otherwise use installed behavior. Parked/offline replay cannot supply missing dynamic force or release observations. Bench/HIL counterfactual tests can exercise the contract first, but a fitted hypothetical plant does not fill the missing physical response regime. Controlled command changes would require a separate validated and explicitly authorized identification plan. No test plan is activated here, no new road maneuver requested, and no device connection or custom CAN is authorized by this report.

## Preservation and scope

All implementation/evidence files are confined to this new research directory and task-specific private compressed outputs. Earlier receipts remain unchanged. Parent/child remain clean at `e05e42f43` / `5097b993`, owner 1.20/.97 unchanged. No SSH/network/device operation, source integration, commit, push, setting/service/calibration/OS/firmware change or CAN transmission occurred.

Result: transaction causality, representational authority and the delayed integral crossover are tangible local findings. The joint physical allocation/integral response blocker remains unresolved; this candidate must not be integrated or installed.


## Additional offline dynamic identification

The [dynamic-identification addendum](dynamic-identification/REPORT.md) now tests original timed OEM/Alpha data rather than inferring unlearnability from missing settled coast windows. Across a 175-original-segment input inventory, strictly origin/past features forecast short transient trajectories; commands add modest predictive value beyond state history on held-out Alpha highway data. A secondary seven-session fit confirms that modest value but leaves the 0.1-second observed-command-direction sensitivity sign unstable and current-session nominal90% bands under-covering. Most Alpha inactive origins naturally return propulsion within the forecast horizon, so successful forecasts do not validate holding inactive propulsion.

This narrows the missing prerequisite to causal achieved-authority identification and transferable uncertainty, not an assertion that transient prediction cannot be learned. The failed controller's 212 weaker strong requests and extra brake exposure remain rejected. The prior controller receipt is preserved in controller-focused-VERIFICATION.json; no new controller or full/native replay is claimed.
