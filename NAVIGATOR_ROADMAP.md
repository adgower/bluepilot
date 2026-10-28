<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator project roadmap

Last updated October 28, 2026. This is Alex's main planning reference for the Navigator work across openpilot, opendbc, and BluePilot. Status reflects the last documented checks, not continuous device monitoring. The [feature inventory](docs/research/navigator-branch-feature-list.md) holds implementation details and commit references.

## Main reference guide and document catalog

Start with the [tuning and development guide](NAVIGATOR_TUNING_GUIDE.md) for the complete working process, current baseline, lateral/longitudinal lessons and evidence limits. The [full catalog](docs/research/NAVIGATOR_RESEARCH_INDEX.md) indexes all saved research/design documents; the [documentation audit](NAVIGATOR_DOCUMENTATION_AUDIT.md) explains coverage and remaining gaps. Historical status entries below retain their original dates.

## Latest saved-drive review — October 28 (unchanged installed source)

[Drive report](docs/research/navigator-returned-drive-review-2026-10-28/REPORT.md): three newly retrieved recordings / 29 segments from <private clock time>–<private clock time> local retain installed e05e42f43 / 5097b993, Alpha ON and 1.20/0.97. No recorded controlsMismatch or coordination faults. Pulsing remains: a 61–62 mph 15-second window has 17 brake-bit changes; a 24–26 mph city window has 11. The owner reports one high-RPM incident; a likely <private clock time> match has decoded peak 4,362 RPM in reported first gear, with target changing toward second and no pedal/brake/precharge. RPM quality remains unresolved.

A 3.25-second rising-demand episode near 15–17 mph achieves about 53% body/request and 51% wheel-model/request before steering input. Modest excess is present descriptively at 50–65 mph, but no episode passes the stronger uncertainty-qualified coherent-excess screen. Driver inputs remain candidate interventions, not confirmed failures. No 70–85 mph evidence was added. The new analysis separates inactive propulsion from ordinary brake-clear engine requests; earlier frozen coasting labels are not reused as quiet-coast authority. Originals are checksum-verified and privately archived. No new tuning or device changes.

## Post-clear rebraking — October 28 (local diagnostic rejected)

[Combined report](docs/research/navigator-postclear-rebraking-2026-10-28/REPORT.md): the 13 received-clear/rebrake pairs split into five pitch-proxy dominated, four integral dominated, three planner dominated and one without an intervening released callback. All four integral-dominated pairs have negative average target-minus-actual acceleration; clearing I is not justified. The OEM/Alpha pitch ranges overlap; no sensor defect or physical coast authority is established.

A fixed bounded grade filter passes 14 focused software tests but fails the fresh 21-segment coupled replay: brake-bit changes 280→246, full-brake exposure +9.816 s, combined exposure +11.129 s, and 218 stronger-demand rows one encoding increment weaker (maximum 0.0039 m/s²). Changing release timing alters integral freeze behavior and persists after strong-demand bypass. Changed-reference omissions against locked original accounts are unsupported. The separate eight-segment city control is identical (17 changes), not improved. No full 316-segment expansion or integration is selected. Paired branches, Comma and 1.20/0.97 remain unchanged.

## Maneuver brake-release validation — October 28 (local; pulsing remains unresolved)

[Combined report](docs/research/navigator-maneuver-release-validation-2026-10-28/REPORT.md): the complete current clearance chain qualifies three clean moving maneuver releases after 1.560–1.584 seconds without timeout. Status clear precedes reported torque clearance; keep measured qualification. Eleven other negative-reference windows are stopped/creep, interrupted or held and remain censored.

Fresh road-window analysis preserves 14/15/12 brake-bit edges. Five of 18 release/rebrake pairs lack a new received clear sequence, while 13 have one; only two have positive reported torque at rebrake. A release-delay change alone does not explain all pulsing. The low-speed tests do not identify highway quiet-coast/grade authority. An offline observer and 10 focused tests are retained; no controller change is selected. Existing suite: 210 passed, one native test failed to load macOS UBSan; the separate unsanitized native permission contract passes. No device or paired-source changes; 1.20/0.97 preserved.

## Maneuver evidence recovery — October 28 (local; blockers remain)

[Combined report and verification](docs/research/navigator-evidence-recovery-2026-10-27/REPORT.md): the expanded bounded inventory covers 1,669 original segments and recovers two genuine longitudinal maneuver sessions (20 completed-session segments and 22 partial-session segments). Clean repeated low-speed PID braking provides usable reference-response evidence. Command/status clearance still precedes measured torque clearance; highway coast authority remains unidentified. No lateral maneuver execution was observed in this retained set; recording gaps and missing parameters remain unknown.

The pre-action steering bias refinement worsened held-out moving-target RMSE from 1.016 to 1.171 degrees and was rejected. Next work can build source-bound PID/release fixtures from the recovered longitudinal tests; neither a new allocator nor a validated steering response provider is ready. No integration, device changes or new full controller replay; paired sources and 1.20/0.97 are preserved.

## Response-state resolution — October 27 (local fixes; control blockers remain)

[Combined report and verification](docs/research/navigator-response-resolution-2026-10-27/REPORT.md): joint brake/authority transactions and a one-outstanding steering correction were prototyped locally. The brake focused replay adds about 0.888 seconds of braking and weakens 212 encoded strong-request rows, so it is rejected. Its causal chain identifies mode-dependent integration/freezing after the initial correction.

Steering resolves prior synthetic delayed/quantized counterexamples and respects the selected deviation constraint, but the fresh 21-segment replay has three trials and zero response associations. A separate 14-test revision fixes the exact target-basis bug and receive/quality contract; it has no raw replay or validated moving-reference provider. Neither version is selected for integration; no new full 316/737-segment candidate run is claimed after failed focused gates.

Original-data models establish predictive value but not the needed directional authority or two-prefix steering discrimination. The next prerequisite is validated response/timing support (existing maneuver records or a separately authorized controlled-identification plan), preserving clearance and stronger-braking gates. Comma, paired branches and 1.20/0.97 remain unchanged.

## Remaining pulsing and tracking prototypes — October 27 (not selected)

[Local investigation and replay](docs/research/navigator-remaining-control-prototypes-2026-10-27/REPORT.md): full longitudinal comparison covers 316 unique segments / 23 routes; full steering/controller/native comparison covers 737 unique segments / 42 routes. Both bounded initial prototypes leave commands unchanged, so neither is a demonstrated treatment. Device and paired branches remain unchanged, including 1.20/0.97.

The pulsing trace identifies the narrow effective release/reentry band and exhausted coast allowance. Next work must build on existing response-model evidence and address mode/authority/integral dynamics without reopening budgets or weakening measured clearance. A separate angle-led steering prototype reduces relevant saved commands but fails quantized-delay stress tests; a correction-only hold also fails a later stress case. It was stopped before full replay, rather than presented as ready. The next lateral blocker is an explicit delayed/quantized feedback-state design, not a global gain change. No new prototype is installed or approved for integration.

## Post-install road review — October 27

[All-range road evidence](docs/research/navigator-post-regression-drives-2026-10-27/REPORT.md):79new segments archived and verified; only one new-source session provides meaningful assisted driving. No controlsMismatch or active pose-freshness fault recurred on that drive. This does not guarantee permanent resolution.

Pulsing remains at40–70mph, including14brake-request changes in15s with positive planner/producer demand. Moving5–40mph exposure is only69.94s, insufficient to establish a cure. Brief bounded true-coast activation is confirmed; physical comfort improvement remains unproved. Next local priority is allocation/integral/actuator-response reconstruction.

The driver-confirmed49mph input was a planned move into a newly added rightmost lane for an exit, excluded as problem-takeover evidence. Independent40–45mph steady tracking remains about15% above request in25.25s of selected samples;45–50mph has only4.65steady seconds after maneuver exclusion. These are tracking observations, not demonstrated lane crossing. Retain local target/unwind and60–70mph quiet-demand review. No new-source70–85mph coverage exists. Device/source/settings remain unchanged, including1.20/0.97.

## Regression repair active — October 27 (offroad and powered Park checks passed)

[Completed installation and checks](docs/research/navigator-regression-repair-staging-2026-10-27/POWERED_ACCEPTANCE_REPORT.md): exact `e05e42f43` / `5097b993` is active. Verified fresh68parameter device/Mac backup and whole-install rollback retained. Ignition-off and55s powered Park checks passed:20Hzbig model,0drops,all telemetry valid, no observed coordination/mismatch/board faults or new blocked transmissions; assistance remained disengaged.

Final source/settings/firmware/OS audit passed. Alpha ON,1.20/0.97, geometry and learned steer ratio/average offset/delay retained; normal route-start cache refresh documented. Entire old `df788e027` / `1d29e6e` tree is retained. **Installation complete; moving-road pulsing/tracking/fault improvement remains unproved.**

## Regression repair staging — October 27 (checks passed; inactive)

[Completed staging](docs/research/navigator-regression-repair-staging-2026-10-27/REPORT.md): exact `e05e42f43` / `5097b993` published and separately staged. Full device/Mac backup plus fresh post-drive settings/calibration checkpoint verified;253LFS assets checked. Complete ARM build/recheck and1,304Ford/native/context/engagement tests plus12,083subtests passed (79skipped). The earlier test run was stopped for departure and retained; the resumed suite completed afresh.

Final audit passed: clean self-contained candidate Git trees, current Alpha ON/settings/calibration,1.20/0.97, geometry, firmware/launchers/AGNOS20.1slotB and running active service preserved. Original `df788e027` / `1d29e6e` remains active. **Candidate not activated; no candidate powered or road acceptance.** Activation requires a separate request. Physical pulsing/tracking benefits and the two historical release faults remain open.

## Paired regression repairs — October 27 (local integration)

[Integration and checks](docs/research/navigator-regression-repair-integration-2026-10-27/REPORT.md): signed-coast clearance/integral repair and midrange steering admission are integrated locally on the existing paired branches. New current-install drive evidence isolates a producer-clock race behind one20.4mph controls mismatch; local ordering correction retains source timestamps and all freshness/invalidity guards. Owner **1.20/0.97** and vehicle geometry remain unchanged. Local exact pair **`e05e42f43` / `5097b993`** has passed full Mac/Panda builds and parent1,107/child4,733 tests. Production237segment longitudinal parity is exact; known two release faults remain. Full658segment steering strategy parity at production cadence passed. Both checkouts are clean; postcommit builds passed. Exact final receipts are tracked in that report. At the local integration checkpoint this pair had not been published or installed; the staging entry above is current.

[Latest14-segment drive review](docs/research/navigator-latest-mismatch-review-2026-10-27/REPORT.md) confirms remaining sub40mph pulsing:14 actual brake-bit changes in15s near21–25mph, with corresponding torque cycles. Do not count the new timestamp fix or short precharge-to-coast substitutions as a physical comfort cure. Next: retain this exact window and identify planner demand, integral/grade contribution and actual actuator response together; compare command-level changes without weaker braking or extra timeout exposure. Separate ARM/parked acceptance and moving evidence are required before any future installation/comfort claim.

## Latest status — October 24

Latest-master parent **`74eaa6a60`** / child **`3a5fe9fe`** is now active. It includes upstream `9fba666fd` (Flip Flop model, logging socket and WebRTC changes) and retains all Navigator steering, coasting and pose fixes. Alpha ON, **1.20/0.97**, selected settings and fresh calibration hashes were preserved. AGNOS remains 20.1, slot B; signed firmware and launch behavior are unchanged.

[Activation report](docs/research/navigator-master-staging-2026-10-24/ACTIVATION_REPORT.md): fresh private 64-parameter snapshot verified on device and Mac; atomic whole-install switch completed and ignition-off acceptance passed. The entire prior `2aa86b78d` installation is retained for rollback. Owner confirmed the new home screen responds. Powered Park acceptance passed: 1,101 big-model samples at **20.002 Hz / 38.77 ms**, zero dropped frames; no CAN, Panda or coordination faults. Exact final source/settings/firmware/OS audit passed. New-stack parked cadence is verified; road improvement is not claimed.

## Latest master build and hardware evidence

[Staging report](docs/research/navigator-master-staging-2026-10-24/REPORT.md): full ARM build, 1,094 native/context tests, 12,083 subtests, 75 contracts, 14 parent smoke tests and calibration/startup checks passed. Correctly powered exclusive-GPU testing passed two candidate starts and 70 finite synthetic inferences. Chestnut requires ignition ON; earlier ignition-off PCIe errors were not a valid model-regression verdict.

Activation guards bind both powered-start receipts to the exact candidate model SHA and verify all 253 tracked LFS assets. Review's identity-check gap was reproduced and corrected; 43 guard tests passed. Actual new-stack model cadence has now passed the powered Park check. Moving tracking, brake-release reliability and Alpha comfort still require drive evidence.

## Coasting and pose device staging — October 24 (historical preactivation evidence)

[Staging report](docs/research/navigator-coast-pose-staging-2026-10-24/REPORT.md): published exact parent `2aa86b78d` / child `3a5fe9fe`; fresh private device/Mac backup verified (69 parameters, 147 manifest files). Separate isolated full ARM build, 1,094 native/Ford/context tests, 12,083 subtests, 75 retained contracts, 14 parent smoke tests and calibration/startup/pipeline checks passed. Both staged repositories clean, Git objects self-contained, installed firmware image retained. Final read-only audit confirms exact active/staged pairs, settings/calibration, service, AGNOS 20.1 slot `_b` and **1.20/0.97** preserved.

**Candidate inactive:** current `49be383b2` / `d459133a` remains active. Current-stack passive offroad check passed with no new blocked transmissions; no candidate powered/road acceptance claimed. Quiet-release excluded; known release timeouts and physical pulsing concerns remain. No activation, service restart, OS/firmware update or active ECU/CAN requests.

## Coasting and pose paired integration — October 24 (local checks passed; not published)

[Integration report](docs/research/navigator-coast-pose-integration-2026-10-24/REPORT.md): exact local parent `2aa86b78d` / child `3a5fe9fe` on `codex/navigator-tracking-release`, clean paired gitlink. Bounded coasting and expiry-only consumer pose recovery are integrated with live subscriber lifecycle and a shared post-validation apply clock. Minimal/full Mac builds, 1,059 parent tests, 4,570 child tests and Panda compilation pass. All 247,765 fresh extracted callback rows equal the accepted prototype. Native recorded RX and all-TX comparison: 19.83 million RX / 597,172 TX per variant, original non-ACC packets retained, 35 shared rejects and zero added rejects/relay faults.

**1.20/0.97, steering/geometry, clearance and deadline retained. Quiet-release excluded.** Four known release timeouts remain; command-level pulsing reduction is not physical comfort proof. No new 75–85 mph or lateral tuning claim. Local commits only: no push, Comma contact, ARM/device/parked/road validation or activation. Next gates are separate from this completed local integration.

## Pose expiry recovery and quiet-release investigation — October 24 (local only; release unresolved)

[Report and validation](docs/research/navigator-release-pose-resolution-2026-10-24/REPORT.md): expiry-boundary consumer refresh prevents the62mph100.120ms pose fault using a real30.552ms source, retaining100ms limit, producer identity and lateral snapshot. Finalv4 replay247,765callbacks/four moving sessions has no new fault initiation; all4known release timeouts remain. Earlier80ms refresh introduced an old-route fault and was rejected.35focused contracts and226retained guard tests pass; native ACC-only19.83millionRX/247,734TX per variant has zero added rejects, six shared rejects retained.

Factory release comparison:25qualified non-stopping OEM brake-bit falling edges allhave resume off. Local quiet-resume prototype clears only that bit during confirmed moving release waits, retaining inactive propulsion, brake enable, torque clearance and original deadline. **Recorded torque remains non-clear; release-resolution gate remains RED.** Need ECU/bench/HIL response evidence before calling this solved; stationary Park cannot establish loaded release. No paired-source/device changes, **1.20/0.97 retained**, no installation readiness. Consumer live lifecycle/clock integration and full build/hardware gates remain pending.

## New-drive review and bounded-coast prototype — October 24 (local only; not installable)

[Report, plots and evidence](docs/research/navigator-highway-pulsing-prototype-2026-10-24/REPORT.md):38new available completed segments verified; about31active longitudinal minutes, max73.79mph. First session is partial (segments13–24); reconstruction warmup excluded. Seven selected6.7mph crossings retain propulsion. Three mismatch faults: release timeouts near24.8/20.5mph, and a62mph consumed-pose freshness race at100.120ms despite a newer motion publication. Retain clearance and100ms limits; resolve semantics/scheduling rather than bypass guards.

Report-local bounded weak-entry allocator reduces60–74mph brake-command edges348→246 and a70.8mph20s window26→12, with identical healthy coverage and all3faults retained. Across4saved moving sessions247,765callbacks compared.23candidate contracts and226retained guard tests pass; native ACC-only replay8.92millionRX/111,444TX per variant has zero added rejects, five shared rejects retained. Experimental sampled admission/debt bounds, frozen vehicle feedback, residual pulsing and existing faults prevent installation readiness. No paired-source/device changes; **1.20/0.97 retained**.

Lateral screen identifies requested-target oscillation plus amplified measured wheel movement on low-curvature69–73mph episodes. No75–85mph evidence; reported steeringRate is zero, so angle-derived swing screening is used. Next: separate path/calibration-offset/roll/mapping response before any lateral tuning; no blanket high-speed gain cut. All11longitudinal deactivations screened (3fault-related,8with driver pedals); intent not inferred.

## Highway pulsing investigation — October 24 (reproduced; local correction design)

[Investigation and proposed design](docs/research/navigator-highway-pulsing-investigation-2026-10-24/REPORT.md): current restart pair reproduces 39 brake-command edges/20s near60mph; 20 entries are tiny negative residuals, with propulsion withdrawn49.7% of the window. Minimal actual-controller constant-demand/pitch-oscillation reproduction also cycles. Simple causal pitch/demand filtering reduces selected-window edges but reaches later release faults against frozen recorded feedback; **rejected as installation candidates**. Recommend stable residual-demand reference, bounded coast/brake allocation and continuous qualified propulsion, retaining measured clearance, urgent braking and fault deadlines. No paired or device changes; **1.20/0.97 retained**. Incoming current-pair drive and broader replay remain pending. Do not count fewer outputs after faults as an improvement.

## Restart-continuity activation — October 24 (active; ARM and parked checks passed)

[Report and evidence](docs/research/navigator-restart-continuity-staging-2026-10-24/REPORT.md): exact published parent `49be383b2` / child `d459133a` activated after verified 69-parameter device/Mac backups. Full isolated ARM build, 1,045 native tests (79 skipped), 12,083 subtests, 75 actual-source restart contracts, 14 parent smoke tests and calibration/engagement regression passed. Whole prior `064e086d2` / `50719b1e` installation retained at `/data/openpilot.pre-restart-continuity-<private timestamp identifier>`.

Ignition-off and settled powered Alpha stationary Park acceptance passed. Initial powered capture included startup identification mode and failed the strict all-Ford gate; unchanged settled recheck passed, initial evidence retained. Final audit confirms exact clean active/rollback sources, **1.20/0.97**, settings, firmware and AGNOS 20.1 preserved. Alpha enabled by owner. **Road restart smoothness remains unproven; separate release timeouts and highway pulsing remain unresolved.**

## Restart-continuity integration — October 24 (local builds passed; not published)

[Integration report](docs/research/navigator-restart-continuity-integration-2026-10-24/REPORT.md): parent `49be383b2` / child `d459133a`, clean exact paired gitlink. The measured-clearance prototype is now in production source with 35 new permanent regressions. Actual-file 75-contract check, minimal/full Mac builds, 1,029 parent tests, 4,551 child tests and Panda compilation passed. Fresh 136,308-callback extracted traces match the prototype exactly; prior 47-segment native comparison retained with AST/source binding, not rerun here. **1.20/0.97 and protected steering/geometry/safety source unchanged.**

Local commits only: no push or Comma contact. No new ARM/parked/road validation. The separate release timeouts and highway pulsing remain unresolved; physical restart smoothness is unproven.

## Restart-continuity prototype — October 24 (local replay passed; not integrated)

[Prototype report and graph](docs/research/navigator-restart-continuity-prototype-2026-10-24/REPORT.md): fresh measured clearance can survive a speed-only crossing of 3 m/s, preserving an already valid propulsion request. Original RED diagnostic becomes GREEN; 75 focused/retained contracts, 4,516 child tests and 47-segment native comparison pass with zero added rejection. Across 136,308 saved callbacks, 10 qualified carries remove the reset in all nine selected launches; 1,261 propulsion slots change only between 6.71 and 14.09 mph. Brake commands, both existing timeout episodes, inactive/non-PID/below-boundary outputs remain unchanged in this replay.

Prototype only: paired source and Comma untouched, **1.20/0.97 preserved**. Physical smoothness unproven; highway pulsing and release-feedback semantics still unresolved. Production integration/build and physical validation remain separate work.

## Brake-release road review — October 24 (Alpha blockers confirmed; local diagnosis only)

[Road review and figures](docs/research/navigator-brake-release-road-review-2026-10-24/REPORT.md): 55 new segments verified; two moving Alpha sessions, about 40 active minutes. All four checked feedback fields match at 136,308 reconstructed callback slots. Two release timeouts reproduced at 34.18/45.97 mph with fresh pose and residual reported torque. Nine selected launches show propulsion withdrawal at 6.71 mph with zero reported torque and first gear unchanged; the isolated speed-only diagnostic is intentionally RED. Full-rate cycling reaches 39 brake-command edges in 20 seconds near 60 mph, including near-level pitch proxies.

Next local work:
- [x] Prototype measured-clearance/propulsion continuity across 3 m/s locally; replay and guard checks passed.
- [x] Port restart continuity into paired source and complete local integration/build checks.
- [x] Publish, back up, ARM-validate and activate the exact restart pair; offroad and powered Park acceptance passed.
- [ ] Resolve ABS arbitrated/actual torque versus ACC/CMBB status and ownership-preserving release semantics; retain clearance/deadline guards.
- [ ] Stabilize causal coast/precharge/brake allocation and grade-reference transitions; validate sustained braking and stop/restart.
- [ ] Complete controller/native regression, timing, integration and build gates before another installation.

Passive protocol analysis now covers 55 new + 35 saved OEM segments. OEM precharge/propulsion combinations and differing feedback semantics provide a concrete research direction; no new raw-throttle protocol or physical clearance proof established. OEM ACC remains the preferred baseline. **No device changes, paired edits, pushes or new tuning; 1.20/0.97 preserved.** Road smoothness/fuel superiority remains unproven.

## Brake-release activation — October24 (active; offroad and powered Alpha acceptance passed)

[Activation report](docs/research/navigator-brake-release-staging-2026-10-24/ACTIVATION_REPORT.md): exact published ARM-validated parent `064e086d2` / child `50719b1e` activated via atomic exchange after fresh69-parameter device/Mac verification. Whole previous install retained; settings/calibration hashes and **1.20/0.97 preserved**, no OS/firmware update. Ignition-off acceptance197Panda samples/0blockedTX passed. **Powered Alpha stationary Park acceptance passed**:55seconds,551Panda samples,0blockedTX/vehicle orcoordination faults,1,101fresh requests/feedback samples,20Hzmodel/0drops. Final audit confirms clean exact active/rollback pairs,sourcehashes,owner settings and1.20/0.97,firmware andAGNOS20.1 retained. Moving engagement,physical brake release androad smoothness remain unproven.

## Brake-release device staging — October 24 (ARM and parked acceptance passed; inactive)

[Staging report](docs/research/navigator-brake-release-staging-2026-10-24/REPORT.md): published parent `064e086d2` / child `50719b1e`, exact remote heads verified. Fresh private device/Mac backup verified (147manifest members,69parameters). Candidate built in a separate isolated directory: full ARM build,1,010native/Ford/context tests,12,083subtests,40admission comparisons,14parent smoke and1pose/engagement test passed. Both staged repos clean; Git objects self-contained; installed firmware image retained. Active install remains `fe08ede1a` / `d2e8d040`; **1.20/0.97/settings preserved during build**, no service restart or OS/firmware update.

Ignition-off current-stack check passed with no new blockedTX. **Powered Park check passed** with Alpha OFF and assistance disengaged:55seconds,550Panda samples, no faults/new blockedTX,20Hzmodel/0drops and1,100healthy pose samples. Final read-only audit confirms clean exact active/staged pair and1.20/0.97 in both sources. Candidate **not activated**; physical brake-release and road-smoothness improvements remain unproven.

## Brake-release integration — October 24 (local build checks passed)

[Integration report](docs/research/navigator-brake-release-integration-2026-10-24/REPORT.md): paired branch commits parent `064e086d2` / child `50719b1e`; clean paired trees and exact parent gitlink. Bounded mild-edge admission and continuous received-torque clearance integrated with 31 permanent regressions. 40 baseline-comparison contracts, independent review, minimal/full Mac builds, 1,029 parent tests, 4,516 child tests and Panda compilation pass. Actual controller/admission ASTs match the frozen 1,066-segment prototype implementation. Fresh active-path replay receipt is linked in the report.

**Local only:** no push or device access. **1.20/0.97**, lateral source, vehicle values, default-off and native limits preserved. Original frozen-response release-timeout episode remains: physical brake-release improvement is unproven. ARM, staging, parked and road validation remain separate steps.

## Brake-release prototype — October 24 (local prototype and full comparative replay passed)

[Investigation/prototype](docs/research/navigator-brake-release-prototype-2026-10-23/REPORT.md): exact trigger is a one-update near-zero compensated request (~−0.00118 m/s²) despite +0.302 m/s² planner intent, latching ~140 ms of braking before the non-clear torque timeout. Prototype qualifies only new mild edges while coasting, with bounded dwell/exposure and immediate stronger/existing braking. Continuous received-torque protection preserves measured clearance and the one-second deadline.

40 focused contracts and independent review pass; default-off full-stream parity retained. Generic command-dependent episode models avoid the triggering pulse; matched response/native checks add no safety rejection. Old-response counterfactuals still fault and cannot prove physical improvement. The final 1,066-segment historical/native regression and 51-segment active-Alpha replay passed native comparison with no added rejection; full candidate child and canonical parent suites also pass. The original release episode still faults against the original torque response; physical timeout resolution is unproven. Paired branches, device and **1.20/0.97 unchanged**; no integration/installation in this spike.

## Timing integration and new release fault — October 23 (local checks passed; Alpha blocker remains)

[Integration and new-drive investigation](docs/research/navigator-timing-integration-2026-10-23/REPORT.md): local parent `9590ea8fd` / unchanged child `d2e8d040`, both paired branches clean. Exact reviewed timing code retained; minimal/full Mac builds, 1,029 parent tests, 4,485 child/native tests and Panda build pass. All 44 focused contracts and independent review pass. Historical 1,048-segment replay remains bound by matching source hashes; fresh 18-segment replay adds no native rejection. Nothing pushed or installed; **1.20/0.97 preserved**.

**New evidence / next blocker:** 18 new segments downloaded and verified. One mismatch at about <private clock time> / 41.45 mph is `release_timeout_disengage`, not stale pose (77.70 ms valid pose). After a short brake/precharge pulse, 52 distinct fresh torque samples remain 136–388 Nm over the release wait, with 156 Nm at fault. No pedals pressed. Baseline and timing candidate reproduce the same fault, so the timing integration does not fix it. Investigate brake-pulse admission, grade effects, torque arbitration and release/clearance behavior before another Alpha evaluation. No timeout/clearance weakening is included; post-disengagement clearance does not establish safe continued-control behavior.

## Remaining Controls Mismatch timing — October 23 (local prototype and full replay passed)

[Prototype and evidence](docs/research/navigator-coordination-timing-prototype-2026-10-23/REPORT.md): opt-in, two-topic nonblocking pose refresh at publication. Each topic uses the newest publication across main/late caches, with coherent calibration, original timestamps and the existing 100 ms guard. Independent review caught and repaired older-cache rollback. All 44 focused contracts, the 1,029-test parent suite, unchanged child suite and Mac build pass. The exact saved 104.368 ms fault becomes 44.724 ms using a genuinely newer sample.

The final 33-segment native replay reproduces one baseline timing fault and zero prototype faults, with no added rejection across 7.77 million RX frames. The final historical 1,048-segment / 73-route regression passed with zero added rejection, protected-scope change or phase/counter mismatch; frozen source hashes match. This timing fix does not resolve Alpha smoothness or model speed policy.

**Local only:** parent working prototype on `fe08ede1a`, child `d2e8d040` unchanged; **1.20/0.97**, default-off, stop/creep and safety limits retained. No push, commit, installation or device contact. ARM, parked and road scheduling evidence remain separate gates.

## Post-calibration-fix road review — October23 (one timing mismatch remains; Alpha cycling/policy work needed)

[Full review](docs/research/navigator-calibration-road-review-2026-10-23/REPORT.md): all37new segments downloaded/hash-reverified;33post-fix segments/two moving sessions.129,779active requests have zero poseValid=false, but one Controls Mismatch at8:03:39p.m./64.2mph: pose81.52ms old at producer plus22.85ms request age at consumer crosses100ms. Nearby healthy fresh motion not reflected until a later control packet. Prior false-calibration-validity mechanism absent; coherent snapshot/consumer timing remains first priority. Preserve100ms/fault guards.

85mph setting was real, but126.4s no-lead/above45mph data is almost entirely model/e2e-limited (median actual55.8mph); no evidence of a dedicated posted-speed-limit limiter in the inspected planner path. Separate model-vs-cruise policy from actuator tuning. Cycling remains: up to29brake transitions/20s, rare strict coast commands, stronger braking association with downhill-indicated pitch; grade proxy not ground truth. Five active stop/restarts observed, without intervening pedals, but smoothness/fuel superiority unproved.

Lateral:40–50mph steady body response114–116% (route/direction/pose uncertainty apply),55–65mph roughly101–102%; sharp18–27mph shortfalls/turn-limit warnings and58mph excess-before-input episode retained.29grouped inputs/disengagements classified, not29 confirmed unsafe takeovers. Actual speed below66mph: no80–85mph validation. **Next:** local timing reproduction; speed-policy design; integrated coast/grade/feedback replay; targeted lateral mapping/unwind and bounded low-speed work. Device/settings/1.20/0.97 unchanged; OEM ACC remains baseline while Alpha is unresolved.

## Calibration fix activation — October 23 (active; powered parked acceptance passed)

[Activation report](docs/research/navigator-calibration-staging-2026-10-23/ACTIVATION_REPORT.md): exact published parent `fe08ede1a` / child `d2e8d040` activated after69-file fresh device/Mac parameter verification, retained whole original installation and atomic exchange.1.20/0.97/preferences/firmware/AGNOS20.1 retained; no OS/firmware update. All offroad learned hashes match; post-ignition cache hash changes documented without manual writes. Initial automatic rollback for transient OnroadCycleRequested was resolved in the checker only; candidate production source unchanged.

Responsive screen confirmed; owner Alpha ON.55-second powered Alpha/Park acceptance passed:16topics healthy,551Panda samples with zero RX/blockedTX/transport faults,20.003fps/zero drops,1,101valid atomic calibration and coordination pose samples, zero coordination faults. Assistance remained disengaged. **Next:** short supervised low/moderate-speed moving trial and saved-drive analysis; parked evidence does not prove moving Controls Mismatch resolved or brake/accel cycling improved. Whole original rollback and backups retained.

## Calibration fix staging — October 23 (staging and parked checks passed; inactive)

[Staging evidence](docs/research/navigator-calibration-staging-2026-10-23/STATUS.md): parent `fe08ede1a` / child `d2e8d040` published and remote heads verified. Fresh device/Mac backup verified (145 manifest files, 68 parameters). Separate candidate full ARM build and979native tests/12,083subtests,14parent tests, calibration engagement regression and pipeline checks passed. Candidate Git objects finalized independently, source clean and firmware image preserved. Ignition-off passive acceptance passed with 551 safety samples and no new rejects/faults. Active install, firmware, settings and1.20/0.97 unchanged. Final offline validation acceptance and55-second passive powered Park check passed: nine topics healthy,550safety samples,~20fps/zero drops,no new blockedTX/faults. Owner turned Alpha off; current install is still the prior version. Startup cache hash changes documented without restoring values. No activation; candidate live checks and road proof remain pending.

## Calibration update repair — October 23 (integrated locally; full build checks passed)

[Repair and evidence](docs/research/navigator-calibration-update-fix-2026-10-23/REPORT.md): parent-only atomic pose/validity rebuild on calibration or motion change; original motion timestamp and100ms/health/reversal/fault limits preserved. Five exact first-fault inputs now pass without forced validity.26focused tests (19new cases), real card transport/parent latch/rearm,1,029parent tests and915Ford/native tests/12,083subtests pass.94,980saved producer updates retain disabled exact byte parity;6,713calibration-only gaps removed while277genuine invalid samples remain. Fresh failed-drive native replay adds no rejection and clears five baseline pose fault slots; retained full longitudinal/native/model regression matches prior integrated hashes. Minimal Mac build/lint pass; full 1,015-segment replay passed with no added rejection, scope change or phase/counter mismatch.

**Device remains unchanged with the prior installed bug.** Keep Alpha off pending separately authorized ARM/parked/install checks and later physical drive validation. Child steering/geometry/safety and1.20/0.97 unchanged. Local parent commit `fe08ede1a` retains child `d2e8d040`; no push or installation. Shared recorded cancellation rejects remain documented; this is not a road smoothness/fuel result.

[Paired integration and build evidence](docs/research/navigator-calibration-integration-2026-10-23/REPORT.md): exact source hashes retained, paired trees clean, minimal/full Mac builds and fresh parent suite (1,029 tests) passed. Full child suite (4,485 passed /24,693 passing subtests) and standalone Panda build also passed. All five build/check phases succeeded; no ARM, device or road validation is implied.

## Coordination engagement failure — October 23 (road trial blocked; calibration timing root cause reproduced)

[Failure investigation](docs/research/navigator-coordination-engagement-failure-2026-10-23/REPORT.md):18new completed segments/three sessions downloaded and hash-verified read-only. Five `invalid_pose_or_accel` faults around15–25mph immediately trigger Controls Mismatch; only~1.5seconds total longitudinal-active time, so no ride-quality result. Healthy fresh72–81ms motion gets poseValid=false during calibration-only updates. Production Controls.update clears validity until a subsequent motion update; unchanged calibrated extrinsics reproduce the bug locally. Production-controller/alert reproduction fails in all five captured cases; flag-only diagnostic counterfactual removes them, but is not an acceptable fix.

**Next:** atomic calibrated-pose/validity recomputation on either input update, keeping original motion timestamp/100ms limit/health checks and real-fault latching. Add independent message-cadence and engagement regressions, saved sensor chronology replay and native rejection-boundary replay.14Ford blocked-TX increments follow the faults and remain a separate replay item. Owner should keep Alpha off/use OEM ACC pending repair. Device and paired production code unchanged this investigation;1.20/0.97 preserved. Earlier parked acceptance did not exercise moving PID and is superseded as a road-readiness claim.

## Coordination activation — October 23 (historical parked pass; subsequent road trial blocked)

[Installation and evidence](docs/research/navigator-coordination-staging-2026-10-23/REPORT.md): exact published pair e9ddc7668/d2e8d040 installed after verified original device/Mac backup plus fresh67-file parameter snapshot. Whole prior install remains at `/data/openpilot.pre-coordination-<private timestamp identifier>`. ARM build,979native tests/12,083subtests and14parent smoke tests passed during staging. Candidate ignition-off acceptance and corrected55-second powered Alpha/Park acceptance passed: all16streams healthy, assistance disengaged, zero blocked transmissions or coordination/vehicle/transport faults. Live coordination producer/feedback observed; model about20Hz with no drops. Alpha and coordination on; settings/owner1.20/0.97, firmware and AGNOS20.1/B preserved. No OS/firmware update or manual CAN/ECU query.

**Next:** short controlled Alpha road evaluation at low/moderate speeds, followed by log review of cycling, acceleration, brake release and interventions before highway expansion. Stationary acceptance does not prove physical smoothness, grades, moving release/restart or fuel efficiency. Stop/creep below3m/s retain baseline behavior. Rollback remains available. The installation helper's asynchronous-write readback issue and checker typo were corrected; full final parked acceptance passed without production-code changes.

## Paired longitudinal coordination — October 23 (integrated locally; default off)

[Integration and evidence](docs/research/navigator-long-integration-2026-10-23/REPORT.md): actual request/feedback schema, owner epochs/producer timestamps, optional original-time CAN125 observations, directional integral inhibition, OEM-derived relative grade reference, and driver-visible latched fault/disengagement are integrated into the paired branches. Fresh review found and repaired override-history, moving-entry clearance and reversed-context gaps;35focused contracts pass. New `FordPrefLongitudinalCoordination` defaults off; Alpha alone does not select it. Published/staged and ARM-validated as recorded above; current installed code/settings/1.20/0.97 remain unchanged.

Final65,736slot replays retain default-off exact ACC parity and identical non-ACC hashes;36,086inactive/stop/creep excluded packets unchanged. Model: frozen213→77brake edges; real parent221→65,1,561positive-I updates inhibited; zero modeled faults.288response scenarios:172better, none>10%worse, zero faults. These remain model/command results, not road smoothness/fuel proof. Original-command observer zero faults;58rlog hashes reverified. Two final5.26million-RX native ACC replays add zero rejections. Minimal/full Mac builds,915Ford/native tests and full parent1,028tests pass. Broad opendbc4,485tests pass; three sandbox-blocked MISRA subchecks pass in the canonical offline rerun with existing-cache access. Parent/child type and lint checks pass.

Local pair: parent `e9ddc7668`, child `d2e8d040`, exact gitlink verified and paired trees clean.

**Next:** controlled road evaluation and log review. Activation, responsive-screen confirmation and candidate Alpha powered stationary acceptance are complete as recorded above. Do not install the report adapter; the integrated runtime is the candidate. Hardware behavior remains unproven. Separate precharge-only experiment is not included.

## Longitudinal integral / actuator / fallback — October23 (local policy and replay complete)

[Local coordinator/report](docs/research/navigator-long-coordination-2026-10-23/REPORT.md): timestamped epoch/sequence feedback; freeze only positive I growth into deliberate propulsion caps, retaining stockKi0.5/unwinding/genuine braking. Brake release needs three distinct fresh <=4Nm samples over>=40ms; no timeout-based propulsion permission. A real~0.7srelease tail rejected the original500msfault deadline;1snow permits observed clear or requests latched disengagement. Original-command observer trace passes; new-command/old-feedback faults remain explicitly separated from performance scores. Strong brake-only requests retain installed conservative onset.

58source rlogs reverified;40,544OEM selected commands retain default-off parity. Full65,736Alpha-slot replays: frozen/model213→77edges; recomputed-parent/model221→63,1,458limited positive-I updates inhibited; no modeled faults. Parent reconstruction0.0051m/s²RMS.288response-stress cases/1,152,000updates,212better tracking and none>10%worse, zero modeled faults; these are not an identified vehicle model or road proof.30new contracts plus886default-off Ford/native tests/12,083subtests (79skips); native RX/timer ACC replays add zero rejects. No inactive/stop/creep or non-ACC differences in frozen modeled replay. Paired branches/device/settings/1.20/0.97 untouched. Next: actual paired runtime IPC plus driver-visible fault/disable integration and builds; no installation of the in-memory adapter alone.

## OEM/Alpha pitch reference — October23 (relative mapping validated locally; integration blocked)

[Investigation/prototype](docs/research/navigator-grade-resolution-2026-10-23/REPORT.md):58fresh hash-verified saved segments (35OEM/23Alpha) support a relative zero-reference gap, not a demonstrated pitch transport/sign bug. Four moving OEM routes/15windows give+0.149913m/s² (~0.876°); Alpha is held out and its moving median relative residual improves0.164→0.014m/s². GNSS proxy RMSE improves on every moving route; physical sensor/frame ownership remains unresolved and route-holdout error reaches0.061m/s². No global calibration reset.

Default-off report-local mapping slews in and fades out3–5m/s. Corrected direct past-only pose context avoids a replay freshness artifact.65,736Alpha-slot replay:213→79eligible brake edges, highway33→4/20s, low-speed24→2/20s; no inactive/stop/restart/below3m/s packets or non-ACC differences, default-off exact wire parity.11contracts and886Ford/native tests/12,083subtests (79skips) pass; fresh5.26million-RX native ACC replay adds zero rejects (three shared pedal/permission rejects). This is command evidence, not physical smoothness. Next: atomic validity/withdrawal and integral/actuator-consistent integration plus justified closed-loop response checks. Paired sources/device/1.20/0.97 unchanged; not ready to install or request another Alpha trial.

## Separate coast/precharge/brake prototype — October 23 (replayed; insufficient, not installable)

[Local prototype/report](docs/research/navigator-coast-transitions-prototype-2026-10-23/REPORT.md): distinct precharge/brake packing plus retained coast behavior tested against65,736Alpha slots and40,544saved OEM commands.589Alpha packets switch actual braking to precharge-only; actual brake edges remain213, highway33/20s and low-speed24/20s unchanged. Precharge edges also unchanged; no physical improvement claim. Nominal120ms qualification reaches147.97ms between recorded commands, so deadline timing remains a blocker.13new contracts,886Ford/native tests/12,083subtests (79skips), one parent contract pass. Fresh5.26million-RX native ACC replay adds zero rejects (three shared pedal/permission rejects). No inactive/stop/restart/below3m/s/non-ACC changes in saved Alpha replay. Paired sources/1.20/0.97/device untouched. Next: resolve gravity frame/offset ownership and bumpless demand consistency before tuning transitions further; no Alpha road trial or installation from this spike.

## Fork comparison and OEM coasting — October 23 (evidence gathered; local design next)

[Pinned fork/source and fresh OEM report](docs/research/navigator-forks-oem-coasting-2026-10-23/REPORT.md): BluePilot has relevant Ford coasting, separate precharge/brake outputs and pitch options; Dustin's examined long implementation matches it. StarPilot's relevant changes are Mach-E-specific; inspected sunnypilot Ford actuation retains baseline logic. BluePilot PR212 is open/EV-only, not a proven Navigator cure.

Fresh hash-verified review of35saved OEM segments/five routes yields40,544eligible OEM commands, including3,032brake/precharge-free inactive-propulsion samples and1,605precharge-only/valid-propulsion samples. Observed brake-free slowing includes2.23s near62.6mph with zero median reported brake torque. Current paired packer couples precharge/deceleration bits; OEM demonstrates distinct states. This is a representation gap, not yet proved causal or fixed. Next: resolve gravity alignment and prototype distinct allocation/transition semantics locally with urgent braking, grades, release/restart and native replay checks. No device contact or paired source/settings/1.20/0.97 changes.

## Alpha pitch/actuator feedback — October 23 (strong relative-offset hypothesis; not resolved)

[Investigation and local experiments](docs/research/navigator-alpha-pitch-feedback-2026-10-23/REPORT.md): a second received Ford motion signal closely follows wheel acceleration + Comma gravity term with relative offset about **+0.18 m/s² (~1.05°)** in highway and low-speed windows. Thirteen additional same-drive windows show median +0.157 (p05/p95 +0.113/+0.204). GNSS proxies point in the same direction, but channel compensation/zero ownership and grade ground truth remain unresolved.

A decision-term-only +0.18 sensitivity test changes reconstructed brake edges **213→56**, including **33→2 highway /24→2 low speed**. This is command switching, **not physical ride improvement**. It changes 1,474 below-3m/s slots; no installation/stop/grade/restart approval. Causal pitch smoothing leaves159/151 edges; response-aware admission205, so neither simple approach resolves the loop.

ECU observations show large propulsion-state swings, modest/intermittent brake torque and release lag; they do not prove widespread brake riding/fuel waste. Slow acceleration cycling appears in wheel and IMU-derived estimates. Eight new diagnostic contracts pass; prior full-build/native proof does not cover these new experiments.

**Next implementation direction:** timestamped validity-gated relative gravity calibration, independent-route/OEM checks, bumpless consistency with integral demand, and observed actuator-aware propulsion/coast/brake allocation. No hard-coded pitch adjustment, calibration reset or new Alpha road trial. Paired sources/1.20/0.97 unchanged; no device contact this turn.

## Alpha cycling local prototype — October 23 (partial; not ready to install)

[Prototype and verification](docs/research/navigator-alpha-cycling-prototype-2026-10-23/REPORT.md): report-local bounded brake admission plus signed negative-demand debt. Full-drive reconstruction reduces eligible brake edges **213→179 (16%)**, but worst highway window only **33→31**; main cycling unresolved. Weak new grade braking may be delayed within the prototype envelope. Do not loosen bounds simply to improve edge counts.

11 new contracts, 33 retained coordination/actual-parent restart tests, full Ford/native **886 tests / 12,083 subtests** (79 skips) pass; counts overlap. Export matches prototype over 65,736 slots. Corrected RX chronology honors logged diagnostic→Ford configuration transition: 5,260,361 RX / 65,728 ACC slots, shared three intervention-boundary rejects, no added candidate rejection/final relay fault. Initial all-rejected startup replay retained as invalid. Baseline only96.04% byte match to recording; frozen-input comparisons are not closed-loop vehicle proof.

Paired sources clean and unchanged, 1.20/0.97 untouched, no device access/mutations. **No installation candidate or new road trial.** Next local investigation: separate steady grade/body-pitch effects and feedback/actuator release/resumption response from this saved drive; remaining persistent net requests cannot safely be suppressed indiscriminately.

## Alpha road result — October 23 (poor smoothness; local fix required)

[Road review](docs/research/navigator-alpha-road-review-2026-10-23/REPORT.md): all32new completed rlogs downloaded, three sessions; actual Alpha drive12:36–12:58CDT,13.44minutes active, maximum73.94mph. Owner reports constant brake/acceleration. Full-rate commands show209brake-request edges while active/no pedals/>5mph, including33edges/20s near69mph and24/20s near22mph. Zero simultaneous active brake/valid-propulsion commands, but repeated near-zero pitch-adjusted brake switching resets propulsion qualification/rise. Narrow release qualification/ramp interaction is the leading mechanism to reproduce locally; no cure proved.

Nine stationary/creep intervals (not independent stops), six subsequent unassisted active crossings above3mph; one accelerator override after38s stopped. Three brake-pedal disengagements at11.1/6.2/19.8mph. Eight blocked-TX increments occur at override/disengagement boundaries, not sustained cycling; exact rejected frames still need replay. No Panda/RX/radar faults. **Do not advance Alpha road trials until local cycling/boundary regression work is resolved. OEM ACC recommended for ordinary use; device unchanged and Alpha remains owner's enabled setting.** Road evidence supersedes parked-only smoothness assumptions;1.20/0.97unchanged.

## Longitudinal pair installation — October 23 (installed; powered checks passed)

Published and activated parent `ffebc43497f8015c37be5927800832f2719c7dca` / child `0ac9618972dd580281c5e933c7990f186522fbd4`. Fresh ARM build, 944 native tests (79 skips), 14 parent smoke tests and live-source/settings preservation gates passed. Fresh private Mac backup verified: 843,605,227 bytes and 135 manifest members. Whole previous installation retained on device. AGNOS20.1/B, firmware, launchers, learned calibration, owner settings and **1.20/0.97** preserved.

Ignition-off acceptance passed: 201 passive samples, zero blocked TX, no unexpectedly stopped processes. **Powered stationary acceptance passed:** 55 seconds stationary in Park, assistance disengaged; no vehicle/Panda faults, invalid RX or blocked TX; large model 20.0006 Hz with zero dropped frames; clean exact pair and calibrated state. Owner confirmed responsive home screen. **Owner subsequently enabled Alpha via UI; separate Alpha powered Park acceptance passed:** live longitudinal enabled, Ford safety parameter11, radar/planner healthy, no faults or blocked TX. Alpha is now on. Physical braking/restart/comfort and lead response remain unverified. No physical longitudinal benefit, release/grade response, comfort, fuel economy or highway stability claim. See [installation record](docs/research/navigator-longitudinal-installation-2026-10-23/REPORT.md). Earlier local-only status sections below describe their historical stages.

## Latest master /AGNOS 20.1 — October 23 (installed; parked checks passed)

AGNOS **20.1/B is booted** and exact published parent `24e981d6d` / child `01f32a6f` is activated. Fresh full ARM build and offline gates passed (911 native/controller tests, 79 skips, 12,063 subtests; 14 parent smoke tests, six allowed skips). Original firmware, launcher, owner settings and **1.20/0.97** preserved. All seven target partitions verified and saved actual A hashes unchanged; old source retained.

Ignition-off and **powered stationary Park acceptance passed**. No vehicle/Panda faults, invalid RX or blocked TX; all expected processes healthy. Large model 20.036 Hz with zero reported frame drops; UI 60.215 fps. Owner confirmed responsive home screen. Clean paired heads, all Navigator options, stock longitudinal and Alpha off confirmed. Installation is complete; road evaluation remains pending and parked checks do not establish tracking improvement or 85 mph stability.

[Master merge/build record](docs/research/navigator-master-agnos201-integration-2026-10-23/REPORT.md): pinned upstream `ff47f484e`, 91 protected files unchanged, Mac/Panda builds and 1,021 parent / 4,424 child tests passed. [Installation evidence](docs/research/navigator-agnos201-preparation-2026-10-23/REPORT.md) tracks device checks and rollback. No road-benefit or 85 mph stability claim.

## Ford longitudinal coordination — October 23 (local investigation complete)

[Current-pair investigation](docs/research/navigator-longitudinal-current-baseline-2026-10-23/REPORT.md): the installed pair's longitudinal block remains identical to the old pre-candidate controller. Original Alpha751active-braking commands all retain valid propulsion; original OEM216and newer saved OEM8,562eligible active-braking commands all withdraw it. Newer subset covers35segments/fiveroutes,39,992eligible commands. Prior5.68× vibration association and ECU brake/propulsion torque differences reproduce; physical cause/cure is not established.

Report-local current-controller comparison:751/2,984ACC outputs change only propulsion, all2,984pass native debug TX hook;3,889non-ACC outputs identical for frozen reconstructed inputs. Eight command contracts give baseline4expected failures/candidate8passes;12settled pitch/speed sequences reviewed. No exact original scheduling/full RX/closed-loop or full steering-context replay claim.

**Next:** explicit brake/propulsion handoff design before PID/planner tuning. Old latch holds propulsion through small positive requests; pitch/creep affect release. OEM release periods vary~0.018–2.228s, so do not copy a fixed timer. Precharge-only behavior, release/restart/grades and physical benefit remain unresolved. No paired-source/device changes; 1.20/0.97 and stock ACC retained. Alpha installation is not ready.

## Ford handoff prototype — October 23 (local; not ready for installation)

[Design/prototype/replay](docs/research/navigator-longitudinal-handoff-2026-10-23/REPORT.md): explicit inactive/braking/qualification/resume handling removes valid propulsion during brake requests and bounds positive resumption.15tests,20speed/pitch controller combinations and90,000randomized helper updates pass. Baseline/simple/nine-stateful comparisons each emit2,984ACC frames accepted by scoped native Mac debug TX hooks;3,889non-ACC outputs identical per variant. Main experimental0.5m/s³/20mssetting removes751conflicting request frames and reduces52other positive-request frames; brake commands and existing limits remain unchanged. Synthetic-clock/frozen-input evidence is not full RX/closed-loop or fuel/road proof.

**Blockers:** original brake latch still prevents small-positive-request restart; unknown physical grade/hydraulic release response; missing/stale pitch and production lifecycle policy; acceleration-lag tradeoff. No paired integration, full retained build/replay, device access or installation. Owner1.20/0.97andstockACCunchanged. [Future testing/OEM comparison plan](docs/research/navigator-longitudinal-handoff-2026-10-23/TEST_DRIVE_PLAN.md): collectOEMreference now, keepAlphaoff; later verified installation/parked acceptance and controlled low-speed-first evaluation. No80–85mphshaking reproduction or fuel-saving guarantee.

## Ford restart/release correction — October23 (local resolved; integration next)

[Qualified release/candidate package](docs/research/navigator-longitudinal-release-2026-10-23/REPORT.md): reproduced near-cruise0.2request cap versus old>0.3brake release deadlock, including actual stopping→pid path. New conditional positive-intent/pitch-aware release resolves the flat0.2case while retaining negative-net braking; near-zero noise and invalid input/time cannot clear a prior brake.33focused tests,854Ford tests/79skips/12,063subtests pass;100,000release-state/90,000handoff updates pass. Original AlphaRX-driven replay:239,195RXframes,2,983actualACCslots, no added rejection; one driver-brake cancellation rejection is shared by original/baseline/candidates. Review-found invalid fallback double-creep bug fixed and independently rechecked.

Reviewable patch exported and package-import controller tests pass. **Next:** paired integration/in-tree tests and exact-pair build/context checks, then separately authorized backup/ARM/parked acceptance before low-speed physical evaluation. Paired sources/Comma untouched,1.20/0.97andstockACCpreserved. No physical launch/grade rollback/shaking cure/fuel benefit or road readiness claimed. Prior prototype's small-positive software blocker is superseded; positive-net noise-band holds and acceleration-lag tradeoff remain explicit design choices.

## Paired longitudinal integration — October23 (local complete; full checks passed)

[Final integration/build report](docs/research/navigator-longitudinal-integration-2026-10-23/REPORT.md): parent`ffebc4349`/child`0ac96189`committed on paired`codex/navigator-tracking-release`, clean and matched gitlink. Reviewed handoff/qualified release plus standalone child tests and actual parent stopping→pid cap regression integrated. Owner1.20/0.97,84protected child files, all parent runtime source and Panda pin unchanged. Independent review clean.

**All configured local checks pass:** minimal/full Mac and Panda builds;1,022parent tests/87skips/1xfail/281subtests;4,456child tests/1,690skips/24,693subtests;33focused/20subtests and lint. Frozen export/production replay matches5,967updates/2,984ACC/3,889other messages exactly. ActualRX replay239,195frames/2,983send slots matches export bytes/results with no added rejection; inherited driver-brake cancellation edge retained. Initial host sandbox failure is preserved; final full suites ran with normal temporary-directory/IPC permissions.

**Next:** separately authorized publish/backup/fresh ARM/device and stationary acceptance before a low-speed trial. No push or Comma access/settings/firmware changes. Physical release/grade rollback/comfort/shaking cure/fuel benefit remain unproved; Mac/offline checks are not road acceptance.

## Highway observer paired integration — October22 (local complete)

[Integration/build record](docs/research/navigator-observer-highway-integration-2026-10-22/REPORT.md): committed parent `38172286f7` /child `01f32a6f66` on paired `codex/navigator-tracking-release`; clean matched gitlink. Existing combined opt-ins select validated highway observer continuity; other routing/default-off preferences preserved. Owner 1.20/.97 and85prior Ford/native files unchanged.

- Minimal/full Mac and Panda builds pass;1,021parent and4,424child tests pass. Production factory/native replay on48target segments/281,846invocations per variant exactly matches frozen prototype result/command/stream hashes. Earlier1,015segment prototype proof retained by AST identity, not a fresh integrated corpus run. Independent review clean.
- New low actuation remains withdrawn;23–24mph saturation open. No publication, Comma access, ARM/device build, physical benefit or85mph stability proof. Next: separately authorized publish/backup/device staging validation.

## Observer continuity broader validation — October 22 (local pass)

[Final report](docs/research/navigator-observer-continuity-validation-2026-10-22/REPORT.md): **71 recordings / 1,015 segments / 5,805,897 controller invocations per variant passed** corrected offline native replay. No additional native rejections; full counts and complete event lists match. 71 focused tests, six timing transport tests and 196 timing/abort scenarios / 15,680 frames pass. Exact source fingerprints verified.

- Replay now follows recorded sendcan invocation cycles and freezes pre-state topic snapshots; synthetic fixture clocks remain separate. The two current target drives retain 20 baseline timing-ambiguous frames; candidate changes none of them. Exact receive timing remains unlogged.
- Initial broader testing exposed shared-history/budget scope leaks. Final independent highway overlay changes only 70–80 mph; commands below70 and at/above80 remain unchanged. **New low actuation withdrawn; severe23–24mph saturation remains open.**
- Paired sources, owner 1.20/0.97 and Comma untouched. No physical improvement or85mph stability proof. Next: separately authorized paired integration/build validation; no deployment readiness claim.

## Initial observer continuity prototype — October 22 (superseded)

[Local prototype and evidence](docs/research/navigator-observer-continuity-prototype-2026-10-22/REPORT.md): source-only throwaway candidate; paired branches and Comma untouched;1.20/0.97 preserved.67focused tests pass. Two complete target drives/48segments/277,065controller updates per variant pass frozen native replay with no additional rejection and default-off parity. Same two inactive0x83rejections occur in both baseline/candidate; no new steering rejection.

-Highway: valid original-target wheel observations survive body-margin crossings, but current independent body/wheel agreement remains mandatory for trim. Tests now reach the actual selected `unchanged.stock.upper_reference` above75mph. Existing withdrawal, caps and slew limits retained.
-Low speed: original intent observed independently from bounded command, with unchanged episode/budget/headroom limits. Earlier admission works in synthetic cases, but the severe recorded23–24mph clipped windows remain unchanged. This is not a saturation fix.
-Native controller scheduling changes110highway updates and none outside intended bands;40–50mph unchanged. Original-send-time replay changes169highway and4low-speed packed commands; the low changes are outside the severe windows and timing-sensitive. No physical improvement/damping claim.
-Initial native runs failed source-provenance checks after test expansion; both full drives rerun frozen, exit0 and identical result/stream hashes. Broader current-corpus replay, timing integration and additional stress validation remain before paired integration. No build/deployment or85mph road proof.

## AGNOS 20 steering diagnosis — October 22

[Local command/observer diagnosis](docs/research/navigator-agnos20-steering-diagnosis-2026-10-22/REPORT.md): all91focused low-speed and284focused highway eligible send commands reproduce within half a wire step. Paired sources and Comma untouched;1.20/0.97 retained. Whole-route replay has11/39unresolved mismatchframes, so only focused matching windows support exact command attribution.

-23–24mph: application fixed-pinion deviation clipping plus `command_deviation_limited` / `episode_spent` keeps early effort zero. Calibrated feedback also compares a bounded curvature against the original atomic target and can reject the mismatch. Next design separates original intent from feasible command without widening limits; fully clipped demand remains a limitation.
-75–79mph: final predecessor output trims in73/248focused frames, in seven short bursts. Prototype work corrected the selected layer to `unchanged.stock.upper_reference`; earlier adjacent-policy reason counts are withdrawn. That selected class resets wheel history on eligibility withdrawal. New70–75mph onset policy is deliberately not selected above75. Roll map is zero here.
-Ping-pong concern: broad alternating errors coexist with alternating requested paths; seven sustained meaningful same-direction highway bends show no persistent alternating-error pattern under the screening thresholds. This neither proves80–85mph stability nor dismisses the driver's feel; meaningful80–85mph evidence remains absent.
-Next: local continuous-valid-observer/admission separation and bounded release design, with transition/abort/native replay before any deployment. No correction candidate or full safety replay completed in this diagnosis.

## First AGNOS 20 drive review — October 22

[All new drives reviewed](docs/research/navigator-post-agnos20-drives-2026-10-22/REPORT.md): 11 recordings / 137 segments downloaded and hash/completion verified; seven identify AGNOS 20/current parent. Five assistance-active recordings total 43.8 minutes with 363.5 clean meaningful seconds. All 67 AGNOS 20 input/disengagement groups reviewed; owner tentatively recalls obstacle avoidance for the queried inputs without identifying an exact event. These are not confirmed tracking-failure takeovers. Comma unchanged, owner settings and 1.20/0.97 retained.

- Recorded runtime healthy: no unexpected process stops or active steering faults/CAN-invalid samples; no model drops while assistance active; UI about60Hz and thermal status ok. Startup/manual transient flags remain distinguished.
- Repeated23–24mph shortfall: focused windows about48–51% body response with saturation and subsequent input; separate24mph window about66%. Investigate target/command/clamp/admission locally.
- Highway excess remains:77–79mph bend123% body/134% wheel, not removed by a simple reference delay.70–75mph and64–70mph unwind remain open.40–50mph steady evidence also shows113–117% body response, so45mph is not assumed perfect.
-15mph evidence remains sparse; max speed about80mph with no clean80–85mph evidence. No85mph validation or matched OS-only performance claim. Next step is local diagnosis, not a blanket speed/gain adjustment.

## Latest master / AGNOS 20 — October 22

[Merge, checks and installation status](docs/research/navigator-upstream-sync-2026-10-22/REPORT.md): parent `26b3416a6b` includes official master `34d4241e1`; child `fe59e503` unchanged. Both remote heads verified. All 507 child file hashes and eight protected parent sources preserved, including 1.20/0.97, steering corrections, geometry, settings and calibration transport. Minimal/full Mac and Panda builds, 1,021 parent tests and 4,353 child tests pass.

- Requires AGNOS 20, with OS-owned modem management and new boot/system images. No new longitudinal tune or MADS is introduced.
- **AGNOS 20 installed; powered parked acceptance passed:** exact pair `26b3416a6b` / `fe59e50338`, fresh full ARM build, 840 native tests / 79 skips / 12,063 subtests, pipeline/scheduler and parent smoke checks passed. UI now renders about 60 Hz; display service has zero restarts this boot. 55-second Park check passed with 20 Hz big model, no dropped frames or vehicle/Panda/Chestnut faults. Owner 1.20/0.97, five Navigator options, geometry, stock ACC and paused updates retained. Reversible graphics loader configuration is documented; prepared Raylib upgrade not installed. Original 19.9/B and old source remain preserved. Learned hashes matched before startup and evolved afterward; both snapshots retained. Road behavior and high-speed stability remain unproved. [Installation record](docs/research/navigator-agnos20-installation-2026-10-22/REPORT.md).

## Paired earlier-entry integration — October22

[Integration/build record](docs/research/navigator-early-low-high-integration-2026-10-22/REPORT.md): locally committed parent `21325dccb0` /child `fe59e50338` on `codex/navigator-tracking-release`; clean matched gitlink. Existing combined opt-ins select the new20–25mph/70–75mph onset policy. Owner 1.20/0.97, previous Ford/native sources, settings and geometry preserved.

- Minimal/full Mac and Panda builds pass;1,021parent and4,353child tests pass. Production-factory native replay on10target segments/54,157updates exactly matches all frozen prototype stream hashes, with zero native rejections. Previous878segment corpus evidence retained by normalized implementation identity; no fresh integrated full-corpus run claimed.
- Severe low-speed clipped section remains unresolved; no physical benefit or85mph stability claim. No publication, ARM/device build, activation or Comma changes. Last documented installed pair remains db5842348/8ccc6cf0.

## Earlier-entry prototype — October 21

[Local candidate and evidence](docs/research/navigator-early-low-high-onset-prototype-2026-10-21/REPORT.md): bounded rising-demand admission at20–25mph and history-aware onset at70–75mph. Paired source,1.20/0.97 and Comma unchanged. No wider application/Panda limits, no roll-map extension.

- Final saved low episode changes two commands about0.35s before clipping; the severe29-command clipped section remains unchanged. Earlier-entry hypothesis, not full shortfall resolution.
- The two74mph pre-input windows change9/32 floating commands with current caps/withdrawal retained. Human input remains tire-debris avoidance; counterfactual commands do not prove physical improvement.
- 90focused tests,966transition cases/309,120frames,112active-abort cases and17,000shadow checks pass. Independent review found no remaining material issue after measured-time exposure-budget repair.
- Full60recording/878segment controller/native replay **accepted locally**:5,063,641updates per variant, zero added native rejections; five exactly shared existing events. Whole default-off streams and commands outside20–25/70–75mph identical. Input/source audit passes. No integration, build, publication, activation or road proof.
- [Clamp/parking distinction](docs/research/navigator-early-low-high-onset-prototype-2026-10-21/CLAMP-AND-PARKING.md): observed clip is host software; vehicle EPS authority remains unproved. Factory parking capability is not evidence of unrestricted authority through the current on-road interface.

## Latest local diagnosis — October 21

[22–25 mph /74 mph command diagnosis](docs/research/navigator-master-tracking-diagnosis-2026-10-21/REPORT.md): exact installed strategy reconstructs all 4,466 active/unpressed commands in the focused drive within half a wire step. Paired source clean; all 85 protected child hashes and owner 1.20/0.97 preserved. Comma untouched.

- **Low speed:**29/29 focused commands hit application deviation clipping. Clipped curvature is then compared against the original atomic wheel target, yielding28 target-mismatch resets despite valid/fresh calibration; actual output equals clipped feedforward throughout. Original target is consistent to0.00000264deg. Only~0.15s of admissible pre-clip evidence exists. Calibrated wheel reference still exceeds the same band27/29frames, so reference correction alone cannot resolve the severe turn. Hard EPS limit unproved.
- **74 mph:**trim activates but only4/56 and19/56pre-input commands, max2.15%/3.39%; final slew and15%ceiling are not binding. Permission resets/five-frame confirmation/ramp dominate; earlier-onset credit covers60–70only. Roll feedforward mapping is off above70; possible scope extension is a separate model hypothesis, not validated tuning. Human inputs remain tire-debris avoidance.
- **Next design:**separate original intent/calibration validation from feasible command, then investigate bounded pre-clip admission; do not relax deviation safety. Separately evaluate history-aware70–75onset with current evidence/predictive withdrawal retained. Full controller/native/corpus/transition/abort proof required for any later prototype; no fix/prototype installed or claimed here.

## Latest road review — October 21

[All new drive evidence](docs/research/navigator-post-master-drives-2026-10-21/REPORT.md): seven recordings/59 segments downloaded and hash/stability verified; five moving drives use master-sync `db5842348` with unchanged child `8ccc6cf0`. No device changes; owner 1.20/0.97/settings preserved. All 40 input/disengagement groups retained.

- **22–25 mph shortfall:** 1.4 clean pre-input seconds near <private clock time> at 35.1% body /40.5% wheel response, with turn-exceeds-limit/steerSaturated alert. Still 56.5% body after 0.4 s reference shift; no rejected command in that focused window. Next: trace rising demand, packed command, rate/deviation clamps and correction admission. Hard EPS limit remains unproved.
- **74 mph excess:** 2.8 clean seconds before <private clock time> input at 127.3% body /127.1% wheel response; 0.25 s reference shift leaves 123.6%. **User reports avoiding tire debris in the lane** during the <private clock time>–<private clock time> inputs: annotate as debris avoidance, not confirmed tracking-failure takeovers. Independently investigate calibrated target/unwind; no lane-crossing or master-regression claim without further evidence.
- **55–65 mph steady:** 105.2% over 13.55 s and 103.4% over 16.10 s respectively. 64–70 mph unwind remains open with only 4.5 s; timing explains part of observed excess. No causal before/after improvement established.
- No active steering faults or CAN-invalid samples. Seven active steering rejection echoes are brake-associated. Inactive startup/shutdown temporary faults, a brief inactive low-speed RX-check warning, and pre-state startup supply flags retained separately. Big model/zero frame drops during assistance.
- **Evidence gaps:** no clean 13–17 mph demand; only 0.4 s at 15–20 mph; 35–50 mph has only 2.9 steady seconds. Maximum 74.6 mph, so no new 75–85 mph validation. Do not treat 45 mph as calibrated. Road behavior after master is observational; child controller unchanged.

## Latest local upstream merge — October 20

[Merge and checks](docs/research/navigator-upstream-sync-2026-10-20/REPORT.md): local parent `db5842348` merges upstream `1ace967a7`, retaining child `8ccc6cf0` and owner 1.20/0.97. Branch clean; minimal/full/Panda Mac builds,1,021parent tests,4,263child tests,UI regressions and20/100Hz stall scenarios pass. Two settings conflicts preserve Navigator offroad controls while adopting upstream initial-speed UI and ExperimentalMode removal. No new child commit or fresh full-corpus replay; no ARM/road proof for this merge.

**Published and installed; ignition-off and powered stationary acceptance passed.** Comma now runs `db5842348`/unchanged child `8ccc6cf0`. [Deployment record](docs/research/navigator-master-sync-installation-2026-10-20/REPORT.md): fresh verified private backup and whole previous install retained; full ARM build,750 native tests/12,063 subtests and14 parent tests pass. Runtime harness adaptation and exact six parameterized base-class skips documented; retained child matrices explicitly carried by source identity. Owner 1.20/0.97,settings,learned calibration,update pause,stockACC/AlphaOff,firmware/launchers andAGNOS19.9 preserved. **Powered stationary acceptance passed:** 55 seconds, big model20Hz/zero drops, no CAN/steering/Panda/supply faults, all topics alive/valid, learned calibration retained. No road proof for this master merge yet. MADS and Ford longitudinal repair remain separate workstreams.

## Recommended QoL direction — October 20

[Current-master/Autospeed/MADS/longitudinal assessment](docs/research/navigator-qol-priorities-2026-10-20.md) recommends closing the latest steering trial with road review, refreshing upstream locally, then optional default-OFF MADS with stock ACC as the next convenience feature. Ford command coordination plus Autospeed is the larger eventual capability project. These are recommendations, not authorization to merge, implement or install.

Fresh master `1ace967a7` is21 upstream commits beyond the current source base, with13 custom parent commits retained. Master makes former Experimental planning the Autospeed default on supported cars, removes Chill/ExperimentalMode selection, and still requires working openpilot longitudinal actuation. Version 0.11.3 has a placeholder release date. The paired child/Panda upstream pins and AGNOS manifest are unchanged in this interval; preserve the custom child,1.20/0.97 and explicit Alpha opt-in. No merge/device change performed.

[Draft longPR3](https://github.com/adgower/openpilot/pull/3) remains separate on old navigator-angle-v1; not in the installed pair and not road-validated. Current BluePilot has braking/propulsion mutual exclusion and highway coasting changes, but still recommends stock Ford ACC. MADS and ICBM are different features. **85 mph stability remains unproved**; use saved83/85 mph episodes now and retain the need for representative legal-speed road evidence. Latest onset patch affects60–70 mph and preserves>=75 mph replay output.

## Earlier unwind installed — October20

[Installation record](docs/research/navigator-earlier-unwind-installation-2026-10-20/REPORT.md): published and installed exact pair `f7b0c47d2`/`8ccc6cf0`. Fresh device/Mac backup verified,whole previous install retained. Full isolated ARM build,750native tests,retained320/480/714transitions,128aborts,new714onset transitions/128aborts andCard/IPC checks pass. Ignition-off acceptance passed; **powered stationary acceptance passed**. Owner 1.20/0.97,all settings,learned hashes,firmware/launchers andAGNOS19.9 preserved. Physical60–70mph improvement remains unproved;28mph deviation issue remains open.

## Latest paired integration — October 20

[Earlier bounded unwind onset paired build](docs/research/navigator-paired-earlier-unwind-build-2026-10-20/REPORT.md) is committed locally: openpilot `f7b0c47d2`, opendbc `8ccc6cf0`, with the child pinned and both checkouts clean. Minimal, full/development and Panda Mac builds pass, including post-commit builds; 1,018 parent tests, 4,263 child tests, 72 focused tests, 714 transitions and 128 abort cases pass. Exact port and 86,400 factory-equivalence updates carry the accepted 819-segment evidence; no fresh integrated full-corpus replay claimed.

Owner 1.20/0.97 and protected steering/safety sources remain unchanged. **Not pushed or installed; Comma untouched.** Physical tracking improvement remains unproved; 28 mph deviation work remains open. Next gate is separately authorized publication, backup and device validation.

## Latest local unwind-onset prototype — October20

[Earlier bounded unwind onset](docs/research/navigator-earlier-unwind-onset-prototype-2026-10-20/REPORT.md) accepted locally:53recordings/819segments, 4,735,309generated-controller updates per variant, zero additional native rejections; exact shared-rejection parity.60focused tests,714transition cases and128abort cases pass;32abort cases start with new correction active.14,000shadow-intent updates and full stored-command envelope audit pass.

-Saved67mph/69mph encoded onset moves earlier by0.249s/0.101s. Reuses confirmed distinct histories during withdrawing60–70mph demand; existing wheel/body guards, caps, rate and predictive release retained. Physical tracking improvement is unproved.
-Default-off recorded stream and replayed below60mph/40–50mph/>=75mph output unchanged.28mph clipped window unchanged. Owner 1.20/0.97 and native safety preserved; paired sources clean. **Report-local only; not integrated, built or installed. Comma untouched.**
-Next gate: paired integration/build checks, then separately authorized hardware/road validation. Retain28mph authority/model and lower-demand allowance issues as separate open work.

## Latest local diagnosis — October20

[28mph deviation and64–70mph timing investigation](docs/research/navigator-deviation-unwind-timing-2026-10-20/REPORT.md): saved logs only; paired sources clean and device untouched,1.20/0.97 preserved.

-28mph tight entry requests2.83m/s² while body/wheel indicate~1.9. Native clip verified in32/32 wire+shadow updates. Fixed/calibrated mismatch exists, but does not explain away the physical shortfall. Possible EPS authority limit remains unproved in this rising-demand episode. Lower-demand23–29mph shortfalls are unclipped and often allowance-aborted/spent; widening the native limit will not resolve the band.
-Exact-parity highway trace shows~0.35s from body-margin crossing to first encoded correction;20/29 admission bursts end before five-update persistence. Final slew is not binding. Next candidate: bounded earlier onset using already validated distinct wheel/body history, retaining all current guards and predictive release. Full controller/native replay and transition/abort proof required before integration. **Diagnosis complete; no control fix or physical improvement claimed.**

## Latest road evaluation — October20

[All new recordings reviewed](docs/research/navigator-post-calibrated-rearm-drives-2026-10-20/REPORT.md): five recordings/35segments downloaded and hash/completion-verified; two moving drives use installed f750/de70, two use the previous pair and one is stationary. No device changes; 1.20/0.97 preserved.

- **23–29mph remains open:**7.4clean seconds,78.6% body/79.1% wheel response; no matched previous/new low-speed comparison. At27.5–29.5mph before steering pressure,1.65s at67.7% response. Exact-parity diagnostic replay shows native deviation clipping, so the added correction is withheld. Brief earlier mid-speed activation is confirmed; investigate mapping/native-reference disagreement locally without relaxing safety limits.
- **64–70mph unwind remains open:**11.2clean unwinding seconds at127.8% body response. A small same-location/phase/speed/demand/roll matched steady subset improves114.1→107.3%, but matched unwind does not129.0→132.7% over1.95s. Correction activation is confirmed, road benefit unresolved; diagnose admission/release, delay and effective packed output locally.
-17input/disengagement groups retained. Prioritize27.7mph pre-input shortfall and67mph excess before63.5mph pressure/brake episode; flags do not prove driver intent or lane crossing. No active steering fault/CAN-invalid samples; one inactive startup supply-fault sample retained.
-Below20mph is not calibrated;13–17mph has only2.25clean seconds.35–50mph remains sparse,45–50has no meaningful clean demand, and no new>=70mph coverage. Keep45mph subject to evidence, not assumed perfect. Full all-speed tables and event timestamps are in the report.

## Latest installation — October20

[Calibrated/mid/unwind/rearm installation](docs/research/navigator-calibrated-rearm-installation-2026-10-20/REPORT.md): parent`f750d756ca`pins child`de70d4f945`. Installed; ignition-off and powered stationary acceptance passed. First ordinary road evaluation completed above; target issues remain open. Owner 1.20/0.97,settings,geometry,native safety and AGNOS/firmware preserved; fresh post-drive device/Mac backups verified,whole previous install retained.

Fresh ARM build,690native tests/12,063subtests,320/480retained transition cases,714calibrated cases,128abort cases and Card/IPC pipeline checks pass. First attempt aborted on ignition; full fresh parked retry passed before activation. Next: ordinary supervised matched road evidence. Physical15/24/26mph and64–70mph tracking improvement remains unproved; preserve35–50mph and upper-speed evidence gaps.

## Latest paired integration and build checks — October 20

[Calibrated/mid/unwind/rearm integration](docs/research/navigator-paired-calibrated-rearm-build-2026-10-20/REPORT.md) committed locally: parent`f750d756ca`pins child`de70d4f945`, both clean. **Published and subsequently installed; see latest installation and road evaluation.** Existing prerequisites,1.20/0.97,geometry/native limits/settings preserved.

-103focused tests; full parent1,018tests/343subtests and child4,203tests/24,673subtests pass. Configured incremental minimal/development/Panda Mac builds pass again at committed revisions.
-714transition cases/228,480frames,128active-abort cases and70,560actual-factory equivalence updates pass; independent review found no material findings. Prior766segment controller/native evidence carried by exact source/factory equivalence, not a fresh integrated full corpus run.
-Next gate: separately authorize publication, private backup and device staging/build/parked acceptance. Physical tracking benefit remains unproved.

## Additional road evidence during integration — October 20

[Two new recordings/18segments](docs/research/navigator-post-rearm-build-drives-2026-10-20/REPORT.md), starts10:48and11:00CDT, use the prior installed pair unchanged; downloaded/hashed and preserved privately. All22input/disengagement groups retained.

-24mph pre-input shortfall remains:1.7clean seconds at70.4% median body response.65–70mph unwind has10.8s at131.0% body/122.4% wheel response; lag sensitivity explains part of the excess. These are observational findings, not a test of the new integration.
-No clean meaningful13–17mph demand;40–50mph has only0.4clean seconds and no steady window. No new>=75mph coverage. Keep these data gaps open.
-No active steering faults/CAN-invalid samples, permanent steering or supply/Panda faults. Four active-mode0x3d6 rejection echoes are brake-transition-associated; preserve safety cancellation.

## Latest local controller replay — October 20

[26 mph rearming and full controller replay](docs/research/navigator-mid-rearm-controller-prototype-2026-10-20/REPORT.md): resolution-aware quiet detection resolves the saved rearming blocker without changing gains, exposure budgets, one-second dwell or native limits. **Report-local only; paired branches and Comma unchanged, 1.20/0.97 preserved.**

- Full generated-controller replay passes: 46 recordings /766 segments /4,432,831 updates per compared variant, zero additional native rejections (two shared inactive/not-allowed 0x83 rejections retained). Recorded and causal-calibration-fixture streams use independent native hooks and original RX/timing.
- 91 focused tests,714 transition cases/228,480 frames and128 active-abort cases pass. Default-off generated output and protected30–60mph and>=75mph output remain byte-identical to reference.
- Saved26mph episode rearms after21 fresh frames/1.0004s, then adds seven bounded packed commands before catch-up withdrawal. Later native deviation clipping remains; physical improvement is unproved.
- Next gate: integrate the combined calibrated/mid/unwind/rearm prototype into the paired branches and run build checks. Hardware and road proof follow separately; no device change under this task.

## Latest local prototype — October 20

[Calibrated feedback /25–30mph /unwind prototype](docs/research/navigator-calibrated-mid-unwind-prototype-2026-10-20/REPORT.md) complete as a report-local artifact. **Not integrated or installation-ready; device and paired branches unchanged.**

-78focused tests,714transition cases/228,480updates and128active-correction abort cases pass. Original-send-time native replay covers46recordings/766segments, with zero additional rejections (232shared reference/candidate rejects retained). Protected recorded30–60mph and>=75mph output is unchanged, including40–50mph and saved83mph incident.
-23mph calibrated feedback admits6changed command frames/3packed signals, but retained fade/exposure makes effort small.29mph bounded allowance changes15packed signals. Highway encoded differences versus the same older baseline rise from9to64samples; this is command effectiveness, not a measured handling improvement.
-**Main26mph shortfall remains unresolved:** an earlier mid episode aborts without valid quiet rearm; later deviation clipping also blocks effort. Investigate resolution-aware valid rearm/headroom without refilling on turns/resets or widening native limits. Prior15mph fixture has one earlier-release frame retained for regression review.
-Next local gates before integration: rearm/effectiveness review, generated CarController/context replay and paired build checks. Preserve1.20/0.97; hardware and physical tracking proof remain separate.

## Latest local mechanism diagnosis — October 20

[23–29 mph and64mph investigation](docs/research/navigator-shortfall-unwind-diagnosis-2026-10-20/REPORT.md) complete; paired production source and device unchanged. Full-session instrumented replay exactly matches the existing command arrays.

- **23mph:** calibrated wheel/body deficit is confirmed on six frames but original fixed-pinion catch-up veto blocks all six; budgets are unused. Native feedback estimates about82% tracking versus calibrated wheel/body about60%. Reconcile experimental admission measurements before increasing gain or budget.
- **26–29mph:** below25mph correction is outside scope. At26mph the existing measured-curvature deviation clip also binds; at29mph calibrated wheel/body agree on a sustained deficit without range/slew binding. Treat25–30mph as a separate bounded experiment, preserving native limits.
- **64mph:** wheel trim repeats the60–70mph speed weight; confirmation resets frequently. Only nine packed path-angle samples differ from the preceding policy despite69 floating-point changes. Body-response lag explains part of the127–129% figure, while measured wheel unwind error remains about0.75–0.83degrees.
- **Next:** locally prototype consistent application-frame admission, an explicitly scoped25–30mph design and effective bounded unwind weighting/history. Preserve1.20/0.97, native safety/abort/release bounds,40–50mph parity and protected upper-speed behavior. Require focused tests, encoded-command evidence, full replay and builds before any installation; no road benefit claimed yet.

## Latest road evidence — October 20

[All new drives reviewed](docs/research/navigator-post-sustained-drives-2026-10-20/REPORT.md): 26 segments across three recordings (two moving), installed parent `0171b897` / child `4167433e`, settings and 1.20/0.97 unchanged. No device changes during analysis.

- **15 mph: untested.** No meaningful active demand at 13–17 mph and no sustained-extra activation. Need ordinary safe broad-bend data; do not hold engagement to collect it.
- **64 mph unwind: unresolved.** Extension changed 69 active command frames. Same-phase road matching gave approximately129% current versus127% previous body response over only4.45s of unwind observations; no improvement or causal regression proved.
- **Next local diagnosis:** saved23–29mph turn-entry/admission episodes, especially08:58:47,<private clock time> and09:18:11CDT; preserve current factors. Inspect existing60–65mph unwind evidence before tuning.
- All20 input/disengagement groups documented. No new coverage above65.23mph;35–50mph steady-demand proof remains sparse. Three active-mode rejected steering echoes coincide with brake transitions; retain safety cancellation behavior and investigate timing rather than bypassing it.

## Goals

1. Use the stock openpilot Chestnut foundation on the Navigator while retaining the useful Ford steering behavior from BluePilot.
2. Make steering predictable across speed ranges, preserving the owner's 1.20/0.97 calibration and good behavior around 45 mph.
3. Improve Ford brake/propulsion coordination so openpilot longitudinal and upstream Autospeed (formerly Experimental planning) can be evaluated, preserving stock ACC until validated.
4. Add independent steering and cruise engagement similar to MADS, allowing manual speed control with lane centering.
5. Keep paired branches, backups, validation evidence, and rollback instructions identifiable for every installation.
6. Work toward first-party Lincoln Navigator support through focused upstream opendbc/openpilot PRs with reproducible evidence. Maintainer acceptance and supported scope remain separate from personal-fork functionality.

## Priority and board

Priority is a qualitative WSJF assessment, not a measured score. October20 recommendation: close the current steering trial, maintain the paired baseline, then optional MADS with stock ACC for near-term convenience. Ford longitudinal/Autospeed is the next larger capability track. Keep targeted steering evidence review alongside those tasks; avoid broad gain changes without a demonstrated deficit.

| ID | Card | Status | Priority | Next action | Stuck area or dependency |
| --- | --- | --- | --- | --- | --- |
| NAV-01 | Verify tracking across speed ranges | Earlier bounded unwind pair installed; powered Park checks pass | Close current trial | Review next ordinary drive and saved83/85mph path/unwind/takeover windows; preserve1.20/0.97 | Latest60–70mph physical benefit unproved;28mph deviation issue and85mph road proof remain open |
| NAV-02 | Package a reproducible baseline and rollback | Paired branches installed; private backups and final normal boot verified | Supporting requirement | Retain backups; package replay in CI, audit legacy log-retention applicability and verify the fork update path | Exact OS/firmware rollback remains untested; model-download retry does not fix dirty Git updates |
| NAV-03 | Evaluate Ford longitudinal coordination | Paired local integration committed; full Mac/Panda builds and parent/child suites pass | Next larger capability project | Publish exact pair and perform backup/fresh ARM/offline/parked acceptance only under separate installation scope | Physical grade/restart/comfort/shaking/fuel unproven; keep existing device configuration until validated installation |
| NAV-04 | Add optional MADS independent engagement | Researched; recommended next convenience feature, not implemented | Next feature after baseline refresh | Specify Ford buttons/brake/cancel/DM/fault/resume states; defaultOFF; retain stock ACC and matching Panda/application/UI behavior | Cross-layer safety/permission integration; not a one-line latActive change; distinct from ICBM speed buttons |
| NAV-05 | Evaluate anti-weave smoothing | Research candidate | 4 | Determine whether command oscillation contributes to the saved hunting windows; evaluate separately from calibration | Filtering may affect response timing; no Navigator proof of benefit |
| NAV-06 | Evaluate automatic angle-factor calibration | Offline gain/bias/delay estimator implemented; onboard auto calibration not integrated | 5 | Use whole-route validation and abstention results to scope a supported command-map candidate | Current low-speed map lacks held-out support; broad60–70 prediction works but delay is ambiguous. No automatic factor writes or new steering tune |
| NAV-07 | Adopt upstream mass normalization | Installed; first road recording analyzed | Part of NAV-10 | Retain normalized model tests and investigate remaining low-speed response | Low-speed undertracking remains; no controlled old/new model comparison |
| NAV-08 | Verify Chestnut operation on this installation | Parked and first road recording show sustained big-model inference | Separate foundational check | Continue normal-drive reliability observation | This recording has zero reported frame drops and no sampled supply faults; long-term reliability remains unproven |
| NAV-09 | Determine factory parking-assist hardware requirements | Research waiting on evidence | Later | Find OEM assembly mapping and compare with confirmed APA 2.0-equipped vehicles | RJ6T-14H102-BAH software identification is insufficient; no implementation planned from current evidence |
| NAV-10 | Maintain current upstream openpilot foundation | Local master merge db5842348 checked; not pushed/installed | Foundation local step complete | Keep candidate separate; adapt future installer checks to ExperimentalMode removal and new initial-speed preference before any authorized staging | Mac source/build proof is not ARM/road proof; preserve explicit Alpha/stock-ACC choice |
| NAV-11 | Upstream native Navigator identification and vehicle definition | Planned PR track; evidence audit pending | After reproducible baseline | Separate Navigator from the forced Expedition override; assemble matching, geometry, hardware/harness and regression evidence for a focused opendbc PR | Forced recognition currently masks natural identification; SWB/L variants and parameter provenance must be distinguished |
| NAV-12 | Upstream Navigator/Ford angle-control and paired safety changes | Planned PR track; not submission-ready | After NAV-01 and NAV-11 scope review | Isolate justified control/protocol changes, add paired tests and reproducible logs, and prepare focused opendbc PRs with an openpilot dependency PR if needed | Experimental personal gain tuning and incomplete road evidence are not a generic Ford support claim; maintainers must agree on design |
| NAV-13 | Upstream Ford brake/propulsion coordination if validated | Planned follow-up; candidate only | After NAV-03 | Establish actual vehicle benefit and platform scope before preparing a separate opendbc fix PR | Replay passed earlier, but highway issue remains unproven and brake-release behavior needs validation |
| NAV-14 | Explore Comma control of factory Auto Start/Stop | Passive state changes captured; actuation unresolved | Later | Confirm genuine request protocol; offline one-bit candidate exists but current native safety rejects it and factory acceptance is unknown | Six rapid selected/deselected transitions visible; expected button-request signals do not show pulses; current Panda allowlist has no actuation support |
| NAV-15 | Show useful steering and runtime diagnostics | Availability distinguished from control/limit/capability; delay provenance checked | Alongside NAV-01 | Show availability as status, never measured authority; expose delay estimate and admission speed/source alongside request/response | Current delay is fixed at 0.262 s with full calibration, but estimator admits only above 50 mph; no low-speed calibration or torque map established |
| NAV-16 | Separate camera and learned steering resets | Research candidate from bp-exp | Later maintenance improvement | Audit current reset semantics; preserve learned delay/vehicle/torque values during camera-only reset where appropriate | Requires deliberate offroad reset choices and tests; no current reset behavior changed |
| NAV-17 | Evaluate compatible model packages and resilient downloads | Research candidate; not integrated | Later | Pin model/parser/tinygrad/warp/Chestnut compatibility; retain verified cached artifacts | bp-exp README gates Chestnut off; current big model already works, so broad selector port has low immediate yield |
| NAV-18 | Adopt upstream Autospeed defaults when Ford longitudinal is ready | Present in local master merge; not installed | After NAV-03 | Keep upstream planner/defaults; validate scene/max-speed behavior with reliable Ford actuation | Stock ACC does not provide model gas/brake control; no validated Navigator long fix |

“Current focus” identifies a recommended workstream, not a running job. Archived episodes can be reviewed now; new installation road benefit requires new representative observations.

## Delivered baseline

These are implemented or operationally completed, with the limits below:

- [x] Navigator short-wheelbase geometry on the Expedition profile: wheelbase 3.1115 m, historical base mass 2742 kg, steering ratio 19.6; current source uses equivalent normalized dynamics. This remains a profile override rather than independent Navigator identification.
- [x] BluePilot-derived Ford angle steering and engagement ordering on the stock openpilot fork.
- [x] Preserve the owner's 1.20/0.97 calibration and archive the original source.
- [x] Install optional paired pinion-derived feedback and optional low-speed gain trial with Comma 4 settings.
- [x] Run the local 45-segment steering replay and targeted checks. Replay compatibility does not establish all-road handling.
- [x] Back up the prior installation and retain a rollback copy before deployment.
- [x] Analyze the first post-install drive: partial evidence of better gentle-turn tracking; slower interventions still require explanation.
- [x] Temporarily pause updates after dirty-source checkout failures. Permanent updater/branch maintenance remains outstanding.

The earlier pre-migration trial drive reached 35.47 mph. Replay preserved commands at and above 45 mph in its covered data; that trial supplies no fresh 45 mph road comparison. That earlier trial used a prebuilt marker after an incomplete build. The new master integration now has a complete native build, AGNOS19.9, matching firmware and normal offroad reboot verification, without a prebuilt marker. Mass normalization is included; MADS, the longitudinal candidate, auto calibration and new smoothing are not.

## Completion criteria for the next cards

**NAV-01:** produce a source-backed explanation of the selected slow-turn discrepancies, distinguish command response from measured vehicle response, and identify a justified local experiment if needed. Any proposed change must preserve the current calibration and be assessed for oscillation and steering limits. Do not mark it fixed based only on replay acceptance.

**NAV-02:** retain durable paired source revisions and reports, identify what actually runs on the Comma, establish reproducible build status, and provide installation/rollback steps. Local commits, publication, installation, and road validation each need their own status.

**NAV-03:** integrate without replacing the newer pinion/low-speed implementation; verify braking, pitch effects, brake release, stopping/restart and disengagement with controller tests and paired replay. Then establish vehicle response before calling the highway issue resolved. Alpha actuation and Experimental planning should be evaluated separately.

**NAV-04:** agree on engagement behavior, implement matching software/firmware and visible states, and verify brake/cancel/main-off/fault/driver-monitoring transitions. Existing steering limits and longitudinal disengagement must remain coherent.

**NAV-10:** pin and record upstream openpilot/opendbc, AGNOS, Chestnut firmware/model artifacts and custom patch versions. Port the current geometry, angle steering, engagement ordering, pinion option, low-speed trial and Comma 4 controls without importing unrelated candidates. Resolve mass-normalized fields and saved-log migration. Complete build, paired controller/safety checks and replay, then prepare backup/rollback and a reviewed device migration. No OS update or feature installation is authorized merely by this planning card.

## First-party support and PR track

First-party compatibility means an accepted upstream implementation that identifies the intended vehicle without the personal forced-Expedition override, uses justified vehicle parameters and protocol behavior, and passes the applicable upstream checks. It does not automatically include Alpha longitudinal, Experimental planning, MADS, Chestnut road validation, or every personal steering preference.

1. **Evidence audit:** identify the actual model year/trim and short/long wheelbase scope, hardware/harness topology, existing passive CAN and cached firmware data, natural matching result, parameter provenance, software/firmware revisions, representative routes and known failure cases. No active ECU queries are authorized by this roadmap. Verify whether current saved data is enough before requesting any new collection.
2. **Native vehicle definition PR (NAV-11):** add the smallest justified Navigator definition/matching/docs/tests change to opendbc, preserving actual Expedition behavior. The current Navigator geometry overload must not become a supposed correction for every Expedition. Record authoritative versus inferred parameter sources; current master no longer requires a mass field.
3. **Control and safety PRs (NAV-12):** separate protocol/engagement fixes from feedback changes and tuning. Provide reproducible controller/Panda evidence, failure and recovery cases, and other-Ford regression coverage. Assess whether pinion feedback is suitable for upstream use; personal 1.20/0.97 and the trial gain map are not automatically upstream defaults.
4. **Parent integration:** prepare an openpilot PR only for required parent integration, dependency updates or other parent changes. Native vehicle support may primarily belong in opendbc; two repositories do not necessarily require two equally large PRs. Respect the maintainers' dependency/release workflow.
5. **Longitudinal PR (NAV-13):** submit separately only if vehicle evidence supports the coordination change and its scope. Keep the highway symptom and the established command difference distinct.
6. **Submission and acceptance:** for every PR record URL, exact head/base, evidence, current-head CI, review requests and unresolved comments. PR creation, publication, merge and release availability are distinct states. Do not mark first-party support complete until the necessary upstream changes are accepted and their actual distribution status is verified.

MADS, automatic calibration and experimental low-speed trial settings remain personal-fork candidates unless separately justified and accepted upstream. Keep private backups, credentials and device identifiers out of public commits; plan any shared route evidence deliberately. No upstream PRs have been created by this roadmap update.

## Settings preservation and installation approach

The [device settings inventory and migration checklist](docs/research/navigator-migration-settings-2026-10-14.md) records fresh observed preferences, launcher overrides, source tuning and installed workarounds. Create paired fork branches: custom opendbc commits plus an openpilot gitlink that references them. The intended outcome is a clean reproducible installation, not continued device-only patches.

A factory reset is not inherently required. Prepare a tested SSH-assisted branch installation or fork-installer path with a separate AGNOS/firmware/model update and rollback plan. Preserve the temporary update pause during preparation and deliberately revisit it after the new fork's update path is verified. Do not copy the old OS pin or prebuilt marker into the new build to bypass compatibility checks.

## Branch and device reference

Latest installation evidence is a saved receipt, not continuous device monitoring. Current research made no SSH connection.

| Item | Last documented state |
| --- | --- |
| Installed paired branch | `codex/navigator-tracking-release`; parent`f7b0c47d23de697b73f1247cd5d32021b37e19bc`,child`8ccc6cf0ee123afddddbf6e0a0ea3d3316669a5e`; powered parked acceptance passed |
| Current local paired checkouts | `${USER_HOME}/Apps/openpilot/.navigator-master-integration-20261014` at`db5842348` and its `opendbc_repo` at`8ccc6cf0`; clean,local-only merge |
| Longitudinal candidate | DraftPR3,`codex/ford-longitudinal-coordination`; parent`d8123f013`,child`d5ccadb7`; older navigator-angle-v1 target, not installed |
| Latest verified backup | `/data/navigator-backups/<private timestamp identifier>-pre-earlier-unwind`; verified private Mac copy`${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-earlier-unwind` |
| Complete previous installation | `/data/navigator-previous-earlier-unwind-<private timestamp identifier>` retained |
| Update/actuation preferences | DisableUpdates=true; all existing steering opt-ins retained; AlphaLongitudinalEnabled=false,ExperimentalMode absent/off in the saved installed-state receipt |
| Installed AGNOS |19.9; no OS/firmware changes during latest install |
| Fresh upstream master | `1ace967a7e27d2537a956c683978f646d6b6d739`; now included by local merge`db5842348`; not published or installed |
| Upstream dependency snapshot |opendbc`b3bd79a659dae961af169a3baac723961f720133`,Panda`a59195163c32a3a375ea6c86715dc08fd0984c1b`,msgq`a95f3c1c5e7a4d84b193433a2a04d20c7a72878c`; custom opendbc pin must be preserved |
| Latest road status |Current earlier-onset revision has parked proof; physical tracking improvement and85mph stability unproved |

No GitHub Project or Trello board is connected to this file. It remains the local planning reference. Historical installation records below retain their original dates and states.

## Evidence and detailed plans

- [EPS availability, command delivery, delay and local correction investigation](docs/research/navigator-eps-authority-investigation-2026-10-14/REPORT.md)

- [Low-speed stall-rescue comparison and new EPS availability evidence](docs/research/navigator-stall-rescue-comparison-2026-10-14/REPORT.md)

- [Bounded tracking local prototype and full 72-segment replay](docs/research/navigator-bounded-tracking-prototype-2026-10-14/REPORT.md)
- [Current fork/PR feature ideas and priorities](docs/research/navigator-fork-ideas-2026-10-14.md)

- [Feature inventory and provenance](docs/research/navigator-branch-feature-list.md)
- [Latest drive analysis](docs/research/navigator-post-trial-analysis-2026-10-14/REPORT.md)
- [Low-speed response investigation](docs/research/navigator-low-speed-response-2026-10-14/REPORT.md)
- [Low-speed prototype](docs/research/navigator-low-speed-prototype-2026-10-14/REPORT.md)
- [Pinion implementation and replay](docs/research/navigator-pinion-implementation-2026-10-14/REPORT.md)
- [Deployment and backups](docs/research/navigator-deployment-2026-10-14/REPORT.md)
- [Longitudinal coordination candidate](docs/research/navigator-longitudinal-coordination-2026-10-14.md)
- [MADS exploration](docs/research/navigator-mads-exploration-2026-10-14.md)
- [Automatic calibration and smoothing](docs/research/navigator-autocal-exploration-2026-10-14.md)
- [Mass normalization](docs/research/navigator-mass-removal-exploration-2026-10-14.md)
- [Parking hardware investigation](docs/research/navigator-active-park-assist-2026-10-14.md)
- [Historical Chestnut compatibility research](docs/research/chestnut-egpu-big-model-compatibility.md)
- [Current master and OS migration comparison](docs/research/navigator-upstream-master-comparison-2026-10-14.md)
- [Device settings inventory and paired-branch migration checklist](docs/research/navigator-migration-settings-2026-10-14.md)
- [Paired master port results, patches, bundles and remaining blockers](docs/research/navigator-master-integration-2026-10-14/REPORT.md)

## Maintaining this board

Keep card IDs stable. When work changes, update the status, next action, blocker and date together, and link the evidence. Distinguish researched, implemented locally, tested/replayed, published, installed, and observed on a drive. Move a card to delivered only when its completion criteria are met. Record a brief change entry below for decisions or material status changes.

## Progress log

- **2026-10-14:** Consolidated the Navigator goals, installed steering baseline, remaining low-speed issue, branch/build blockers, longitudinal candidate and MADS roadmap. Added calibration/smoothing and mass-normalization candidates. Priority order is provisional. This update changes documentation only.
- **2026-10-14:** Read-only live device/version audit confirmed AGNOS 19.7 and paused updates. Current upstream master requires 19.9. Added NAV-10 to plan a controlled upstream migration alongside baseline packaging; no device update performed.
- **2026-10-14:** Captured migration settings, including Alpha disabled, both steering trial settings enabled, forced Expedition identity and source-based geometry/calibration. Added NAV-11–13 for native Navigator recognition, control/safety integration and a separately validated longitudinal fix. No branches, PRs or device installation changes were made in this documentation turn.
- **2026-10-14:** Created and committed paired `codex/navigator-master-integration` branches from fresh master `6eb63e045` and pinned opendbc. Preserved 1.20/0.97, geometry, options and UI; adapted normalized fields and upstream flag collision. Child suite: 3746 passed/24673 subtests; focused parent: 23 passed; native Params/messaging and H7 build pass. Both trial-on and options-off replay CAN streams match their prior baselines across 45 segments; trial-on has zero TX rejection. Independent review found no important actionable issues. Full build/parent suite remain blocked by local model/compiler/generated-artifact prerequisites. Saved verified delta bundles. No Comma access, publication or deployment occurred.

- **2026-10-14 build follow-up:** Full minimal and development Mac builds pass after installing LLVM 20 and native prerequisites and fetching verified Git LFS artifacts. Parent suite: 957 passed, 86 skipped, 1 expected failure, 343 passing subtests. Five test files received reviewed macOS portability/collection fixes; vehicle control code, 1.20/0.97 and child c09baff5 are unchanged. Parent 6ae31161b73de2ce5043f708569759ac5f55f283 and refreshed bundles are saved locally. Publication, clean remote clone and AGNOS/Chestnut/device validation remain separate. No Comma access or changes.

- **2026-10-14 pre-install parity audit:** Known custom steering features and persistent preference registrations are preserved; recorded-input command equivalence is established. Whole-stack no-regression is not established because AGNOS/models/firmware/upstream behavior change. Saved [migration parity assessment](docs/research/navigator-master-integration-2026-10-14/MIGRATION_PARITY.md) with settings preservation and parked verification gates. No fresh device access, publication or installation.

- **2026-10-14 publication:** Published both Navigator branches at parent 6ae31161b / child c09baff5. Verified remote SHAs, a clean remote clone, all pinned submodules and an actual upstream LFS model download. Saved [publication evidence](docs/navigator-reference/PRIVATE_ARTIFACTS.md) and [installation/recovery plan](docs/research/navigator-master-integration-2026-10-14/INSTALLATION_PLAN.md). DisableUpdates does not block OS/firmware compatibility updates on first launch. No Comma access or changes; parked inventory/backups/recovery remain before migration.

- **2026-10-14 live backup:** SSH inventory confirms AGNOS 19.7/slot A, installed overlay, Chestnut ed4e39b7, existing trial preferences and 1.20/0.97. Full private application/configuration/parameter backup saved on Comma and Mac; SHA256, gzip/content checks and calibration/source/settings consistency pass. See [backup record](docs/research/navigator-master-integration-2026-10-14/DEVICE_BACKUP.md). No update, flash, reboot, service stop, source switch or active ECU query. OS/firmware recovery and target installation remain pending.

- **2026-10-14 staging/recovery:** Staged parent 6ae31161b / child c09baff5 separately at `/data/navigator-master-staged-6ae31161b`; all six submodules and 262 LFS asset hashes pass. Current source/settings/calibration/1.20/0.97, AGNOS19.7/slot A and Chestnuted4e39b7 remain unchanged. [Stage evidence](docs/research/navigator-master-integration-2026-10-14/STAGING_STATUS.md) and [recovery options](docs/research/navigator-master-integration-2026-10-14/RECOVERY_OPTIONS.md) saved. Mac factory recovery exists but erases userdata; exact A/B rollback and Chestnut ROM recovery are unproven, with no saved 256-byte Chestnut config yet. No build, launcher switch, reboot, update or flash.

- **2026-10-14 completed migration:** User authorized updates and confirmed physical readiness. Saved three-read Chestnut config backup privately on Comma/Mac; updated AGNOS19.7→19.9 on slot B; clean native build passed; four isolated native startup combinations passed; Chestnut8516b768 and matching Panda verified. Installed clean parent6ae31161b/childc09baff5 with 1.20/0.97, both options, calibration and paused updates preserved. Explicit ExperimentalMode=0 preserves old absent/off behavior against new default-on. Final normal reboot passes live offroad checks, no alerts. Old source retained. [Execution record](docs/research/navigator-master-integration-2026-10-14/MIGRATION_EXECUTION.md). Full-power/onroad and road behavior remain unverified.

- **2026-10-14 parked powered acceptance:** User stationary in driveway; passive one-minute check confirms live Navigator geometry, both options, Ford safety10, valid CAN, calibrated state and no reported faults/unexpected stopped processes. Actual big-model inference ~20fps, sampled mean39.43ms, zero reported drops; powered Chestnut telemetry valid. Separate Panda counters remain RX-invalid0/TX-blocked0, no faults. 1.20/0.97/source/settings unchanged. [Stationary evidence and limits](docs/research/navigator-master-integration-2026-10-14/PARKED_IGNITION_ACCEPTANCE.md). Road evaluation remains pending.

### First master-integration road analysis — October 14

The [17-segment drive report](docs/research/navigator-master-drive-analysis-2026-10-14/REPORT.md) confirms a late 14.8 mph response shortfall before driver intervention. Full trial weighting already includes that speed; extending coverage alone changes nothing. Maximum speed was 35.08 mph, so 45 mph remains without fresh road evidence. Chestnut stayed on the big model throughout sampled messages with no reported frame drops. Native recorded replay found three lateral transition-time rejections outside the selected turn, plus button rejections; these remain follow-up items. No device changes were made for this analysis.

### ~15 mph investigation — October 14

[Local diagnosis and proposed experiment boundary](docs/research/navigator-15mph-investigation-2026-10-14/REPORT.md): actual-strategy replay shows yaw/pinion switching has no command effect in the late 15 mph turn. Up to one-second response alignment reduces but does not eliminate undertracking. Primary experiment target is a separate very-low-speed conversion correction, smoothly zero by 25 mph; no numeric calibration or controller change is implemented. Raw CAN yaw remains biased, while fixed pinion again substantially improves agreement with calibrated motion. The workaround is selected; factory yaw calibration and complete handling resolution are not established. No Comma changes.

### Very-low-speed prototype — October 14

[Local prototype and replay report](docs/research/navigator-very-low-speed-prototype-2026-10-14/REPORT.md): separate default-OFF +10% conversion factor through 15 mph, smoothly fading to zero by 25 mph. Full recorded-input replay of 62 segments from four complete cached drives: 208,186 accepted candidate TX, zero generated TX rejections or checked RX-invalid frames. Default OFF matches every update; 12,425 messages at ≥45 mph remain byte-identical. All 36 prototype tests pass. Broad opendbc run has 3,746 passes plus three MISRA mutation failures caused by sandbox-denied uv-cache access; broad suite is not fully green. Physical handling benefit remains untested. No Comma changes, integration, firmware update or installation.

### Very-low-speed correction installed — October 14

[Installation, backups and rollback record](docs/research/navigator-very-low-speed-installation-2026-10-14/REPORT.md). Device now runs paired branch `codex/navigator-very-low-speed-trial`, parent `76d78d46f`, child `f50241ca`. Existing trial preferences enable the added +10% through 15 mph, tapering to zero by 25 mph; no new toggle. Fresh private source/settings backups verified on Mac; native build and final offroad acceptance pass. Owner 1.20/0.97, selected settings/calibration and Panda image preserved. Final selector replay is byte-identical to the tested prototype across 62 segments, including unchanged recorded ≥45 mph messages. Startup tap-reset prompt was closed without reset; normal manager is running. New road-response validation remains pending.

### First drive after the very-low-speed addition — October 14

[Read-only 10-segment analysis](docs/research/navigator-post-vlow-drive-2026-10-14/REPORT.md): recorded new revision confirmed; sharp 13.8/14.9 mph turns still undertrack before detected driver input. Aggregate before/after results are mixed and no slowly changing sub-20 mph matched stratum has sufficient coverage; no handling-improvement percentage is established. Native recorded replay has zero lateral rejections and ten permission-false button rejections; counters are not fully reconciled. Auto Start/Stop selected/deselected state alternates six times at <private clock time>–<private clock time>, consistent with the user's button test. State visibility is established; a usable Comma transmit request is not. New Auto Start/Stop control research card is separate from MADS/steering engagement. No device changes.

### Remaining response mechanism and Auto Start/Stop feasibility — October 14

[Local mechanism/protocol investigation](docs/research/navigator-response-and-autostop-investigation-2026-10-14/REPORT.md): equal-cohort probes show one post-patch interval largely aligns with +1 s response shift, another remains near half demand. Actual source confirms no continuous wheel-error correction in the sub-20 mph Ford conversion. Next local comparison should separate tracking correction from timing, fade additions by 25 mph, and preserve 1.20/0.97/high-speed map. No final gain or handling fix established. Auto Start/Stop offline candidate changes only the named request bit and preserves other stock fields, but the current Panda rejects it and factory acceptance is unproven; no sender or safety rule was integrated. No Comma access or changes.

- **2026-10-14:** Built report-local bounded filtered tracking prototype with current feedforward/1.20/0.97 intact, full through 15 mph and zero added term by 25 mph. Five complete cached drives/72 segments: 242,250 generated TX accepted, zero rejected, recorded ≥25/45 mph byte parity, default-OFF parity. Preserved inherited rate history; synthetic speed transitions can briefly retain an output difference despite zero extra term. No vehicle-response improvement or deployment claimed. Reviewed all six supplied fork pages in BrowserOS neo, including 17 open PRs and recent closed/commit pages. Added NAV-15–17; retained diagnostics/stall-rescue research under NAV-01, replay/storage under NAV-02, AOL/button fixtures under NAV-04. No Comma access or changes.

- **2026-10-14:** Compared BluePilot #153/#148 reactive rescue conditions with 27 cached segments from the two relevant drives. Installed fixed pinion model produces zero candidate fires across both drives/all five20Hz sampling phases; learned ratio/offset/roll sensitivity yields two near100.5/105.4s, none near the later15mph event. Newly decoded EPS availability is0 in every valid5–20mph status frame, generally2 above25mph, including the same low-speed pattern without lateral requested. Earlier [2,0,2] state/limit/capability tuple omitted availability; it did not exclude this policy. This supports further availability/authority analysis, not a claim of physical limit or pulse benefit. No comparable brief recorded reset pair proves recovery. Updated NAV-01/NAV-15; bounded prototype stays local, no Comma access or changes.

- **2026-10-14:** Audited EPS availability against installed source, the exact 2023 owner manual and saved response. No application/Panda gate uses the flag; flag-0 response is nonzero and varies, while matched boundary comparisons are absent, so firmware derating remains unresolved. GNSS/CAN median speed ratios ~1 rule out a gross unit mix-up. Selected commands reach the wire without local bounds clipping. First latest deficit persists; later response catches up with time. Recorded delay remains 0.262 s, estimator admission starts above 50 mph. Existing bounded P screened against 96 hypothetical gain/lag/delay cases: half-response improves only to ~60%, and other cases overshoot; not a road result. Persistence-admission grid discriminates selected patterns but is threshold-sensitive. Updated NAV-01/NAV-15; no source tuning or Comma changes.


### 2026-10-14 — Persistent-error prototype and saved button evidence

NAV-01: [persistent-error prototype](docs/research/navigator-persistent-error-prototype-2026-10-14/REPORT.md) remains local only. Preserves1.20/0.97, fades to zero by25mph;24 behavioral tests and full72-segment/five-drive native safety replay pass with242,250 configured TX accepted, zero rejected, defaultOFF and recorded ≥25/45mph byte parity. Persistent selected window35/40 commands changed, later catch-up window0/40. Hypothetical plants still overshoot up to19%; stale/lane-change context and threshold justification remain blockers before deployment. No road improvement claimed.

NAV-14: [Auto Start/Stop evidence package](docs/research/navigator-autostop-button-evidence-2026-10-14/README.md) saves70,808 relevant bus0 frames, exact transition payloads, native status/request decode checks, anonymous segment hashes and a verified portable ZIP. Six status transitions near the user-reported button experiment; no asserted request pulse in5,901 main request frames or2 alternate request frames. Sender/actuation remains unresolved. No Comma access or changes.


### 2026-10-14 — Tracking overshoot and context guards addressed locally

NAV-01: [release-aware candidate and paired patches](docs/research/navigator-tracking-release-2026-10-14/REPORT.md) preserve1.20/0.97, existing feedforward and25mph fade. Added observed-response admission (no blind boost), catch-up projection veto, half gain/cap, fresh state/control/model context and lane-change/blinker guards. Long-hold alternative suppressed the selected event; retained prior persistence with new guards.23 behavioral and24 staged tests pass; native Ford213 passed/79 skipped/12,063 subtests. Final72-segment replay242,250 configured TX accepted, zero rejected; defaultOFF and recorded≥25/45mph parity. Persistent event14/40 commands changed, catch-up event0/40. Original96 and expanded210 hypothetical plants no added unit-gain overshoot; assumed50% response improves only to~55%. No road fix claimed. Paired patches/defaultOFF FordPrefPersistentTracking prepared locally; device backup/build/startup/parked validation is next before road comparison. No Comma access or changes.


### 2026-10-15 — Tracking candidate installed; powered parked check pending

NAV-01: [installation receipt](docs/research/navigator-tracking-installation-2026-10-14/REPORT.md). Private device+Mac backup verified12files/1,037,386,553bytes before source change. Paired `codex/navigator-tracking-release` parent74f66e7a0bf1dc0718431532948ece2c4fb0041c / child1b965caadd4a6aea4d09985532bf7cca6c0873ca installed.24 integrated tests and actual-source full72-segment replay match prototype hashes. Native device build and trialOFF parked checks passed, then FordPrefPersistentTracking enabled and app restarted. Final offroad topics healthy/noOutput, clean source, captured preferences/calibration and1.20/0.97 preserved; no OS/firmware update. Ignition-on parked check requested and pending; no road benefit claimed. No remote publication.


### 2026-10-15 — Powered parked acceptance passed

NAV-01: [tracking installation powered checks](docs/research/navigator-tracking-installation-2026-10-14/REPORT.md) passed55seconds after user ignition-on confirmation. Vehicle remained Park/0m/s, controls disallowed; all12 topics valid/alive. Live Navigator geometry, flags15, Ford safety10, new trial enabled, Alpha/Experimental off.1,101 big-model samples~20fps/39.44ms, zero reported drops;550 Panda samples zero RX-invalid/TX-blocked/faults. Calibration calibrated, exact clean paired source;1.20/0.97 preserved. No injected queries, engagement or steering tests. Road response remains untested for this revision.


### 2026-10-15 — First tracking-correction drive: benefit unproven

NAV-01: [17-segment latest-drive assessment](docs/research/navigator-post-tracking-drive-2026-10-15/REPORT.md). Recorded new preference/source confirmed. Broad13–17mph body/wheel response36.9/45.9%→41.3/52.7%, but steady cohorts~44.4/52.6%→45.4/53.4%;42 matched-road clean pairs effectively flat with zero also-steady pairs. Detectable extra command only29/1,730 active13–17mph samples (~1.45s); rising demand delays first burst to~0.3s before intervention. Under-response remains; no causal improvement established. Next local question: ramping-demand admission with existing catch-up/freshness/driver bounds preserved. Seven Ford-mode hardware TX-blocked increments outside bursts; recorded native replay reproduces6, one remains unattributed. No Comma writes or tuning.


### 2026-10-15 — Local rising-demand admission prototype

NAV-01: [prototype/replay report](docs/research/navigator-rising-demand-prototype-2026-10-15/REPORT.md). Bounded rising-demand admission and fractional recovery veto; observed-response/freshness/lane-change/driver guards kept. Half term during rising>5%window;1.20/0.97 and speed fade unchanged. Saved weak turn extra command starts~0.947s earlier, not a road-response result.36 behavioral tests;213 Ford tests/79 skips/12,063 subtests. Full6-drive/89-segment native replay:299,496 configured TX accepted, one identical baseline/candidate rejection near28mph, zero new rejections; defaultOFF and recorded≥25/45mph parity.300 changing-demand toy cases retain a worst1.327-point aborted-turn residual increase vs installed correction; not deployment-ready evidence. Common548s rejection and turn-exit residual remain local investigation items. No Comma access or changes.


### 2026-10-15 — Stale-marker rejection and turn-exit budget investigated locally

NAV-01: [local rejection/residual report](docs/research/navigator-rejection-residual-prototype-2026-10-15/REPORT.md). The28.44mph native rejection is a stale advertised shadow-curvature marker (old C value80 outside allowed86–301; actual current intent98 passes). Offline controller adapter refreshes truthful intent before active angle TX, without changing Panda limits or actuation packets. Rising-demand extra-command integral capped at.001rad*s; spent budget survives temporary invalid-data pauses. Independent review caught and regression-tested the reset bypass.51 focused tests;213 native Ford tests/79 skips/12,063 subtests. Corrected full89-segment/six-drive replay:322,306 configured TX accepted,zero rejected vs one baseline rejection;20,227,501 physical RX frames,89 input hashes verified.1.20/0.97 and recorded≥25/45mph actuation parity retained; metadata traffic intentionally changes (+22,809 frames), so full CAN-stream parity is not claimed. Saved-turn extra onset still0.947s earlier;300 hypothetical cases reduce worst added turn-exit excess1.327→0.00761 percentage points of peak demand, not road improvement. Budget is pre-limiter/per-demand episode; hardware marker timing and actual vehicle response remain unvalidated. Report-local only, no paired branch integration, device access or changes.


### 2026-10-15 — Metadata-only local integration and fresh device backup

NAV-01: [integration/baseline receipt](docs/research/navigator-metadata-branch-review-2026-10-15/REPORT.md). Current-intent metadata fix is an uncommitted local opendbc edit on existing paired checkout; parent has review note only, child pin not advanced. Experimental rising-demand/turn-exit correction remains offline and is not runtime-integrated or installed.21 actual-controller tests,213 native Ford tests/12,063 subtests pass. Actual metadata-only full89-segment replay:322,306 configured TX accepted,zero rejected vs one baseline rejection; nonmetadata actuation identical at every speed/update. Read-only SSH source/settings backup936,435,888 bytes, hashes verified, selected settings unchanged.151 passive Panda samples: offroad/noOutput/ignition false/controls disallowed, RX valid, historical TX-blocked6 without increase;1.20/0.97 confirmed. Powered parked acceptance not verified (vehicle off). No installation, restart, param writes, OS/firmware changes or ECU queries.


### 2026-10-15 — Budgeted tracking paired integration complete locally

NAV-01: [paired integration and evidence](docs/research/navigator-paired-budget-integration-2026-10-15/REPORT.md). Parent0cc74c94f pins childd64ffcfa on `codex/navigator-tracking-release`; both clean, local-only commits. Existing opt-in selects bounded rising-demand correction; defaultOFF unchanged. Budget reduced.001→.00025rad*s after final-range/slew residual testing. Rearm requires1s continuous fresh settled quiet demand/measurement; isolated floor crossing/reversal/invalid data cannot replenish it.312 cases across both signs include explicit forced-abort execution and final slew tails: observed max final area.0019235→.0009798rad*s (~49.1% lower), all endpoints settled; not a universal or physical bound. Saved-send reconstruction retains0.947s earlier onset; generated replay has limited rising-budget/rearm exposure, documented separately. Actual final-source89-segment replay322,306 configured TX accepted,zero rejected vs one baseline reject; defaultOFF and recorded≥25/45mph actuation parity preserved.57 focused tests;268 Ford tests/79 skips/12,063 subtests; full parent970 passed/86 skipped/1xfail/343 subtests.1.20/0.97, geometry and native safety source unchanged. Mac development build checked; hardware timing, device build/boot, parked acceptance and road response remain unvalidated. No publication or Comma access/changes.


### 2026-10-15 — Fresh backup and passive baseline; no installation

[Backup/status receipt](docs/research/navigator-backup-request-2026-10-15/REPORT.md). Current clean device source/settings backed up privately;1.20/0.97 preserved.150 passive samples show offroad/noOutput/ignition off/controls disallowed, RX healthy, historical TX-blocked6 stable. Powered stationary check unverified. Device still74f66e7a0bf1dc0718431532948ece2c4fb0041c/1b965caadd4a6aea4d09985532bf7cca6c0873ca; local0cc74c94f/d64ffcfa not installed. No device source/settings changes, restart, flash or queries.

### 2026-10-15 — Separate device validation started

NAV-01: [isolated device validation record](docs/research/navigator-device-staged-build-2026-10-15/REPORT.md). Exact paired parent0cc74c94f/childd64ffcfa staged separately under `/data/navigator-validation/<private timestamp identifier>-0cc74c94f`; 89 saved segments and 262 source LFS objects verified. Isolated full device build passed, including Qualcomm models; 277 native tests and 12,063 subtests passed/79 skipped. All six drives/89 segments replayed on ARM: 20,227,501 physical RX, 322,306 accepted candidate TX, zero rejections vs one baseline; exact full-result match to Mac reference, option-OFF parity and recorded ≥25/45mph actuation parity. Candidate remains unactivated. Original clean active repositories, settings/1.20/0.97, firmware-image hashes and manager/service identity preserved; only heartbeat/offroad-uptime counters changed. Final passive offroad check passed with historical TX-blocked6 stable. Device build/offline validation complete; physical bus timing, powered parked acceptance and handling remain unvalidated.

### 2026-10-15 — Validated budgeted tracking pair activated; powered parked check pending

NAV-01: [backup/activation record](docs/research/navigator-budgeted-activation-2026-10-15/REPORT.md). Fresh verified source/settings backup on Mac and device; old pair retained under `codex/navigator-pre-budgeted-20261015-123129`. Active release branch now parent0cc74c94f/childd64ffcfa, exact ARM-replayed candidate. Existing tracking opt-in selects new bounded strategy;1.20/.97, geometry, options/update pause, persistent calibration, AGNOS19.9 and signed Panda image preserved. Initial overly strict live-CarParams comparison stopped startup and restored old source; documented manager-start state reset handled correctly on retry. Final ignition-off acceptance passed201 Panda samples, TX-blocked0, no faults/unexpected stopped required processes. Waiting for ignition-on in Park before powered acceptance; road response not yet evaluated.

### 2026-10-15 — Budgeted pair powered parked acceptance passed

NAV-01: [powered acceptance](docs/research/navigator-budgeted-activation-2026-10-15/REPORT.md). Owner confirmed ignition on/in Park.55.01s check passed:12 topics alive/valid,0m/s/Park/assistance disengaged/no alerts;550 Panda samples Ford10, zero RX-invalid/TX-blocked/faults;1,101 big-model samples20fps/39.72ms, zero reported drops and no Chestnut supply fault. Exact clean installed0cc74c94f/d64ffcfa;1.20/.97, geometry, update pause and options preserved. Decoded learned steer ratio/average offset/delay retained; normal ignition-on cache/state refresh distinguished from reset of owner calibration. Road response of this revision remains untested.

### 2026-10-15 — All retained post-<private clock time> logs assessed; 15mph result inconclusive

NAV-01: [71-segment assessment](docs/research/navigator-post-budgeted-drives-2026-10-15/REPORT.md).16 parked +55 driving/stopped segments, four moving stretches, all on0cc74c94f; source/child/settings preserved.13–17mph:76.6s travel,71.8s selfdrive/stock cruise disabled,2.9s actual active angle requests,1.0s clean meaningful demand, no steady/matched-road pairs and no reconstructed added term in that band; no improvement percentage established. Best new fixture is21–22mph near08:33:51CDT: body/wheel response~59/64% in0.70s clean window before driver input; reconstruction shows waiting/catch-up withdrawal and only tiny pulses. Zero rising-budget use/rearm, so increasing budget is not the supported next change. Next local task: test request-jitter/recovery/hold continuity while retaining genuine-unwind release, driver/freshness guards and aborted-turn residual bounds; add direct reason/term/budget telemetry. Highway usable bends closer to target; preserve1.20/.97 and45mph behavior.

NAV-02/steering robustness: actual Panda rejected-frame echoes fully reconcile20 moving TX blocks:18 redundant cancel packets and2 brake-edge active steering packets. Host-order native replay reproduces13; actual echoes identify the additional6 cancel+1 steering event. No steering reject coincides with the low-speed deficit windows. Investigate conservative app-side brake/cruise-off/cancel gating locally; keep firmware safety limits unchanged. Eleven other echoes occur during stationary startup/shutdown and are separate from the20 moving count. No source/settings writes, restart or ECU queries during analysis.

NAV-04: latest drive demonstrates low-speed engagement availability matters separately from steering gain: stock cruise/selfdrive disabled for93.7% of sampled13–17mph travel; profile min-enable20mph/min-steer0. MADS-style lateral independence remains separate application/UI/Panda research, not a minimum-enable constant change or a demonstrated fix for physical undertracking.


### 2026-10-15 — Local 22 mph wait/catch-up prototype replayed

NAV-01: [prototype, regressions and full replay](docs/research/navigator-wait-catchup-2026-10-15/REPORT.md). Fractional catch-up caused by a shrinking request denominator now needs measured recovery; sustained unwind retains predictive release, and newly admitted exceptions consume the unchanged0.00025rad·s episode budget. First candidate rejected for unwind weakness; final58 focused tests and552 hypothetical plant/abort cases pass with no added peak excess in the tested grid. All160 cached segments replayed:36,949,571 physical RX;577,162 configured candidate TX accepted, zero rejected; defaultOFF and ≥25/45mph byte parity.1.20/.97 and paired branches unchanged. Actual-send-time target gets four earlier continuation frames (~0.20s, peak1.34mrad difference), then budget exhaustion suppresses later pulses; no quiet rearm and no demonstrated15mph improvement. Road response remains unproven; existing actual permission-edge rejection evidence remains unresolved. Prototype stays report-local; no SSH/device changes or activation.

### 2026-10-15 — Wait/catch-up pair integrated; latest drive reviewed

NAV-01: [integration/deployment report](docs/research/navigator-wait-integration-2026-10-15/REPORT.md). New local paired9da98d0c9/18175406 commits preserve1.20/.97 and original option.188-segment replay:43,382,812 RX;682,076 configured candidate TX accepted, zero rejected; full frozen-prototype/defaultOFF/high-speed parity.284 tests+12,063subtests;552 plant cases; full Mac build pass. Fresh verified Mac/device backups and rollback refs exist. Separate ARM build/newest28-segment replay running; active pair not yet changed. Latest pre-install drive shows15mph body/pinion response disagreement (~49/71% request), no moving active-angle rejection, eight actual cancel echoes. Investigate calibration/model/alignment independently before more gain; this candidate is not proof of a15mph fix. Initial stale RTC date documented; no clock/settings tuning.

### 2026-10-15 — Wait/catch-up pair activated; powered parked check pending

NAV-01: [installation and latest-drive report](docs/research/navigator-wait-integration-2026-10-15/REPORT.md). Full isolated Comma build passed;284 native/selector tests and12,063 subtests passed; newest28-segment ARM replay exactly matches Mac. Original source/settings/service unchanged during staging. Fresh verified Mac/device backups and original-pair rollback refs retained. Active clean pair now9da98d0c9/18175406. Exact startup selector and ignition-off acceptance passed:201 Panda samples,noOutput,TX-blocked0,no faults/unexpected stopped process;1.20/.97, geometry, all preferences/persistent calibration, AGNOS19.9 and signed Panda image preserved. Powered Park acceptance awaits owner ignition-on confirmation; no road-improvement claim.


### 2026-10-15 — Wait/catch-up pair powered Park acceptance passed

NAV-01: [final installation/parked record](docs/research/navigator-wait-integration-2026-10-15/REPORT.md). Owner confirmed ignition on/in Park;55.05s passive check passed,12 topics alive/valid,0m/s/Park/assistance disengaged/no alerts or vehicle faults.550 Panda samples Ford10, controls disallowed,RX-invalid/TX-blocked0,no heartbeat/SPI/fault issues. Big model20.003fps/39.43ms/zero reported drops; Chestnut no supply fault. Exact clean9da98d0c9/18175406,1.20/.97, geometry/options/update pause/stock long retained. Learned ratio21.95196, offset−1.234525deg, delay0.25983146s and camera calibration preserved; torque-cache payload unchanged, normal timestamp refresh distinguished from setting loss. Installation and parked checks complete; road response remains to be tested.15mph body/pinion discrepancy still open.


### 2026-10-16 — Post-install road review: highway coverage; low-speed trial untested

NAV-01: [84-segment review](docs/research/navigator-post-wait-drives-2026-10-16/REPORT.md). Six retained sessions on installed9da98d0c9/18175406; 8.9 minutes active steering, entirely55–69mph. Zero active5–25mph frames and no added tracking term or budget use. Latest10:02–10:23drive confirmed manual by owner. No supported15/22mph improvement percentage or direct45mph comparison. Highway clean bends show no sustained meaningful weak-response episode; no active steering rejected echoes. Two moving cruise-cancel rejects reproduced in native recorded-TX replay. Brief first-two-second Chestnut supply flags clear; no later flags, Panda faults or reported model drops. Both source checkouts remain clean; no Comma changes. Next useful evidence is engaged15–25mph exposure; investigate body/pinion calibration disagreement separately before further gain. NAV-04 low-speed engagement independence remains a separate feature.


### 2026-10-16 — New engaged low-speed evidence; tracking correction mostly inactive

NAV-01: [afternoon63-segment review](docs/research/navigator-latest-drives-2026-10-16/REPORT.md). Three new moving sessions plus one stationary session;36.4min lateral-active,27.6s active5–25mph/no-driver requests,1.8s clean meaningful13–17mph demand. Weak windows near10:56:16CDT/14mph and12:40:04–07/19–21mph remain. Only three reconstructed extra samples; no new-versus-previous output differences. At19–21mph pinion response87–96% versus body48–57% means admission/catch-up veto cannot infer the full body deficit. Budget exhaustion/rearming is not the explanation. No causal improvement percentage. Next: local admission trace plus raw/learned calibration and wheel/body alignment audit; preserve1.20/.97 and high-speed path. Two active steering rejects at43/61mph are brake/cruise permission edges, reproduced offline, separate from low-speed windows; redundant cancel timing remains a robustness task. Exact clean installed pair unchanged; no device writes.


### 2026-10-16 — Feedback and admission explained; larger control-design decision

NAV-01/NAV-15: [local investigation](docs/research/navigator-feedback-admission-2026-10-16/REPORT.md), [proposed next design](docs/research/navigator-feedback-admission-2026-10-16/DESIGN.md). Actual14mph admission trace: demand-window variability resets hold; only three extra samples before unwind/catch-up release.11mph acceleration exceeds0.5m/s speed-spread gate. Fixed pinion proxy uses19.6/zero offset; recorded learned22.45/−2.1deg largely reconciles19–21mph wheel/body estimates. Stationary-debiased OEM CAN independently corroborates body undertracking; no DBC or native calibration changed. Five-to80mph audit supports deficits below25 but not a broad higher-speed boost. Body-only tracking feedback prototype, separate from unchanged native proxy, passes335 segments/19sessions:77,170,084RX,1,219,156accepted candidateTX, zero rejections; defaultOFF and≥25/45mph parity.11 tests and552 modeled cases pass, but target receives no useful added correction. Faster and half-gain variants give short earlier pulses with small added modeled excess; neither establishes a road fix.12.5% bounded term cannot generally compensate for a hypothetical50% steady-response plant. Next design: identify steady gain/bias/delay with uncertainty and held-out episodes before changing command map, separate transient tracking; review required before architecture implementation. Report-local prototypes only, release pair clean and unchanged, no device writes or new installation.


### 2026-10-16 — Approved calibration-first implementation and high-speed audit complete

NAV-01/NAV-06/NAV-15: [implementation/report](docs/research/navigator-calibration-first-2026-10-16/REPORT.md), [runner/code](docs/research/navigator-calibration-first-2026-10-16/README.md). Pure offline module separates transmitted-command gain, yaw bias and delay/timeconstant, conditional route-bootstrap uncertainty, per-drive prediction/dependence checks, historical whole-route CV and explicit abstentions.335retainedsegments/19sessions freshly extraction-bound to raw hashes/code/payload;31tests pass, independent review repaired cache-provenance issue and found no remaining material findings. Broad60–70mph predicts held-out drives; separate delay remains ambiguous. Narrow55/65focus estimates fail per-route/consistency gates and are not calibration recommendations. Current-release meaningful bends:55mph median112.2% request over18.95s,65mph110.1% over96.15s; no sustained below70% response in these bands. Brief65mph high-response window accompanies shrinking request; post-hoc0.5s alignment brings ratio near103%, not an identified new delay.75band contains only72.5–74mph/15.4s eligible and no meaningful bends;85mph no recordings. No exact low-speed replacement map validates: latest eligible turns too short for4s episodes and older-route folds inconsistent. No controller change proposed or installed;1.20/.97, clean paired source and native safety preserved. Durable raw/private evidence preserved withAPFSclones. Next work is held-out low-speed model/support, not another inverse-ratio gain or budget increase.

### 2026-10-16 — Low-speed evidence collection plan (awaiting drives)

NAV-01/NAV-06/NAV-15: Owner will collect more drives using the existing installation. **Keep all settings and 1.20/0.97 unchanged.** No controller calibration or device change is authorized by this collection plan. Baseline findings and selection criteria: [calibration-first report](docs/research/navigator-calibration-first-2026-10-16/REPORT.md).

Missing evidence:

- [x] First current-version, uninterrupted qualifying low-speed turn obtained: the October 16 evening collection includes one 12-second 13–17 mph episode. More episodes and independent drives remain needed; see the [collection review](docs/research/navigator-collection-review-2026-10-16/REPORT.md).
- [ ] Both left and right turns near 15 mph, with entry, a reasonably steady middle and exit, to distinguish response delay from sustained undertracking.
- [ ] Repeatability over two or three separate drives, preferably ordinary travel in both directions where practical. Retain whole drives for independent validation; do not split adjacent frames between training and validation.
- [ ] Comparable 18–22 mph and 23–27 mph turns to check persistence and the correction's fade-out, plus a short normal 40–50 mph reference section.
- [ ] Review new logs for actual lateral engagement and eligibility; travel time alone does not count as calibration coverage. Record qualifying episodes, duration, turn direction, source version and independent-drive coverage after analysis.

Practical route plan:

| Priority | Speed exposure | Desired observations |
| --- | --- | --- |
| Main | 13–17 mph | Several naturally occurring gentle left and right bends per drive, including entry and exit |
| Comparison | 18–22 mph | Similar bends to check whether the same shortfall persists |
| Transition | 23–27 mph | Behavior around the existing correction's fade-out |
| Reference | 40–50 mph | Short normal section where steering already feels good |

Choose a familiar, low-traffic route with good visibility, ordinary lane markings and gentle bends. Drive normally, with reasonably steady speed only where road and traffic conditions permit; do not force an exact speed or use sharp zigzags/intersections as calibration exercises. Maintain normal supervision and intervene whenever needed. Four seconds is an offline selection criterion, never a reason to delay an intervention. Several usable turns is an initial collection goal, not a guarantee of sufficient evidence. No 75/85 mph collection is needed for this low-speed investigation.

After parking, note approximate problem locations and whether the shortfall felt like late turn entry, insufficient steering through the bend, or excessive steering on exit. A passenger may note timestamps; the driver should not operate a phone while driving. Interventions remain useful diagnostic evidence even when excluded from calibration fitting.

Analysis and decision checklist:

- [ ] Trace planner request → transmitted steering command → measured steering → body yaw for each shortfall; distinguish limiting, delay, steady response and measurement disagreement.
- [ ] Organize evidence into approximately 10–15, 15–20, 20–25 and 25–30 mph reporting bands, while fitting speed continuously. Five-mph bins are coverage summaries, not independently tuned multipliers.
- [ ] Evaluate time-aligned steady-turn response near 100%, alongside absolute error and transient/exit behavior. An instantaneous ratio above 100% during request withdrawal, or near-zero demand, is not sufficient evidence for reducing gain.
- [ ] Validate any proposed smooth correction on separate whole drives, preserve 1.20/0.97 and good steering around 45 mph, and complete applicable replay/build checks before proposing deployment. Do not derive a map by simply inverting response percentages.

Initial plan status: awaiting new drives. **Updated below: first qualifying episode collected; physical 15 mph issue remains unresolved.** Creating this plan changed documentation only; the subsequent collection review used read-only SSH.


### 2026-10-16 — First collection review: useful 15 mph episode obtained; repeatability still open

NAV-01/NAV-06/NAV-15: [new-drive assessment](docs/research/navigator-collection-review-2026-10-16/REPORT.md), [coverage evidence](docs/navigator-reference/PRIVATE_ARTIFACTS.md). All 51 new segments downloaded and hash-verified: 23-segment <private clock time>–<private clock time> CDT session stationary; 28-segment <private clock time>–<private clock time> CDT session moving/stopped, max 38.8 mph. One session's moving stretches are not independent drives. Current factors 1.20/0.97 and clean tracked paired source confirmed read-only; no device changes.

| Plan coverage | Eligible / meaningful turning | Qualifying episodes | Remaining gap |
| --- | --- | --- | --- |
| 13–17 mph | 31.05 / 19.60 s | 1 × 12.0 s | More episodes, opposite-direction sustained turns and separate drives |
| 18–22 mph | 34.20 / 12.10 s | 1 × 9.85 s | Repeat across drives; calibration 17–20 subset still duration-limited |
| 23–27 mph | 29.90 / 5.10 s | 0 | Longer eligible turns without excessive speed drift, where naturally available |
| 40–50 mph | 0 / 0 s | 0 | Normal reference section still absent from this outing |

- [x] Latest recordings verified and stationary/moving sessions distinguished.
- [x] Current-version qualifying uninterrupted 13–17 mph episode obtained; earlier “no four-second episode” gap is now partially resolved.
- [x] Both request directions represented in meaningful 13–17 mph samples; strongest qualifying episode remains mainly one direction.
- [ ] One or two more separate moving drives with comparable gentle turns; collect additional near-15 mph episodes, especially the opposite direction to the strongest new one. Existing entry gate needs at least three held-out episodes across two routes; meeting it is not a validation guarantee.
- [ ] Repeat 18–22 mph and improve 20–25/23–27 mph transition coverage; no qualifying 20–25 mph episode collected.
- [ ] Add short normal 40–50 mph reference section when appropriate; no high-speed collection required.
- [ ] Evaluate cross-drive model consistency and entry/exit behavior before proposing a smooth correction. Keep 1.20/0.97 and good 45 mph steering.

At <private clock time> CDT a 12 s episode spans 13.94–15.48 mph; inside it a ~9.85 s weak-response window has body/request ~40.7%, OEM stationary-debiased yaw/request ~44.9%. Substantially changing request prevents interpreting this as a constant-demand gain. New evidence corroborates the deficit, not an improvement or a recommended multiplier. Historical-training/new-whole-route-holdout check still abstains: 13–17 mph 10/1 episodes, 17–20 mph 16/1, 20–25 mph 15/0; independent-route/episode coverage remains inadequate. Retain ordinary supervision and intervene/brake whenever needed; four seconds is an offline filter, not a driving requirement. Private recordings/caches preserved in CommaBackups. **Status: collection progressed; 15 mph issue unresolved; no tuning or installation.**


### 2026-10-16 — 12-second 15 mph episode traced: feedforward delivered, correction unavailable

NAV-01/NAV-06/NAV-15: [episode investigation](docs/research/navigator-15mph-episode-2026-10-16/REPORT.md). Full-session frozen-signal reconstruction matches all 241 target commands within half a 0.0005 rad wire step; transmitted commands equal feedforward alone. No target brake/override/fault, no new TX-blocked increment, no effective command range/slew clipping or >9 m/s deviation clip. Inner-window body response40.7%, learned-ratio/offset wheel40.5%, fixed pinion57.6%; learned wheel/body agree on insufficient physical steering and fixed proxy overstates recovery. +0.5 s alignment only raises response to47.1%, not100%.

New session-specific finding: reconstructed0.00025rad·s budget spent around8:57:22p.m./6mph, never rearmed before9:15:43p.m. episode. Of227 meaningful frames:119waiting,56catch-up veto,37spent-budget veto,15otherwise ineligible; zero extra term. Longest reconstructed quiet dwell0.4005s vs required1s; measured-slope gate permits only~0.0358°/50ms at15mph, below commonly observed0.1° wheel steps. These are inferred internal states, not direct runtime telemetry; exact target output parity is verified. Earlier drives' “budget not the explanation” findings do not generalize to this new session.

- [x] Trace request→transmitted command→wheel→body for strongest saved near15mph episode.
- [x] Identify session-specific correction/rearm failure to cover with regression fixtures.
- [ ] Evaluate resolution-aware quiet rearming locally with bounded budget, freshness/driver guards and aborted-turn residual checks; no unconditional reset or budget increase.
- [ ] Resolve calibrated application feedback versus unchanged native safety proxy, and collect independent low-speed drives before proposing a feedforward map.

Diagnosis only; physical15mph issue still unresolved. Existing1.20/0.97 and good45mph path untouched; no device access, source tuning or installation.


### 2026-10-16 — Resolution-aware rearm prototype and full replay complete locally

NAV-01/NAV-06/NAV-15: [prototype/report](docs/research/navigator-resolution-rearm-2026-10-16/REPORT.md), [verification](docs/navigator-reference/PRIVATE_ARTIFACTS.md). Report-local subclass permits one0.1° wheel-signal quantum in the adjacent-curvature slope test. One-second valid quiet dwell, absolutequiet0.0005/m, whole-dwellrange0.0001/m, one-shot refill,0.00025rad·s budget,1.20/0.97 and native safety remain unchanged. Test-first7fail/9pass→16pass; expanded direct/inherited87pass. Ford/native/selector284pass/79skips/12,063subtests. Independent review repaired provenance and reset/range coverage; no remaining material finding.

**Full386segment/21session native replay passed:**88,982,329physicalRX,2,235,484controllerupdates,1,400,055candidateTXaccepted,zero rejected; baseline likewisezero.19changedupdates, allbelow25mph. TrackingOFF and≥25/45mph full generated-byte parity retained. All386raw hashes verified;72completed segments retained from sequential execution, remaining routes independently replayed in parallel, no duplicate/incomplete routes counted. Clean expected paired revisions and dependency hashes checked.540modeled changing-demand+2saturation+10forced-abort cases settle;72quantized repeated-turn cases settle,32exercise more rearms, worst peak-excess increase~0.000428percentage points in that finite model grid.

**Target15mph scene remains unchanged:** latest-drive post-spend quiet dwell improves to0.7506s in signal reconstruction but still misses1s; no rearm. Native replay's240target steering frames have zero extra correction and exactly unchanged output. This validates the bounded prototype against recorded native safety, not physical improvement or deployment readiness.

- [x] Implement resolution-aware rearm as an isolated local prototype with unchanged budget/quiet/freshness/driver bounds.
- [x] Run expanded regressions, independent review, modeled residual/abort checks and full retained-corpus native replay.
- [ ] Investigate remaining continuous-quiet/admission blockers and calibrated application feedback/feedforward before another15mph correction proposal. Keep independent-drive collection plan open; do not force refill by shortening dwell or enlarging budget.

No paired branch integration, Comma access/settings changes, build or installation. Owner 1.20/0.97 and good45mph path preserved. Physical15mph issue remains unresolved.


### 2026-10-16 — Priority shifted to mid/high-speed evidence, starting30–50mph

NAV-01/NAV-06/NAV-15: Owner requested focus on higher ranges through85mph. [Current coverage and sequence](docs/research/navigator-higher-speed-priority-2026-10-16/REPORT.md). **Below25mph remains unresolved**, not marked complete; resolution-aware rearm remains report-local and does not correct the target turn.

- [x] Summarize existing current-revision normalized evidence in5mph reporting bins.
- [x] First: initial phase/route-separated30–50mph audit completed, explicitly including40–45and45–50mph; calibration validation remains open (see latest audit entry). The owner’s earlier positive45mph feel is subjective feedback, not verified tracking or an exemption from improvement.30–35mph has71.3s meaningful turning/3sessions and descriptive median99.7%;35–50mph bins have only11.2–13.1s each. Do not equate these medians with validated calibration.
- [ ] Second:50–70mph audit, using existing highway logs;60–65mph has111.65s meaningful turning/4sessions. Investigate timing/bias/entry-exit effects before any gain change.
- [ ] Third:70–85mph evidence assessment.70–75mph has8.35s meaningful turning from one session; max recorded speed~74mph.75–85mph has no exposure. No dedicated85mph collection needed; use available ordinary legal driving data.

Five-mph bins track coverage, not independent multipliers. Any eventual map must be smooth and validated across held-out whole drives; retain1.20/0.97 while investigating. Assess45mph objectively and allow evidence-supported improvements there, with handling/stability regression checks rather than an assumption that its current calibration is optimal. No Comma or paired-source changes made for this priority update.


### 2026-10-16 — Clarification: 45 mph is included in objective validation

The owner explicitly clarified that “feels good around45mph” was not a requested-versus-applied review. This supersedes earlier planning language that treated45mph as an already-correct calibration to preserve unchanged. Historical byte-parity results remain valid statements of what earlier prototypes changed; they are not proof of optimal45mph tracking.

- [x] Initial saved-data audit completed for40–45and45–50mph as first-class ranges (repeatability validation still open): planner request, transmitted command, measured wheel steering and body yaw, with physical timing alignment.
- [ ] Compare turn entry, sustained turns, unwind/exit, both directions, absolute tracking error, delay, overshoot and repeated corrections across separate drives. Treat subjective feel as additional feedback.
- [ ] Establish an objective baseline and assess any candidate improvement on held-out whole drives; retain or revise45mph behavior according to evidence, not an exemption. Current descriptive~118% response medians alone do not justify a gain reduction.

Current device settings and1.20/0.97 remain unchanged. This update changes the investigation plan only; it does not authorize immediate device tuning or claim any range is perfectly calibrated.


### 2026-10-16 — Initial30–50mph audit complete; next collection35–50mph in both directions

NAV-01/NAV-06/NAV-15: [phase/route/command audit and collection needs](docs/research/navigator-30-50-audit-2026-10-16/REPORT.md). All21normalized inputs match prior hashes; five-mph phase totals reconcile with prior coverage. Predeclared past-only1s steady-request rule (10%variation;5/20%sensitivity) separates entry/unwind timing.30–35mph steady10.9s/101.4% response, chiefly one session; rising93.6%→99.6% and unwind108.3%→97.7% with diagnostic+0.25s response shift, not an identified new delay.

35–40mph steady1.3s/117.9%;40–45mph1.35s/124.8%;45–50mph6.35s/112.9%. All40–50steady exposure has one request sign. These sparse medians are diagnostic, not gain recommendations. At45–50, learned wheel(no-roll)/request104.5%, with recorded roll113.3%, body112.9%; OEM yaw broadly corroborates body. At40–45, learned wheel95.0%→125.7% with roll versus body124.8%. Investigate directional/roll/model effects before a blanket gain reduction; roll estimate is not road-bank ground truth. Normalized wire/feedforward medians near100%; no broad command-delivery shortfall indicated.

- [x] Complete initial objective30–50mph audit, including40–45/45–50 without treating good subjective feel as proof.
- [x] Separate rising/steady/unwind phases, compare wheel/body/OEM/roll and command mapping, check sensitivity and whole-route support.
- [ ] Collect two or three more ordinary drives with gentle marked bends at35–50mph, both turn directions, particularly sustained40–45/45–50 examples. Opposite-direction travel on a familiar route where practical helps separate directional effects. Add some30–35 reference bends naturally; no forced speed/duration or delayed intervention.
- [ ] Reassess independent-route calibration support and phase/directional consistency. Broad30–50historical-trained/current-heldout fit fails residual/per-route/gain consistency; current-onlyCV has3qualifying routes vs4required. Narrow bins lack episode/route support. No new gain map validated.
- [ ] Continue50–70mph audit using existing highway recordings; new mid-speed collection need not block it. No dedicated75/85mph collection required.

Settings/1.20/0.97 and paired/device code unchanged. Lower-speed issue remains open; neither subjective feel nor these medians mark a speed range perfectly calibrated.


### 2026-10-17 — All new drives preserved;50–70mph audit and all-range evidence refresh complete

NAV-01/NAV-06/NAV-15: [full analysis and remaining needs](docs/research/navigator-speed-evidence-2026-10-17/REPORT.md), [all-range index](docs/research/navigator-speed-evidence-2026-10-17/EVIDENCE_INDEX.md), [verification](docs/navigator-reference/PRIVATE_ARTIFACTS.md). Read-only SSH downloaded all6new sessions/129segments (1,119,859,843bytes); final remote inventory exactly matches. Private raw/GPS-bearing caches preserved in CommaBackups. All515retained raw hashes reverified; expanded27session corpus,27normalized input hashes and6new extraction bindings verified. New data adds66.86min eligible active-control exposure. Live paired source remains clean9da98d0c9/18175406;1.20/0.97/settings unchanged.

- [x] Analyze saved50–70mph with unchanged phase/support criteria, then evaluate new drives separately and in expanded cohorts.
- [x] Incorporate every new session and every recorded speed band into the evidence index; distinguish travel, eligible active control, meaningful turns, steady-request fragments and fit support.
- [x] Close the specific missing opposite-direction steady40–50mph coverage: both turn signs now appear in40–45and45–50. Calibration consistency is still open.
- [x] Trace the only new≥30mph below70% window lasting≥0.5s: ~61mph at4:37:12p.m.CDT in session05. It begins immediately after engagement; actual command ramps0.009rad/20Hzframe, all160send-time reconstructed outputs match within half a wire step, Panda blocked counter stable. Initial rate limiting plus subsequent response timing makes it a transition fixture, not a steady-gain increase justification.

Expanded steady response/exposure:50–55mph109.7%/20.40s;55–60mph113.8%/49.35s;60–65mph112.2%/81.25s;65–70mph111.2%/11.20s. Combined50–70steady56.1→162.2s, median112.1%, both directions. Wire/feedforward medians near100%; learned-wheel without roll is generally nearer request than body, with recorded roll bringing model/body closer. This suggests investigating model/roll/directional effects; it does not establish causal road-bank compensation or a universal gain reduction.

The previously supported saved-only55–60transfer model was frozen for62new episodes: pooled normalizedRMSE0.0825 and every new session below0.25error gate, but session06's one episode has residual/input dependence0.4075>0.35. Expanded validation therefore abstains. Other narrow/broad models also fail or lack route/episode/consistency support. This is a model-support limitation, not a steering-fault alert; no calibration map recommended.

New mid-speed steady exposure:35–40mph5.0s;40–45mph9.4s;45–50mph27.35s. Lower13–17mph deficit remains (51.25s meaningful demand/~43.9% median, almost no steady request). Maximum recorded speed now79.68mph, but75–80only6.2s new travel/no meaningful bends;80–85no data. No dedicated85mph driving requested.

- [ ] Continue ordinary35–50mph collection, especially sustained35–45bends and independent45–50examples in both directions. Previous blanket direction gap is resolved; more sustained/independent examples remain useful. Maintain normal supervision/interventions; no forced speed or duration.
- [ ] Investigate application-side learned ratio/offset/roll propagation, per-route residuals and entry/exit timing before proposing a speed map. No special additional50–65mileage needed for that work;65–70can accrue naturally.
- [ ] Reassess current-only whole-drive consistency and any future candidate with the expanded evidence. Keep subjective45mph feel separate from objective tracking.

Analysis only: no device setting/source changes, restart, update, ECU query, firmware action or installation. No new native safety replay was run; the386segment prototype replay remains distinct from the now515segment analysis corpus. Existing1.20/0.97 remain unchanged.


### 2026-10-17 — Highway wheel/roll integration gap investigated locally

NAV-01/NAV-06/NAV-15: [source/data investigation and proposed next change](docs/research/navigator-highway-model-2026-10-17/REPORT.md).50–70steady3,244samples/162.2s/10sessions: pooled learned wheel(no-roll)/request100.6%, body112.1%, wheel+recordedroll113.8%. Fixed physics roll reduces wheel-to-body measurementMAE0.005399→0.002848rad/s (~47.2%) and improves all10sessions; this is prediction-error improvement, **not improved steering** or causal road-bank proof. Per-session roll/ratio/offset differences and estimator coupling remain relevant; no universal gain reduction justified.

Source/control-stream trace: standardLatControlAngle already computes learned ratio/offset/roll-aware desiredwheelangle; recorded target matches reconstruction (session median difference<0.003°), while actualwheel differs by~0.89–1.56° medianabsoluteerror. Ford's path-angle-primary strategy ignores that angle target, using curvature×speed×provisionalfactor; card context does not carry vehicleParameters. Upstream roll-dependent curvature limits are not equivalent to roll-aware feedforward mapping. Current extra-feedback speedweight0above25mph, so budget/rearm changes cannot fix highway tracking.

- [x] Decompose highway wheel/body/roll discrepancy and verify route-level consistency of the measurement model.
- [x] Trace calibrated target production versus Ford map consumption; distinguish missing mapping semantics from native safety geometry.
- [ ] Next local prototype: opt-in bounded/smooth calibration- and roll-aware application mapping for50–70, with existing calibrated target as reference, explicit fresh/valid parameter seam/fallback and1.20/0.97 retained. Identify desiredwheel→pathangle conversion; never send wheelangle directly aspathangle or change nativefixed19.6safety model. Preserve truthful intent metadata and all output/safety bounds; no double compensation.
- [ ] Validate candidate on515segment fullnative replay plus sign/unit/freshness/zero-demand/transition/abort tests and independent review before proposing deployment. Calibrated residual feedback only if still justified after feedforward evaluation.

Investigation only: no prototype command change, paired integration, Comma access/settings changes or installation. More special highway driving is not required before this offline prototype work;35–50collection remains useful.45mph still requires objective validation and is not exempt from eventual improvement.


### 2026-10-17 — Roll-aware mapping prototype and full515-segment replay complete locally

NAV-01/NAV-06/NAV-15: [prototype, results and limitations](docs/research/navigator-roll-mapping-2026-10-17/REPORT.md), [machine-readable verification](docs/navigator-reference/PRIVATE_ARTIFACTS.md), [independent review](docs/research/navigator-roll-mapping-2026-10-17/REVIEW.md).

- [x] Prototype an opt-in calibrated-target/roll mapping seam, with a separate application model, fresh/valid/consistent calibration gating, bounded onset and explicit fallback. Initial50–70mph blend; capped0.01rad/15%feedforward; retain owner 1.20/0.97 and nativefixedpinion model. Same-model inverse cancels ratio/offset at zero roll: this is roll-compensation sensitivity, not an identified actuator/ratio remap.
- [x] Complete27session/515raw-segment native replay:2,986,854controller updates;1,904,757TX checks accepted per variant;zero rejections.9,983pre-Ford-configuration frames per variant separately counted/unhooked. All515input hashes checked, independent native states, no controls override.23,477mapped steering evaluations;17,520generated controller updates changed. Default-off and mapping-disabled byte-parity gates pass.
- [x] Complete35focused tests and320transition/abort cases/115,200frames; preserve final range/slew and truthful intent. Independent review's clipped-sign reversal bug fixed with requested-sign reset and red/green regression. Five saved steering-frame release tails explicitly measured (peak0.00570527rad;totalarea0.000469680rad·s), native accepted; synthetic traces settle.
- [x] Verify no saved final-output differences≤50mph or≥70mph;45mph preserved against baseline, without declaring its tracking optimal. Paired heads/dependencies remain clean and unchanged9da98d0c91/18175406d0;no Comma access/changes.
- [ ] Resolve live vehicleParameters publisher/subscriber integration, arrival/cadence/freshness and safe release behavior locally before considering a deployable paired candidate. Timestamp-ordered logs do not prove live subscription timing.
- [ ] Establish calibrated actuator/path-angle transfer and roll-estimator uncertainty/causal response. Same-input native replay does not establish improved wheel/body tracking, real-world stability or hardware readiness. No universal ratio/gain change validated.
- [ ] Continue ordinary35–50mph collection and objective all-range evidence review; no dedicated high-speed collection requested. Existing lower-speed investigation remains open.

Local prototype/testing only. No paired integration, device setting/source change, reboot, update, firmware action, ECU query or CAN transmission;owner 1.20/0.97 unchanged.


### 2026-10-17 — Atomic calibration delivery, timing guards and release/rearm contract implemented locally

NAV-01/NAV-06/NAV-15: [candidate and evidence](docs/research/navigator-calibration-integration-2026-10-17/REPORT.md), [paired patches/provenance](docs/navigator-reference/PRIVATE_ARTIFACTS.md), [replay verification](docs/navigator-reference/PRIVATE_ARTIFACTS.md), [independent review fixes](docs/research/navigator-calibration-integration-2026-10-17/REVIEW.md).

- [x] Resolve separate-topic calibration race locally: additive optional CarControl snapshot from the exact producer inputs used for its angle target, including input/computation timestamps and target speed/anchors. Actual staged Controls.state_control→serialized Event/local msgq→Card.controls_update screen passes. No extra calibration publisher/subscriber or CAN sender.
- [x] Validate timing/order/freshness: legacy/missing/invalid/future/expired/reordered/changed snapshots fall back; repeated controls expire; producer speed prevents receiver-speed skew; controlled50ms stale-packet test establishes prior correction then verifies invalidation and final baseline return.
- [x] Independent unchanged baseline and bounded nearest-baseline release; rearm blocked until final output rejoins. Regression covers baseline moving away at maximum allowed rate, then stopping/rejoining. No universal instantaneous release claimed or rate limit relaxed. Five saved release-tail frames remain unchanged in peak/area from v1(0.00570527rad/0.000469680rad·s); no false tail-reduction claim.
- [x] Separate registered default0 FordPrefRollAwareMapping opt-in, preserving existing trial selection. Unknown-key compatibility fallback; actual staged Params C ABI rebuilt and temporary-store default/enable/disable checks pass. Additive C++ schema generated/compiled/round-trip tested.54focused tests and320transition/abort cases pass; review findings fixed.
- [x] Rerun27sessions/515segments:1,904,757native TX checks accepted per variant/zero rejections;9,983pre-configuration generated frames separately unhooked. Original legacy-message path byte-identical to installed baseline across2,986,854updates; synthetic causal snapshot fixtures exercise23,440mapped steering evaluations,17,528changed generated updates. Fixture reconstruction is not proof of historical producer consumption or live scheduling. No saved command changes≤50or≥70mph.
- [x] Stage reviewable openpilot.patch/opendbc.patch; both apply-check on clean pinned paired bases9da98d0c91/18175406d0. Original paired trees, owner 1.20/0.97, native geometry/safety and Comma unchanged.
- [ ] Next integration phase: apply/review paired patches in an authorized candidate checkout, perform full vehicle application build and paired commit/submodule provenance validation. No device activation or parameter write authorized by this local work.
- [ ] Hardware/road validation and identified actuator/ratio calibration remain separate. Current transform is bounded roll-compensation sensitivity; no fitted ratio gain or observed steering improvement established. Continue existing35–50mph/all-range evidence plan; no special high-speed collection requested.


### 2026-10-17 — Calibration/roll patches integrated into paired branches; full local builds/tests pass

NAV-01/NAV-06/NAV-15: [integrated pair and build report](docs/research/navigator-paired-roll-build-2026-10-17/REPORT.md), [verification](docs/navigator-reference/PRIVATE_ARTIFACTS.md).

- [x] Preserve exact clean bases/source/settings documentation before applying staged patches; add portable parent/child regressions and branch-local integration documentation.
- [x] Integrate on both existing codex/navigator-tracking-release branches; local openpilot99645f2222ea2ba1fd4124808774bcd6381f8154 pins child8cbc834fe534a248a3bc6d56ce964106c0f49503. Both checkouts clean; no push.
- [x] Full minimal/development Mac SCons builds pass, with post-commit checks at final paired heads. Local Panda/H7 build passes without flashing.
- [x] Parent989passed/86skipped/1expectedfailure/343subtests; child3880passed/1690skipped/24673subtests. Scoped lint and independent applied-source review pass. Native child suite uses existing unsanitized Mac debug hooks; no UBSan result claimed.
- [x] Integrated producer/card IPC and320transition/abort cases pass. Source/normalized-AST receipts bind integrated logic to prior515segment staged replay; no redundant new515segment run this stage.
- [x] Owner 1.20/0.97, vehicle geometry and native safety unchanged. New roll mapping separately default-off. No Comma contact, settings change, deployment, reboot or flash.
- [ ] Publication/fetchable paired provenance, AGNOS/Chestnut runtime/hardware checks and any installation/activation remain separate. Physical actuator/ratio identification and road improvement are not established by these successful local Mac builds/tests.

### 2026-10-17 — Paired publication and backed-up device staging

- [x] Publish exact roll/calibration parent99645f222 and child8cbc834fe to existing paired branches; remote refs verified.
- [x] Back up installed source, parameters, launchers and signed firmware; download to Mac and verify archive/member hashes.
- [x] Stage separate ARM checkout with protected active source and isolated hardware/network/parameter access. Review guarded whole-install swap and rollback.
- [x] Complete full ARM build,338tests/12063subtests,320transition cases/115200frames and actual producer/card IPC check. Verify independent local Git objects, exact LFS assets and preserved firmware. Activate exact published pair with whole-original rollback retained; ignition-off acceptance passes with settings/calibration/1.20/0.97 preserved and new roll option enabled.
- [x] Powered stationary Park checks pass: all12topics valid/alive, large model20fps/zero drops, healthyChestnut,550Panda samples with zeroRX/TX faults,1101valid atomic calibration snapshots. Learned ratio/average offset/delay and calibration retained; normal startup stiffness reset noted in report.
- [ ] Ordinary supervised road tracking validation remains outstanding; compare50–70mph and continue35–50mph evidence plan.
- [ ] Road evidence remains required: compare ordinary 50–70mph opportunities and continue35–50mph data plan. Current mapping is a bounded roll sensitivity trial, not a demonstrated ratio/actuator calibration fix.

[Installation report and receipts](docs/research/navigator-roll-installation-2026-10-17/REPORT.md).

### 2026-10-17 — First post-roll drive: promising50–65mph response;29mph takeover remains

NAV-01/NAV-06/NAV-15: [all-speed review](docs/research/navigator-post-roll-drives-2026-10-17/REPORT.md), [complete27-event input/disengagement timeline](docs/navigator-reference/PRIVATE_ARTIFACTS.md), [verification](docs/navigator-reference/PRIVATE_ARTIFACTS.md).

- [x] Read-only download of all new data:1session/25segments/219,415,234bytes, hash-verified against final remote inventory. Retained corpus now28sessions/540segments;18prior-revision sessions used for comparable baseline metrics. Private raw/GPS extraction backed up on Mac. No Comma source/settings/service changes, queries, updates or firmware action.
- [x] Verify trial was delivered: recorded clean99645f222 and roll option1;17,439active non-driver angle sends match reconstructed mapped strategy within half a wire step.4,857highway frames differ from quantized no-map baseline.40–50mph candidate/baseline commands identical.
- [x] First50–70steady body/request median112.1%→103.0% (new55.8s).55–60:113.8%→105.2%;60–65:112.2%→98.2%.50–55little aggregate change. Matched-road subset favorable, but only6.85s after deduplication. One drive, observational evidence; no causal or universal calibration claim.
- [x] Review every recorded speed and intervention:22assistance-active steering-input episodes,11lane-change-associated;4brake-associated disengagements;1additional post-disengagement steering interval. Clear29.4mph `turn exceeds limit` input at22:33:39.891CDT lasts24.87s; actual mode0/manual release totals20s.
- [x] Separate moving blocked messages:8cancel echoes+1active steering frame during69mph braking. Native replay reproduces steering rejection with controls already disallowed; mapped/base command quantize identically there. Native replay misses2hardware cancel rejections; transport ordering not fully reproduced. Startup/end transient steering flags are separate from assisted road driving.
- [ ] Next local diagnostic: rising-demand/body-response lag around24–30mph; shortfalls recover against earlier request about0.5s later and brief unwind over-response exists. Not evidence for a blanket gain boost. Retain successful highway trial evidence.
- [ ]35–50mph still deserves review: roughly13–14% above request in this session's steady subset. Mapping inactive there; route/roll/model effects remain possible.
- [ ]15mph issue remains unresolved: virtually no useful assisted<20mph turn evidence in this drive.65–70has only0.20s steady evidence;70–85has travel but no qualifying meaningful bend. No dedicated high-speed collection requested.

### 2026-10-17 — Reported inside-of-bend event matched near83mph; entry delay localized

NAV-01/NAV-06/NAV-15: [local investigation](docs/research/navigator-entry-highspeed-investigation-2026-10-17/REPORT.md), [high-speed scenes](docs/navigator-reference/PRIVATE_ARTIFACTS.md), [entry stages](docs/navigator-reference/PRIVATE_ARTIFACTS.md), [verification](docs/navigator-reference/PRIVATE_ARTIFACTS.md).

- [x] Correct earlier coverage gap:0.001/m curvature floor excluded gentle high-speed bends. New60–85scan uses absolute acceleration error and requested acceleration>=0.25m/s² while retaining freshness/override/lane-change guards. Previous stronger-turn improvement is not evidence that gentle/high-speed tracking is satisfactory.
- [x] Match user's no-signal inside-bend report at22:42:41–<private clock time>:47CDT,logged81.8–83.0mph:134.4% body/request response,0.3635m/s² median excess; wheel7.3°versus target4.99°. Model-estimated inner-line distance1.58→0.41m, before driver correction22:42:49.113. Model estimates support inward encroachment; no video/surveyed tire-clearance proof.
- [x] Establish map inactive in event: term0 and mapped/no-map outputs identical above70mph. Atomic angle target recomputes correctly. Upper-speed baseline conversion and angle-target tracking remain unvalidated; owner0.97 only affects one curvature branch, not every high-speed command.
- [x] Broaden gentle-bend evidence:60–65gentle subset114.8% versus98.2% stronger-turn all-phase subset;65–70gentle113.4%. Sparse70–75and single-bend80–85over-response retained. Separate84mph nearly straight peak follows a signaled lane change.
- [x] Localize29mph entry error: growing desired wheel angle~65°versus actual~46° before takeover. CAN matches reconstruction, final software slew not binding in selected approach; wheel/body lag downstream of target production remains. One older29mph scene repeats55%response and~107%against0.5s-earlier request; another27mph fixture is an engagement case and is kept separate.
- [x] Preserve red-capable recorded-signal witnesses for low-speed shortfall and fast excess-response/inward-lane-estimate proxy. These do not predict changed-controller road response.25raw segment hashes and18baseline normalized sessions verified. No Comma contact or controller implementation.
- [ ] **Priority before another device trial:** investigate/prototype upper-speed calibrated-target/response handling across speed×demand×roll, with the reported fast bend as an explicit blocker fixture. Do not merely extend current map or divide gain by observed response.
- [ ] Separately design bounded24–30turn-entry compensation with immediate unwind/reversal/driver release; preserve24mph unwind counterexample and lower/upper speed isolation. Keep1.20/0.97 and native safety limits unchanged.
- [ ] Any candidate requires full retained replay including gentle-turn fixtures, abort/reversal/release checks, native safety/build checks, then separate device/hardware acceptance. No new high-speed reproduction drive needed for next local stage.


### 2026-10-17 — High-speed gentle-bend reduction prototype and full replay complete

NAV-01/NAV-06/NAV-15: [local prototype/report](docs/research/navigator-highspeed-correction-prototype-2026-10-17/REPORT.md), [design](docs/research/navigator-highspeed-correction-prototype-2026-10-17/DESIGN.md), [verification](docs/navigator-reference/PRIVATE_ARTIFACTS.md), [exact recorded-timing native check](docs/navigator-reference/PRIVATE_ARTIFACTS.md).

- [x] Prototype bounded reduction-only wheel-excess feedback in gentle curves: smooth60–70mph onset, acceleration-based demand screen,5-frame persistence,0.5degree wheel-excess deadband,15%/0.01rad cap and final native slew envelope. Meaningful short-window withdrawal/reversal/invalid context release and residual-join re-arm gate. Owner 1.20/0.97 unchanged; installed roll mapping remains reference.
- [x] Test39cases including12,000transition/abort sweep frames, mirrored bends, stale/invalid state after activation, driver release, reversal, re-arm, jitter and slow unwind. Independent review findings on event-envelope validity and source provenance resolved before acceptance run.
- [x] Actual83mph no-signal bend1011–1017.5s: reference matches recorded wire within half LSB; candidate changes117/130frames with median15%command reduction. This is command mitigation evidence, **not measured tracking improvement**. All1,567active40–50mph scene frames unchanged.
- [x] Full28-session/540-segment replay:124,787,149physical RXframes,3,134,371controller updates,2,004,203accepted configured TXframes per native/controller variant, zero generated-TX rejects. Original atomic packets and separately labelled causal calibration fixtures; default-off and below60mph streams identical; identical unchanged source hashes across workers.
- [x] Exact original recorded timing:839encoded steering packets changed, including117bend packets; zero additional native rejects. Same seven historical rejections remain (six cancel plus one steering after braking); generated-controller zero-reject result does not erase them.
- [x] Investigated locally in the later wheel/body-release entry:14brief body-under-response samples where wheel guard still reduces command (largest4.54%); distinguish transients/model agreement from actual calibration. Slow continuous unwind can stay eligible; do not claim universal unwind rejection. No changed qualifying75–80mph scene evidence.
- [ ] Production context integration, paired build and hardware/closed-loop acceptance remain separate. No Comma contact/changes, branch integration, push, firmware or physical transmission this turn. Continue24–30mph entry-delay work independently; no new high-speed reproduction drive needed for next local investigation.


### 2026-10-18 — Wheel/body and slow-unwind guard blockers resolved locally

NAV-01/NAV-06/NAV-15: [report](docs/research/navigator-highspeed-release-2026-10-17/REPORT.md), [design](docs/research/navigator-highspeed-release-2026-10-17/DESIGN.md), [guard audit](docs/navigator-reference/PRIVATE_ARTIFACTS.md), [full verification](docs/navigator-reference/PRIVATE_ARTIFACTS.md).

- [x] Diagnose 14 wheel/body counterexamples using original timestamps:11 remain below 90% with source-time target matching; all 14 reach 90% of the frozen target within 300 ms diagnostically. No fixed yaw offset or replacement gain established; future data is excluded from controller input.
- [x] Add fresh real calibrated body confirmation, source/receipt/consumption timing, unique sample history and invalid-calibration cache revocation. All 14 original samples now have zero added final correction; zero new measured-under 90% counterexamples in latest-route changed frames.
- [x] Replace forgetting rolling window with admitted fixed peak, causal 3-sample median, cumulative 10% retreat latch and immediate 20% raw-retreat abort. Slow 0.2/0.5/1% declines are covered; lower plateau cannot rearm. New demand must exceed retained peak by 2% for 5 fresh wheel/body-confirmed frames, then restart persistence after reference join. Invalid speed/neutral/direction evidence cannot reset a latch.
- [x] 84 focused tests pass; independent review findings resolved. Full 28-session/540-segment replay: 124,787,149 RX frames; 2,004,203 configured generated TX accepted per variant, zero rejects. Exact recorded timing adds zero rejects; seven shared historical permission/cancel rejects remain. Native library independence and identical unchanged worker source hashes verified.
- [x] Owner 1.20/0.97, fixed pinion model, disabled behavior and below 60 mph/40–50 mph generated streams preserved. Installed paired source remains clean and unchanged; no Comma contact, update, firmware or transmission.
- [x] Document tradeoff: stricter candidate changes 31/130 unquantized 83 mph bend frames (28 encoded), versus 117 in the wheel-onlyprototype. Changed-frame median 4.36% command reduction; whole-bend median 0%. This is narrower admission, **not proof of improved road tracking or fixed lane departure**.
- [ ] Production paired integration/build and hardware/closed-loop acceptance remain separate. This package is local and inactive. Keep 24–30 mph entry-delay and previous low-speed evidence work separate; no special 85 mph reproduction drive needed for next local stage.

- [x] Additional driver-pressure stress regression: immediate reference return during rising demand could exceed the inherited slew limit (0.014155 vs 0.009 rad/frame). Ordinary pressure now withdraws extra correction through native-slew release, matching installed reference behavior; inactive/human-turn modes retain their original behavior. Mirrored regression and takeover-inclusive transition sweeps pass. Earlier full evidence is preserved under `pre-driver-slew-fix/`; final corrected-source 28-session/540-segment repeat passed with zero additional native rejects.


### 2026-10-18 — Paired high-speed integration and full local validation complete

NAV-01/NAV-06/NAV-15: [paired integration report](docs/research/navigator-paired-highspeed-build-2026-10-18/REPORT.md), [verification](docs/navigator-reference/PRIVATE_ARTIFACTS.md), [paired revisions](docs/navigator-reference/PRIVATE_ARTIFACTS.md).

- [x] Parent `ff6ff2630` pins child `9d5a3d48` on paired `codex/navigator-tracking-release`; local commits, clean checkouts. Separate `FordPrefHighSpeedTracking` defaults off and requires existing pinion, low-speed, persistent and roll-mapping prerequisites. No UI toggle or device preference writes.
- [x] Port validated controller unchanged in all 12 method ASTs; integrate actual subscriber receipt time and calibration invalidation. Actual producer/card capture test is subprocess-isolated to avoid process-module import state leaking into forked replay tests; the affected radar replay and full suite pass after this test-only correction.
- [x] Full Mac minimal/development builds pass, including repeats at final paired heads. Complete parent: 1,018 tests / 343 subtests, 86 skips / 1 expected failure. Complete child: 3,953 tests / 24,673 subtests, 1,690 skips. Local Panda target and scoped lint pass; independent review has no important findings.
- [x] Fresh integrated factory/module 28-session / 540-segment replay exactly matches every retained prototype route result and all four generated stream hashes: 124,787,149 physical RX; 2,004,203 configured accepted TX per variant; zero generated rejects. Exact recorded timing adds zero rejects and retains seven historical rejects. Reported bend: 31/130 unquantized strategy frames, 28 encoded packets changed. No measured handling/lane-clearance claim.
- [x] Protected 1.20/0.97, geometry, fixed pinion, native safety, existing roll source and historical settings-snapshot hashes unchanged. Below-60 mph/40–50 mph replay commands preserved. No Comma contact, installation, update, firmware flash, publication or physical CAN transmission.
- [ ] Separate publication and device backup/build/activation, powered parked acceptance and road comparison remain. Mac debug-hook evidence is unsanitized and does not establish live bus timing or AGNOS/ARM runtime. Continue 24–30 mph entry-delay investigation independently; no special high-speed reproduction drive requested.


### 2026-10-18 — High-speed paired branches published and installed; parked acceptance passed

NAV-01/NAV-02/NAV-06/NAV-15: [installation report](docs/research/navigator-highspeed-installation-2026-10-18/REPORT.md), [backup](docs/navigator-reference/PRIVATE_ARTIFACTS.md), [powered check](docs/navigator-reference/PRIVATE_ARTIFACTS.md), [final preservation](docs/navigator-reference/PRIVATE_ARTIFACTS.md).

- [x] Published and activated exact parent`ff6ff2630`/child`9d5a3d48` on paired`codex/navigator-tracking-release`, clean. Explicit user approval of both adgower repository destinations recorded after automatic approval review requested destination clarification; no force push.
- [x] Fresh843,575,681-byte private backup verified on Mac/device;145manifest members and both source archives checked. Whole previous install retained at`/data/navigator-previous-highspeed-<private timestamp identifier>`; rollback refs retained. No OS/firmware update.
- [x] Full isolated ARM build,440native tests/79skips/12,063subtests,320transition cases/115,200frames, actual producer/local-msgq/card pipeline and8constructor combinations pass. One stale isolation-prefix helper assertion corrected; candidate source unchanged. Live-source/preferences/service preservation passed.
- [x] Only new preference`FordPrefHighSpeedTracking=True`; all other selected settings,1.20/0.97, geometry/fixed pinion, signedfirmware and launchers preserved. DisableUpdates remains on; AlphaLongitudinal/Experimental remain off; AGNOS19.9.
- [x] Ignition-off acceptance201healthyPanda samples; powered stationary55s acceptance550healthyPanda samples with0RX-invalid/blockedTX/faults. Large model~20fps,0drops;1101/1101atomic snapshots valid. Passive motion adapter700samples/697valid after startup; finalsource31.38ms/receipt2.69ms ages.
- [x] Learned ratio22.7136803, averageoffset−0.5723621deg, delay0.2542532s, calibration/vehicledefinition/torquecache payload retained. Normalstartupstiffness0.9977184→1.0; no cache restoration.
- [ ] Ordinary supervised familiar-road comparison, noting approximate times/speeds/interventions. No special85mph reproduction requested. Parked/runtime/replay evidence does not establish physical handling improvement or fixed lane departure. Existing lower-speed and24–30mph diagnosis remains open.


### 2026-10-18 — All new post-high-speed drives reviewed; synchronized override video saved

NAV-01/NAV-06/NAV-15: [report](docs/research/navigator-post-highspeed-drives-2026-10-18/REPORT.md), [all speed bands](docs/navigator-reference/PRIVATE_ARTIFACTS.md), [all62input/disengagement groups](docs/navigator-reference/PRIVATE_ARTIFACTS.md), [verification](docs/navigator-reference/PRIVATE_ARTIFACTS.md).

- [x] Read-only download of all4new sessions/97rlogsegments (841,980,293bytes), including stationary acceptance and3moving drives; before/after hashes/source/settings/service unchanged. All source records match installed`ff6ff2630`/`9d5a3d48` and high-speed option enabled. No device changes.
- [x] Reconstruct67,726active/no-driver steering packets,100%within halfwirestep of installed candidate. Trial changes343strategyframes/17.15s (299encoded differences versus prior reference), across58.74min assisted recording. Recorded below60mph parity retained. This confirms execution, not better trajectory.
- [x] All-range coverage: best steady60–65mph48.7s/102.8% estimated body response;65–70mph27.75s/111.9%.70–85clean-turn medians122–133% with sparse strict-steady support, particularly80–85only0.35s.35–50still sparse and not certified perfect. Body yaw is an uncertain temporally-correlated calibrated pose estimate; no universal factor inferred.
- [x] Matched prior-road support only41.45s, mostly60–65; new/prior median responseboth108.8%, medianabsolute ratioerror13.1/14.8%. Only0.65s matched correction exposure; no useful70–85matched proof. Do not attribute that small aggregate difference to the trial.
- [x] Save high-speed fixtures:10:32:28/83mph brake-associated input (136% estimated response),<private clock time>/81mph pressure (144%),<private clock time>/82mph input (169%,159% with0.25s lag). The last has0/56pre-input correctedframes despite39body-confirmedframes awaiting unwind/rising confirmation. Owner, after viewing video, reports apparent lane-edge oversteer and possible metal/debris avoidance. Object/tire crossing/controller causation are not independently proved.
- [x] Save separate11:04:30.95low-speed5.7s/13.3–18.8mph deficit,median53.4%,2.2s strictsteady. High-speed trial makes no change in this range.
- [x]62driver-input/disengagement groups exported;21include disengagement,21brake,19signals (overlap). No active-travel steering faults;10fault episodes are inactive/startup/stopping.7active-angle hardware echo markers allcoincide withbrake edgeswithin~10ms;4native-reproduced permissionrejects,3notreproducedinloggedbatchorder.22,703,325originalphysicalRXnativeaudit,0RXinvalids. Counts/markers/nativeoutputs are not assumedone-to-one.
- [x] Owner-requested20s forward/wide road clip and [synchronized steering overlay](docs/navigator-reference/PRIVATE_ARTIFACTS.md),<private clock time>–<private clock time>:09CDT. Actual/requested wheelangles, driverpressure/torque, speed and activeflag are recorded; correction/guardare labelled reconstruction.400frames/20fps, source-time alignment; pressure starts10.02s, assistactiveflagremains on. No cabin video or synthetic lane path.
- [ ] Next local investigation: high-speed unwind/rearm/withdrawal behavior in these fixtures, preserving release safety; separate low-speed sustained deficit. Continue ordinary35–50mph evidence. No new gain/design/devicechange authorized by this read-only analysis, and no special85mph reproduction requested.

### 2026-10-18 — Post-unwind rising-leg rearming prototype, local only

NAV-01/NAV-06: [investigation and prototype](docs/research/navigator-highspeed-rearm-prototype-2026-10-18/REPORT.md), [design](docs/research/navigator-highspeed-rearm-prototype-2026-10-18/DESIGN.md).

- [x] Diagnose retained-peak coverage gap: after unwind, five confirmed requests above102%of the old peak can exclude a fresh rising leg below that peak. Separate this gap from valid blocking during continued withdrawal.
- [x] Prototype fresh causal trough/rising-window admission after complete reference rejoin, with unchanged current wheel/body/timing/calibration/driver guards, onset persistence and bounds. Preserve prior peak during provisional onset and clear stale filter history on invalid evidence.
- [x]94focused tests pass; independent source review finds no important new issue. Original send-time replay changes7/29frames in sessions03/04;34encoded packet differences total. Exact recorded-timing native replay adds0rejections, with32baseline rejects retained across allTXtypes. All14earlier under-response counterexamples remain uncorrected.
- [x] Full32-session/637-segment replay acceptance:3,704,143updates/variant;14recorded-context/18labelled-fixture changedupdates;0configured native rejects. Default-off whole-stream parity and below60mph/40–50mph parity pass. All28prior-route installed-reference hashes match, protectedsource/HEADs unchanged. See [acceptance](docs/navigator-reference/PRIVATE_ARTIFACTS.md). This is offline Mac proof, not hardware/road proof.
- [ ] Reported15:19:59lane-edge event remains unresolved: prototype changes0frames in final2.8s, where demand is largely withdrawing. Separate requested path, wheel unwind and calibrated body-yaw behavior before proposing further behavior changes. No handling improvement or installation readiness claimed.
- [x] Research files only. Paired branches, device, settings and1.20/0.97 untouched; noSSH/CAN/publication/integration/install.

### 2026-10-18 — High-speed wheel unwind and requested-path incident diagnosis

NAV-01/NAV-06: [report](docs/research/navigator-highspeed-wheel-unwind-2026-10-18/REPORT.md), [verification](docs/navigator-reference/PRIVATE_ARTIFACTS.md), [exact-send-time audit](docs/navigator-reference/PRIVATE_ARTIFACTS.md).

- [x] Trace15:19:59CDT lane-edge/possible-debris fixture. Final56steering frames follow1.425×speed×requestedcurvature within halfwirestep, with0extra high-speed residual/release-pending frames. No software release tail demonstrated; EPS internal target/application is not recorded.
- [x] Wheel evidence also supports excess: pre-input5.8s median calibrated wheel/request162.1%, body/request161.9%, signed wheel-target error1.52°.0.25s lag comparison still154.4%/152.5%. Learned/body estimates are uncertain and correlated; no inverse-response gain fit. Low-level driver input remains possible below pressure threshold.
- [x] Separate model path position: predicted path remains inside estimated lines but around0.70m toward near/left of estimated center at50m horizon (24%of lane width from left). Predicted centerpoint margin is not tire clearance or executed trajectory.98.6%of580control samples match latest logged model action curvature; wheel targets reconstruct within0.0000011°.
- [x] Similar excess in retained83mph and opposite-signed81mph bend windows. Strictsteady support remains sparse:70–75mph5.4s,75–80mph1.65s,80–85mph0.35s; no eligible85–90mph meaningful demand. No proven85mph switch or universal factor.
- [ ] Next local design study: high-speed baseline/calibrated wheel-target mapping and controlled unwind, separately from requested-path near-edge bias. Preserve fixed native pinion model/safety, all owner settings,1.20/0.97 and lower speeds; explicitly test already-under-target exit, both signs, uncertain calibration and driver release. Do not force old trim to remain active during withdrawal or apply a blanket speed gain.
- [x]71raw model-input segment hashes reverified, anonymous diagnostics saved; paired HEADs/protectedsource/tracked-clean state unchanged. No device access, CAN, control implementation, integration, push or install. No new full637replay needed for diagnostic-only files; previous prototype acceptance remains separate.

### 2026-10-18 — Local calibrated wheel-target/unwind prototype

NAV-01/NAV-06: [research report](docs/research/navigator-highspeed-wheel-target-prototype-2026-10-18/REPORT.md), [design](docs/research/navigator-highspeed-wheel-target-prototype-2026-10-18/DESIGN.md), [incident proposed commands](docs/navigator-reference/PRIVATE_ARTIFACTS.md).

- [x] New bounded feedback policy blends70–75mph; current/sustained body excess, calibrated wheel error and fresh atomic context required. Five distinct source-stamped wheel observations;150ms closing projection may withdraw, never amplify onset. Keep15%/.01rad total cap and native slew,1.20/0.97/fixed pinion/geometry. No learned gain or OEM wheel-degree conversion.
- [x]110tests pass, including73unchanged installed-reference cases and37prototype cases,12,000transition/abort frames. Independent review/regressions resolve duplicate-source evidence, signed under-target fixture, lower-speed warmup state contamination and explicit-disable overwrite. Separately advanced installed baseline preserves its policy; native handoff tails are explicit.
- [x] Saved lane-edge final2.8s now receives20additional trim frames, route1079.480720–1080.427611s, maxextra0.002754742rad, withdrawing before two already-under-target frames. All14prior underresponse counterexamples remain at0extra correction.0scene changes at/below70mph. Coverage is not physical improvement proof.
- [x] Exact recorded-timing native checks:404encoded steering differences across sessions03/04,0additional rejections;32baseline all-TX rejects retained,0RXinvalids. No transport/permission override.
- [x] Final32-session/637-segment replay passes:3,704,143updates/variant,503recorded-context/558labelled-fixture changed updates;0configured native rejects,0changes at/below70mph or40–50mph,0handoff frames in this corpus, default-off whole-stream byte parity. All28old reference stream hashes match;32source snapshots agree and paired source/HEADs stay unchanged. [Acceptance](docs/navigator-reference/PRIVATE_ARTIFACTS.md). First boundary-obsolete partial replay is not acceptance evidence. Native Mac/frozen-input proof remains distinct from physical handling and ARM/H7.
- [ ] Requested model path near lane edge remains separate; true physical handling/trajectory, EPS/internal target, ARM/H7 and road readiness remain unproved. No installation claim.
- [x] Research-only files. NoSSH/CAN, integration/push/install or device/settings/paired source changes.

### 2026-10-18 — Calibrated wheel-target trial integrated into paired local branches

NAV-01/NAV-06: [integration/build report](docs/research/navigator-paired-wheel-target-build-2026-10-18/REPORT.md). Local`codex/navigator-tracking-release`pair: openpilot`50baa6fd6acf9d37b7e0768e5736efab2a357ddc`pins opendbc`0e65f296260ec16da3c3b814c10ac5f36f8b2e4c`.

- [x] Child adds portable calibrated wheel-target/unwind policy and37regressions; parent selects it through existing opt-in/prerequisites. Original high-speed controller remains unchanged as the independent installed baseline. Exact class/test/helper AST equivalence to accepted prototype; no new preference, publisher/card plumbing or UI.
- [x]139focused tests; full parent1,018tests/343subtests (86skips,1expectedfailure), full child3,990tests/24,673subtests (1,690skips). Minimal/development Mac SCons and Panda targets pass before and after local commits. Independent review finds no important issue,49tests independently passed. Builds are configured incremental targets, not clean-room or device boot proof.
- [x] Protected1.20/0.97, geometry, fixed pinion, old controller, safety source/library, registry, card/motion adapter and historical settings snapshot unchanged. Both paired checkouts clean; no fresh device inventory claimed.
- [x] Actual-factory send-time rows match accepted prototype exactly across83,978rows in two high-speed drives. Committed exact recorded-timing native check:404encoded differences,0additional rejects,32baseline all-TX rejects preserved.
- [x] Fresh committed factory/native32-session/637-segment replay passes: all128whole-stream hashes equal accepted prototype;3,704,143updates/variant,503recorded-context/558fixture changed updates,0new native rejects,0changes at/below70mph including40–50mph, default-off byte parity. Candidates use actual parent factory; references explicitly use unchanged installed controller. Final pin/source/clean-state checks pass. [Final receipt](docs/navigator-reference/PRIVATE_ARTIFACTS.md).
- [x] Local commits only; no push, SSH/ECU/CAN transport, install, firmware operation or Comma settings change. Requested-path near-edge behavior and physical handling proof remain separate.

### 2026-10-18 — Wheel-target pair publication and guarded installation in progress

NAV-01/NAV-02: [installation report](docs/research/navigator-wheel-target-installation-2026-10-18/REPORT.md). User authorized pushing/backing up/installing and confirmed parked ignition off with screen/recovery access.

- [x] Published existing paired branches without force: parent`50baa6fd6`/child`0e65f2962`; exact remote heads verified.
- [x] Fresh private device/Mac backup verified:66parameters, both source archives, launchers and signed installed firmware; archive hash,143manifest members and nested archives checked.
- [x] Additional local280transition cases/100,800in-memory frames pass bounds/slew/settling checks. Installer review finds no material rollback/preservation defect.
- [x] Full isolated ARM build;477tests/12,063subtests (79skips);600transition cases/216,000frames;8factory combinations and IPC checks pass. Exact pair activated by atomic exchange; ignition-off acceptance and settings/calibration preservation pass.
- [x] Powered stationary acceptance passed after user ignition-on/Park confirmation:55seconds, all topics healthy, correct Ford safety, no sampled faults or TX-block increments, big model approximately20fps/zero drops. Learned ratio/offset/delay/calibration and geometry retained; normal estimator stiffness reset documented.
- [ ] Ordinary supervised road comparison pending; parked checks do not prove tracking improvement. Preserve1.20/0.97, all settings, geometry/pinion/native safety and existing OS/firmware. No claimed physical improvement or requested high-speed reproduction.

### 2026-10-19 — All new post-wheel-target drives reviewed

NAV-01/NAV-02/NAV-06: [103-segment review](docs/research/navigator-post-wheel-target-drives-2026-10-19/REPORT.md), [all50input/disengagement windows](docs/navigator-reference/PRIVATE_ARTIFACTS.md), [verification](docs/navigator-reference/PRIVATE_ARTIFACTS.md).

- [x] Downloaded/hashed all11new sessions,103segments/851MB;98.47recorded/38.10assisted minutes. Every session identifies installed parent50baa6fd6; clean live pair/prefs/protected source/service unchanged before/after read-only acquisition.
- [x]43,934active/no-driver wire packets match installed reconstruction within half encoding step; zero added command changes versus prior high-speed policy. New70–75mph+wheel-target benefit remains unevaluated:12.3s assisted above70, only1.65s meaningful demand, none qualifying clean meaningful; max76.8mph and no80mph+travel. No activation-bug or physical-improvement claim.
- [x]50intervention/pressure/disengagement groups reviewed (39pressure,22brake,16signal associations overlap); do not count these as50emergency takeovers. All-range CSV/report retained.66.1s road/direction/speed/demand-matched prior comparison below70mph is mixed/near-flat and cannot be attributed to new code.
- [ ] New local fixtures:13:14:14.70CDT/14.8–15.0mph1.55s body46.5%/wheel46.5%,21.7°shortfall,49.3%body even with0.4s lag; subsequent reversal shortfall separate.<private clock time>/28–31mph0.7s body45%/wheel52%. Diagnose requested→bounded command→wheel; do not infer blanket inverse gains or blame only body yaw. Preserve1.20/.97.
- [ ]64mph unwind fixtures09:08:57/<private clock time>/<private clock time>:34show wheel/body excess below new policy scope.<private clock time>:57preceded brake/steering input; others differ in intent/timing. Continue local transient/lag/admission diagnosis;40–50mph still lacks steady proof.
- [x] Native original traffic23.15Mphysical RX/noRXinvalid; hardware steering rejection echoes at brake permission transitions (same-batch ordering limits native reproduction). No active steering faults or active invalidCAN.
- [ ] Separate reliability follow-up: Chestnut supply warnings in inactive09:50and09:56sessions, no assisted-session supply flags. Not diagnosed as cable/harness fault.
- [ ] High-speed physical benefit needs ordinary supervised natural bends at legal speeds when appropriate; no special85mph/lane-edge reproduction requested. No device code/settings/service/OS/firmware/CAN changes.

### 2026-10-19 —15mph budget and64mph unwind mechanisms reproduced locally

NAV-01/NAV-06: [diagnostic report](docs/research/navigator-low64-diagnosis-2026-10-19/REPORT.md), [mechanism verification](docs/navigator-reference/PRIVATE_ARTIFACTS.md). Full causal warmup for sessions04/05/11; exact whole-stream parity against uninstrumented installed-policy replay.

- [x]15mph13:14:15episode:31valid frames admit a positive upstream term but return zero after0.00025rad·s budget exhaustion. Three20Hz frames spend the budget at13:14:14.53–14.63. Native range/slew limits and freshness do not block this window. Fixed pinion57%versus calibrated wheel/body46.5%shows estimator/model differences, but all remain below target.
- [x] Tested existing resolution-aware rearm research unchanged: one earlier refill succeeds, then a new catch-up exception marks the later steady correction budgeted again. All8,394candidate commands unchanged. Rearming alone does not fix this recording; no inverse-response gain proposed.
- [x] Three64mph unwind windows: old latch blocks while wheel/body show excess, because demand remains below old peak. Command itself unwinds and final extra residual is zero—no stuck software correction tail. Current new wheel-target behavior starts70mph+, so64mph remains previous behavior by design. Lag explains a substantial fraction, not all, of current-target wheel error.
- [ ] Next local design: separately bounded sustained-error treatment versus transient exception budget; preserve guard/cap/exposure/release behavior. Evaluate calibrated wheel-target/predictive-withdrawal scope at60–70mph with40–50unchanged, sign/neutral/closing/abort counterexamples, then full replay/native checks. Neither new candidate implemented or physically validated this turn.
- [x] NoSSH, device/source/preference/service/firmware/CAN changes; exact paired HEADs/clean tracked state and1.20/0.97preserved.

### 2026-10-19 — Bounded sustained-error and60–70mph unwind prototype complete locally

NAV-01/NAV-06: [report](docs/research/navigator-sustained-unwind-prototype-2026-10-19/REPORT.md), [design](docs/research/navigator-sustained-unwind-prototype-2026-10-19/DESIGN.md), [acceptance](docs/navigator-reference/PRIVATE_ARTIFACTS.md).

- [x] Separate sustained allowance max0.0025rad/0.0025rad·s/1s, inside existing total cap and25mph fade; requires wheel/body deficit, calibrated target, persistence/freshness and predictive withdrawal for both sensors. Independent full valid quiet pinion/body dwell; no refill on override/reset/short invalidity. Three review-found rearm/body gaps reproduced and repaired.
- [x] Report-local calibrated reduction blends60–70mph.15mph saved target gets16extra frames/0.8s atmax0.0025rad;64mph episodes get6/14/1extra reduction frames. These are command differences, not observed physical gains.
- [x]95tests,480transition/abort cases/172,800frames; fresh43-session/740-segment native replay4,289,417updates pervariant.369recorded/796fixture changed updates;2shared native rejects preserved/no added rejects. Default-off parity and protected25–60mph/40–50mph unchanged; original1.20/.97/geometry/safety/paired source remain.13exact original-timing scene comparisons modify244candidate packets/no new rejects; historical-reference404packet difference tracked separately.
- [x] The75.11mph/0.0005rad history-boundary item was reproduced and subsequently resolved in the separate upper-boundary prototype below. Fresh whole-corpus>=75parity now passes; original package remains preserved as historical evidence.
- [ ] Research-only; no paired integration/push/build/device activation or physical-improvement proof. Next integration stage must verify exact runtime contract and retain bounded exposure/abort behavior; no special85mph/lane-edge reproduction drive.

### 2026-10-19 —75mph history-boundary correction validated locally

NAV-01/NAV-06: [report-local candidate](docs/research/navigator-upper-boundary-prototype-2026-10-19/REPORT.md), [design](docs/research/navigator-upper-boundary-prototype-2026-10-19/DESIGN.md).

- [x] Reproduced stored-onset-history divergence; keep independent installed controller history and fade extension out70–75mph. Actual-output diagnostics repaired after independent review.
- [x]122focused tests and480transition/abort cases/172,800frames pass.13original-send-time scenes preserve previous candidate commands through70mph and have zero>=75mph differences.
- [x] Fresh43-route/740-segment replay:4,289,417updates/variant;355recorded/783fixture changed updates. Zero>=75wire differences in both contexts; exact75.111mph candidate now0.0285rad equals installed reference. Zero added native rejects (2shared baseline rejects/variant), default-off and protected25–60mph/40–50mph parity.13original-timing native scenes pass/235encoded changes; previous15/64mph prototype outputs preserved. [Acceptance](docs/navigator-reference/PRIVATE_ARTIFACTS.md).
- [x] Local research only. Paired source/device/settings untouched;1.20/0.97retained. No physical-improvement or release claim.

### 2026-10-19 — Paired sustained-error / boundary integration complete locally

NAV-01/NAV-06: locally committed parent`0171b8972`pins child`4167433e5`, both clean.134focused tests; full parent1018tests/343subtests (86skips/1xfail), child4112tests/24673subtests (1690skips); minimal/development/Panda incremental Mac builds pass again at committed heads.480transition cases/172,800frames and30,240actual-factory equivalence updates pass; independent review reports no material issue. Existing default-off/prerequisite selection and1.20/0.97/geometry/pinion/native safety/settings remain preserved. Prior740-segment native proof carried by exact class/factory equivalence; no fresh integrated740-segment run, ARM/device or physical handling claim. No push/device access/installation. [Integration report](docs/research/navigator-paired-sustained-build-2026-10-19/REPORT.md).

### 2026-10-19 — Sustained/unwind pair publication and device staging

Exact parent`0171b8972`/child`4167433e5` published to the existing adgower origins, remote heads verified. User confirmed parked ignition off/stable power/Wi-Fi/screen/recovery cables. Fresh backup includes66parameters/source/launchers/signed firmware; independent private Mac copy verification and isolated ARM/native validation are in progress. Separate stage only; no activation yet. Existing1.20/0.97 and settings retained. No OS/firmware update or active ECU diagnostics. [Installation plan](docs/research/navigator-sustained-installation-2026-10-19/PLAN.md).

### 2026-10-19 — Sustained/unwind pair activated; powered check pending

Published and installed parent`0171b8972`/child`4167433e5` after fresh private device/Mac backup and isolated ARM build.599native tests/12063subtests (79skips),320legacy+480newtransitioncases and factory/IPC checks pass. Ignition-off acceptance passed with1.20/0.97, firmware/launchers/settings and5learned hashes preserved. Powered stationary confirmation requested before the planned drive. [Installation report](docs/research/navigator-sustained-installation-2026-10-19/REPORT.md).


### 2026-10-19 — Sustained/unwind powered parked acceptance complete

Exact installed parent`0171b8972`/child`4167433e5` passed55-second passive ignition-on/Park/disengaged acceptance. All topics alive/valid, approximately20fps big model/zero reported drops, no sampled steering/CAN/vehicle/Chestnut supply faults or blocked-TX increments. Existing1.20/0.97/preferences/geometry/pinion/safety and core learned calibration preserved. Normal startup stiffness1.000095→1.0/cache timestamp change documented without restoring stale data. Installation and parked checks complete; ordinary supervised drive evidence remains uncollected. [Final report](docs/research/navigator-sustained-installation-2026-10-19/REPORT.md).

### 2026-10-24 — Alpha comfort: scan all 0–85 mph operation

Owner reports persistent pulsing, sluggish highway entry in the 50s, delayed initial launch and no-lead under-speed. Do not restrict investigation to one highway fixture. Downloaded 23 new completed segments; automatic five-mph exposure/transition scan includes stopped operation. New recording reaches69.33mph; 50–60mph has substantial brake transitions. Model is selected during263.47s of no-lead highway operation more than8mph below a valid setpoint. One actual47.71mph brake-release timeout/ControlsMismatch remains. An isolated coasting-admission sensitivity experiment reduces rapid reversals7→1 in an older fixture; broader/fresh replay and braking regressions remain prerequisites, not installation approval. Preserve1.20/0.97/lateral and measured clearance. Additional3.33GB redundant model/cache cleanup completed, storage80% used; recordings/backups/rollback untouched. [Evidence and remaining gates](docs/research/navigator-alpha-comfort-investigation-2026-10-24/REPORT.md).

Comfort investigation follow-up: fresh command reconstruction matched67,687/67,687 sampled feedback records. Broader replay **rejects** the simple longer coasting deadline as an overall solution:50–55mph rapid reversals7→8,55–60unchanged. Trace baseline admission/grade mapping and model demand next; do not cherry-pick the older70mph fixture. Automatic scan needs no owner-labeled sections. Existingrelease-timeout remains; no candidate tuning installed.

### 2026-10-24 — Model/grade prototypes tested across all available Alpha speeds

Local-only investigation complete:9cached Alpha session datasets audited, active coverage reaches73.787mph;75–85mph remains unvalidated. Current-controller replay spans61segments/179,144callbacks plus20exact-command baseline fixtures. Three prototypes tested: pending-release continuity ineffective, measured-under-acceleration coast worsens some episodes, neutral-intent bounded admission modestly improves50–55and60–65mph but leaves most cycling and adds one rapid reversal at35–40mph. Ninecontracts pass; full native RX/non-ACC TX/timer replay adds zero rejections; research comfort acceptance remainsRED, so **do not integrate/install these as the overall fix**. Threeexisting release timeouts persist. Model-selected acceleration dominates most50–70mph braking entries and much no-lead under-speed; forcing cruise past model slowing is not justified. Next: combined consumed-planner/PID/integral/received torque response analysis and a defensible coast response, using existing recordings first. No device/source/setting changes; 1.20/0.97 preserved. [Report and evidence](docs/research/navigator-model-grade-prototype-2026-10-24/REPORT.md).

### 2026-10-24 — Joint planner/integral/actuator replay established; prototypes rejected

Local-only follow-up now reproduces all135,449 latest-drive producer outputs/integrals and67,687 returned feedback callbacks without reseeding integral history. One-step actual-controller validation matches353,281 updates across61saved segments. Sign-sensitive anti-windup permits integral growth while positive demand is withheld if planner target becomes negative(1,565 latest-drive updates), but freezing all of it increases brake-command time and worsens some speed bins. Release-request anchoring creates earlier simulated timeouts; removing integral is also rejected despite fewer edges.15contracts and full raw RX/non-ACC TX/timer native replay pass with zero added packet rejections; **comfort/availability acceptance fails; do not integrate/install**. Original response-model hold-out tests have~45Nm brake-torque one-second RMSE and false-clear samples, so no physical comfort claim is justified. Next: validate mode/hold/deadband/transport behavior against original OEM and Alpha command/torque traces, distinguishing inactive(-5) from valid coasting requests. No device or paired-source changes; 1.20/0.97 retained. [Detailed report](docs/research/navigator-joint-longitudinal-prototype-2026-10-24/REPORT.md).

### 2026-10-24 — OEM/Alpha coast-release forecaster improved locally

Research-tool milestone, **not a driving feature or installation**. Re-read96hashed segments(35OEM/61Alpha); fixed whole-route fit/calibration/evaluation roles. Added arbitration state, valid-coast/inactive/precharge distinctions, causal command history, direct horizons and a low-torque probability/magnitude head. Same-split one-second brake RMSE:OEM127.4→67.9Nm,Alpha91.2→60.3Nm; propulsion281.9→179.4and179.0→87.6Nm. High-confidence one-second low-torque forecasts cover~91% of both evaluation release/coast sets with zero early errors in that finite sample; shorter horizons still have erroneous forecasts. Sevencontracts and original-command model replays pass primary research checks. Remaining gaps: OEM negative-coast propulsion regression, sparse prolonged inactive-coast/low-speed data, unvalidated70–85mph evaluation, broad prediction uncertainty and no off-policy/closed-loop physical proof. Do not replace actual torque clearance or claim pulsing fixed. Comma/paired branches/1.20/0.97 unchanged. [Model report and evidence](docs/research/navigator-coast-release-response-model-2026-10-24/REPORT.md).

### 2026-10-25 — Model-assisted coast prototype replayed; rejected

Implemented an isolated model-selected valid-coast policy with measured-torque clearance, bounded tracking debt and non-timer rearming. Forty local contracts pass. Full coupled LongControl/CarController replay covers all 61 saved Alpha segments/179,144 callbacks, but newest-drive rapid reversals worsen at 50–55 mph (7→16) and 65–70 mph (10→24), with two different release-timeout episodes. Point predictions favoring coast do not establish stable integral/actuator behavior. **Do not integrate/install this candidate.** Next regression is the 21.39 mph first divergence and its subsequent integral/clearance evolution; following behavior also needs fresh radar context in replay. No new drive required for that local work. 75–85 mph remains a road-evidence gap. Comma and paired source unchanged; 1.20/0.97 retained. [Prototype, full comparison and remaining work](docs/research/navigator-model-assisted-coast-prototype-2026-10-25/REPORT.md).

### 2026-10-25 — Coast/integral regression repaired; overall pulsing remains

Local prototype now keeps the original qualifier after retiring a model trial, admits coast only when planner/PID/compensated demand agree on mild nonpositive intent, and checks actual tracking before a trial. The saved 21.39 mph divergence and subsequent integral regression pass; newest 135,449 producer computations match baseline, and 61-segment/179,144-callback comparison has no added faults, weaker strong-deceleration samples or increased rapid reversals. Forty-six contracts pass. No PID gains, integral logic or feedback schema changes are needed. The remaining model admissions reduce only ~0.249 seconds of brake-command time and do not reduce cycling counts: **introduced regression repaired, original comfort issue still open; not an overall fix to install**. Existing 47.71 mph release timeout and 75–85 mph evidence gap remain. Comma and paired branches unchanged; 1.20/0.97 preserved. [Diagnosis, regression and next constraint](docs/research/navigator-coast-feedback-repair-2026-10-25/REPORT.md).

### 2026-10-25 — Highway pulsing prototype: neutral release, local benefit with open gates

Investigated grade switching, model/minimum-selection requests, tracking-aware allocation and integral sensitivity. Selected a bounded neutral-release hold with explicit coast-intent feedback and pickup-aware anti-windup. Newest healthy 50–70 mph replay: rapid reversals **71→59 (~17%)**, total transitions263→256, with no added timeout episodes. All61segments/179,144callbacks and full native RX/TX replay complete; no added native rejections. However, brake-command time grows193.819→207.970s,65–70mph reversals10→11, and27strong-brake samples differ one quantization count weaker. **Local prototype only; overall acceptance remains RED; do not integrate/install yet.** Next: distinguish neutral/precharge/friction demand and validate ECU response rather than further blanket smoothing. Existing47.71mph timeout and75–85mph data gap remain. Comma/paired branches/1.20/0.97 untouched. [Selected code, comparisons and remaining gates](docs/research/navigator-highway-pulse-shaping-2026-10-25/REPORT.md).


### 2026-10-25 longitudinal maneuver mismatch

- Downloaded and hash-verified 68 completed segments across five sessions for offline work.
- Two maneuver failures were one-second release-watchdog expirations during progressing brake release after completed 20 mph braking steps. A bounded progress-aware waiting prototype preserves measured brake clearance.
- Local validation: 156 tests and 20 subtests passed; 61-segment controller replay and native hook replay added no safety rejections. One native sanitizer permission-boundary test excluded; replay is not hardware proof.
- Eleven partial maneuver runs are useful evidence. Separate highway pose fault and longitudinal pulsing remain open.
- Candidate remains local and inactive; paired integration, ARM build and parked checks still required.
- [Investigation and evidence](docs/research/navigator-maneuver-mismatch-2026-10-25/REPORT.md).


### 2026-10-25 brake-release timeout paired integration

- Locally committed parent `ead00c30e` / opendbc `d4a20125` on `codex/navigator-tracking-release`; exact pin verified, both trees clean. No publishing or device changes.
- Full Mac/Panda builds pass. Parent 1,061 tests / 281 subtests passed; child 4,581 tests / 24,693 subtests passed (platform skips retained).
- Integrated 61-segment replay exactly matches tested prototype wire and feedback; steering 1.20/0.97 and protected safety/CAN files unchanged.
- Next: separately authorized publish, backup, isolated ARM build/staging, activation and parked checks before repeating maneuver tests. Highway pulsing and separate pose fault remain open.
- [Integration report](docs/research/navigator-release-timeout-integration-2026-10-25/REPORT.md).


### 2026-10-25 release-timeout staging and storage cleanup

- Published verified paired parent `ead00c30e` / child `d4a20125`; fresh private Mac/device recovery backup verified (147 manifest files).
- Reclaimed 11.8 GiB by removing 30 old source archives only after verifying retained Mac copies and device hashes; current install, recent rollback, settings, firmware and drive recordings retained.
- Isolated full ARM build passed: 1,105 tests / 12,083 subtests, including all 11 new regressions/guards; 75 retained contracts, 14 parent smoke tests and calibration regression passed.
- Ignition-off passive acceptance and final preservation audit passed. Candidate finalized but inactive; powered Park check also passed (20 Hz, no drops/faults/new blocked TX, healthy pose inputs). Alpha and 1.20/0.97 preserved.
- [Staging report](docs/research/navigator-release-timeout-staging-2026-10-25/REPORT.md).


### 2026-10-25 release-timeout fix activated

- Activated paired `ead00c30e` / `d4a20125` after explicit authorization and fresh verified 69-parameter snapshot; latest learned values preserved, Alpha ON and 1.20/0.97 retained.
- Whole previous install retained at `/data/openpilot.pre-release-timeout-<private timestamp identifier>`. No OS/firmware update or device reboot.
- Ignition-off acceptance, owner home-screen confirmation, activated-stack powered Park check and final preservation audit passed: 20 Hz, zero drops/faults/blocked TX, all 1,101 observed coordination pose inputs valid.
- Next evidence: retry longitudinal maneuver tests; new release behavior is not yet road-proven. Separate pose faults and highway pulsing remain open.
- [Activation report](docs/research/navigator-release-timeout-staging-2026-10-25/ACTIVATION_REPORT.md).


### 2026-10-25 full maneuver follow-up and pulsing evidence

- Downloaded all 93 new completed segments / six sessions (793 MB), hashes verified; no device changes. Exact source versions separated.
- New `ead00c30e` / `d4a20125` test reached Maneuvers Finished: seven types × three runs, zero recorded ControlsMismatch/coordination faults; 19 uninterrupted valid runs, two pedal-interrupted runs excluded. Three moderate-braking recoveries cleared after 1.56–1.58 s and resumed propulsion afterward without the old timeout. Targeted moving-release repair now has test evidence.
- A separate pose-related mismatch at ~40.9 mph occurred before installation; not proven resolved by low-speed testing. No post-fix normal active highway coverage was recorded.
- Acceleration benchmark limits identified: 25 mph cruise cap constrained first +1 trials; 31 mph-headroom trial tracked ~0.97 m/s². +2 trials were dominated by measured release waits and existing 0.5 m/s²/s gas ramp, so do not increase gains from requested/actual ratios alone.
- Two pre-installation highway drives provide ~35.7 qualified active minutes through ~65 mph. Selected ~55 mph window: gentle positive planner demand, 24 transmitted brake transitions/15 s, real reported torque cycling, stable 10th gear and no brake denial; occurs without a lead too.
- Next local priority: coupled near-zero-demand coast/brake/propulsion mode stability, integral recovery and release/ramp dynamics, preserving measured clearance/urgent braking. No new tuning installed.
- [Analysis and plots](docs/research/navigator-maneuver-followup-2026-10-25/REPORT.md).


### 2026-10-25 near-zero handoff/integral spike — rejected for integration

- Implemented local bounded coast/debt/recovery state and separate marker-aware integral settling over the actual controllers; corrected deadline requalification defect with RED/GREEN regression. No Comma access or paired-source changes; 1.20/0.97 retained.
- 18 focused tests plus 157 retained tests / 20 subtests passed. Full coupled replay: 137 segments, 401,970 callbacks. Fresh native replay of 76 new segments: 17,832,115 RX / 521,403 TX per variant, zero added rejection, no permission override. Older 61 segments and maneuver-route wire outputs remain identical to their current-stack baselines.
- No new faults, but no meaningful highway switch reduction. One route adds transitions at 35–40 (21→23) and 40–45 mph (44→46); 50–55 mph brake time increases ~0.585 s. Small downstream integral/deceleration shifts remain (maximum raw difference ~0.00051 m/s²). Not an installation candidate.
- Next local investigation: effective near-zero actuator force/response and timing with grade/integral mode-level consistency. Do not increase gains, relax clearance or extend coast grace simply to pass the replay.
- [Prototype report](docs/research/navigator-near-zero-handoff-prototype-2026-10-25/REPORT.md).

### 2026-10-25 actuator timing + mode-selection replay — rejected

- Investigated release/coast/drive jointly with continuous speed-reference debt and bounded positive-integral recovery. Corrected added weak-release timeout with measured-progress backout; original received-pressure clearance, stalled/progressing timeouts and propulsion interlock retained.
- Full coupled replay: 137 cached segments / 401,970 callbacks. Fresh native replay across all 137: 32,171,016 RX and 951,332 TX per variant, zero added safety rejection/relay fault, no forced permission. Fourteen focused tests plus 157 retained tests / 20 subtests passed. Native checks are plain debug, not hardware/road validation.
- **Do not integrate:** combined trial increases matched brake transitions 992→1,050, rapid reversals 218→275 and brake time ~67.5 s. Some named windows improve but overall cycling regresses. No added coordination faults in the revised replay; older baseline faults remain.
- Integral history survives mode fallback: first later lead-braking regression at relative 453.188 s / 31.24 mph. Across that route, 588 generated wire requests are weaker during strong planner deceleration, maximum delta 0.0117 m/s². Not solely sub-quantization noise. Mode-only ablation also fails improvement gates.
- Next useful local task: identify effective coast/engine-braking force and apply/release response, validating by gear/grade on held-out OEM/Alpha data. Evaluate authority-aware integral with that dynamic response; frozen-pressure replay alone cannot establish ride improvement after changed commands. No gain increase, indefinite freeze or clearance relaxation to hide the blocker. No new owner drive requested by this result.
- Paired branches remain clean at `ead00c30e` / `d4a20125`; Comma untouched, 1.20/0.97 preserved. [Full report](docs/research/navigator-timing-mode-resolution-2026-10-25/REPORT.md), [machine result](docs/navigator-reference/PRIVATE_ARTIFACTS.md).

### 2026-10-25 gear/grade coast identification and bounded propulsion trial

- Reused 96 verified OEM/Alpha segments; extracted 2,137 overlapping stable-mode/no-reported-brake windows and retained route-separated evaluation. Valid near-zero/negative propulsion and inactive propulsion have distinct observed responses. Near-zero does not mean zero reported wheel torque. Vehicle pitch is a grade proxy, not surveyed road grade.
- Held-out weak-demand net-request prediction RMSE: ~0.059 m/s² OEM / ~0.079 Alpha. Added gear/grade context did not outperform simple net-request prediction on the broader held-out Alpha set. No justification for a blanket extra grade or gear correction.
- Identified 277 moving brake-release episodes, 243 observed-clear completions. Typical completed 10th-gear release ~0.15–0.2 s is not a maximum or clearance permission. Zero qualified Alpha inactive/no-brake windows and zero isolated coast steps under strict criteria: full engine-drag/response-delay map remains unidentifiable from this selection. Uphill/other gears and 70–85 mph remain insufficiently covered.
- **Rejected bounded valid-propulsion bridge:** final 137-segment / 401,970-callback replay adds no coordination faults but increases brake transitions 992→1,008 and rapid reversals 218→243. Later integral history weakens 430 strong-deceleration wire requests, max delta 0.1326 m/s². The named highway pulsing windows do not improve.
- Nine focused tests, 157 retained tests / 20 subtests passed after deadline/fallback and invalid-pitch regressions were fixed. Fresh native replay of all 137 segments: 32,171,016 RX / 951,332 TX per variant, no added rejection/relay fault/forced permission; final fixes have exact wire/producer identity to the native-tested variant. This is not hardware/road comfort proof.
- Next design gate: explicit actuator allocation and authority-aware integral recovery must contain the **later lead-braking divergence**, with dynamic-response uncertainty visible. Do not widen support, infer clearance or use recorded integral as an oracle to pass. No new ordinary highway trial requested by this result.
- Comma and paired clean branches unchanged; 1.20/0.97 retained. [Report](docs/research/navigator-gear-grade-coast-2026-10-25/REPORT.md), [result](docs/navigator-reference/PRIVATE_ARTIFACTS.md), [gear/grade support](docs/navigator-reference/PRIVATE_ARTIFACTS.md).

### 2026-10-25 separate downhill-off and BP allocation comparisons

- Verified live BluePilot source at `54acf36b6`; Ford extension/controller unchanged from previously examined cached files. Tested downhill negative-pitch clamp and an explicitly adapted independent brake/precharge threshold allocator separately; BP lead caps, no-lead zero braking and eligibility gates excluded. Also replayed a conservative precharge-only gas-withdrawal ablation.
- Each primary variant: full 137-segment / 401,970-callback causal controller replay and fresh native replay (32,171,016 RX / 951,332 TX per variant), zero added native rejection/relay fault/forced permission. Eight focused tests each pass; retained behavioral contracts fail (A: 6 tests + 8 grade subcases, B: 5 tests + 4 grade subcases). Original baseline remains 157 tests / 20 subtests passing.
- Fixed-original-request raw-threshold diagnostics: brake-on time ~36% lower with downhill off and ~70% lower with allocation; allocation raw transitions increase 298→340. These are pre-guard command decisions, not actual brake time or comfort proof.
- **Neither ready for integration:** recent 76 segments have 10/9 release-timeout episodes versus baseline zero. Frozen recorded torque continues following old brake commands; 12/16 and 13/19 newly faulted contexts across the whole corpus still have baseline braking active. Do not interpret these as proved real-world BluePilot faults or credit disengagement as reduced pulsing.
- OEM reference confirms independent precharge: 1,609 eligible precharge-only samples, 1,605 with valid propulsion; all 8,667 actual-brake samples have propulsion inactive. Physical ownership/clearance remains unresolved under the current observer contract.
- Next gate: allocator must share an explicit sustained-demand/actual-speed-error budget with admission/release and retain truthful authority feedback. Reconcile grade-policy contracts with supported ECU response semantics; validate later lead-braking integral recovery. Do not reset clearance or rewrite recorded torque to pass.
- PR [#38367](https://github.com/commaai/openpilot/pull/38367) merged July 22, 2026 and is already an ancestor of the paired branch. It separates cruise-speed planning from lead MPC; relevant to selected-target/slow-speed diagnosis, not a missing Ford actuator fix. No cherry-pick needed.
- Comma/settings/paired source unchanged; 1.20/0.97 retained. [Comparison report](docs/research/navigator-downhill-allocation-ab-2026-10-25/REPORT.md), [results](docs/navigator-reference/PRIVATE_ARTIFACTS.md).

### Allocator contract resolution — bounded precharge entry passes locally

- Resolved budget bypass, clearance-phase classification and integral recovery for a **constrained precharge-entry allocator**, retaining nominal release timing. Full BP early coasting/release and downhill-disable behavior remain disabled/deferred; highway pulsing is not proved fixed.
- Signed demand area and absolute deadline run independently of BP thresholds. Committed actual braking cannot downgrade to precharge. Rearming requires a continuous eligible positive-intent dwell with observed clearance and fresh low torque; override, invalid context and delivery gaps interrupt the dwell. A positive-net latched nominal request cannot leave precharge unbounded.
- Brake OR precharge counts as active brake actuation for the observer/handoff. Only after both bits withdraw does unchanged measured release qualification start. Separate truthful precharge/phase metadata preserves signed brake-stage PID behavior; ordinary release/ramp antiwindup resumes immediately. Broad one-sided integral freeze/extra recovery hold were rejected because they held braking longer.
- **20 focused tests, 157 retained tests / 20 subtests pass**, including seeded 5,000-step policy checks and RED/GREEN regressions. Full current longitudinal replay: 137 segments / 401,970 callbacks, zero added faults, exact baseline integral/gas/acceleration histories and brake/precharge actuation union; zero strong-deceleration regression. Two older baseline faults remain unchanged.
- Only actual-deceleration bit changes: 1,879 callbacks / 189 entry episodes, 37.657 s of precharge-only, longest observed 0.324494 s including callback quantization. Matched actual-brake transitions 992→971, rapid reversals 218→224; no comfort claim and no change to propulsion-inactive time.
- Native safety coverage: final changed 79 segments rerun, remaining 58 reused only by exact wire identity; 32,171,016 RX / 951,332 TX per variant, zero added rejection/relay fault/forced permission. Not ARM/hardware/road/sanitizer proof.
- **Not paired-integrated or installed.** Next integration must explicitly version precharge/nominal-demand/phase/budget metadata and coherently transport the consumed target, replacing research-only seams before normal build/ARM/staging checks. Comma/settings and clean paired `ead00c30e` / `d4a20125` untouched; 1.20/0.97 retained.
- [Report](docs/research/navigator-allocator-contract-resolution-2026-10-25/REPORT.md), [design and IPC requirements](docs/research/navigator-allocator-contract-resolution-2026-10-25/DESIGN.md), [results](docs/navigator-reference/PRIVATE_ARTIFACTS.md).

### 2026-10-26 — coordinated coast/integral Stage A complete

- **Not identifiable with the unchanged archived model.** Audited 17,943 cases / 53,829 case-horizon evaluations; preserved original whole-route roles and immutable source/model hashes.
- Reconstructed all 54 original paired coast/brake queries: 43 point-forecast improvements, **zero conservative interval advantages**. All 54 old query caches additionally lack fresh independently received radar context.
- Training coverage at 60–70 mph has only 2 stable 200 ms valid-negative engine-request cases and 1 near-zero case (plus 8 inactive-propulsion cases), from one route/gear identifier. Global model support is not conditional gear/grade authority proof.
- 52 contract tests pass; independent result review found no actionable issue. No new mode-selector/back-calculation prototype, paired runtime edit, device connection or activation. The approved feasibility gate stops Stage B. The committed local low-speed guard and 1.20/0.97 remain unchanged.
- Next useful local work: re-extract received torque, RPM/gear, pose/grade and radar from already saved newer routes; inventory naturally occurring coast exposure before asking for more drives or training a separately versioned model. Preserve independent route evaluation and the immutable current archive.

[Feasibility report](docs/research/navigator-coast-authority-feasibility-2026-10-26/REPORT.md).

### 2026-10-26 — coast signal recovery and existing OEM highway evidence

- Recovered and hash-verified 37 newer saved segments across four sessions. Two active Alpha sessions have 40,977 command observations (~819.56 s), all with fresh radar. Exact torque reconciliation covers 284,854 observations.
- The named 62–64 mph episode has 20 brake transitions while actual/target gear stays 10 with fully engaged clutch. Newer Alpha data has 49 provisional coast episodes, only six at 60–70 mph, all shorter than 600 ms.
- Continued into the older saved OEM evidence: re-extracted 19 more segments from `oem-04` and `oem-05`, preserving original calibration/test labels and separating incoming stock commands from outgoing Alpha commands. Another 454,730 decoded stream observations reconcile exactly; all 25,114 active stock-command observations have fresh radar.
- Found **34 OEM highway coast episodes, 10 lasting at least 600 ms, including eight in the negative-gravity-proxy band**. This gives the next offline model experiment relevant saved evidence. No new drive needed for that step.
- RPM quality remains unresolved (flag 0 in both older and newer data); all coast candidates remain provisional. No archived model, training/evaluation role, paired runtime or Comma change. Steering 1.20/0.97 preserved.
- 25 contract tests pass; independent initial and supplemental result reviews found no actionable issue. Next: a separately versioned research model with consistent grade frames, explicit RPM uncertainty and honest route separation; no controller prototype until conservative support and coupled replay gates pass.

[Signal recovery report](docs/research/navigator-newer-coast-signals-2026-10-26/REPORT.md).

### 2026-10-26 — latest city drives and MAX-speed behavior

- Acquired 14 new completed segments across two sessions, with clean installed pair `5b301a944` / `884c9f491` and AGNOS 20.1. All 154 completed device rlogs at acquisition have hash-matching local copies. No device writes.
- New trips are city driving: max active 29.51 / 30.05 mph, max set 30 / 37 mph. No 85 mph run in these recordings. No recorded controls mismatch or coordination fault.
- Installed planner always considers model acceleration alongside cruise and lead MPC; MAX is a ceiling. Model selected 94.9% / 73.0% of qualified planner samples. No separate posted-limit controller/toggle; the old ExperimentalMode parameter does not gate the model candidate in this code.
- At <private clock time>–<private clock time> Central: MAX 35 mph, median 25.28 mph, lead present, model target median +0.019 m/s² and 17 brake-bit changes. New moving city regression for combined planner/actuator smoothing; not proof of a 25 mph sign cap.
- Owner explicitly chose to leave the Comma unchanged. Below-6.7 mph guard remains local; coast model is not validated runtime code. Existing OEM ACC path is Alpha OFF. A new stock-like Alpha option would require explicit model-stopping tradeoffs and validation.

[Latest drive report](docs/research/navigator-latest-smoothness-road-review-2026-10-26/REPORT.md).

### 2026-10-26 — city handoff prototype rejected; highway regression retained

- Traced the city 25 mph / 17-change episode. All 17 transitions occur after precharge budget exhaustion. Tested a narrow negative-target release/ramp antiwindup extension, preserving actual braking and signed recovery.
- Standalone city 17 → 17 with braking exposure 21.538 → 22.671 s: no demonstrated smoothing. Named 63 mph highway 20 → 20. Full 176 segments / 512,066 callbacks increase 1,193 → 1,196 changes and produce 441 less-negative strong-target brake acceleration fields (max 0.0312 m/s²). Not covered by the earlier low-speed guard's limited variation acceptance.
- Rejected: no paired integration, native firmware replay, ARM build or device deployment. 48 research tests pass; independent review's route-coverage issue fixed with fail-closed manifest checks. No remaining review finding.
- New city frozen replay also gives the earlier **uninstalled** low-speed guard 7 changes but much more braking than the installed 17-change baseline. Keep the commit unchanged, but reassess before staging; this is not a proven physical outcome or a smoothing benefit.
- Highway work remains active: recovered OEM 34 coast episodes / 10 sustained cases are inputs for a separately versioned response-aware allocation experiment. This integral-only candidate does not fix highway pulsing. Steering 1.20/0.97 and Comma unchanged.

[City/highway prototype evidence](docs/research/navigator-city-handoff-prototype-2026-10-26/REPORT.md).

### 2026-10-26 — response-aware allocator remains research; high-RPM protocol evidence

- Downloaded 2 new drives/21 completed segments read-only, verified hashes and unchanged source/settings. No recorded controls mismatch or coordination fault; max active66.35 mph, no new 75–85 mph proof.
- Highway regression confirmed:23 brake changes in20 s at 57.8–60.7 mph, tenth gear, received brake torque 0–232 Nm. Preserve this separately from the original 63 mph regression.
- Response prototype versions retain2,036 cases from147 saved OEM/Alpha segments in v3, with separate mode evidence and whole-route exclusion; latest drives excluded from fitting.364 entry opportunities / 200 context passes, zero qualifying coast/engine alternatives. Model uncertainty remains too wide; no city/highway smoothing fix is proved.
- V1 full actual-controller shadow replay:197 segments / 12 routes / 570,269 callbacks, zero changed longitudinal packets;1,370 → 1,370 brake changes.34 focused tests pass. V3 is additional causal diagnostic scoring, not a counterfactual physical/controller validation claim. No native/ARM work for the unqualified candidate.
- Matched owner's high-RPM episode:decoded 4,136 RPM at 16.6–22.7 mph, Alpha active/no driver gas, first-to-second target/actual shift delay. RPM quality unresolved. OEM predicted acceleration and target-speed fields vary; Alpha holds −5 and 145 km/h. Investigate timing/torque semantics passively before changing CAN fields; no causal transmission claim.
- No integration, device changes or steering/geometry changes; 1.20/0.97 preserved. Earlier uninstalled below 6.7 mph guard still needs city-exposure reassessment. Remaining saved maneuver routes can be incorporated into response extraction locally; no new drive required merely for that.

[Response-aware allocator and new-drive report](docs/research/navigator-response-aware-allocator-2026-10-26/REPORT.md).

### 2026-10-26 — OEM prediction/target-speed protocol investigation

- Compared 168 saved segments / 16 routes; 40,548 qualifying OEM and 250,474 Alpha command samples. Prediction −5 and target-speed 145 km/h are constant across active Alpha, including normal and problematic driving. Saved data cannot isolate their physical effects from owner/controller differences.
- OEM prediction mostly mirrors same-time signed request; OEM target speed resembles a varying near-term speed trajectory, not the selected maximum. Do not simply copy set speed or forward OEM prediction. 6,193 OEM prediction samples exceed the current native gas-channel range; 64-case synthetic native unit probe confirms limits, not ECU response.
- Two high-RPM rolling starts report second-gear target at 20.69/21.23 mph versus median 9.21 mph in 30 completed Alpha first-to-second cases. Reported completion delays are within the normal selected range. RPM quality remains unresolved.
- Recorded PID identifies a stronger local lead: integral ~0.77/0.83 at 6.7 mph raises raw request to ~2.0; same-drive normal start has integral ~0.17 / raw ~1.29 with similar planner demand. Installed positive-demand ramp anti-windup starts at 3 m/s. Revisit bounded low-speed integral/release recovery with both high-RPM starts plus the city 17-change regression; existing uninstalled guard is not cleared by this analysis.
- Five contract tests and native range probe pass; no new controller replay, source integration, CAN transmission or device access. 1.20/0.97 and exact paired pins unchanged. Highway pulsing remains unresolved; no causal field fix is established.

[OEM protocol and rolling-restart evidence](docs/research/navigator-oem-long-protocol-investigation-2026-10-26/REPORT.md).

### 2026-10-26 — rolling-restart integral recovery prototype rejected after full replay

- Implemented narrow moving-restart qualification in offline seam, replacing the uninstalled broad guard only for research. Bounded second trial omits at most 0.25 m/s² of positive integral growth per approach (observed max 0.24913), with 3 s deadline; signed recovery, physical clearance and native limits unchanged. This does not bound later trajectory divergence.
- Raw request peaks in the two high-RPM windows fall about 2.0 → 1.71 / 1.77 m/s². Entire named city route remains byte-identical: 17 brake changes and 21.533 s command exposure; normal stopped-launch fixture unchanged. No physical RPM/shift/comfort improvement proven.
- Full controller corpus: 197 segments / 570,269 callbacks processed. 185 segments have no active atomic-input gaps; one retained 12-segment route has five active prefix gaps and stays diagnostic-only. Encoded gate now checks every strong-target row independently of raw request ordering.
- REJECTED: 19 one-increment weaker strong-target brake fields and a simulated 61.23 mph release-timeout in input-complete alpha-comfort route; 8,969 later callbacks lose activity. Last rolling hold precedes fault by about 317 s. Lower request peaks do not clear later brake/feedback-history failures. Do not relax release safeguards to force a pass.
- Fresh native replay of all 197 segments: 570,178 replacement ACC send slots; 134 retained TX rejections each, zero added TX rejections or relay faults; no forced permission. This does not clear software gates or prove hardware response. 46 focused tests pass; independent review supports rejection.
- No paired integration, push, Comma access/install or steering change. Preserve 1.20/0.97; earlier broad local guard remains uninstalled and unchanged. Next local design must address post-ramp recovery/history with truthful changed-response evidence, retaining these regressions.

[Rolling-restart prototype and full-replay evidence](docs/research/navigator-rolling-restart-recovery-2026-10-26/REPORT.md).

### 2026-10-26 — post-ramp recovery: 61 mph regression removed, candidate still rejected

- Added local bounded recovery/accounting and clipping-aware same-input integral revaluation; 91 focused tests pass. Exact paired source and 1.20/0.97 preserved; no Comma access or integration.
- Full 197-segment / 570,269-callback controller replay removes the old 61.23 mph timeout, but adds a 20.59 mph timeout (104 lost-active callbacks), 472 weaker encoded strong-target brake rows (max 0.1014 m/s²), and two new low-speed positive-gas/retained-torque rows. Keep rejected; do not widen pressure/deadline limits.
- Named city route remains byte-identical (17 brake changes / 21.533 s exposure). Selected rolling request peaks decrease, but actual RPM/shift/comfort remain unproved. Zero pending recovery debt did not prevent later integral/command divergence (~0.1803 m/s² near the new fault).
- Highway pulsing remains unresolved: selected highway regressions unchanged at 20, 22 and 12 reconstructed brake changes. Next design must coordinate integral recovery and coast/brake mode history, with a post-recovery command bound and all braking/release gates retained. Native compatibility alone cannot clear controller failures.

[Post-ramp recovery evidence and full results](docs/research/navigator-post-ramp-recovery-2026-10-26/REPORT.md).

- Final native replay for post-ramp recovery: all 197 segments, 570,178 replacement ACC slots, zero added TX rejections/relay faults (reference 134 TX rejections, candidate 133), no forced permission. Controller rejection remains authoritative.

### 2026-10-26 — command recovery clears named replay failures; highway comfort unresolved

- Replaced rejected integral-debt repayment with a local transient positive-demand reduction plus anti-windup for that explicit output constraint. No saved-baseline I/wire copying, pressure/deadline relaxation or permission changes. 58 focused tests pass; independent review caught/fixed overlay sequence rollback.
- Full197segment /570,269callback controller replay: **zero added timeouts, lost/gained activity, weaker raw/encoded strong-target requests (33,194checked), or new positivegas with retained torque**. Old20.6mph and61.23mph failure episodes now remain in actualbraking. Two preexisting reference release-timeouts remain unchanged.
- City route byte-identical:17changes /21.533s. Normal stopped launch unchanged; rolling-window peak raw demand2.0→~1.75. Physical RPM/shifting not proved. Post-overlay integral is not globally identical to reference; audit retains all differences.
- **Highway pulsing remains unresolved:** selected20/22/12-change windows unchanged. Aggregate brake changes1434→1434; brake-command exposure **+4.349s** across corpus. Treat stronger/longer braking as a tradeoff, not comfort improvement or install approval.
- Candidate remains local/separate; exact paired branches, Comma and1.20/0.97 unchanged. Native replay receipt recorded alongside report. Next decisions must separate rolling-recovery regression clearance from highway coast/brake comfort and physical response validation.

[Command recovery design, regressions and limits](docs/research/navigator-command-recovery-2026-10-26/REPORT.md).

- Final native replay for command-recovery candidate: all197segments /570,178replacement ACC slots; zero added TX rejections/relay faults,134retained TX rejections on each side, no forced permission. Source/header/binary receipts verified; paired checkouts remain clean. This does not establish highway comfort or hardware response.

### 2026-10-26 — command recovery integrated locally; full checks pass

- Local clean pair on `codex/navigator-tracking-release`: openpilot `1dbbc01892616c4b1a5c7c841d132f724ea5132c`, opendbc `beb10c25770471534261606072c131db5eefa117`; exact gitlink verified. Replaces earlier uninstalled broad low-speed I guard with qualified command recovery and local-output anti-windup.
- Minimal/full Mac and Panda builds pass. Parent 1,086 passed /87 skipped /1 expected failure /281 subtests; child 4,686 passed /1,690 skipped /24,693 subtests. Targeted lint/diff and whole-pair review pass.
- Exact accepted-prototype parity: all197segments /570,269callbacks /1,104,297producer updates, zero differences. Native proof explicitly reused for identical wire stream and unchanged safety binary/headers. No new ARM or hardware proof.
- 1.20/0.97 and protected geometry/controller/safety files unchanged. Highway pulsing remains unresolved; named windows unchanged, aggregate braking exposure+4.349s and two preexisting release-timeouts retained. No push or Comma changes. ARM/model-startup, parked and road checks remain separate.

[Paired integration receipts and scope](docs/research/navigator-command-recovery-integration-2026-10-26/REPORT.md).

### 2026-10-26 — command recovery published and staged; inactive

- Published and remote-verified openpilot `1dbbc0189` / opendbc `beb10c25` on both adgower release branches. Fresh private source/settings/calibration/launch/firmware backup verified on Mac (145 manifest members).
- Inactive stage `/data/navigator-validation/<private timestamp identifier>-1dbbc0189/source`: full ARM build pass; native/Ford/transport 1,235 passed /79 skipped /12,083 subtests; retained regressions75 pass, parent smoke14 pass/6skip, calibration continuity1 pass. All63 new policy/transport cases explicitly pass without skip.
- Isolation/preservation audit passes; no active-tree or preference changes. Installed firmware image/prebuilt behavior retained. Offroad and powered Park baseline checks pass on **existing install**, model~20Hz/drop0, no new safety/transportfaults, AlphaON unchanged. 1.20/0.97 preserved.
- **Not activated.** Existing5b301a944/884c9f491 remains live. Highway pulsing unresolved; +4.349s replay braking exposure/two preexisting reference timeouts remain caveats. Activation and candidate hardware/road evaluation are separate.

[Device staging receipts](docs/research/navigator-command-recovery-staging-2026-10-26/REPORT.md).

### 2026-10-26 — command recovery activated; parked acceptance passed

- Active openpilot `1dbbc0189` / opendbc `beb10c25`; exact pin, clean active and retained rollback trees verified. Fresh68-file parameter/calibration Mac snapshot verified before guarded atomic exchange. Previous complete install retained at `/data/openpilot.pre-command-recovery-<private timestamp identifier>`.
- Ignition-off and new-install powered Park acceptance pass. AlphaON unchanged,1.20/0.97 and steering opt-ins retained. ~20Hz bigmodel/drop0; no new safety/transport/coordinationfaults, controlsdisallowed while stationary and disengaged. Firmware,launchers,OS20.1slot_b unchanged; appservice restart only.
- Latest learned calibration retained at activation; normal post-ignition learning updates logged without manualwrites. Highway pulsing remains unresolved; road rolling-recovery/RPM/comfort improvement unproven. Next evidence is ordinary controlled road comparison, not another speed-range claim from parked data.

[Activation and powered acceptance](docs/research/navigator-command-recovery-staging-2026-10-26/ACTIVATION_REPORT.md).

### 2026-10-26 — command-recovery road review: restart exposure missing; highway pulsing persists

- Downloaded and hash-verified all34 new completed segments /3 sessions; only one current-pair moving drive, approximately20:44–21:03CDT, maximum74.51mph. Private archive retained; no Comma changes.
- Rolling command recovery was **not exercised**: minimum active speed9.6469mph versus admission below6.7mph. Assisted RPM peaked2870 after manual acceleration; absolute3358RPM peak was manual/assistance inactive. No assisted4000RPM repeat, but no improvement claim until natural qualifying rolling-restart evidence exists.
- Zero controlsMismatch/coordination faults this trip. Two brake-pedal disengagements;14 blocked-TX increments associated with startup and pedal/queued-command boundaries remain documented.
- Highway cycling persists in Relaxed:14/12/10 brake-bit changes per15s at58–62/62–64/~74mph, corroborated by reported torque. Both lead/no-lead affected. Next local priority remains coast/grade/integral allocation with brake-clearance and strong-braking preservation.
- Lateral: rising-turn software saturation around30.65mph/~70% body response; steady60–70 generally near requested, but unwind excess and straight-like~74mph corrections remain. Sparse steady low-speed evidence; no75–85mph coverage. Keep1.20/0.97; no blanket gain change.

[Road review, limits and next evidence](docs/research/navigator-command-recovery-road-review-2026-10-26/REPORT.md).

### 2026-10-26 CDT /27 UTC — highway coast-entry prototypes rejected after full replay

- Reproduced all54,969 new-drive feedback callbacks on installed pair1dbbc0189/beb10c25. Actual refreshed consumer pitch and net demand confirm weak net crossings select braking despite positive planner targets; precharge already budget-locked in named windows. This is software-chain evidence, not a causal road-grade measurement.
- Tested a bounded weak-entry extension and then explicit coast/propulsion withdrawal. First version adds two release timeouts; second clears those but retains integral/authority recovery differences. First producer crossover is saved as a regression.
- Full216segments /13routes /625,238controller callbacks;204segments have complete active atomic inputs,12older segments diagnostic-only. Explicit-coast candidate reduces brake changes1655→1649 on complete-input routes but adds51.179s brake-command exposure and2071weaker encoded strong-target requests (maximum0.039m/s²). **Rejected; not ready for integration.**
- Fresh native replay216segments /625,140ACC slots:zero added TX rejections/relay faults, no permission forcing.13prototype tests +202installed contract tests and20subtests pass with unsanitized native hooks; macOS denied UBSan loading. Protocol acceptance does not clear performance failures.
- Next design boundary: one owner-consistent coast/precharge/brake state, shared bounded allowance/rearming, and defined delivered-authority feedback for integral recovery. Do not enlarge thresholds or relax physical brake clearance to bypass the regression. Current paired branches, Comma and1.20/0.97 untouched.

[Investigation, rejected prototypes and replay receipts](docs/research/navigator-highway-coast-prototype-2026-10-27/REPORT.md).

### 2026-10-27 UTC — coordinated weak-brake allocation clears replay regressions; modest comfort scope

- Final local `coordinator3.py` removes the rejected extra coast-admission override. Earlier negative-net deferral and prospective weak precharge charge the existing sampled allowance; selected full-brake demand does not create new weak-deferral debt. Existing debt is retained. Rearm requires exactly zero ledger plus100ms continuous eligible measured-clear positive context. Existing0.01demand-area /0.3s deadline and strong fallback remain; no physical speed-loss bound is claimed.
- Truthful precharge retains the installed signed-braking integral role. All1,203,463recomputed producer steps and625,238consumer callbacks retain identical I/raw/gas and combined brake/precharge request. No I repayment, copied reference output, clearance exception or fabricated feedback.
- Full216segments /13routes (204complete-input,12diagnostic):zero weaker raw/encoded strong-target requests, added faults, extra full-brake samples or lost/gained active callbacks. Complete-input full-brake changes1655→1637; command exposure2783.745→2769.615s (-14.130s). Combined brake/precharge exposure unchanged.
- Benefit remains limited: new highway windows still14/12/10full-brake changes, with exposure reductions in the first two. Gas-withdrawal timing is unchanged; physical highway pulsing, smooth coasting and fuel efficiency are **not resolved/proved**. Do not advertise superseded early-start metrics for the final candidate.
- Final native216segments /625,140ACC slots:zero added TX rejections/relay faults, no permission forcing.18focused tests +202installed contract tests/20subtests pass with unsanitized native hooks; independent read-only review found no blocking issue. Source/input/binary/header receipts verified. No ARM/hardware/road proof.
- Local prototype only. Paired1dbbc0189/beb10c25, Comma and1.20/0.97 unchanged. Next larger comfort work requires true coast/precharge response evidence and a delivered-authority design; do not widen/forgive allowances to manufacture fewer switches.

[Final prototype, bounded scope and replay receipts](docs/research/navigator-coordinated-coast-prototype-2026-10-27/REPORT.md).

### 2026-10-27 — coordinated coast/brake fix integrated locally; full checks pass

- Committed on both `codex/navigator-tracking-release` branches: openpilot`df788e02719c05595dab2f980e6fd9fb9e464006` pins opendbc`1d29e6e78abcbf5c6a80eb397d80b349c6cca960` exactly. Both clean; no push or Comma action.
- Real allocator class matches accepted coordinator3 AST. Child16pure regressions and parent1realLongControl equivalence test; updated100ms interruption tests preserve fresh-qualification assertions. Runtime scope only child allocator.1.20/0.97, geometry, matching, consumer, safety, settings/launch and parent runtime remain protected/hash-identical.
- Minimal/full Mac builds and Panda build pass, including builds at committed heads. Parent1087pass/87skip/1xfail/281passing subtests; child4702pass/1690skip/24693passing subtests. Focused29pass, Ruff/whitespace pass. Fresh whole-pair review: no substantive finding.
- Fresh production-bound216segment replay:625,238callbacks /1,203,463producer steps; exact selected-prototype packet/I/raw/freeze/phase/recovery equality.204complete-input segments,12diagnostic-only. Native applicability reused by identical commands/raw manifest/safety headers/verified binary; not claimed as a new native run or hardware proof.
- Accepted benefit/limits unchanged: full-brake changes1655→1637 and exposure-14.130s; gas/combined request timing unchanged, new highway windows14/12/10changes. Highway physical pulsing remains unproved/unresolved. No ARM/model-startup, parked or road acceptance yet for this new pair.

[Integration report and final verification](docs/research/navigator-coordinated-coast-integration-2026-10-27/REPORT.md).

### 2026-10-27 — coordinated coast/brake pair published, backed up and staged inactive

- Both adgower release branches verified at parentdf788e027 /child1d29e6e7. Fresh private Mac source/settings/calibration/launch/firmware backup verified (821,970,076bytes /145manifest members /68params).
- Stage `/data/navigator-validation/<private timestamp identifier>-df788e027/source` finalized clean/self-contained with exact child pin and existing firmware/prebuilt behavior. **Not activated; active install remains1dbbc0189/beb10c25 at final audit.**
- Full ARM/model-target build pass;1,252native tests /79skips /12,083passing subtests;75retained regressions;14parent smoke/6base skips;1calibration continuity test. Initial staging-only private-prefix mismatch corrected; first attempt retained and native results reused only after3,796source/binary/XML hashes verified. No production patch change.
- Final current-stack offroad check551Panda samples,zero new blocked TX; selected prefs/binary calibration/personality/upgrade keys/1.20/0.97/AlphaON/OS20.1slot_b/firmware/service/continue.sh unchanged. Only expected ping/uptime counters changed. No app restart, OS/firmware update or CAN transmission.
- User needed to drive; validation was already complete/inactive and current source untouched. Advised manual driving with assistance disengaged due unresolved Alpha pulsing; remaining documentation completed locally. No candidate powered-Park/road proof and no activation authorized/performed.

[Inactive staging report and receipts](docs/research/navigator-coordinated-coast-staging-2026-10-27/REPORT.md).


## October 27: coordinated coast/brake active

Pair `df788e027` / `1d29e6e7` is active. ARM/replay checks and ignition-off/powered-Park acceptance passed. Alpha ON and 1.20/0.97 preserved; previous complete installation retained. Highway pulsing and comfort improvement still require road evidence. See [activation report](docs/research/navigator-coordinated-coast-staging-2026-10-27/ACTIVATION_REPORT.md).


## October 27: first coordinated coast/brake road evidence

Reviewed all 73 new segments, five sessions; one moving current-code trip. No controlsMismatch or coordination fault recorded. Highway cycling persists (17 and 14 brake-bit changes in 15 s near 59/68 mph). Assisted RPM reached 3,946 at 21 mph in first gear, with no braking during the peak. Restart propulsion remains continuous across 6.7 mph. Calibrated body response supports excess turning at 40–50 mph and residual unwind/straight oscillation near 64 mph. No >70 mph moving evidence. Next local work: coast/grade/integral/response timing; first-gear restart demand and OEM shift response; 40–50 mph mapping/unwind. Road improvement from this allocator remains unproved; installation/settings unchanged. [Full evidence and limitations](docs/research/navigator-coordinated-coast-road-review-2026-10-27/REPORT.md).


## October 27: local pulse / restart / midrange prototypes evaluated

- **Pulsing — rejected candidate:** full 237-segment / 14-route coupled replay completed (685,504 callbacks), plus native saved-traffic replay (685,398 ACC slots, no added native rejections). The unified true-coast / phase-wide integral freeze worsens city cycling 17→27, weakens later strong braking and adds a simulated release-timeout near 55 mph. Native acceptance does not override these controller failures. Keep installed code unchanged.
- **High RPM — diagnosis and shadow exploration only:** received second-gear target appears at 18.885 mph versus roughly 9 mph in saved OEM examples, despite lower propulsion demand. No blanket acceleration cap or literal cruise-target packet policy is supported. Five diagnostic checks and 18 synthetic native packet cases pass; no runtime policy selected.
- **40–50 mph steering — diagnostic candidate:** extend existing bounded roll-aware mapping over 35–55 mph with the exact current ObserverContinuity baseline. Full 658-segment / 33-route saved safety comparisons add no native rejections; 106 targeted tests pass. No changed angle frames above 55 mph; 1.20/0.97 remains unchanged. Recorded path commands shrink about 2% in the 42 mph episode and 7% near the 50 mph input. Transition-direction flags and insufficient correction of the larger 42 mph excess remain open; physical improvement is unproved.

No paired source, device, settings, firmware or installation changes. None of these results authorize installing a new policy. Next local design must address joint demand/grade/delivery response and steering admission during transitions, rather than enlarge allowances or suppress safety faults. [Full experiment reports and verification](docs/research/navigator-control-refinement-prototypes-2026-10-27/REPORT.md).


## October 27: local timeout/braking and steering-transition repairs clear saved replay gates

- **Longitudinal repair selected locally:** ordinary ramp anti-windup preserved; explicit revision-3 signed-coast feedback and logical clearance ownership replace the failed phase-wide freeze. Full 237 segments / 14 routes / 685,504 consumer callbacks have no added fault, lost activity, weaker strong braking or raw/I/gas difference. All 1,311,408 producer steps match the coupled reference. All 627 changed packets only clear precharge. Native replay adds no rejection; 32 tests pass. The two older reference timeouts remain identical, and main highway brake-count/propulsion cycling is unchanged: physical pulsing improvement remains unproved.
- **Steering transition repair selected locally:** elapsed fresh coherent body/wheel admission, hysteresis and exact original mapping fallback. All 18 prior transition risk slots now equal baseline; some useful mapping correction remains. Full 658-segment / 33-route coverage adds no native rejection, preserves default-off and all protected speed bands, and matches prior reference hashes. 123 tests pass. Historical 637 segments freshly replayed; same-candidate focused 21 reused with hash binding. Physical oversteer correction remains partial/unproved.

Paired sources and Comma unchanged; owner 1.20/0.97 retained. Next step is deliberate paired-source transport/controller integration plus build/integration validation, not activation from a research hook. High-RPM protocol identification and physical coast response remain open. [Repair reports and final verification](docs/research/navigator-control-regression-repair-2026-10-27/REPORT.md).
