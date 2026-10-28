<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Brake/propulsion handoff local spike

October23,2026, America/Chicago. **Local prototype and scoped replay checks passed; not integrated, installed or road-ready.** Exact paired source remains24e981d6d/01f32a6f, clean and unchanged;1.20/0.97 retained. No Comma access or active ECU queries.

## What was built

A report-local pure state machine and source-copy injection into the current production Ford controller. Inactive/braking/stopping/invalid pitch withdraw propulsion; brake-clear qualification precedes resumption; positive valid propulsion rises with an explicit bound, while reductions and renewed braking withdraw immediately. Sentinel−5 is treated as inactive, not interpolated as an acceleration. This removes valid propulsion while active brake deceleration is requested, without changing any brake demand, creep/pitch compensation, existing latch, brake jerk limit, precharge/deceleration/stop bits, predicted acceleration, target speed, safety code or steering.

Exploratory main setting:0.5m/s³ positive propulsion-request rise and20ms elapsed brake-clear qualification. Nine combinations sweep rates0.25/0.5/1.0 and qualifications20/60/100ms. These are explicit experimental choices, not OEM-derived calibration or a recommended vehicle tune. The limiter remains active on positive increases; a low target cannot end the limiter and permit a large next-sample jump.

See [design](DESIGN.md), [spike plan](PLAN.md), [helper](../../navigator-reference/PRIVATE_ARTIFACTS.md), [current-controller seam](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Checks completed

- Test-first helper reproduction captured before implementation: missing helper caused the expected red import. Ten helper cases then pass; five current-controller test groups bring the total to15passing tests. Grade/controller group covers20speed/pitch combinations and11settled demands each, alongside restart, disengagement, missing/NaN pitch and two other Ford/OEM parity cases.
-90,000 deterministic randomized helper updates across nine parameter combinations pass finite/bounded output, mutual exclusion, immediate withdrawal and positive-rise invariants, including timestamp reversals/duplicates/gaps, invalid targets, pitch availability and repeated brake/stop transitions.
- Original Alpha frozen-input replay compares baseline, old simple withdrawal and nine stateful configurations: **2,984ACC outputs per variant**, all pass the current native debug TX hook. Every candidate difference is confined to propulsion. **3,889non-ACC outputs per variant remain identical for these reconstructed inputs.** Existing permission checks reject active braking with controls disallowed and allow neutral disengaged output.
- Baseline has751brake+valid-propulsion frames; simple withdrawal and all nine stateful variants havezero. This is command mutual exclusion, not proof that actual positive engine torque and brake torque never overlap.
- Main variant changes803propulsion frames:751baseline braking frames plus52other positive-request reductions with brake clear. Wire positive slew between valid requests peaks0.5m/s³ versus baseline1.5in this sample. Sentinel transitions are excluded from that physical-unit calculation. Brake output and bits remain identical. Exact reasons/counts are in results.json; qualification and ramp counts may overlap reduced-request counts and must not be added as independent events.
- Parameter tradeoff: rate0.25 variants reduce positive brake-clear requests in115–122frames;0.5 variants52–60;1.0 variants26–35. More smoothing adds command lag. Quantization makes0.25internal-rate wire increments reach0.5m/s³ on individual50Hz samples. No preferred vehicle calibration selected.

[Scoped replay results](../../navigator-reference/PRIVATE_ARTIFACTS.md), [tests](../../navigator-reference/PRIVATE_ARTIFACTS.md), [test-first red](../../navigator-reference/PRIVATE_ARTIFACTS.md), [helper green](../../navigator-reference/PRIVATE_ARTIFACTS.md), [replay log](../../navigator-reference/PRIVATE_ARTIFACTS.md). Prior [saved OEM investigation](../navigator-longitudinal-current-baseline-2026-10-23/REPORT.md) supplies35segments/39,992eligible commands/8,562braking samples and varying release behavior. Those OEM records remain observation/reference data, not newly simulated vehicle response.

## Independent review and input provenance

An independent reviewer ran all15tests and found no material correctness issue within the offline scope. A replay-provenance finding was resolved: replay now re-extracts inputs fresh from the original recording, checks raw hash before/after and records canonical extracted-data, extractor/LogReader/schema hashes and event counts. A fresh replay reproduced the same counters; reviewer confirmed the finding resolved. [Review record](REVIEW.md).

## Remaining blockers and what this does not prove

**Small-positive restart remains blocked by the original brake latch.** At standstill after braking, a sustained+0.2request still leaves braking latched and propulsion inactive. A flat-road+0.31request releases it; negative pitch compensation can raise the effective required raw request. The prototype deliberately does not clear brakes by timer or weaken the original braking decision. Passing the test that demonstrates this blocker does not mean a successful restart.

The exploratory rate can also delay acceleration: a hypothetical0→2m/s² valid request needs about4seconds at0.5m/s³, plus qualification. That may be unacceptable for some driving and is not justified by the small Alpha recording. Urgent acceleration, lower-speed launch and different grades need explicit design/validation. Reductions remain immediate; comfort improvements cannot be traded against response safety.

Other unresolved issues: precharge-only selection versus active deceleration, actual hydraulic release/propulsion torque response, valid/fresh pitch provenance and full controller/context freshness, nonfinite upstream pitch before the helper (e.g.infinity can raise in the unchanged baseline math), production lifecycle/reset policy, sustained low-speed behavior and physical shaking outcome. The source-copy seam is not production integration.

Replay uses selected recorded control/state fields and a synthetic100Hz schedule, explicit historical initial accel/latch seed, latest preceding state without lookahead and no vehicle feedback simulation. One early control without past state is skipped. Original recording has2,983outgoing ACC messages; the constructed schedule has2,984. No exact-original-wire, complete native RX/forwarding/permission replay, full contemporary steering-calibration-context replay, fresh ARM build, road benefit, fuel savings or OEM equivalence claim. Native Mac debug hooks are unsanitized. No public-road/highway test is cleared by these results.

## Next work and driving guidance

Next local work is a brake-release/restart design with explicit feedback/freshness/grade assumptions and an acceleration-response budget, before any paired integration. Evaluate precharge independently and retain brake authority. A fitted response/closed-loop validation needs data beyond these counterfactual commands. Full native RX/TX and retained steering regression/build gates follow actual integration.

**Keep Alpha OFF and OEM ACC ON for now.** That collects comparison drives, not prototype tests. Only a later reviewed installation plus verified Alpha enablement exercises openpilot gas/brake actuation. The current UI exposes Settings→Developer→openpilot Longitudinal Control(Alpha), warns about possible AEB disablement and requests reinitialization; do not turn it on now to test code that is only local. Current upstream planning uses Autospeed rather than the former Experimental toggle.

The [testing and OEM comparison plan](TEST_DRIVE_PLAN.md) explains later parked activation/rollback, controlled low-speed-first progression, comfort/response/vibration/torque/fuel measurements and stopping criteria. No80–85mph reproduction is needed. Smooth commands cannot guarantee no shaking, and fewer conflicting commands cannot establish fuel savings.
