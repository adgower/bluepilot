<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Separate coast/precharge/brake prototype — October 23, 2026

## Verdict

The requested local prototype and saved OEM/Alpha replay are complete. **Separate states alone do not resolve the observed Alpha cycling. Do not install this spike.** It reduces actual-braking command exposure, but merely delays the same brake entries. Pitch/gravity decision consistency remains the next investigation. No calibration offset was applied or learned here.

No Comma access, CAN queries, paired source modifications, push, integration or activation. Clean paired heads remain parent `ffebc43497f8015c37be5927800832f2719c7dca` / child `0ac9618972dd580281c5e933c7990f186522fbd4`; owner 1.20/0.97 unchanged. All changes are report-local Python/docs. The prototype is not a deployable patch.

## Prototype

`allocation.py` distinguishes actual braking from precharge. The report-local controller factory (`replay.py`) retains independent shadow baseline brake/release history and the installed propulsion Handoff. Split-bit packing occurs only in an in-memory fordcan proxy. Existing brake-free slowing/coast is retained, rather than forcing inactive propulsion from a negative acceleration sign; OEM shows that negative requested acceleration can still require positive engine torque.

New weak entries (-0.12 < pitch-adjusted net < 0m/s²), with positive planner intent >0.02m/s², valid pitch, PID phase and speed >=3m/s, first request precharge. Persistent demand admits actual braking after a nominal120ms qualification or0.006m/s signed demand debt. Actual braking forces propulsion inactive. Negative planner demand/strong braking, existing actual brake hold, low speed, stop/restart and invalid data/timing use the installed brake decision. Precharge is actuation, not a promise of zero hydraulic brake torque.

Initial test-first run caught missing precharge/disengagement behavior (four failing contracts). A subsequent failing recovery contract caught actual braking being started merely because net demand crossed positive while shadow braking remained latched; the bounded precharge state now continues through that recovery. The first replay and native results remain under `first-pass/`. No search over larger delay bounds or imported EV thresholds.

## Alpha actual-send-slot replay

23 saved segments,65,736 ACC slots, same SHA-256-verified full-rate input cache as the prior cycling investigation. Fresh baseline reproduces the earlier baseline stream hash `76e9a328104be225c1a72b0a87be25df3501b1c2d3ec5826456c7d1abba22130`. Reconstructed baseline matches recorded bytes on63,132/65,736slots (96.04%); unknown internal receive order/frame phase remains a fidelity limit. Compare candidate against reconstructed baseline, not directly against recorded packets as though they were identical.

| Eligible active/no-pedal/>5mph measure | Baseline | Candidate |
|---|---:|---:|
| Actual brake edges |213|213|
| Precharge edges |213|213|
| Actual-braking slots |13,411|12,822|
| Precharge-only slots |0|589|
| Valid propulsion slots |16,467|17,056|
| Brake/precharge-free mild-negative propulsion slots |387|387|
| Brake/precharge-free inactive propulsion slots |183|183|

The589changed packets differ only in propulsion request and actual-brake bit. Precharge bit and brake acceleration are unchanged. This is4.39%less actual-brake-command exposure, **not4.39%better ride or reduced physical brake use**. Coast-state counts do not increase. Highway worst20s window remains33brake edges; low-speed worst20s remains24. By speed band, edges are unchanged:5–15mph4,15–25mph56,25–35mph34,35–50mph31,50–70mph79,70–85mph9. The last band is not85mph evidence; original Alpha drive maximum was73.94mph.

Zero changes while inactive, below3m/s or in stopping/starting; zero suppression when raw planner intent <=0.02 or net braking <=-0.12. No simultaneous actual brake/valid propulsion. Every non-ACC packet hashes identically to baseline, so steering commands are unchanged in this replay. Brake acceleration is identical at every slot.

**Timing blocker:** nominal120ms qualification is evaluated at discrete recorded send slots. The longest observed precharge-instead-of-braking interval until the next actual command is147.97ms. Do not describe this as a guaranteed120ms physical delay bound. A deployable design needs deadline/packet-timing treatment; making a longer delay to remove edges would not be an acceptable fix.

## Saved OEM replay

35 previously hash-verified segments/five OEM routes,40,544eligible received OEM commands. Every selected command's active/brake/precharge/propulsion/brake-acceleration/stopping fields round-trips through the pinned CAN packer/parser without mismatch. This is a selected-field encoding replay, not full original packet equality.

Observed states:3,032inactive-propulsion/no-brake/precharge;3,371mild-negative propulsion/no-brake/precharge;1,610precharge-only (1,605with valid propulsion);8,674actual brake;23,857remaining drive. This proves the split representation fits the saved OEM states.

OEM logs do not contain an Alpha planner command. A separate, explicitly labeled surrogate run uses valid OEM propulsion request, otherwise OEM brake acceleration, as planner intent and recorded pitch to exercise the allocator. It changes one OEM brake sample to precharge, adds no brake requests, and preserves known OEM precharge input. This is not proof of Alpha comfort or closed-loop equivalence to OEM. No sensor calibration was estimated from this replay.

## Verification

-13allocation contracts pass after observed RED failures and fixes (`allocation-tests.log`).
-886Ford/native regression tests and12,083subtests pass;79skipped (`ford-tests.log`, `ford-tests.xml`). These use the in-memory candidate controller, not an installed patch.
-One parent plant/coordination contract passes (`parent-contracts.log`); it does not recreate the owner's road/grade response.
-Fresh native ACC-hook replay:5,260,361recorded RX packets per variant,65,728ACC TX slots after logged Ford safety configuration. Recorded/baseline/candidate each have the same three rejected ACC packets at driver-pedal/permission boundaries; **zero added candidate rejections**. No forced controls permission or relay faults. Uses retained debug Mac safety binary; only ACC TX hooks exercised, no physical hardware or full lateral/forwarding/heartbeat replay (`rx-results.json`). Eight earlier slots are excluded before the logged Ford11 configuration.
-Source hashes recorded; paired trees clean before and after. No ARM build, device/parked checks or physical validation was performed or claimed.

`comparison.json`, `replay-baseline.json`, `replay-candidate.json`, `oem-replay.json` and their logs hold detailed results. Private drive rows remain outside the repository.

## What this settles / next work

Keep separate command states in the eventual design, but this bounded transition change is insufficient. It retains the same oscillating brake decision and precharge edges, which could still feel rough physically. The prior relative gravity offset remains a hypothesis, not calibration: next compare independent saved OEM motion channels/grades, establish which signal owns the offset, then prototype a validity-gated, bumpless mapping consistent with integral demand. Only then reevaluate state allocation, actual actuator release, urgent braking and stop/restart. No new Alpha road trial is justified by this spike.
