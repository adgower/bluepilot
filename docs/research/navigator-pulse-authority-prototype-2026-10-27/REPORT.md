<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Pulse/authority local prototype — October 27, 2026

**The local candidate is rejected. Do not integrate or install it.** The full237-segment controller comparison finds weaker later strong braking, increased cycling, and a new release-timeout in the latest drive. The steering and restart investigations are separate artifacts; none of this work changes the Comma or paired branches.

## Experiment and scope

The installed reference is parent `df788e02719c05595dab2f980e6fd9fb9e464006` / child `1d29e6e78abcbf5c6a80eb397d80b349c6cca960`. Owner1.20/0.97 and source remain unchanged. Inputs are the existing216-segment13-route longitudinal corpus plus today's21-segment moving route: **237segments/14routes**.

The throwaway candidate removes the independent legacy weak-entry admission clock and uses the existing allocator's single0.01 sampled signed-demand allowance,0.3sdeadline,debt retention and earned100ms rearm. Before commitment, within the same allowance and with valid fresh owner/pose/target, no pedals/FCW and measured clear torque, it selects true coast rather than precharge for weak negative net demand with positive planner intent. Propulsion withdrawal is truthful; engine qualification returns limited/engineRamp feedback. It also tests holding positive integral growth throughout a reported engineRamp phase rather than allowing the request-dependent0.011 numerical margin to unfreeze it near the ramp tail. No integral reset, referenceIcopy, torque prediction, gear command, extra budget or clearance bypass is introduced.

The direct weak/strong-entry tests pass, but that is insufficient: the changed feedback history changes later raw demand and release timing.

## Recorded producer reproduction versus coupled replay

With original recorded consumer feedback returned to LongControl, all **107,945** recomputed producer steps on the newest route match recorded raw acceleration within1e-5m/s² (maximum1.19e-7), and I within1e-5(maximum2.98e-8). Zero active atomic-input gaps occur. This confirms the producer implementation/input reconstruction.

The coupled reference instead returns reconstructed consumer feedback causally at recorded publication times. On the newest route it reproduces66.85% of producer raw requests within1e-5, maximum difference0.01114m/s²; exact hidden receive-drain/snapshot order is not logged. Thus the coupled reference is not asserted to be bit-exact installed-road reproduction. Both reference and candidate use the same declared causal state-boundary torque snapshot. Software feedback is closed; recorded vehicle/ECU/lead/driver response remains frozen. These limits restrict physical inference but do not turn the candidate's visible software regressions into a pass.

## Full joint controller comparison

All **685,504 consumer callbacks** complete on both sides. Of237segments,225segments/13routes have no missing active atomic inputs; one older12-segment route has disclosed active-prefix gaps and is diagnostic-only. The comparison retains that route separately. Counts below include all14routes unless noted; fault histories alter active exposure, so aggregate durations are not clean comfort effect sizes.

- City protected fixture: brake changes **17→27**, brake time21.448→23.957s.
- Earlier63mph highway fixture: **20→26**, brake time9.914→10.489s.
- Latest~59mph fixture: **17→27**, brake time9.232→9.410s; valid-propulsion time decreases.
- Latest other~59mph fixture: **12→12**, brake time4.456→7.417s.
- Latest~68mph and high-RPM restart fixtures become inactive after the candidate's earlier release-timeout. Their zero brake changes are **lost activity**, not successful smoothing or lower RPM.
- **1,620 weaker encoded strong-target requests** occur (1,614 with the brake bit), also present when the diagnostic-only route is excluded. These are later history effects despite immediate strong-demand bypasses.
- New latest-route `release_timeout_disengage` at relative892.958s, around55.43mph; reference has no fault there. One older reference fault disappears, but that does not compensate for the new fault.
- Commanded gas-under-brake/precharge and moving-PID gas with retained torque remain zero. Two additional positive-propulsion samples paired with valid retained torque occur in the broader low-speed classification and are retained as failed comparison items, not dismissed as clearance proof.
- Across all routes, brake changes1,877→2,253, extra-full-brake callbacks32,150, and full-brake exposure3,074.722→3,531.600s. These include changed fault/active histories and the diagnostic route; do not interpret the456.878s difference as predicted physical braking.

[Full comparison](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Complete-input subset](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [First divergence diagnosis](DIAGNOSIS.md)

## Why this failed

The first protected-city producer difference occurs before true coast: the broadened engineRamp freeze holds a positive integral increment near a numerically tiny remaining request limitation. Candidate I/raw becomes lower. Later the reference reaches net+0.03124 and releases braking while candidate remains at+0.01963 and retains braking. The finite allowance subsequently operates on this changed demand history.

A separate early coast example reinforces the loop: coast withdraws propulsion→limited feedback holds positiveI→raw/net remain lower→the sampled allowance exhausts→nominal braking returns. Later histories can cross back and produce weaker strong braking. Selecting fewer switches in one window is therefore insufficient; one older window improves12→5 changes while brake time increases4.159→10.586s.

This falsifies the proposed phase-wide freeze/coast combination on the retained software-history regressions. It does not establish that natural coasting cannot work. Do not enlarge the allowance, resetI, weaken clearance, suppress the timeout or cherry-pick the favorable switch count.

## Tests, review and protocol repair

The initial two behavioral assertions failed on the installed behavior before prototype implementation; five focused candidate checks then passed. Independent review identified unsupported-protocol handling and missing retained budget tests. `prototype2.py` adds allocator-feedback protocol validity plus positive owner/sequence checks. **26 focused/retained tests pass**, covering stale/future/faulted/wrong-owner feedback, signed braking, delivered drive, debt, deadlines, earned rearm, strong braking and existing signed-precharge behavior. Imported runtime source hashes and clean exact paired heads are captured in `runtime-source-before.json`.

The full237-segment v2 replay completes; every reconstructed wire artifact is SHA-identical to v1 across14routes. Thus fixing protocol validation does not fix the observed valid-context regressions. The first candidate and its logs remain retained as superseded research. Native replay outcome is recorded separately when complete; it cannot override the failed controller gates.

## Decision and remaining work

Reject this candidate. Keep the installed allocator unchanged. The next longitudinal design must distinguish demanded acceleration, measured delivery and actual coast/gear/grade response consistently, with the retained first producer/release divergence as a failing regression. The data do not justify a broad acceleration cap or unverified target-speed packet substitution. See the separate [restart diagnosis](../navigator-restart-response-prototype-2026-10-27/REPORT.md).

No hardware/ARM build, device installation, SSH, parameter writes, CAN transmission or physical/RPM/comfort validation occurred. Native saved-traffic replay is offline only. No branch integration, commits or publication occurred.

## Completed native replay

Fresh final-v2 native saved-traffic replay completes **237segments/14routes**, replacing **685,398 ACC slots** while retaining original received packets, non-ACC sends and timers. It adds **zero native TX rejections or relay faults**, with no forced controls permission. Native debug hooks are unsanitized; no UBSan, ARM, hardware or road proof is claimed. Source/header/binary hashes are recorded in `pulse2-native-source-provenance.json`; complete per-route counts are in `native-pulse2-results.json`.

This native acceptance does **not** change the rejection decision: controller-history gates fail, including the new release-timeout. Native limits alone do not ensure correct coordination or smooth vehicle behavior.

`urgent-input-audit.json` records zero archived FCW-plan or force-deceleration samples in all14routes. The coupled harness defaults urgent=false and cannot validate urgent behavior absent from the corpus; strong-demand unit guards and recorded braking comparisons are separate evidence. Consumer receive-drain ambiguity remains disclosed above.
