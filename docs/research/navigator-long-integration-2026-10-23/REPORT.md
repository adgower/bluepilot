<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Paired Navigator longitudinal integration — October 23, 2026

The report-local coordination policy is now integrated into the existing paired `codex/navigator-tracking-release` source trees. This task is local only: no push, SSH/device access, CAN transmission, settings mutation or activation. Owner1.20/0.97, all lateral mapping/refinements, vehicle geometry and installed stop/creep policy are retained. The new `FordPrefLongitudinalCoordination` parameter defaults off; Alpha alone does not activate this research feature.

## Integrated behavior

- Real Cap'n Proto request/feedback schema, controller-produced timestamps, producer sample time, controlsd process/engagement epoch and sequence. carOutput carries the actual controller result back to LongControl.
- Directional integral inhibition only for positive growth into a fresh, same-owner, deliberate propulsion cap. Ki0.5, legitimate braking integration and negative-error unwinding remain unchanged; no reset/rebase to hide a steady error.
- OEM-derived relative decision-reference mapping +0.14991323424078207m/s², at0.005m/s³, output fade3–5m/s. This is owner-specific reference alignment, not a camera-pitch reset or universal Ford gain. Strong brake-only demand preserves installed conservative onset and3.5m/s³ request slew.
- Actual CAN125 brake-torque observation with original parser timestamps. Only the opted-in trial registers this optional message; stock/OEM default-off validity requirements remain unchanged. Cached samples cannot count repeatedly, and DBC Unknown/Fault values cannot qualify.
- Moving entry and post-brake release require three distinct fresh<=4Nm samples spanning>=40ms. A1s deadline requests a fault/disengagement, never blind propulsion permission. A pedal override retains the release obligation and restarts fresh qualification when automatic control returns; its manual duration does not consume the deadline. Low-speed stop/creep wire policy is unchanged.
- Stale/invalid/reversed required context or release timeout latches local neutral longitudinal output. Fresh data/longActive dropping cannot rearm. controlsd inhibits longitudinal and resets LongControl; selfdrived emits the normal controlsMismatch immediate-disable/no-entry alert, with detailed reason in carOutput. A new enabled ownership cycle must qualify entry again.

See [fresh review and repairs](REVIEW.md) and paired child `docs/navigator-integration/LONGITUDINAL_COORDINATION_20261023.md`. All three Important fresh-review findings received failing/passing regression tests. No deferred minor findings.

## Final replay evidence

All six full-slot variants rerun using the actual integrated controller and LongControl. Replay adapters supply producer inputs and model/observed torque; they do not rewrite production policy. Controller feedback crosses a real schema serialization boundary before parent use.

| Check | Baseline | Integrated candidate |
|---|---:|---:|
| Full frozen-request, modeled152ms release brake transitions |213|77|
| Recomputed real parent, modeled152ms release brake transitions |221|65|
| Recomputed parent positive-I updates inhibited |0|1,561|
| Faults in either modeled full-drive candidate |0|0|

Each variant covers65,736actual Alpha command slots. Parent replay recomputes128,549updates with no missing active plan; baseline reconstructed command RMS error0.00510m/s². Stricter entry/override clearance deliberately changes the earlier prototype's63edges to65; do not relax entry validation to recover the previous number.

Default-off exact ACC stream parity; identical non-ACC hashes across all six variants. All36,086frozen replay slots excluded for inactivity/stop/creep/below3m/s preserve exact packets. Protected steering/geometry source hashes match the pre-integration child. [Comparison receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Changed commands evaluated against the OLD observed actuator response produce a fault at611.969s and27,549fault slots. Their reduced27brake edges are **not** a performance result. The causally matched original-command observer has zero faults over65,736slots. Independently settled OEM evidence contains25,552samples with maximum reported torque0Nm.58raw-rlog hashes reverified and40,544OEM selected-command fields preserve disabled representation; these are not counterfactual Alpha control of OEM routes.

288uncertainty scenarios /1,152,000real parent/controller updates:172improve acceleration RMSE; none worsen by more than10%; zero modeled faults. Median modeled RMS0.09875→0.06062m/s². Includes0.7s release tail,±0.06m/s² relative-zero uncertainty, grade, lag and pitch disturbance. Generic response assumptions, not an identified Navigator mechanical model; 116cases do not improve, and no road/fuel-efficiency claim follows.

Fresh final native ACC RX/timer replays, frozen and parent:5,260,361RX inputs and65,728ACC slots per variant; three shared baseline/candidate intervention-boundary rejections; zero added rejections, no final relay fault. Permission was not forced. Retained Mac debug hooks, unchanged safety source; only ACC TX hooks are exercised, not full steering/forwarding/heartbeat/hardware acceptance.

## Build/test status

Minimal and full development Mac SCons builds pass, including generated schema/native targets. Final repeat build passes. Ruff and whitespace checks pass. Final contract checks cover schema roundtrip, actual parent/card/controller pipeline (captured send only), integral behavior, real optional parser sample identity, faults, entry/override, stop/creep, urgent braking and timestamp reversal. Final results:

-35focused integration/observer contracts pass, including actual producer/card/controller transport and faults.
-915Ford/native tests /12,083subtests pass;79skips. The retained broad Ford/native suite primarily checks default-off compatibility; enabled behavior is covered by the focused contracts and replays.
-Full parent suite:1,028passed,87skipped,1expected failure,281passing subtests (`parent-suite-final-isolated.log`).
-Broad opendbc run:4,485passed,1,690skipped,24,690passing subtests; three MISRA mutation subchecks initially failed because sandboxed setup could not access the existing uv cache. Offline setup dry-run outside the sandbox showed no dependency changes; isolated canonical MISRA rerun then passed all three subchecks (`misra-mutation-final.log`:1test/3subtests). The broad run was not rerun merely to combine those separate green receipts.
-Changed production files pass parent/child ty checks; changed source/tests pass Ruff and whitespace checks.

Initial environment/registration/test-isolation failures remain preserved. No failing code or unaddressed review finding remains in the checked scope; hardware/road limitations below remain.

## Remaining boundary

No ARM/AGNOS build, device boot, real alert presentation, powered Park acceptance or road smoothness proof in this task. The paired runtime integration removes the research-adapter installation blocker, but a separate authorized device staging/build/backup and acceptance step remains necessary before activation. The separate precharge-only prototype is not included. No settings changed on the Comma.

## Exact paired source

- openpilot `e9ddc7668eb996f8c0912004facd66aed9206072`
- opendbc `d2e8d0404143da0f2685c2ff4932b9b9f702951f`
- Branch in both: `codex/navigator-tracking-release`; parent gitlink verified, both checkouts clean. Local commits only.
