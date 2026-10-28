<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local integral, actuator feedback and fallback coordination

October23,2026. The report-local software policy is implemented and replayed. **No paired-source integration, device access, CAN queries/transmission, calibration/settings changes, push or installation. Owner1.20/0.97 remains unchanged.**

## Outcome

The prototype now has a concrete parent/controller feedback contract, directional integral inhibition during deliberate propulsion limits, measured brake-release qualification, conservative brake-only demand handling, and explicit latched disengagement on required-data failure. Reference withdrawal is slewed; stop/creep behavior and default-off parity are tested. This addresses the local software-policy gaps. It does not establish physical Navigator comfort or make the research adapter deployable without runtime integration/build/alert plumbing.

The full parent-in-the-loop saved-drive replay produces **221→63eligible brake transitions**, with1,458positive integral updates inhibited during a deliberate release/ramp cap. It recomputes the real LongControl against recorded vehicle acceleration and a command-consistent modeled brake-release channel. Those are not observed road results. Separately,288closed-loop response-model scenarios have no faults;212improve acceleration tracking, and none are worse by more than10%under the stated model assumptions.

## What changed

### Integral: acknowledge actual command limits without resetting I

`parent_class()` in`experiment.py` adapts the actual current LongControl source in memory. Ki remains0.5and all other stock tuning/limits remain. The existing PID freeze input is used only when:

- Feedback is fresh, from the same engagement epoch and an already-produced control sequence.
- The controller is deliberately waiting for brake release or limiting its propulsion rise; actual braking is not active.
- Current demand is positive, target acceleration is nonnegative, and positive error would push the integral further into the cap.

Negative error may unwind normally. Genuine deceleration/actual braking may still integrate; a blanket brake-state freeze could deadlock grade release. There is no integral rebasing or step. Invalid/stale/foreign feedback is ignored in favor of stock integration, never reused as a current cap. Feedback contains timestamp/epoch/sequence, request, granted gas, brake state, limit/fault/validity fields. Its immutable JSON transport round-trip is exercised between the local parent and controller. This is an explicit software interface, not an already-wired production IPC schema.

### Actuator release: clearance is observed, never granted by a timer

After an actual moving-speed brake request, require three distinct fresh ECU brake-torque samples <=4Nm spanning>=40ms before valid propulsion returns. A repeated cached sample cannot qualify. Stale/future/invalid/out-of-order torque cannot rearm permission. Existing0.5m/s³ propulsion-rise behavior remains after clearance; no torque-to-acceleration or fuel-efficiency mapping is invented.

The first500ms fault deadline failed an original-command episode near20mph. Reported brake torque remained60–90Nm for roughly0.7s after the brake bit cleared while the original controller resumed propulsion. Independent settled OEM commands have25,552samples with maximum reported torque0Nm. This is **not** evidence to raise the clear threshold and ignore80Nm. The revised1s deadline keeps waiting for measured clearance and requests disengagement if release fails. Elapsed time alone never enables propulsion. The final observer passes the complete original-command trace without a fault (`recorded-command-observer.json`). The initial failure is preserved under`before-release-tail/`.

This channel is ECU-reported torque, not a calibrated brake-pressure/force instrument. The160Nm value in response models is only a binary above-threshold marker; it is never converted into force or acceleration. Unknown physical sensor semantics remain a hardware-validation limit.

### Fallback and re-entry

Missing required pose or release feedback, clock discontinuity and release timeout produce a latched fault. The controller adapter sends neutral longitudinal fields; the parent resets via inactive LongControl rather than accumulating I. Fresh data cannot silently rearm while the owner still requests assistance. A genuine off/on generation change is required; old-generation acknowledgements cannot unlock the new episode.

The source keeps requested ownership separate from granted output. Failed assistance coverage is counted explicitly. Static-reference loss slews the correction toward zero; stop/creep uses zero correction and preserves the static estimate for continuous3–5m/s fade on moving re-entry. Below3m/s uses the installed release policy so the new moving-speed gate cannot create a standstill launch deadlock.

The enabled tests also found that a positive grade correction could delay the brake bit relative to the installed controller during a strong negative request. Demands below Ford's existingMIN_GAS bound now keep at least the installed conservative brake-decision gravity. This does not remove or change the installed3.5m/s³ brake-acceleration slew; the new layer adds no onset delay in the urgent-request regression.

## Replay scope and results

All58source rlogs were freshly SHA-256 verified:35OEM segments/five routes and23segments in the actual Alpha drive. Reproduced context arrays include all66,278brake-torque observations and24,521plans, with past-only timestamp joins and ordering assertions. Parent replay uses128,549updates and has zero missing-plan active updates. Reconstructed baseline raw demand has0.005105m/s²RMS error versus recorded demand and0.000329median error. Controller reconstruction retains96.04%recorded ACC-byte agreement; original internal ordering/call phase is not exactly reproduced.

| Test | Baseline | Candidate | Interpretation |
|---|---:|---:|---|
| Frozen requests, modeled152ms release: brake edges |213|77|Actual65,736send slots, recorded vehicle response |
| Recomputed parent, modeled152ms release: brake edges |221|63|Real integral recomputed; vehicle response/planner still recorded |
| Parent highway20s window |35|0|Command/model result, not physical lane/ride proof |
| Parent low-speed20s window |28|0|Same limitation |
| Frozen-request highway/low windows |33/24|4/2|Comparable to earlier frozen-request prototypes |

Each variant processes65,736actual ACC slots. Default-off is exact wire parity. Every non-ACC hash matches across all six variants. In the frozen-model comparison, inactive/below3m/s/stopping/starting packets are unchanged. No actual-brake/valid-propulsion overlap is generated. The recomputed-parent variant intentionally changes acceleration requests as I changes; do not claim brake-acceleration parity for that variant.

The **changed-command replay using the old observed actuator trace** faults first at611.969s and contains27,549faulted slots. Its27remaining eligible brake edges are **not an improvement score**. Those observations followed the old commands and cannot predict brake release after newly different commands. This limitation is separated from the now-passing original-command observer check. Both observed-feedback and command-consistent modeled-feedback outputs are retained. `comparison.json` reports faults and coverage alongside edge counts.

OEM longitudinal remains factory controlled:40,544selected OEM commands pass default-off policy and selected-field encoding parity, including precharge-only states. This is not counterfactual Alpha operation on OEM routes. The prototype retains the paired packer's current brake/precharge coupling; the earlier separate-precharge spike was not imported wholesale.

## Closed-loop response stress tests

`response_scenarios.py` runs the real parent and controller with simulated acceleration fed back into the integral. It uses two recorded20s acceleration-target trajectories,0.081/0.152/0.3/0.7sbrake-release delays,0.15/0.5sacceleration time constants,±0.3m/s²grade cases,0/0.04m/s²attitude disturbance and±0.06m/s²relative-zero uncertainty. There are288cases/1,152,000controller updates across baseline and candidate.

-212cases improve acceleration-tracking RMS; none worsen by more than10%.
-Median modeled RMS:0.09875→0.05989m/s².
-Zero modeled fault frames; all command-overlap assertions pass.

These are generic uncertainty/stress models. Coast is assumed-0.25m/s²minus grade, delivery delay100ms, acceleration response first-order, and the mid-drive static reference is prequalified. Sensor start/re-entry is tested separately. This is not an identified Navigator dynamics simulator, perception/lead replanning, stop-distance/road/fuel validation or proof of better-than-OEM behavior. Engine/brake force and tire/grade ground truth are not identified by this work.

## Verification receipts

-30new contracts pass, including actual-parent I behavior,4,000step exact stock-parent parity, enabled release/fault/urgent-brake paths, stop/creep parity and a regression for the real0.7srelease tail. RED failures and corrections are retained in logs.
-Full retained Ford/native compatibility suite:886tests/12,083subtests pass,79skips. **This suite runs the feature default-off**; enabled behavior is covered by the new contracts, recorded replay and response scenarios. Do not conflate the two.
-Native ACC-hook replay uses all5,260,361recorded RX packets per variant and65,728TX slots after logged Ford11configuration. For both modeled streams, recorded/baseline/candidate retain the same three pedal/permission-boundary rejects, zero added rejects. Final modeled wire hashes match those exact native-tested streams after the brake-priority/deadline repairs. The final observed-feedback stream is replayed separately; its neutral faulted output adds zero rejects (candidate0versus baseline3, which reflects lost assistance coverage, not improved safety).
-No forced controls permission; no relay faults. Retained debug Mac safety binary, ACC TX hooks only—not full lateral/forwarding/heartbeat/hardware safety validation. Eight preconfiguration slots are excluded.
-Source/cache hashes and clean paired heads are verified in`acceptance.json`; no new ARM build/device/parked or physical checks.

## Status and next integration boundary

Local policy, interface and replay work is complete within the stated evidence limits. Parent/child remain clean at`ffebc43497f8015c37be5927800832f2719c7dca` /`0ac9618972dd580281c5e933c7990f186522fbd4`. The local candidate is default off; no on-device parameter or UI was created.

Paired integration must wire the explicit producer timestamps/owner epochs/feedback into real runtime messages and connect the latched fault to the normal driver-visible disengagement path. The in-memory neutral-output adapter must not be installed alone without that alert/state plumbing. Then run paired builds and integration checks before any separately authorized device stage. Physical performance remains unproven; there is no reason to hard-code a global camera-pitch reset or change steering1.20/0.97.
