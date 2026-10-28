<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Brake-release timeout investigation and local prototype

Started October 23; continued October 24, 2026. **Report-local prototype only. Final historical safety replay completed successfully with no added rejection.** Paired branches, device, firmware and settings are untouched. Parent `9590ea8fd`, child `d2e8d040`; owner **1.20/0.97** retained.

## What caused the recorded fault

The new event at 41.45 mph / <private clock time> CDT is `release_timeout_disengage`, with healthy 77.70 ms pose data. Received torque remains 136–388 Nm across 52 distinct fresh samples during the 1.020 s release wait; latest torque is 156 Nm, 2.25 ms old. Neither pedal is pressed. The existing guard correctly withholds propulsion and requests disengagement when clearance is not established.

Tracing the command before the wait exposes a specific admission problem:

| Relative to fault | Recorded paired-controller behavior |
|---|---|
| −1,157 ms | Raw planner acceleration is +0.30177 m/s². Compensated decision dips to about **−0.00118 m/s²** for one update; braking latches. |
| −1,140 ms onward | Compensated demand is positive again, but hysteresis/release qualification retains the brake command. |
| −1,020 ms | Brake/precharge command releases after roughly **140 ms**; clearance wait begins. |
| 0 ms | Reported torque is still 156 Nm; the existing one-second deadline requests disengagement. |

The old torque response cannot prove the physical result of deleting the pulse. It belongs to the original brake command; torque first clearing after disengagement does not establish safe clearance under continued ownership.

## Prototype

Only a **new, mild compensated-braking edge** may be qualified: raw planner intent >+0.02 m/s², net demand between about −0.05 and 0, coordinated Navigator PID ≥3 m/s, previous brake false, already qualified clearance, valid context and fresh measured torque ≤4 Nm.

During qualification the command **coasts with propulsion withdrawn**. Sustained mild demand qualifies after 40 ms, or sooner at a 0.002 m/s negative-command exposure limit. Tiny positive crossings credit exposure rather than resetting it indefinitely. Stronger braking, nonpositive planner intent, existing braking, missing clearance, invalid input and stop/creep paths bypass qualification. Tests verify discrete delivery latency and command exposure; these are not physical speed/trajectory bounds.

The clearance observer also revokes prior clearance when unexpected reported torque appears, and faults on stale/invalid/reversed feedback. The original three distinct clear samples over ≥40 ms and the **one-second release deadline are unchanged**. Thus a removed command does not become permission to accelerate against old, non-clear feedback. Coast limitation is serialized in feedback so the existing directional integral inhibition still applies.

All changes live in `admission.py` and an explicitly transformed **in-memory** controller in `experiment.py`. No paired production files are patched, committed or installed.

## Completed evidence

- Test-first failures retained for the actual tiny pulse, sustained braking, unexpected torque, alternating demand and reversed feedback. **40 focused contracts pass**; a fresh reviewer independently passed the initial 22-case set and found no blocker.
- In the exact recorded pre-fault command sequence, the baseline emits seven brake-command slots while the candidate emits none for the triggering pulse; one qualification/coasting slot replaces its onset.
- **54 explicit actuator-response episode models:** baseline faults in 17 modeled cases, candidate in zero; triggering brake slots 378→0. These use synthetic precleared entry and arbitrary command-dependent lag/release shapes, not identified vehicle mechanics. Ownership is not extended past the original fault.
- **288 parent/controller response scenarios:** zero candidate modeled faults; 25 tracking improvements, none >10% worse; median error unchanged. This is narrow improvement evidence, not general Alpha smoothness or fuel proof.
- Retained 65,736-slot command/model streams: frozen modeled brake edges **77→69**, coupled-parent modeled edges **65→65**. Both modeled variants have zero faults. Full default-off ACC and non-ACC hashes match exactly.
- Mixed new-command/old-observed-response streams deliberately retain faults: baseline 27,549 fault slots, candidate 32,505. They are **not** used to score braking-edge/ride improvement. Candidate clearance protection is more conservative when old torque appears without the now-suppressed command.
- Matched retained native replays process 5,260,361 RX frames / 65,728 ACC slots per variant, with no added rejection. Modeled runs share three recorded pedal/permission-boundary rejects. No controls permission is forced.
- Full child/native suite with the process-local candidate controller: **4,485 passed, 1,690 skipped, 24,693 passing subtests**. The Mac debug hooks are unsanitized; no UBSan/ARM result is implied.

- The final frozen-source **51-segment active Alpha replay** passes native rejection comparison: 11,903,572 RX / 352,930 TX per variant, 31 shared recorded rejections, zero added rejection or relay fault. All **57,931** fixed-input inactive/stop/creep packets match exactly. Paired baseline has one release-fault slot and candidate two earlier/adjacent fault slots in the same recorded episode, because the old torque response remains non-clear.
- Additional **72 high-frequency response cases** at 3/8/16 Hz: zero modeled faults; 33 better tracking cases, none >10% worse. Total response coverage is 360 generic cases / 1,440,000 controller updates, separate from the 54 pre-fault episode models.
- The **canonical full parent suite** passes: 1,029 passed, 87 skipped, one expected failure, 281 passing subtests. This protects unchanged parent code; it is not a full in-memory candidate/process-replay integration result.
- Fixed-input retained exclusions match in 36,088 slots. In coupled-parent modeling, changed integral history produces 2,447 low-speed/stopping acceleration-payload differences, maximum **0.0078 m/s²**. Gas, brake flags and wire engagement remain identical there, with zero modeled faults. Thus coupled stop packets are not claimed byte-identical.

The historical **1,066-segment / 75-route** lateral/native regression passed: 244,237,412 physical RX frames, 3,966,453 generated TX frames per variant, 412 shared rejections, zero added rejection, phase/counter mismatch or protected-scope change. See [full summary](../../navigator-reference/PRIVATE_ARTIFACTS.md). Historical regression exercises the opt-out/protected controller behavior; active longitudinal behavior is exercised by the separate Alpha/native and modeled tests.

The historical replay retains 412 shared rejections (364 button, 48 steering), 861 generated frames before Ford configuration excluded from TX-hook evaluation, and 74 shared invalid-configuration ticks. It also records 11,493 baseline-versus-recorded active-angle reconstruction mismatches across 490,096 comparisons. The result is a comparative regression with no added prototype rejection, not an exact reproduction of every original on-road command or a claim that every generated packet was accepted.

## Important retained fault

The saved torque still rises after the pulse is suppressed in the **frozen-feedback** replay. The candidate therefore reopens clearance and still disengages, about one callback earlier in that same episode. This is not counted as physical resolution of the timeout. The experiment addresses the unnecessary command that plausibly causes the long release obligation while preserving a fail-closed response to non-clear torque.

Physical confirmation remains necessary to establish whether avoiding this pulse prevents the vehicle's brake-torque response. Do not interpret the modeled 17→0 result as a demonstrated road fix or extend the timeout based solely on post-disengagement data.

## Harness corrections retained

The custom parent-suite runner initially omitted PYTHONPATH for isolated subprocess tests; `test_actual_producer_card_motion_and_invalid_calibration_release` and `test_production_parent_card_pipeline` pass after correcting that environment. Custom whole-parent substitution attempts also reported `TestMessaging.test_recv_one_retry` and stalled at the unrelated forked Toyota radar replay (`TestLeads.test_radar_fault`). Those attempts are retained and not used as validation. The radar test passed canonically in isolation; the complete canonical parent run then passed. Process-local candidate controller behavior is covered by the full child suite, focused contracts and actual candidate native replays; a future production integration must rerun actual parent/process-replay checks. A retained native comparison initially paired an observed-feedback baseline with a modeled-response candidate, producing the three already-recorded pedal-boundary rejects as apparent additions. It was corrected to compare matching response modes; failed attempt logs remain available. Neither repair changes prototype policy or weakens replay assertions.

No SSH, active ECU query, CAN transmission, push, commit, device reboot or activation occurs in this task.
