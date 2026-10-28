<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator branch feature inventory

Planning and progress tracking live in the [main Navigator roadmap](../../NAVIGATOR_ROADMAP.md). This inventory supplies the feature details and implementation provenance.

For the reusable workflow and tuning lessons, use the [main tuning guide](../../NAVIGATOR_TUNING_GUIDE.md). The [complete research catalog](NAVIGATOR_RESEARCH_INDEX.md) provides the dated report/design index; historical entries below are not automatically current installation state.

The [device settings inventory](navigator-migration-settings-2026-10-14.md) records what must be carried into paired branches. Native Navigator identification and upstream PRs are planned under NAV-11–13; current forced-Expedition operation is not first-party Navigator support.

Updated October 28, 2026. The goal is to retain the stock openpilot Chestnut software path while bringing Navigator steering behavior from BluePilot into the openpilot and opendbc forks. This is a two-repository feature set: openpilot supplies runtime, settings, and the pinned opendbc dependency; opendbc supplies vehicle geometry, Ford control, and paired Panda safety.

## Latest saved-drive review — October 28 (unchanged installed source)

[Drive report](navigator-returned-drive-review-2026-10-28/REPORT.md): three newly retrieved recordings / 29 segments from <private clock time>–<private clock time> local retain installed e05e42f43 / 5097b993, Alpha ON and 1.20/0.97. No recorded controlsMismatch or coordination faults. Pulsing remains: a 61–62 mph 15-second window has 17 brake-bit changes; a 24–26 mph city window has 11. The owner reports one high-RPM incident; a likely <private clock time> match has decoded peak 4,362 RPM in reported first gear, with target changing toward second and no pedal/brake/precharge. RPM quality remains unresolved.

A 3.25-second rising-demand episode near 15–17 mph achieves about 53% body/request and 51% wheel-model/request before steering input. Modest excess is present descriptively at 50–65 mph, but no episode passes the stronger uncertainty-qualified coherent-excess screen. Driver inputs remain candidate interventions, not confirmed failures. No 70–85 mph evidence was added. The new analysis separates inactive propulsion from ordinary brake-clear engine requests; earlier frozen coasting labels are not reused as quiet-coast authority. Originals are checksum-verified and privately archived. No new tuning or device changes.

## Post-clear rebraking — October 28 (local diagnostic rejected)

[Combined report](navigator-postclear-rebraking-2026-10-28/REPORT.md): the 13 received-clear/rebrake pairs split into five pitch-proxy dominated, four integral dominated, three planner dominated and one without an intervening released callback. All four integral-dominated pairs have negative average target-minus-actual acceleration; clearing I is not justified. The OEM/Alpha pitch ranges overlap; no sensor defect or physical coast authority is established.

A fixed bounded grade filter passes 14 focused software tests but fails the fresh 21-segment coupled replay: brake-bit changes 280→246, full-brake exposure +9.816 s, combined exposure +11.129 s, and 218 stronger-demand rows one encoding increment weaker (maximum 0.0039 m/s²). Changing release timing alters integral freeze behavior and persists after strong-demand bypass. Changed-reference omissions against locked original accounts are unsupported. The separate eight-segment city control is identical (17 changes), not improved. No full 316-segment expansion or integration is selected. Paired branches, Comma and 1.20/0.97 remain unchanged.

## Maneuver brake-release validation — October 28 (local; pulsing remains unresolved)

[Combined report](navigator-maneuver-release-validation-2026-10-28/REPORT.md): the complete current clearance chain qualifies three clean moving maneuver releases after 1.560–1.584 seconds without timeout. Status clear precedes reported torque clearance; keep measured qualification. Eleven other negative-reference windows are stopped/creep, interrupted or held and remain censored.

Fresh road-window analysis preserves 14/15/12 brake-bit edges. Five of 18 release/rebrake pairs lack a new received clear sequence, while 13 have one; only two have positive reported torque at rebrake. A release-delay change alone does not explain all pulsing. The low-speed tests do not identify highway quiet-coast/grade authority. An offline observer and 10 focused tests are retained; no controller change is selected. Existing suite: 210 passed, one native test failed to load macOS UBSan; the separate unsanitized native permission contract passes. No device or paired-source changes; 1.20/0.97 preserved.

## Maneuver evidence recovery — October 28 (local; blockers remain)

[Combined report and verification](navigator-evidence-recovery-2026-10-27/REPORT.md): the expanded bounded inventory covers 1,669 original segments and recovers two genuine longitudinal maneuver sessions (20 completed-session segments and 22 partial-session segments). Clean repeated low-speed PID braking provides usable reference-response evidence. Command/status clearance still precedes measured torque clearance; highway coast authority remains unidentified. No lateral maneuver execution was observed in this retained set; recording gaps and missing parameters remain unknown.

The pre-action steering bias refinement worsened held-out moving-target RMSE from 1.016 to 1.171 degrees and was rejected. Next work can build source-bound PID/release fixtures from the recovered longitudinal tests; neither a new allocator nor a validated steering response provider is ready. No integration, device changes or new full controller replay; paired sources and 1.20/0.97 are preserved.

## Response-state resolution — October 27 (local fixes; control blockers remain)

[Combined report and verification](navigator-response-resolution-2026-10-27/REPORT.md): joint brake/authority transactions and a one-outstanding steering correction were prototyped locally. The brake focused replay adds about 0.888 seconds of braking and weakens 212 encoded strong-request rows, so it is rejected. Its causal chain identifies mode-dependent integration/freezing after the initial correction.

Steering resolves prior synthetic delayed/quantized counterexamples and respects the selected deviation constraint, but the fresh 21-segment replay has three trials and zero response associations. A separate 14-test revision fixes the exact target-basis bug and receive/quality contract; it has no raw replay or validated moving-reference provider. Neither version is selected for integration; no new full 316/737-segment candidate run is claimed after failed focused gates.

Original-data models establish predictive value but not the needed directional authority or two-prefix steering discrimination. The next prerequisite is validated response/timing support (existing maneuver records or a separately authorized controlled-identification plan), preserving clearance and stronger-braking gates. Comma, paired branches and 1.20/0.97 remain unchanged.

## Remaining pulsing and tracking prototypes — October 27 (not selected)

[Local investigation and replay](navigator-remaining-control-prototypes-2026-10-27/REPORT.md): full longitudinal comparison covers 316 unique segments / 23 routes; full steering/controller/native comparison covers 737 unique segments / 42 routes. Both bounded initial prototypes leave commands unchanged, so neither is a demonstrated treatment. Device and paired branches remain unchanged, including 1.20/0.97.

The pulsing trace identifies the narrow effective release/reentry band and exhausted coast allowance. Next work must build on existing response-model evidence and address mode/authority/integral dynamics without reopening budgets or weakening measured clearance. A separate angle-led steering prototype reduces relevant saved commands but fails quantized-delay stress tests; a correction-only hold also fails a later stress case. It was stopped before full replay, rather than presented as ready. The next lateral blocker is an explicit delayed/quantized feedback-state design, not a global gain change. No new prototype is installed or approved for integration.

## Post-install road review — October 27

[All-range road evidence](navigator-post-regression-drives-2026-10-27/REPORT.md):79new segments archived and verified; only one new-source session provides meaningful assisted driving. No controlsMismatch or active pose-freshness fault recurred on that drive. This does not guarantee permanent resolution.

Pulsing remains at40–70mph, including14brake-request changes in15s with positive planner/producer demand. Moving5–40mph exposure is only69.94s, insufficient to establish a cure. Brief bounded true-coast activation is confirmed; physical comfort improvement remains unproved. Next local priority is allocation/integral/actuator-response reconstruction.

The driver-confirmed49mph input was a planned move into a newly added rightmost lane for an exit, excluded as problem-takeover evidence. Independent40–45mph steady tracking remains about15% above request in25.25s of selected samples;45–50mph has only4.65steady seconds after maneuver exclusion. These are tracking observations, not demonstrated lane crossing. Retain local target/unwind and60–70mph quiet-demand review. No new-source70–85mph coverage exists. Device/source/settings remain unchanged, including1.20/0.97.

## Regression repair installed — October 27 (parked acceptance passed)

[Installation proof](navigator-regression-repair-staging-2026-10-27/POWERED_ACCEPTANCE_REPORT.md): `e05e42f43` / `5097b993` active, fresh private backup verified and old whole install retained.1304ARMtests/12083subtests plus offroad and55spowered Park acceptance passed.20Hzbig model,0drops,no observed coordination/mismatch/safety faults or new blocked TX. Alpha ON,1.20/0.97,geometry/settings preserved; learned steer ratio,average offset anddelay retained despite normal route-start cache refresh. Road comfort/tracking improvement is unproved.

## Regression repair device staging — October 27 (inactive)

[Staging and final audit](navigator-regression-repair-staging-2026-10-27/REPORT.md): published `e05e42f43` / `5097b993`, separate clean/self-contained candidate, verified device/Mac backup plus fresh post-drive calibration/settings checkpoint. Full ARM build/recheck,1,304tests and12,083subtests passed (79skipped). Active `df788e027` / `1d29e6e`, Alpha ON,1.20/0.97, learned values, firmware and AGNOS20.1 remain unchanged. **Not activated; candidate powered/road checks and physical benefit remain unproved.**

## Paired coast/admission and clock repair — October 27 (historical local integration)

[Production integration report](navigator-regression-repair-integration-2026-10-27/REPORT.md): bounded truthful signed-coast protocol v3, logical post-coast clearance and original integral margins; independent-history midrange steering admission behind existing preferences; producer pose snapshot frozen before common clock to prevent the new recorded future-source race. **1.20/0.97**, geometry, other lateral bands and native safety sources retained. Local pair **`e05e42f43` / `5097b993`** passes full Mac/Panda builds and parent1,107/child4,733 tests. Production237segment longitudinal replay is exact to the accepted prototype; full658segment scheduled steering parity also passed. Clean exact paired revisions and detailed evidence live in the report. No publication or device activation in this task; physical pulsing/tracking improvement remains unproved.

[Latest road evidence](navigator-latest-mismatch-review-2026-10-27/REPORT.md) still shows real sub40mph brake/torque cycling. This remains an open optimization, independently of the locally tested mismatch timing repair.

## Latest longitudinal integration — October 23 (local/default off)

[Paired coordination and verification](navigator-long-integration-2026-10-23/REPORT.md): parent `e9ddc7668` pins child `d2e8d040`. Adds real timestamped/owner-scoped controller feedback, directional integral inhibition, OEM-derived relative grade-reference mapping, observed moving-entry/brake-release qualification and latched normal disengagement alerts. Override/restart/time-order review gaps repaired. `FordPrefLongitudinalCoordination` defaults off; Alpha alone does not enable it. Owner1.20/0.97, all lateral refinements, stock stop/creep and device settings retained.

Local builds, parent/Ford/native contracts, saved/model replay and standalone MISRA checks pass; detailed counts/limits are in the report. Modelled221→65brake edges is not a road result. **Not pushed or installed; no device access.** Next: authorized staging/ARM build and acceptance before any road trial. This entry supersedes earlier local integration snapshots below without changing their historical installation records.

## Latest local upstream merge — October 20

[Merge and checks](navigator-upstream-sync-2026-10-20/REPORT.md): local parent `db5842348` merges upstream `1ace967a7`, retaining child `8ccc6cf0` and owner1.20/0.97. Branch clean; minimal/full/Panda Mac builds,1,021parent tests,4,263child tests,UI regressions and20/100Hz stall scenarios pass. Two settings conflicts preserve Navigator offroad controls while adopting upstream initial-speed UI and ExperimentalMode removal. No new child commit or fresh full-corpus replay; no ARM/road proof for this merge.

**Local only; not pushed or installed.** Comma remains last-documented `f7b0c47d2`/`8ccc6cf0`. Future acceptance/install helpers must adapt to the removed ExperimentalMode key while retaining explicit Alpha/stock-ACC choices. MADS and Ford longitudinal repair remain separate workstreams.

## Next QoL priorities — October 20

[Latest priorities and sources](navigator-qol-priorities-2026-10-20.md): close current steering road trial; local upstream refresh recommended (21 new master commits),then optional MADS with stock ACC. Reliable Ford command coordination plus upstream Autospeed is the larger next capability track. Autospeed is development-master default model planning; it still needs openpilot gas/brake actuation. Draft PR #3 remains separate/uninstalled; current BluePilot has relevant but not Navigator-proven long changes. Keep85 mph stability as open evidence work. No source/device changes in this research.

## Earlier unwind installed — October20

[Installation record](navigator-earlier-unwind-installation-2026-10-20/REPORT.md): published and installed exact pair `f7b0c47d2`/`8ccc6cf0`. Fresh device/Mac backup verified,whole previous install retained. Full isolated ARM build,750native tests,retained320/480/714transitions,128aborts,new714onset transitions/128aborts andCard/IPC checks pass. Ignition-off acceptance passed; **powered stationary acceptance passed**. Owner1.20/0.97,all settings,learned hashes,firmware/launchers andAGNOS19.9 preserved. Physical60–70mph improvement remains unproved;28mph deviation issue remains open.

## Latest paired integration — October 20

[Earlier bounded unwind onset paired build](navigator-paired-earlier-unwind-build-2026-10-20/REPORT.md) is committed locally: openpilot `f7b0c47d2`, opendbc `8ccc6cf0`, with the child pinned and both checkouts clean. Minimal, full/development and Panda Mac builds pass, including post-commit builds; 1,018 parent tests, 4,263 child tests, 72 focused tests, 714 transitions and 128 abort cases pass. Exact port and 86,400 factory-equivalence updates carry the accepted 819-segment evidence; no fresh integrated full-corpus replay claimed.

Owner 1.20/0.97 and protected steering/safety sources remain unchanged. **Not pushed or installed; Comma untouched.** Physical tracking improvement remains unproved; 28 mph deviation work remains open. Next gate is separately authorized publication, backup and device validation.

## Latest local unwind-onset prototype — October20

[Earlier bounded onset](navigator-earlier-unwind-onset-prototype-2026-10-20/REPORT.md) passes53/819full controller/native replay with zero additional rejects,60focused tests,714transitions,128aborts and14,000shadow checks. Saved highway encoded correction starts0.101–0.249s earlier; physical benefit unproved.1.20/0.97,native limits and protected replay outputs preserved. Local research feature only, not part of the installed paired branches.

## Latest local diagnosis — October20

[Deviation/unwind timing report](navigator-deviation-unwind-timing-2026-10-20/REPORT.md) separates sharp-turn physical shortfall/model disagreement from unclipped spent-allowance deficits. Highway serial confirmation plus onset/quantization explains limited effective output. Bounded earlier onset is the next research candidate, not an implemented feature. Native limits,1.20/0.97,paired sources and Comma unchanged.

## Latest road evidence — October20

[Five new recordings/35segments](navigator-post-calibrated-rearm-drives-2026-10-20/REPORT.md) reviewed; two moving new-pair tests.23–29mph shortfall persists, with native-deviation clipping in the28mph episode. Mid correction briefly activates.64–70mph unwind still has excess response; small matched steady evidence improves but matched unwind does not.17input/disengagement groups retained.15mph/35–50mph/>=70mph evidence remains incomplete. These are observed limitations, not newly fixed features. Device/settings/1.20/0.97 unchanged.

## Latest device installation — October20

[Calibrated/mid/unwind/rearm pair installed](navigator-calibrated-rearm-installation-2026-10-20/REPORT.md): parent`f750d756ca`pins child`de70d4f945`. Fresh post-drive device/Mac backups verified, full ARM build and690native tests,320/480/714transition cases,128abort cases and Card/IPC pipeline pass; ignition-off acceptance and settings/learned preservation pass.1.20/0.97,AGNOS19.9 and firmware unchanged. Previous whole install retained. **Powered stationary acceptance passed; first road evaluation completed above; target tracking improvements remain unresolved.**

## Latest local paired integration — October 20

[Calibrated/mid/unwind/rearm pair](navigator-paired-calibrated-rearm-build-2026-10-20/REPORT.md): parent`f750d756ca`pins child`de70d4f945`on existing branches, published and subsequently installed; see current installation/road evaluation. Existing selector prerequisites/defaults and1.20/0.97 preserved.103focused tests, full parent1,018tests and child4,203tests,714transition cases,128active-abort cases,70,560factory-equivalence updates and configured Mac minimal/development/Panda builds pass. Source/factory equivalence carries prior766segment proof; no fresh integrated full corpus replay or physical improvement claim. [New18segment drive review](navigator-post-rearm-build-drives-2026-10-20/REPORT.md) still uses previous installed code and retains24mph/65–70mph issues and15mph/35–50mph/upper-speed data gaps.

## Latest local rearming/controller proof — October 20

[Resolution-aware26mph rearming](navigator-mid-rearm-controller-prototype-2026-10-20/REPORT.md) preserves the one-second neutral dwell, existing correction budgets/native limits and1.20/0.97. Saved episode now rearms and changes seven bounded packed commands. Full generated-controller comparison passes46recordings/766segments/4,432,831updates per variant with zero additional native rejections;91focused tests,714transition cases and128active-abort cases pass. Default-off and protected30–60mph/>=75mph output remain unchanged. **Local prototype only, not integrated or installed; physical improvement unproved.** Next gate is paired integration/build validation.

## Research-only candidate — October 20

[Calibrated/mid/unwind prototype](navigator-calibrated-mid-unwind-prototype-2026-10-20/REPORT.md): consistent calibrated experimental feedback, finite25–30mph allowance and once-faded wheel unwind trim.78focused tests plus766-segment recorded-timing native comparison pass with no additional rejects; protected recorded40–50mph and>=75mph output unchanged. Main26mph episode still blocked by abort/rearm and native deviation scope; road benefit remains unproved. **These are local prototype features, not changes to the installed pair.** Owner1.20/0.97 remains unchanged.

## Local diagnosis update — October 20

[Shortfall/unwind mechanism report](navigator-shortfall-unwind-diagnosis-2026-10-20/REPORT.md): the23mph calibrated observer is blocked by older fixed-pinion admission,26–29mph lies outside the below25 feedback scope, and repeated speed weighting/confirmation resets leave only nine distinct packed command changes in the highway trial. These are findings and proposed prototype targets, **not new installed features or validated fixes**. Native safety feedback and owner1.20/0.97 remain unchanged.

## Latest installation and road follow-up — October 20

Current documented paired `codex/navigator-tracking-release`: parent `0171b897289be53fd62f330935c55825b86c3c3a`, opendbc `4167433e5c575f620a9dedf8144a0bc7cba14291`. [Installation and parked acceptance](navigator-sustained-installation-2026-10-19/REPORT.md) precede the [26-segment road review](navigator-post-sustained-drives-2026-10-20/REPORT.md). Added bounded sustained low-speed allowance and calibrated60–70mph unwind extension, retaining1.20/0.97. The low-speed extra never activated in this batch; unwind ran but improvement remains unproved. Saved23–29mph shortfalls are next diagnosis targets. Historical installation snapshots below are retained as provenance.

## Current installation — last documented October 14

Paired `codex/navigator-very-low-speed-trial`: parent **76d78d46f**, child **f50241ca**, on the upstream master foundation with AGNOS **19.9 / slot B** and Chestnut **8516b768**. The [installation record](navigator-very-low-speed-installation-2026-10-14/REPORT.md) documents backup, full native build, preserved settings/1.20/0.97 and normal offroad acceptance. The [latest drive](navigator-post-vlow-drive-2026-10-14/REPORT.md) confirms this revision, big-model inference and remaining ~15 mph undertracking; overall handling improvement is not established. The previous master-only pair `6ae31161b` / `c09baff5` is retained. This local-only task did not refresh device state over SSH.

The new [bounded tracking experiment](navigator-bounded-tracking-prototype-2026-10-14/REPORT.md) is a separate report-local artifact, **not installed or selected by either branch**. It preserves current feedforward/1.20/0.97 and fades its extra term to zero by 25 mph. Full 72-segment replay passes with recorded ≥25/45 mph parity; road benefit is unknown.

The feature commit references below describe their original implementations; the clean master port is their current installed packaging. Mass fields are historical provenance: the new base uses equivalent normalized dynamics.

## Features and status

| Feature | Repository | Status and scope |
| --- | --- | --- |
| Stock openpilot Chestnut foundation | openpilot | Inherited upstream capability, rather than a new BluePilot Chestnut port. The installed device enumerated a Chestnut-compatible USB identity and firmware string. The post-correction road recording shows big-model inference with zero reported frame drops; long-term accelerator reliability remains unproven. |
| Navigator short-wheelbase vehicle geometry | opendbc | Existing commit `a6dd3a44`: changes Expedition-profile CarSpecs to wheelbase 3.1115 m, base mass 2742 kg, steer ratio 19.6. Its commit records tape-measured wheelbase, mass inferred from the door sticker, and community-reported steering ratio. Recorded runtime mass is 2878 kg after the standard cargo allowance. This overloads `FORD_EXPEDITION_MK4`; it is not a separate naturally identified Navigator platform. |
| Ford CAN-FD angle steering port | opendbc | Existing `f0e0e32f`: path-angle-primary LAT_CTL2 control, followed by Expedition-only provisional gain selection in `58d7dba5`. Brings the relevant BluePilot-derived steering approach to the stock openpilot fork; it does not port all BluePilot features. |
| Angle engagement ordering | opendbc and openpilot dependency | Existing `699dfc25`, merged at `eb70bef4`, pinned by openpilot `f35e6e5eb`. Orders mode transitions around steering requests. |
| Preserved owner steering calibration | opendbc | Retains 1.20 low-speed and 0.97 high-speed multipliers on the original high-curvature arm. These are not universal multipliers for every requested turn. The original device file and patch are saved in the preservation report. |
| Optional pinion-derived curvature feedback | Both | New paired controller and Panda safety implementation, child `54f25cd4`, parent `97f050c79`. Models curvature from steering pinion angle; it does not select another physical yaw sensor. Guarded for the supported geometry and valid pinion CAN reception. Original feedback remains available with the setting off. Installed and enabled during the latest drive. |
| Optional Navigator low-speed gain trial | Both | Child `fe85f3f7` and `6c17a0af`; parent `6ab602fdd` and `07761dfa1`. Adds 15% to the gentle endpoint and 5% to the tight endpoint, broadens the smooth curvature blend, and fades the added calibration from 30 to 45 mph. The blend can produce up to 35.75% command uplift; it is not a flat 5% or 15% increase. Keeps 1.20/0.97 and existing rate, range, deviation, and driver-override limits. Installed and enabled; experimental. |
| Comma 4 steering settings | openpilot | Parent `c1bf21f3d` adds the controls to MICI, in addition to the large-screen settings. Persistent keys are `FordPrefSteerAngleCurvature` and `FordPrefLowSpeedGain`. Changes apply on the next driving session; the low-speed trial requires the pinion option. |
| Ford/Lincoln Alpha longitudinal brake and propulsion coordination candidate | opendbc and openpilot dependency | Existing separate branch `codex/ford-longitudinal-coordination`: child `d5ccadb7`, parent `d8123f013`. Withdraws propulsion while the existing brake request is latched, scoped to the Expedition profile used by this Navigator. Earlier controller tests and fixed-input replay passed; vehicle improvement is unverified. Absent from the last verified installed steering-trial controller. [Recovered report](navigator-longitudinal-coordination-2026-10-14.md). |
| Independent steering and cruise engagement similar to MADS | Both, including paired Panda safety and UI | Requested candidate for the stock openpilot fork; not installed or implemented in this trial. Intended to allow steering assistance with manual speed control and separate cruise cancellation. Ford button, brake/gas, fault and driver-monitoring behavior require an explicit state-machine design and paired safety validation. [Research](navigator-mads-exploration-2026-10-14.md). |

## Validation and remaining work

The local trial replay covered 45 saved segments, 10,082,330 physical RX messages and 148,765 generated TX messages, with zero trial TX rejections. Messages at or above 45 mph matched the regular pinion baseline byte for byte in the replay coverage. This is recorded replay evidence, not a guarantee of handling in every road condition.

The first road trial recorded both options active and reached 35.47 mph. A selected matched 20–30 mph gentle-bend subset tracked requested curvature more closely, but other groups were mixed. It does not support a uniform handling-improvement percentage or a new 45 mph road claim. Steering discrepancies before driver input around <private clock time> and <private clock time> into the route provide useful local investigation targets for the remaining slower, sharper turns. No angle safety rejection was found near those windows in the recorded replay; hardware blocked-message counts are not completely reconciled.

Next: investigate sub-20 mph transient response, tracking delay, and possible hunting locally using the captured drive. Another drive is not required to begin. Identifying the approximate location of the reported zigzags would help relate perception to those windows, but is optional. Additional tuning is not included in this inventory as completed work.

For the requested return to Alpha longitudinal and Experimental mode, first reconcile the separate coordination candidate with the current steering trial and rerun combined controller/safety replay, including braking, brake release, grades, stopping/restart and disengagement. Qualify Alpha actuation separately before attributing behavior to Experimental planning. Earlier replay is not evidence that the highway issue is fixed. Independent steering engagement is a separate feature and does not improve speed regulation itself.

The targeted native build and tests passed. The original isolated trial build did not complete and used a prebuilt marker. The subsequent master migration completed a clean native build on AGNOS19.9 and uses no prebuilt marker; full-power runtime and road evaluation remain separate.

## Operational changes and research

Calibration/smoothing remain candidates; mass normalization was adopted in the installed master integration:

- **Ford automatic speed-factor calibration, smoothing, and calibration gauges:** BluePilot [PR #172](https://github.com/BluePilotDev/bluepilot/pull/172) is a draft stack; its gauges sit on the actual calibrator in PR #161 and smoothing in PR #171. Its evidence gate starts at 9.5 m/s (about 21.25 mph), excluding the latest sub-20 mph intervention windows. Compatibility with this fork's gain blend and feedback model must be evaluated before porting. [Exploration report](navigator-autocal-exploration-2026-10-14.md)
- **Upstream mass normalization:** openpilot [commit 2713630e](https://github.com/commaai/openpilot/commit/2713630e7950a61dc072467b5394a1043e34547f) plus its paired opendbc change removes redundant mass dependence. This is maintenance with an algebraically equivalent model, rather than a demonstrated handling improvement. The custom pinion guard and paired safety equivalence need attention during adoption. [Exploration report](navigator-mass-removal-exploration-2026-10-14.md)

- Updates are temporarily paused with `DisableUpdates=true` after dirty opendbc source prevented update checkout. This is operational configuration, not a steering feature or a permanent updater repair.
- A complete pre-install backup exists on the device at `/data/navigator-backups/20261014-pinion-low-speed-preinstall/`; the previous installation remains at `/data/navigator-previous-20261014/`. A second backup is in Mac temporary storage and should not be treated as permanent archival storage.
- Active Park Assist 2.0 remains a hardware investigation. `RJ6T-14H102-BAH` alone does not establish APA-capable hardware; the OEM assembly mapping is unresolved. No parking-assist feature has been implemented, and no active ECU queries were performed.

## Branch provenance

The requested master port is now committed locally on paired **`codex/navigator-master-integration`** branches: openpilot `6ae31161b` over fresh master `6eb63e045`, opendbc `c09baff5` over `b3bd79a6`. It preserves 1.20/0.97 and current trial behavior, adapts normalized geometry and the upstream blind-spot flag collision, and retains current OS/model requirements. Full child tests, focused parent checks, H7/native builds and recorded replay pass; full minimal/development Mac builds and the complete parent suite now pass (957 tests; 343 subtests); the full AGNOS-native build and normal offroad startup now pass, and powered stationary Chestnut big-model inference now pass; road behavior remains outstanding. **This branch is published, clean-clone verified and installed.** See the [port report and blockers](navigator-master-integration-2026-10-14/REPORT.md).

Before the migration, read-only SSH on October 14 confirmed installed AGNOS **19.7**, parent Git base `f35e6e5eb`, child base `eb70bef4`, both trial settings enabled, updates paused and a prebuilt marker present. Controller, angle helper, pinion guard and Ford safety source hashes match the saved deployment manifest. Current upstream master snapshot `690fa743b945973d594f2dfa143eee4fabc98a70` requires AGNOS **19.9** and pins mass-normalized opendbc `b3bd79a659dae961af169a3baac723961f720133`. The migration is tracked as **NAV-10** in the roadmap; see the [current upstream comparison](navigator-upstream-master-comparison-2026-10-14.md). That audit performed no update; the subsequent authorized migration is recorded above.

The previous device branch was `navigator-angle-v1`. The trial is committed locally in the isolated checkout at `${PRIVATE_CACHE}`, branch `codex/navigator-low-speed-prototype`, parent head `c1bf21f3d`; its `opendbc_repo` child head is `6c17a0af` on the same branch name.

The previous installation was a source overlay whose Git HEAD did not fully identify behavior. It is now preserved at `/data/navigator-before-master-20261015`; the installed master branch is a clean published checkout with paired child, native build and boot evidence.

## Detailed reports

- [Steering source preservation](navigator-steering-preservation-2026-10-14/REVIEW.md)
- [Startup and update diagnosis](comma-startup-update-diagnosis-2026-10-14.md)
- [Yaw investigation](navigator-yaw-root-cause-2026-10-14/REPORT.md)
- [Pinion implementation and safety replay](navigator-pinion-implementation-2026-10-14/REPORT.md)
- [Low-speed prototype and replay](navigator-low-speed-prototype-2026-10-14/REPORT.md)
- [Deployment, backups, and Comma 4 UI correction](navigator-deployment-2026-10-14/REPORT.md)
- [First road trial analysis](navigator-post-trial-analysis-2026-10-14/REPORT.md)
- [Parking hardware investigation](navigator-active-park-assist-2026-10-14.md)
- [OEM IPMA comparison](navigator-ipma-oem-comparison-2026-10-14.md)
- [Historical Chestnut compatibility research](chestnut-egpu-big-model-compatibility.md) — August snapshots; do not treat its upstream release status as current.

## Local very-low-speed experiment — October 14, 2026

[Prototype report](navigator-very-low-speed-prototype-2026-10-14/REPORT.md): an additional default-OFF 10% path-angle conversion multiplier through 15 mph, smooth fade to identity by 25 mph, on top of the installed trial. Preserves 1.20/0.97. Native generated-command replay passes all 62 segments from four complete cached drives, with recorded ≥45 mph message parity. This standalone local module is **not selected in the branch or installed on the Comma**, and actual response improvement is unproven. Broad-suite MISRA bootstrap limitations are recorded in the report.

## Installed very-low-speed correction — October 14, 2026

The [installation record](navigator-very-low-speed-installation-2026-10-14/REPORT.md) supersedes the earlier local-only status for this candidate. Parent `76d78d46f` and child `f50241ca` are installed on paired branch `codex/navigator-very-low-speed-trial`. Existing low-speed trial toggle selects the extra 10% through 15 mph, smoothly absent by 25 mph. 1.20/0.97 preserved; recorded ≥45 mph commands unchanged. Backup, native build and offroad acceptance verified; handling benefit is not yet road-tested.

## Post-correction road evidence and Auto Start/Stop goal — October 14

[Latest drive report](navigator-post-vlow-drive-2026-10-14/REPORT.md): the installed new revision is present, but significant ~15 mph undertracking remains; overall benefit is not established. Six rapid factory Auto Start/Stop selected/deselected status changes are captured. Future optional Comma control of that factory feature is a research goal; no request path, Panda permission or UI actuation feature has been implemented.

## Bounded tracking prototype and feature survey — October 14

[Local prototype report](navigator-bounded-tracking-prototype-2026-10-14/REPORT.md): bounded filtered proportional tracking term, no integrator, existing limits and 1.20/0.97 preserved. **21 prototype tests**, **213 Ford/native tests / 12,063 subtests**, full five-drive **72-segment** regenerated-controller/native replay: **242,250 TX accepted, zero rejected**, default-OFF parity and recorded ≥25/45 mph parity. Independent review identified rate-history carryover on synthetic cutoff transitions; tests/documentation preserve the inherited limit rather than force instantaneous equality. Not a physical-response improvement claim or an integrated/deployable feature.

[Current fork ideas review](navigator-fork-ideas-2026-10-14.md) covers all six supplied links. NAV-15–17 track read-only steering/runtime diagnostics, separate calibration resets, and compatible model packages/resilient downloads. Low-speed stall rescue remains separate research under NAV-01; model switching, pulse rescue and alert suppression were not added to this prototype.

## Stall-rescue comparison and EPS availability — October 14

[Saved-drive comparison](navigator-stall-rescue-comparison-2026-10-14/REPORT.md): BluePilot #153 plus prerequisite #148 is not yet a demonstrated fix. Installed fixed pinion measurement gives no reactive triggers in the two analyzed drives; PR-style learned-measurement sensitivity gives two near the first latest slow turn, none near the later one. Separate raw EPS availability field is suppressed in all15,116 valid5–20mph status frames and generally available above25mph. This field was absent from the earlier state/limit/capability summary; it is not a direct motor-authority measurement. NAV-01/NAV-15 now prioritize distinguishing speed-linked availability, transient response and true attenuation. No rescue feature, feedback-model change or Comma update was implemented.

## Availability and local correction constraints — October 14

[Authority investigation](navigator-eps-authority-investigation-2026-10-14/REPORT.md): availability is a diagnostic flag, not a command gate in the installed controller/safety; the saved data cannot establish a firmware authority limit. Commands reach the wire in the selected weak turns, which show distinct persistent and delayed response. The recorded 0.262-second delay is fully calibrated for the estimator's admitted data, whose floor is 50 mph, not this low-speed band. Assumed-plant screening shows the current bounded P trial is not a complete universal fix. NAV-01 now separates persistent-error admission from transient timing; current settings/source and Comma are unchanged.


### 2026-10-14 — Persistent-error prototype and saved button evidence

NAV-01: [persistent-error prototype](navigator-persistent-error-prototype-2026-10-14/REPORT.md) remains local only. Preserves1.20/0.97, fades to zero by25mph;24 behavioral tests and full72-segment/five-drive native safety replay pass with242,250 configured TX accepted, zero rejected, defaultOFF and recorded ≥25/45mph byte parity. Persistent selected window35/40 commands changed, later catch-up window0/40. Hypothetical plants still overshoot up to19%; stale/lane-change context and threshold justification remain blockers before deployment. No road improvement claimed.

NAV-14: [Auto Start/Stop evidence package](navigator-autostop-button-evidence-2026-10-14/README.md) saves70,808 relevant bus0 frames, exact transition payloads, native status/request decode checks, anonymous segment hashes and a verified portable ZIP. Six status transitions near the user-reported button experiment; no asserted request pulse in5,901 main request frames or2 alternate request frames. Sender/actuation remains unresolved. No Comma access or changes.


### 2026-10-14 — Tracking overshoot and context guards addressed locally

NAV-01: [release-aware candidate and paired patches](navigator-tracking-release-2026-10-14/REPORT.md) preserve1.20/0.97, existing feedforward and25mph fade. Added observed-response admission (no blind boost), catch-up projection veto, half gain/cap, fresh state/control/model context and lane-change/blinker guards. Long-hold alternative suppressed the selected event; retained prior persistence with new guards.23 behavioral and24 staged tests pass; native Ford213 passed/79 skipped/12,063 subtests. Final72-segment replay242,250 configured TX accepted, zero rejected; defaultOFF and recorded≥25/45mph parity. Persistent event14/40 commands changed, catch-up event0/40. Original96 and expanded210 hypothetical plants no added unit-gain overshoot; assumed50% response improves only to~55%. No road fix claimed. Paired patches/defaultOFF FordPrefPersistentTracking prepared locally; device backup/build/startup/parked validation is next before road comparison. No Comma access or changes.


### 2026-10-15 — Tracking candidate installed; powered parked check pending

NAV-01: [installation receipt](navigator-tracking-installation-2026-10-14/REPORT.md). Private device+Mac backup verified12files/1,037,386,553bytes before source change. Paired `codex/navigator-tracking-release` parent74f66e7a0bf1dc0718431532948ece2c4fb0041c / child1b965caadd4a6aea4d09985532bf7cca6c0873ca installed.24 integrated tests and actual-source full72-segment replay match prototype hashes. Native device build and trialOFF parked checks passed, then FordPrefPersistentTracking enabled and app restarted. Final offroad topics healthy/noOutput, clean source, captured preferences/calibration and1.20/0.97 preserved; no OS/firmware update. Ignition-on parked check requested and pending; no road benefit claimed. No remote publication.


### 2026-10-15 — Powered parked acceptance passed

NAV-01: [tracking installation powered checks](navigator-tracking-installation-2026-10-14/REPORT.md) passed55seconds after user ignition-on confirmation. Vehicle remained Park/0m/s, controls disallowed; all12 topics valid/alive. Live Navigator geometry, flags15, Ford safety10, new trial enabled, Alpha/Experimental off.1,101 big-model samples~20fps/39.44ms, zero reported drops;550 Panda samples zero RX-invalid/TX-blocked/faults. Calibration calibrated, exact clean paired source;1.20/0.97 preserved. No injected queries, engagement or steering tests. Road response remains untested for this revision.


### 2026-10-15 — First tracking-correction drive: benefit unproven

NAV-01: [17-segment latest-drive assessment](navigator-post-tracking-drive-2026-10-15/REPORT.md). Recorded new preference/source confirmed. Broad13–17mph body/wheel response36.9/45.9%→41.3/52.7%, but steady cohorts~44.4/52.6%→45.4/53.4%;42 matched-road clean pairs effectively flat with zero also-steady pairs. Detectable extra command only29/1,730 active13–17mph samples (~1.45s); rising demand delays first burst to~0.3s before intervention. Under-response remains; no causal improvement established. Next local question: ramping-demand admission with existing catch-up/freshness/driver bounds preserved. Seven Ford-mode hardware TX-blocked increments outside bursts; recorded native replay reproduces6, one remains unattributed. No Comma writes or tuning.


### 2026-10-15 — Local rising-demand admission prototype

NAV-01: [prototype/replay report](navigator-rising-demand-prototype-2026-10-15/REPORT.md). Bounded rising-demand admission and fractional recovery veto; observed-response/freshness/lane-change/driver guards kept. Half term during rising>5%window;1.20/0.97 and speed fade unchanged. Saved weak turn extra command starts~0.947s earlier, not a road-response result.36 behavioral tests;213 Ford tests/79 skips/12,063 subtests. Full6-drive/89-segment native replay:299,496 configured TX accepted, one identical baseline/candidate rejection near28mph, zero new rejections; defaultOFF and recorded≥25/45mph parity.300 changing-demand toy cases retain a worst1.327-point aborted-turn residual increase vs installed correction; not deployment-ready evidence. Common548s rejection and turn-exit residual remain local investigation items. No Comma access or changes.


### 2026-10-15 — Stale-marker rejection and turn-exit budget investigated locally

NAV-01: [local rejection/residual report](navigator-rejection-residual-prototype-2026-10-15/REPORT.md). The28.44mph native rejection is a stale advertised shadow-curvature marker (old C value80 outside allowed86–301; actual current intent98 passes). Offline controller adapter refreshes truthful intent before active angle TX, without changing Panda limits or actuation packets. Rising-demand extra-command integral capped at.001rad*s; spent budget survives temporary invalid-data pauses. Independent review caught and regression-tested the reset bypass.51 focused tests;213 native Ford tests/79 skips/12,063 subtests. Corrected full89-segment/six-drive replay:322,306 configured TX accepted,zero rejected vs one baseline rejection;20,227,501 physical RX frames,89 input hashes verified.1.20/0.97 and recorded≥25/45mph actuation parity retained; metadata traffic intentionally changes (+22,809 frames), so full CAN-stream parity is not claimed. Saved-turn extra onset still0.947s earlier;300 hypothetical cases reduce worst added turn-exit excess1.327→0.00761 percentage points of peak demand, not road improvement. Budget is pre-limiter/per-demand episode; hardware marker timing and actual vehicle response remain unvalidated. Report-local only, no paired branch integration, device access or changes.


### 2026-10-15 — Metadata-only local integration and fresh device backup

NAV-01: [integration/baseline receipt](navigator-metadata-branch-review-2026-10-15/REPORT.md). Current-intent metadata fix is an uncommitted local opendbc edit on existing paired checkout; parent has review note only, child pin not advanced. Experimental rising-demand/turn-exit correction remains offline and is not runtime-integrated or installed.21 actual-controller tests,213 native Ford tests/12,063 subtests pass. Actual metadata-only full89-segment replay:322,306 configured TX accepted,zero rejected vs one baseline rejection; nonmetadata actuation identical at every speed/update. Read-only SSH source/settings backup936,435,888 bytes, hashes verified, selected settings unchanged.151 passive Panda samples: offroad/noOutput/ignition false/controls disallowed, RX valid, historical TX-blocked6 without increase;1.20/0.97 confirmed. Powered parked acceptance not verified (vehicle off). No installation, restart, param writes, OS/firmware changes or ECU queries.


### 2026-10-15 — Budgeted tracking paired integration complete locally

NAV-01: [paired integration and evidence](navigator-paired-budget-integration-2026-10-15/REPORT.md). Parent0cc74c94f pins childd64ffcfa on `codex/navigator-tracking-release`; both clean, local-only commits. Existing opt-in selects bounded rising-demand correction; defaultOFF unchanged. Budget reduced.001→.00025rad*s after final-range/slew residual testing. Rearm requires1s continuous fresh settled quiet demand/measurement; isolated floor crossing/reversal/invalid data cannot replenish it.312 cases across both signs include explicit forced-abort execution and final slew tails: observed max final area.0019235→.0009798rad*s (~49.1% lower), all endpoints settled; not a universal or physical bound. Saved-send reconstruction retains0.947s earlier onset; generated replay has limited rising-budget/rearm exposure, documented separately. Actual final-source89-segment replay322,306 configured TX accepted,zero rejected vs one baseline reject; defaultOFF and recorded≥25/45mph actuation parity preserved.57 focused tests;268 Ford tests/79 skips/12,063 subtests; full parent970 passed/86 skipped/1xfail/343 subtests.1.20/0.97, geometry and native safety source unchanged. Mac development build checked; hardware timing, device build/boot, parked acceptance and road response remain unvalidated. No publication or Comma access/changes.


### 2026-10-18 — Local high-speed body-confirmed reduction candidate

[Guard-resolution package](navigator-highspeed-release-2026-10-17/REPORT.md): adds fresh calibrated-body confirmation to the wheel-excess experiment and a cumulative unwind latch with confirmed rising-demand rearm. 84 focused tests and full 28-session/540-segment native replay pass with zero additional rejects; seven historical recorded rejects remain. Preserves 1.20/0.97 and all replayed below 60 mph/40–50 mph commands. All 14 wheel/body counterexamples receive zero added correction. Admission is narrower in the 83 mph bend: 31/130 strategy frames, 28 encoded packets. These are command changes, not measured tracking improvement.

**Local research candidate only:** no production factory/parameter/UI integration, branch publication, Comma install or fresh device inventory this task. The installed paired source is unchanged. The roadmap tracks integration and physical acceptance separately.

Driver-pressure release also retains native slew while withdrawing extra correction; both turn directions are covered. Final 28-session/540-segment corpus repeat after this stress-test fix passed with zero additional native rejects; earlier accepted evidence is archived separately.


### 2026-10-18 — Body-confirmed high-speed trial integrated locally

[Paired integration and full validation](navigator-paired-highspeed-build-2026-10-18/REPORT.md): parent `ff6ff2630` pins child `9d5a3d48` on `codex/navigator-tracking-release`. Portable controller, receipt-aware motion/calibration adapter and separate default-off `FordPrefHighSpeedTracking` factory option are integrated. Existing pinion/low-speed/persistent/roll prerequisites remain required; no UI control added. Preserves 1.20/0.97, geometry and native safety. Full parent/child suites, Mac minimal/development builds, Panda target and fresh 540-segment native replay pass; all replay results and variant stream hashes match the validated prototype. The integrated test is subprocess-isolated to preserve later replay-test startup semantics.

This supersedes the earlier research-only integration status. It remains **local and unpublished**, with the Comma untouched. Device build/boot, powered parked checks and actual handling improvement are separate acceptance steps; frozen-motion replay does not prove lane departure is fixed.


### 2026-10-18 — High-speed trial installed after paired publication and backup

[Installation report](navigator-highspeed-installation-2026-10-18/REPORT.md): exact clean parent`ff6ff2630`/child`9d5a3d48` published to the explicitly approved existing adgower forks and activated after fresh verified Mac/device backup and full isolated ARM checks. `FordPrefHighSpeedTracking` is enabled; existing preferences and1.20/0.97 retained, no new UI toggle. Ignition-off and powered stationary Park acceptance passed, including fresh real-motion adapter delivery, healthy Ford safety and20fps large-model inference. OS19.9/signedfirmware unchanged. Whole previous installation and rollback refs retained. This supersedes local/unpublished status; road tracking benefit remains unverified and lower-speed work remains open.


### 2026-10-18 — Post-trial evidence and offline synchronized video diagnostics

[97-segment review](navigator-post-highspeed-drives-2026-10-18/REPORT.md) verifies installed high-speed correction execution but does not establish overall tracking improvement. Residual high-speed over-response/unwind-rearm blocking and a separate5.7s13–19mph deficit are retained as fixtures. All62input/disengagement groups are exported, with owner-reported lane-edge/possible-debris correction context for15:19:59CDT. Source/settings/services unchanged.

A local20s synchronized forward/wide [steering-overlay video](../navigator-reference/PRIVATE_ARTIFACTS.md) now shows recorded requested/measured wheel angles, driverpressure/torque, speed and lateral-active flag. Reconstruction-derived extra correction/guard are separately labelled. This is an **offline review artifact**, not a new device UI feature or synthetic lane-path overlay.

### 2026-10-18 — Local post-unwind rising-leg research

[Prototype report](navigator-highspeed-rearm-prototype-2026-10-18/REPORT.md) diagnoses old-peak rearm exclusion and adds fresh causal rising-leg admission in a research copy only.94focused tests and full637-segment native replay pass; no additional native rejects, lower-speed or default-off changes. Acceptance and limits are tracked in the roadmap. This is not an integrated or installed feature. It does not change the final2.8s before the reported15:19:59lane-edge input; that event remains unresolved.1.20/0.97 and paired/device state preserved.

### 2026-10-18 — High-speed target/path diagnosis, research only

[Wheel-unwind/requested-path report](navigator-highspeed-wheel-unwind-2026-10-18/REPORT.md) finds measured wheel excess plus a near-edge predicted path in the owner-described82–84mph event. Exact transmitted commands already unwind with the request; there is no extra software release tail in the final2.8s. This is diagnostic evidence, not a new feature or proven physical root cause. Next local study is calibrated high-speed target/unwind tracking with path bias treated separately.1.20/0.97, paired source and device state unchanged.

### 2026-10-18 — Calibrated wheel-target/unwind feedback prototype, local only

[Prototype](navigator-highspeed-wheel-target-prototype-2026-10-18/REPORT.md) admits bounded trim during current wheel/body-confirmed excess under falling demand, with predictive closing release.110tests, exact recorded-timing checks and full637-segment native replay pass, with0additional rejects,0recorded changes at/below70mph, and default-off byte parity. Receipts and limits are tracked in the roadmap. Independent installed-policy state prevents lower-speed warmup contamination. Lane-edge fixture gets20additional trim frames and0added-under-target frames; physical improvement is unproved. This is not integrated or installed;1.20/0.97 and paired/device state stay unchanged.

### 2026-10-18 — Paired wheel-target integration committed locally

[Build/integration report](navigator-paired-wheel-target-build-2026-10-18/REPORT.md): parent`50baa6fd6`pins child`0e65f2962`on existing paired branches. Child owns AST-equivalent wheel-target/unwind policy and37tests; parent uses the existing opt-in factory. Full parent/child suites, minimal/development Mac and Panda targets pass. Fresh committed637-segment factory replay passes: all128variant stream hashes equal accepted prototype,0additional native rejects,0recorded changes at/below70mph and default-off byte parity. Final receipts are linked in the roadmap. This is locally committed, not pushed or installed; owner1.20/0.97/fixed geometry/safety and device state are preserved.

### 2026-10-18 — Wheel-target trial activated; parked acceptance complete

[Installation report](navigator-wheel-target-installation-2026-10-18/REPORT.md): published and activated parent`50baa6fd6`/child`0e65f2962`. Full ARM build,477tests/12,063subtests,600transition cases/216,000frames,8factory combinations and IPC checks pass. Ignition-off acceptance passed; all selected settings and learned calibration hashes match fresh device/private Mac backup.1.20/0.97,geometry,pinion,safety and OS/firmware preserved. Powered stationary acceptance passed: healthy topics, approximately20fps big model, no reported frame drops or new blocked transmissions. Learned calibration semantics retained with normal startup stiffness reset documented; physical improvement unproved.

### 2026-10-19 — Post-wheel-target evidence review

[All103new segments](navigator-post-wheel-target-drives-2026-10-19/REPORT.md):43,934active/no-driver reconstructed packets match, zero added command differences versus installed prior policy. No clean meaningful70mph+bend coverage, so new physical benefit remains unproved.50input/disengagement groups reviewed.15mph/28–31mph wheel-confirmed deficits and64mph unwind excess remain diagnostic work; separate inactive-session Chestnut supply warnings retained. No new feature/tune or device change;1.20/0.97preserved.

### 2026-10-19 — Diagnostic findings, no new feature

[Local15/64mph investigation](navigator-low64-diagnosis-2026-10-19/REPORT.md): positive15mph tracking terms are suppressed after a three-frame transient-budget spend; existing resolution-aware rearm changes zero commands on this new recording.64mph retains the old unwind latch because calibrated wheel-target feedback starts70mph+; command unwinds normally with zero extra release tail. Next designs are separately bounded sustained-error correction and a guarded60–70mph calibrated feedback study. No code integration/device change or physical fix claimed.

### 2026-10-19 — Research-only sustained-error /60–70mph unwind prototype

[Prototype report](navigator-sustained-unwind-prototype-2026-10-19/REPORT.md): bounded one-second low-speed allowance independent of transient budget; calibrated wheel-target reduction blends60–70mph.95tests/480transition cases and full740-segment native replay pass with0additional rejects/default-off/protected25–60parity. Saved15mph/64mph episodes receive bounded additional commands, not proved physical improvement. One75.11mph generated boundary quantum remains explicit for integration review. Not integrated/installed;1.20/0.97and paired/device state unchanged.


### 2026-10-19 — Research-only75mph history-boundary fix

[Boundary report](navigator-upper-boundary-prototype-2026-10-19/REPORT.md): independent installed-controller history with70–75mph fade resolves the prior75.111mph wire quantum.122tests,480transition cases/172,800frames and fresh740-segment replay pass;4,289,417updates/variant, zero>=75mph differences, zero added native rejects (2shared baseline rejects), default-off/protected25–60mph parity.13original-timing native scenes pass; saved15/64mph prototype commands unchanged. Report-local only; no paired integration/install or physical-improvement claim.1.20/0.97and device untouched.


### 2026-10-19 — Sustained tracking / unwind policy integrated locally

[Paired integration](navigator-paired-sustained-build-2026-10-19/REPORT.md): parent`0171b8972`pins child`4167433e5`; both local clean commits. Adds bounded sustained low-speed allowance,60–70mph feedback extension and70–75mph independent-history return through existing default-off prerequisites.134focused tests, full parent/child suites,480transition cases and30,240factory equivalence updates pass; minimal/development/Panda Mac builds pass at committed pair.1.20/0.97, geometry, pinion, safety and settings preserved. No push or device change; local build proof is separate from hardware/road acceptance.


### 2026-10-19 — Sustained/unwind pair activated; powered check pending

[Installation](navigator-sustained-installation-2026-10-19/REPORT.md): both paired branches published and exact parent0171b8972/child4167433e5activated after fresh verified Mac/device backup, isolated ARM build,599native tests/12063subtests and800combined transition cases. Ignition-off acceptance passes; all selected settings and five learned hashes preserved,1.20/0.97unchanged. Powered stationary check awaits user ignition-on/Park confirmation. No OS/firmware update or physical tracking improvement claim.


### 2026-10-19 — Sustained/unwind powered acceptance complete

[Installed pair](navigator-sustained-installation-2026-10-19/REPORT.md) passed ignition-on/Park/disengaged checks: healthy topics,20fps big model, zero reported drops or sampled new faults.1.20/0.97 and core learned calibration retained. No new toggle required. Hardware startup evidence is complete; physical steering improvement awaits ordinary supervised drive analysis.

### 2026-10-26 — Bounded precharge allocator integrated locally

[Integration report](navigator-precharge-integration-2026-10-26/REPORT.md): local parent `5b301a944` pins child `884c9f491`. Versioned consumed-target transport, bounded weak-brake precharge entry, measured-clearance rearm and signed-integral metadata integrated; early coasting stays disabled. Full parent1,065/child4,603 tests and minimal/development/Panda builds pass. Fresh137-segment native replay (32.17M RX/951,332 TX per variant): zero added rejects, two unchanged reconstructed baseline release faults.1.20/0.97 and lateral/safety sources preserved. Both branches clean; not pushed or installed. Physical pulsing improvement remains unproved.

### 2026-10-26 — Bounded precharge activated; powered check pending

[Deployment report](navigator-precharge-staging-2026-10-26/REPORT.md): parent5b301a944/child884c9f491 activated after fresh verified Mac backup, full isolated ARM build,1,131native tests/12,083subtests,75retained cases and startup/IPC/pose checks. Ignition-off201samples pass; AlphaON,1.20/0.97, selected preferences, learned hashes, firmware and launchers preserved. Previous whole installation retained. Final powered Park check requested. Uses existing coordination preference; early coasting disabled. Physical highway-pulsing improvement unproved. No publication or OS/firmware update.

### 2026-10-26 — Bounded precharge powered acceptance complete

[Installed pair and evidence](navigator-precharge-staging-2026-10-26/REPORT.md):55-second powered stationary Park check passes; bothpeers protocol1,1,100fresh targets,20Hzmodel/0%drops,550cleanPanda samples with0invalid RX/blockedTX and no coordination faults. AlphaON,1.20/0.97and all steering preferences preserved. No manual settings changes, OS/firmware update or publication. Moving response and pulsing comfort remain unverified.

### 2026-10-26 — First bounded-precharge road evidence

[Road review](navigator-precharge-road-review-2026-10-26/REPORT.md):37new segments/4exact-new-pair drives,2Alpha-active; no controls mismatch or coordination fault.31actual precharge-only entries/~5.9s confirm activation. Remaining62–64mph downhill-like window has20brake-bit transitions/15s with cruise70, stable10th gear and ECU torque cycling; no new-stage entries there. Rolling restart peaks3,946RPM at20.9mph in reported1st, with reported2nd completing2.24s after target2. SavedOEM examples and prediction/target/resume command differences provide a protocol study lead; causal shift effect unproved. Next: coupled downhill mode/integral/actuator-timing regression, plus separate OEM/Alpha restart protocol comparison. No device/source/settings changes; coverage through65.7mph only.

### 2026-10-26 — Exact downhill replay and low-speed ramp gap

[Continued local investigation](navigator-downhill-restart-investigation-2026-10-26/REPORT.md): installed baseline reproduces all70,291new feedback callbacks and131,258producer updates within tolerance. Downhill precharge budget is spent; nominal release/ramp cycles cause remaining switching.21OEM/Alpha shift events show ordinary newAlpha target2near9mph using same protocol fields; exceptional target selection is20.69mph, not an extraordinary shift-completion delay. Found below 6.7 mph engineRamp antiwindup gap; isolated local guard reducesIpeak0.772→0.199 andgaspeak1.823→1.398.41tests pass;162-segment coupled replay adds no faults/pressure-clearance violations, but27encoded braking samples are one0.0039quantum less negative after later I/handoff crossover. Prototype NOT integrated/installed; next local task is history-consistent recovery, plus separate downhill mode design.1.20/0.97and paired/device state unchanged.

### 2026-10-26 — Narrow low-speed guard selected locally; history holds rejected

[Decision and native evidence](navigator-ramp-history-resolution-2026-10-26/REPORT.md):20/40ms repeated settling adds an older-route timeout; one-shot settling increases braking-history differences. All settling variants rejected. Original narrow guard passes41tests and162-segment native replay (37.8MRX/1,115,518TX per variant), zero added native rejection. Owner accepted the documented27one-quantum0.0039m/s² brake-request variations for this exact local candidate; not installation authorization or blanket future waiver. Candidate/source hashes retained. Paired branches/device unchanged;1.20/0.97 preserved. Next stage: paired integration/build validation if requested; downhill mode/response remains independent.

## 2026-10-26 — selected low-speed ramp guard

Ported the owner-selected narrow anti-windup guard locally. Exact 162-segment prototype parity retained, including the documented 27 one-increment brake-request differences. No device changes; physical RPM improvement unproven and highway pulsing still open. See [integration evidence](navigator-low-speed-ramp-integration-2026-10-26/REPORT.md).

## 2026-10-26 — highway pulsing boundary diagnosis

The selected low-speed guard is locally integrated. Separate highway analysis finds recurrent grade/integral mode-boundary switching, including 20 transitions with positive planner target and fresh lead context in the downhill regression. No new controller patch. Coast authority and integral recovery need a coordinated design with following-context checks. [Evidence and next constraints](navigator-highway-cycle-boundaries-2026-10-26/REPORT.md).

### Coordinated coast + integral recovery — design drafted

Owner selected this direction over planner-only filtering. [Design](../superpowers/specs/2026-10-26-coordinated-coast-integral-design.md) passed an independent builder check. First gate: demonstrate supported coast authority from saved OEM/Alpha data before policy changes; then compare consumer-only, integral-only and coordinated variants. Draft approval pending. No runtime or device changes.

### 2026-10-26 — coast/integral design approved

Owner approved the coordinated design for local research. [StageA execution plan](../superpowers/plans/2026-10-26-coast-authority-feasibility.md) is prepared for review: immutable model/case audit, mode/speed/gear/grade uncertainty and conservative paired-command screening before any runtime prototype. No device changes.

### 2026-10-26 — coordinated coast/integral Stage A complete

- **Not identifiable with the unchanged archived model.** Audited 17,943 cases / 53,829 case-horizon evaluations; preserved original whole-route roles and immutable source/model hashes.
- Reconstructed all 54 original paired coast/brake queries: 43 point-forecast improvements, **zero conservative interval advantages**. All 54 old query caches additionally lack fresh independently received radar context.
- Training coverage at 60–70 mph has only 2 stable 200 ms valid-negative engine-request cases and 1 near-zero case (plus 8 inactive-propulsion cases), from one route/gear identifier. Global model support is not conditional gear/grade authority proof.
- 52 contract tests pass; independent result review found no actionable issue. No new mode-selector/back-calculation prototype, paired runtime edit, device connection or activation. The approved feasibility gate stops Stage B. The committed local low-speed guard and 1.20/0.97 remain unchanged.
- Next useful local work: re-extract received torque, RPM/gear, pose/grade and radar from already saved newer routes; inventory naturally occurring coast exposure before asking for more drives or training a separately versioned model. Preserve independent route evaluation and the immutable current archive.

[Evidence](navigator-coast-authority-feasibility-2026-10-26/REPORT.md).

### 2026-10-26 — coast signal recovery and existing OEM highway evidence

- Recovered and hash-verified 37 newer saved segments across four sessions. Two active Alpha sessions have 40,977 command observations (~819.56 s), all with fresh radar. Exact torque reconciliation covers 284,854 observations.
- The named 62–64 mph episode has 20 brake transitions while actual/target gear stays 10 with fully engaged clutch. Newer Alpha data has 49 provisional coast episodes, only six at 60–70 mph, all shorter than 600 ms.
- Continued into the older saved OEM evidence: re-extracted 19 more segments from `oem-04` and `oem-05`, preserving original calibration/test labels and separating incoming stock commands from outgoing Alpha commands. Another 454,730 decoded stream observations reconcile exactly; all 25,114 active stock-command observations have fresh radar.
- Found **34 OEM highway coast episodes, 10 lasting at least 600 ms, including eight in the negative-gravity-proxy band**. This gives the next offline model experiment relevant saved evidence. No new drive needed for that step.
- RPM quality remains unresolved (flag 0 in both older and newer data); all coast candidates remain provisional. No archived model, training/evaluation role, paired runtime or Comma change. Steering 1.20/0.97 preserved.
- 25 contract tests pass; independent initial and supplemental result reviews found no actionable issue. Next: a separately versioned research model with consistent grade frames, explicit RPM uncertainty and honest route separation; no controller prototype until conservative support and coupled replay gates pass.

[Signal recovery report](navigator-newer-coast-signals-2026-10-26/REPORT.md).

### 2026-10-26 — latest city drives and MAX-speed behavior

- Acquired 14 new completed segments across two sessions, with clean installed pair `5b301a944` / `884c9f491` and AGNOS 20.1. All 154 completed device rlogs at acquisition have hash-matching local copies. No device writes.
- New trips are city driving: max active 29.51 / 30.05 mph, max set 30 / 37 mph. No 85 mph run in these recordings. No recorded controls mismatch or coordination fault.
- Installed planner always considers model acceleration alongside cruise and lead MPC; MAX is a ceiling. Model selected 94.9% / 73.0% of qualified planner samples. No separate posted-limit controller/toggle; the old ExperimentalMode parameter does not gate the model candidate in this code.
- At <private clock time>–<private clock time> Central: MAX 35 mph, median 25.28 mph, lead present, model target median +0.019 m/s² and 17 brake-bit changes. New moving city regression for combined planner/actuator smoothing; not proof of a 25 mph sign cap.
- Owner explicitly chose to leave the Comma unchanged. Below-6.7 mph guard remains local; coast model is not validated runtime code. Existing OEM ACC path is Alpha OFF. A new stock-like Alpha option would require explicit model-stopping tradeoffs and validation.

[Latest drive report](navigator-latest-smoothness-road-review-2026-10-26/REPORT.md).

### 2026-10-26 — city handoff prototype rejected; highway regression retained

- Traced the city 25 mph / 17-change episode. All 17 transitions occur after precharge budget exhaustion. Tested a narrow negative-target release/ramp antiwindup extension, preserving actual braking and signed recovery.
- Standalone city 17 → 17 with braking exposure 21.538 → 22.671 s: no demonstrated smoothing. Named 63 mph highway 20 → 20. Full 176 segments / 512,066 callbacks increase 1,193 → 1,196 changes and produce 441 less-negative strong-target brake acceleration fields (max 0.0312 m/s²). Not covered by the earlier low-speed guard's limited variation acceptance.
- Rejected: no paired integration, native firmware replay, ARM build or device deployment. 48 research tests pass; independent review's route-coverage issue fixed with fail-closed manifest checks. No remaining review finding.
- New city frozen replay also gives the earlier **uninstalled** low-speed guard 7 changes but much more braking than the installed 17-change baseline. Keep the commit unchanged, but reassess before staging; this is not a proven physical outcome or a smoothing benefit.
- Highway work remains active: recovered OEM 34 coast episodes / 10 sustained cases are inputs for a separately versioned response-aware allocation experiment. This integral-only candidate does not fix highway pulsing. Steering 1.20/0.97 and Comma unchanged.

[City/highway prototype evidence](navigator-city-handoff-prototype-2026-10-26/REPORT.md).

### 2026-10-26 — response-aware allocator remains research; high-RPM protocol evidence

- Downloaded 2 new drives/21 completed segments read-only, verified hashes and unchanged source/settings. No recorded controls mismatch or coordination fault; max active66.35 mph, no new 75–85 mph proof.
- Highway regression confirmed:23 brake changes in20 s at 57.8–60.7 mph, tenth gear, received brake torque 0–232 Nm. Preserve this separately from the original 63 mph regression.
- Response prototype versions retain2,036 cases from147 saved OEM/Alpha segments in v3, with separate mode evidence and whole-route exclusion; latest drives excluded from fitting.364 entry opportunities / 200 context passes, zero qualifying coast/engine alternatives. Model uncertainty remains too wide; no city/highway smoothing fix is proved.
- V1 full actual-controller shadow replay:197 segments / 12 routes / 570,269 callbacks, zero changed longitudinal packets;1,370 → 1,370 brake changes.34 focused tests pass. V3 is additional causal diagnostic scoring, not a counterfactual physical/controller validation claim. No native/ARM work for the unqualified candidate.
- Matched owner's high-RPM episode:decoded 4,136 RPM at 16.6–22.7 mph, Alpha active/no driver gas, first-to-second target/actual shift delay. RPM quality unresolved. OEM predicted acceleration and target-speed fields vary; Alpha holds −5 and 145 km/h. Investigate timing/torque semantics passively before changing CAN fields; no causal transmission claim.
- No integration, device changes or steering/geometry changes; 1.20/0.97 preserved. Earlier uninstalled below 6.7 mph guard still needs city-exposure reassessment. Remaining saved maneuver routes can be incorporated into response extraction locally; no new drive required merely for that.

[Response-aware allocator and new-drive report](navigator-response-aware-allocator-2026-10-26/REPORT.md).

### 2026-10-26 — OEM prediction/target-speed protocol investigation

- Compared 168 saved segments / 16 routes; 40,548 qualifying OEM and 250,474 Alpha command samples. Prediction −5 and target-speed 145 km/h are constant across active Alpha, including normal and problematic driving. Saved data cannot isolate their physical effects from owner/controller differences.
- OEM prediction mostly mirrors same-time signed request; OEM target speed resembles a varying near-term speed trajectory, not the selected maximum. Do not simply copy set speed or forward OEM prediction. 6,193 OEM prediction samples exceed the current native gas-channel range; 64-case synthetic native unit probe confirms limits, not ECU response.
- Two high-RPM rolling starts report second-gear target at 20.69/21.23 mph versus median 9.21 mph in 30 completed Alpha first-to-second cases. Reported completion delays are within the normal selected range. RPM quality remains unresolved.
- Recorded PID identifies a stronger local lead: integral ~0.77/0.83 at 6.7 mph raises raw request to ~2.0; same-drive normal start has integral ~0.17 / raw ~1.29 with similar planner demand. Installed positive-demand ramp anti-windup starts at 3 m/s. Revisit bounded low-speed integral/release recovery with both high-RPM starts plus the city 17-change regression; existing uninstalled guard is not cleared by this analysis.
- Five contract tests and native range probe pass; no new controller replay, source integration, CAN transmission or device access. 1.20/0.97 and exact paired pins unchanged. Highway pulsing remains unresolved; no causal field fix is established.

[OEM protocol and rolling-restart evidence](navigator-oem-long-protocol-investigation-2026-10-26/REPORT.md).

### 2026-10-26 — rolling-restart integral recovery prototype rejected after full replay

- Implemented narrow moving-restart qualification in offline seam, replacing the uninstalled broad guard only for research. Bounded second trial omits at most 0.25 m/s² of positive integral growth per approach (observed max 0.24913), with 3 s deadline; signed recovery, physical clearance and native limits unchanged. This does not bound later trajectory divergence.
- Raw request peaks in the two high-RPM windows fall about 2.0 → 1.71 / 1.77 m/s². Entire named city route remains byte-identical: 17 brake changes and 21.533 s command exposure; normal stopped-launch fixture unchanged. No physical RPM/shift/comfort improvement proven.
- Full controller corpus: 197 segments / 570,269 callbacks processed. 185 segments have no active atomic-input gaps; one retained 12-segment route has five active prefix gaps and stays diagnostic-only. Encoded gate now checks every strong-target row independently of raw request ordering.
- REJECTED: 19 one-increment weaker strong-target brake fields and a simulated 61.23 mph release-timeout in input-complete alpha-comfort route; 8,969 later callbacks lose activity. Last rolling hold precedes fault by about 317 s. Lower request peaks do not clear later brake/feedback-history failures. Do not relax release safeguards to force a pass.
- Fresh native replay of all 197 segments: 570,178 replacement ACC send slots; 134 retained TX rejections each, zero added TX rejections or relay faults; no forced permission. This does not clear software gates or prove hardware response. 46 focused tests pass; independent review supports rejection.
- No paired integration, push, Comma access/install or steering change. Preserve 1.20/0.97; earlier broad local guard remains uninstalled and unchanged. Next local design must address post-ramp recovery/history with truthful changed-response evidence, retaining these regressions.

[Rolling-restart prototype and full-replay evidence](navigator-rolling-restart-recovery-2026-10-26/REPORT.md).

### Local research only — post-ramp recovery, October 26

Clipping-aware rolling-restart recovery is **rejected, not integrated or installed**. Full 197-segment controller replay removes the old 61 mph timeout but adds a 20.59 mph timeout and 472 weaker encoded strong-braking rows. City regression unchanged; named highway pulsing regressions unchanged. 91 focused tests pass, which does not clear these failures. Pair and steering 1.20/0.97 unchanged. See [report](navigator-post-ramp-recovery-2026-10-26/REPORT.md).

### Local candidate — coherent command recovery, October 26

Transient rolling-demand reduction with local-output anti-windup clears the saved20.6/61mph added timeouts and weaker strong-braking regressions across197segments.58focusedtests pass; no paired integration/device changes. City regression unchanged; **highway pulsing unchanged**, aggregate braking exposure+4.349s. Not road/comfort proof. See [candidate report](navigator-command-recovery-2026-10-26/REPORT.md).

### Locally integrated — command recovery paired port, October 26

Openpilot `1dbbc0189` / opendbc `beb10c25`, exact pin and clean local pair. Full Mac/Panda builds, parent/child suites and197segment exact prototype parity pass. Supersedes earlier broad uninstalled low-speed integral guard. 1.20/0.97 preserved; **not pushed or installed**. Highway pulsing remains unresolved; +4.349s braking exposure and two preexisting timeouts remain documented. [Integration report](navigator-command-recovery-integration-2026-10-26/REPORT.md).

### Published / inactive device stage — command recovery, October 26

Pair `1dbbc0189` / `beb10c25` pushed to both adgower release branches. Private backup verified; ARM build, native/unit/regression checks and passive current-stack Park baseline pass. **Candidate inactive; installed pair remains5b301a944/884c9f491.** Alpha and1.20/0.97 unchanged. Highway pulsing still unresolved. [Staging report](navigator-command-recovery-staging-2026-10-26/REPORT.md).

### Active on device — command recovery, October 26

`1dbbc0189` / `beb10c25` activated; new-install offroad and powered Park checks pass. Alpha and1.20/0.97 preserved, rollback and private Mac backups retained; noOS/firmwareupdate. Road improvement remains unproven and highway pulsing unresolved. [Activation report](navigator-command-recovery-staging-2026-10-26/ACTIVATION_REPORT.md).

### Road evidence — command recovery, October 26

Current pair `1dbbc0189` / `beb10c25` acquired read-only:34 new completed segments, one moving current-code drive. **Restart improvement remains unproven** because Alpha never went below9.65mph (fix admits below6.7mph). No controlsMismatch/coordination fault this trip; highway brake/coast cycling remains. Assisted RPM peaked2870, with absolute3358 peak during manual acceleration. Lateral rising-turn shortfall around31mph and highway unwind/straight-section corrections remain; no75–85mph coverage. Comma and1.20/0.97 unchanged. [Road review](navigator-command-recovery-road-review-2026-10-26/REPORT.md).

### Local research — highway coast/brake coordination, October 26 CDT /27 UTC

Two weak-entry coast prototypes evaluated against216segments, including the latest19. Explicit coast removes the first prototype's added timeouts but only slightly reduces switching and adds51.179s brake-command exposure /2071weaker encoded strong-target requests; **rejected, not integrated or installed**. Native safety adds no TX rejections or relay faults. Next work is coordinated allocator/integral recovery rather than another threshold increase. Installed pair and1.20/0.97 unchanged. [Evidence and blockers](navigator-highway-coast-prototype-2026-10-27/REPORT.md).

### Local candidate — coordinated weak-brake allocation, October 27 UTC

Final local prototype clears the prior weaker-strong-braking and extra-exposure gates across216segments. All producer I/raw/freeze/recovery history and gas/combined requests remain identical. Complete-input full-brake changes1655→1637 and exposure falls14.130s; no added native TX rejection/relay fault.18focused tests and202installed tests plus20subtests pass; independent review and receipt checks complete. **Not integrated or installed.** New highway windows retain14/12/10changes and gas withdrawal is unchanged, so this is a modest bounded precharge improvement, not a demonstrated highway-pulsing cure. Paired branches, device and1.20/0.97 unchanged. [Report](navigator-coordinated-coast-prototype-2026-10-27/REPORT.md).

### Integrated locally — coordinated coast/brake allocation, October 27

Local committed pair `df788e027` / `1d29e6e7`, exact pin and clean release branches. Full Mac/Panda builds, parent1087tests, child4702tests, focused29tests, lint and whole-pair review pass. Production216segment replay exactly matches accepted final prototype across625,238callbacks /1,203,463producer steps.1.20/0.97 and protected runtime/settings retained. **Not pushed, staged or installed on Comma.** Modest precharge benefit only; physical highway pulsing remains unproved. [Integration receipts](navigator-coordinated-coast-integration-2026-10-27/REPORT.md).

### Published / staged inactive — coordinated coast/brake allocation, October 27

Pairdf788e027/1d29e6e7 pushed and remotely verified. Fresh private Mac backup checked; full isolated ARM build and native/retained/startup/calibration tests pass. Stage finalized clean/self-contained at `/data/navigator-validation/<private timestamp identifier>-df788e027/source`. **Not active: final audit still1dbbc0189/beb10c25.** AlphaON,settings,calibration and1.20/0.97 preserved; no app/OS/firmware restart/update. Staging-only prefix assertion corrected with hash-bound native-result reuse; evidence retained. Physical pulsing benefit still unproved. [Report](navigator-coordinated-coast-staging-2026-10-27/REPORT.md).


## October 27: coordinated coast/brake active

Pair `df788e027` / `1d29e6e7` is active. ARM/replay checks and ignition-off/powered-Park acceptance passed. Alpha ON and 1.20/0.97 preserved; previous complete installation retained. Highway pulsing and comfort improvement still require road evidence. See [activation report](navigator-coordinated-coast-staging-2026-10-27/ACTIVATION_REPORT.md).


## October 27: first coordinated coast/brake road evidence

Reviewed all 73 new segments, five sessions; one moving current-code trip. No controlsMismatch or coordination fault recorded. Highway cycling persists (17 and 14 brake-bit changes in 15 s near 59/68 mph). Assisted RPM reached 3,946 at 21 mph in first gear, with no braking during the peak. Restart propulsion remains continuous across 6.7 mph. Calibrated body response supports excess turning at 40–50 mph and residual unwind/straight oscillation near 64 mph. No >70 mph moving evidence. Next local work: coast/grade/integral/response timing; first-gear restart demand and OEM shift response; 40–50 mph mapping/unwind. Road improvement from this allocator remains unproved; installation/settings unchanged. [Full evidence and limitations](navigator-coordinated-coast-road-review-2026-10-27/REPORT.md).


## October 27: local pulse / restart / midrange prototypes evaluated

- **Pulsing — rejected candidate:** full 237-segment / 14-route coupled replay completed (685,504 callbacks), plus native saved-traffic replay (685,398 ACC slots, no added native rejections). The unified true-coast / phase-wide integral freeze worsens city cycling 17→27, weakens later strong braking and adds a simulated release-timeout near 55 mph. Native acceptance does not override these controller failures. Keep installed code unchanged.
- **High RPM — diagnosis and shadow exploration only:** received second-gear target appears at 18.885 mph versus roughly 9 mph in saved OEM examples, despite lower propulsion demand. No blanket acceleration cap or literal cruise-target packet policy is supported. Five diagnostic checks and 18 synthetic native packet cases pass; no runtime policy selected.
- **40–50 mph steering — diagnostic candidate:** extend existing bounded roll-aware mapping over 35–55 mph with the exact current ObserverContinuity baseline. Full 658-segment / 33-route saved safety comparisons add no native rejections; 106 targeted tests pass. No changed angle frames above 55 mph; 1.20/0.97 remains unchanged. Recorded path commands shrink about 2% in the 42 mph episode and 7% near the 50 mph input. Transition-direction flags and insufficient correction of the larger 42 mph excess remain open; physical improvement is unproved.

No paired source, device, settings, firmware or installation changes. None of these results authorize installing a new policy. Next local design must address joint demand/grade/delivery response and steering admission during transitions, rather than enlarge allowances or suppress safety faults. [Full experiment reports and verification](navigator-control-refinement-prototypes-2026-10-27/REPORT.md).


## October 27: local timeout/braking and steering-transition repairs clear saved replay gates

- **Longitudinal repair selected locally:** ordinary ramp anti-windup preserved; explicit revision-3 signed-coast feedback and logical clearance ownership replace the failed phase-wide freeze. Full 237 segments / 14 routes / 685,504 consumer callbacks have no added fault, lost activity, weaker strong braking or raw/I/gas difference. All 1,311,408 producer steps match the coupled reference. All 627 changed packets only clear precharge. Native replay adds no rejection; 32 tests pass. The two older reference timeouts remain identical, and main highway brake-count/propulsion cycling is unchanged: physical pulsing improvement remains unproved.
- **Steering transition repair selected locally:** elapsed fresh coherent body/wheel admission, hysteresis and exact original mapping fallback. All 18 prior transition risk slots now equal baseline; some useful mapping correction remains. Full 658-segment / 33-route coverage adds no native rejection, preserves default-off and all protected speed bands, and matches prior reference hashes. 123 tests pass. Historical 637 segments freshly replayed; same-candidate focused 21 reused with hash binding. Physical oversteer correction remains partial/unproved.

Paired sources and Comma unchanged; owner 1.20/0.97 retained. Next step is deliberate paired-source transport/controller integration plus build/integration validation, not activation from a research hook. High-RPM protocol identification and physical coast response remain open. [Repair reports and final verification](navigator-control-regression-repair-2026-10-27/REPORT.md).
