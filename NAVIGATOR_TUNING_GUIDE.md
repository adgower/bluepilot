<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator tuning and development reference

Last consolidated: **October 28, 2026**. Start here for how this project works and what the evidence supports. This guide summarizes the durable record; it is not a verbatim transcript or a claim that every historical setting change can be reconstructed.

## Where to find things

| Need | Reference |
|---|---|
| Current goals, priorities, chronological decisions and blockers | [Navigator roadmap](NAVIGATOR_ROADMAP.md) |
| Feature descriptions, paired-repository changes and commit history | [Branch feature inventory](docs/research/navigator-branch-feature-list.md) |
| Every saved research document and design/plan | [Complete document catalog](docs/research/NAVIGATOR_RESEARCH_INDEX.md) |
| Original settings/geometry migration inventory | [October 14 snapshot](docs/research/navigator-migration-settings-2026-10-14.md)—historical, not current defaults |
| Latest observed installed source/settings and road evidence | [October 28 returned drives](docs/research/navigator-returned-drive-review-2026-10-28/REPORT.md) and its acquisition/verification receipts |
| Most recent grade/integral experiment and rejection | [Post-clear rebraking](docs/research/navigator-postclear-rebraking-2026-10-28/REPORT.md) |
| Recovered controlled tests and release observations | [Maneuver recovery](docs/research/navigator-evidence-recovery-2026-10-27/REPORT.md), [release validation](docs/research/navigator-maneuver-release-validation-2026-10-28/REPORT.md) |
| Documentation scope, gaps and link checks | [Documentation audit](NAVIGATOR_DOCUMENTATION_AUDIT.md) |

The roadmap is a history as well as a plan: an old heading saying “current install” applies to its date. Read the latest dated source/installation receipt before treating an old stage, parameter, OS version or local candidate as active. README content inherited from BluePilot describes that project and does not establish which features this Navigator fork has installed.

## Current documented baseline

Last device read: October 28, during the returned-drive acquisition; **no device query is performed merely by reading this guide**.

- Vehicle: 2023 standard-wheelbase Lincoln Navigator, operating through the deliberately forced `FORD_EXPEDITION_MK4` identity. This is not first-party Navigator recognition.
- Installed parent: `e05e42f43d2907a4f02915a924cfd95a46197e79`.
- Paired opendbc: `5097b993965b2b65ea3fcca7e3769cfa9403d49c`.
- Both local paired checkouts currently use `codex/navigator-tracking-release`. The working integration checkout is `${USER_HOME}/Apps/openpilot/.navigator-master-integration-20261014`; its paired child is `opendbc_repo`. The BluePilot directory holds the research/roadmap and is not interchangeable with the installed source checkout.
- Owner **1.20 / 0.97** angle calibration is in source, not two ordinary live parameter keys. Preserve its exact scope and the paired safety/geometry assumptions; it is not a universal gain.
- Latest read: `DisableUpdates=1`, Alpha longitudinal ON, longitudinal coordination ON, high-speed tracking/roll mapping/persistent tracking/pinion-feedback option/low-speed option ON, personality `0`, initial cruise speed `40` km/h. `ExperimentalMode` and maneuver-mode keys were absent in that scoped inventory; absence is not a saved true value and is not a complete runtime-default analysis.
- Geometry was ported for this vehicle, including 3.1115 m wheelbase. The original settings sheet records historical mass/steer-ratio/stiffness values; mass-normalized upstream schemas require equivalent dynamics rather than blindly restoring an old mass field.
- AGNOS 20.1 and Chestnut/model startup work have dated installation records in the catalog. The October 14 sheet’s AGNOS 19.7 and Alpha-OFF observations are historical. OS/runtime state needs fresh verification before another update; the latest log-acquisition inventory is not a fresh OS/firmware recovery audit.

No original full pre-customization parameter baseline exists in the scoped record, so “every setting Alex ever changed” cannot be established. Preserve a fresh private full parameter backup before migration, then separately document the selected nonsecret settings and source constants.

### What remains open

| Area | Latest supported conclusion |
|---|---|
| City/highway longitudinal comfort | Pulsing persists. October 28 adds 17 brake-bit changes in 15 s near 61–62 mph and 11 near 24–26 mph. Different routes are not controlled improvement comparisons. |
| High RPM / rolling restart | Owner reports another incident; a likely <private clock time> match has decoded peak 4,362 RPM with reported first gear and target moving toward second. RPM quality remains unresolved. |
| Controls mismatch | None recorded in the three newest drives; this does not prove all historical timing/release causes permanently solved. |
| Low-speed steering | A new 3.25 s rising-demand episode around 15–17 mph has median body/request about 53% and wheel-model/request about 51%, before driver input. |
| Mid/high-speed steering | Some descriptive excess and unwind lag remain. The latest trips add no 70–85 mph exposure; older high-speed incidents remain part of the historical evidence. “Good at 45” is not a calibration exemption. |
| Latest local prototypes | Grade filter and pre-action steering bias refinement were rejected. They are not installed features. |
| Other feature goals | MADS/always-on steering, Auto Start/Stop transmission, parking assist, auto calibration and upstream Navigator recognition have separate research/status records. Their presence in the backlog is not implementation or compatibility proof. |

## End-to-end workflow

### 1. Establish exactly what is being evaluated

Record the owner symptom and approximate time/speed/context separately from an assistant interpretation. Verify parent/child commits, dirty state/overlays, relevant source hashes, settings and actual active modes. Tag every drive by its recorded startup source; a download date alone does not make it evidence for the newest tune.

Use separate labels for proposed, local prototype, replay-rejected, locally integrated, published, staged inactive, activated, parked-checked and road-observed. Do not turn a successful build or staging job into a claim of installation or driving improvement.

### 2. Preserve recordings and provenance

Use the available Comma Lab connector when it can perform the job; the latest run used existing strict-host-key SSH because the app was unavailable. Acquisition reads files and source/settings; it does not open Panda or query ECUs. Select completed logs, honor logger locks and defer open segments. Deduplicate by original compressed SHA256 and byte count, not route aliases or directory names. Recheck selected files and device source/settings/protected artifacts after download.

Retain private originals and mappings in `${USER_HOME}/CommaBackups`; temporary derived caches are rebuildable and are not a substitute for that archive. The latest returned-drive archive contains 29 verified segments. Raw GNSS, route identities, complete parameter backups, credentials and device identity stay private. Public-facing reports use aliases and scoped nonsecret settings.

Prior acquisition scripts contain real SSH operations and snapshot-specific assertions. Inspect/adapt them rather than treating a historical command as a generic current workflow. [Latest acquisition example](docs/research/navigator-returned-drive-review-2026-10-28/PLAN.md).

### 3. Extract and qualify before computing performance

Decode with the correct schema and source/DBC provenance. Verify derived-cache hashes. Preserve original publication, producer, consumer and CAN-receive clocks; none is automatically the ECU’s internal sample clock. Match consumed epoch/sequence and plan/state references when available. “Nearest row” cannot silently replace exact consumed identity or use future data.

Separate manual driving, overrides, startup, engagement transitions, invalid/stale sensors, signals/lane changes, saturation, actual stopping, rising demand, steady demand and unwind. Missing keys/streams/gaps mean unknown, not false or successful. Report excluded exposure and speed-range coverage, including empty bands. [Latest qualification/metrics](docs/research/navigator-returned-drive-review-2026-10-28/REPORT.md).

### 4. Diagnose one reproducible mechanism

Find a bounded recorded episode and a regression that can fail on the specific software problem. Keep the first divergence. Rank alternative explanations rather than treating the first correlation as the cause. For longitudinal, trace planner → raw demand/I → grade decision → allocator → brake/precharge/propulsion → reported torque/status → returned feedback. For lateral, trace planner reference → calibration/roll mapping → encoded command → wheel/pinion/body response → driver context.

A source-only defect, a frozen-response command reproduction and physical discomfort are different findings. State which one the available loop can reproduce.

### 5. Prototype locally without disturbing the installed pair

Use an isolated research directory/checkout and retain original source/evidence. Declare one hypothesis, scope, fixed parameters and acceptance criteria before searching for a favorable result. Write meaningful behavioral regressions at the real call boundary. Preserve 1.20/0.97 and geometry unless a separate approved change explicitly targets them.

Keep a rejected variant and its failure receipt; do not silently replace its parameters and retain its old passing counts. Do not reset budgets, PID state, clearance history or reference demand just to make a metric pass. [Latest bounded diagnostic and rejection](docs/research/navigator-postclear-rebraking-2026-10-28/DESIGN.md).

### 6. Compare the complete feedback loop

Frozen-response replay must recompute the actual producer PID and consumer controller, with causal returned software feedback. A brake-bit-only edit with recorded PID held fixed cannot validate the later loop.

Compare raw acceleration, I/freeze state, phase, overlays/debt, gas, encoded brake strength, full-brake and brake/precharge union exposure, transitions, faults/timeouts, inactive/disabled output, owner/activity history and retained-torque propulsion. Include later strong braking and transitions out of the prototype’s scope. Fewer bit changes alone is not acceptance.

Run focused regressions first, then the declared broader corpus if the focused gates pass. “Full replay” must name the exact revision, input manifest, unique segments/routes, clocks and exclusions: historical 515/737 lateral or 216/316 longitudinal results cannot be inherited by a new revision. Keep diagnostic-only routes visible. Native permission/rejection checks, local builds, ARM builds and physical tests are separate evidence. An unsanitized Mac native run is not UBSan coverage; the documented runtime-load failure stays visible.

### 7. Integrate and publish the exact pair

Only a selected candidate proceeds to paired integration. Parent runtime/schema/UI, child controller/geometry and matching safety must agree. Pin the exact child commit in the parent and verify that a clean clone can fetch it. Refresh upstream changes intentionally, including schema/model/AGNOS/firmware requirements, instead of an unqualified pull onto a dirty device. Compare the final integrated revision to the replayed revision and run the required build checks.

Publication and device operations are distinct actions; a local prototype or passing replay does not authorize either. This curated export is versioned on `docs/navigator-reference`; publishing documentation is separate from vehicle installation.

### 8. Back up, stage, activate and verify separately

For an authorized device change, inventory the current install and private parameters; preserve a rollback app/source/parameter set and recovery material. An app backup is not a proven OS rollback image. Stage in a separate directory and run ARM/build/model startup checks before activation. Chestnut may require ignition ON for power even when Comma remains powered through Comma Power; a cold-start/GPU test therefore needs its own explicit parked procedure and restoration check.

Switch installations with ignition OFF under the applicable activation guard, stable power/Wi-Fi and screen/recovery access. Older procedures required Alpha OFF; later authorized guards support Alpha ON with ignition-off checks. Inspect the actual guard/version rather than impose an old toggle requirement or bypass a current guard. Then verify home-screen operation, source/settings and passive powered Park checks with assistance disengaged. Parked checks do not prove engagement under load, braking performance or comfort.

### 9. Review the resulting drives and update the record

Acquire all newly completed recordings, identify the exact active tune, compare like-for-like phases and preserve takeovers with owner context/video when available. Never label every driver input a failure or every absence of a mismatch alert permanent resolution. Add exact episodes to the regression set, record unsupported speed ranges and update the roadmap, feature inventory and dated report. Keep human reports distinct from automated candidate matches.

## Lateral lessons to retain

- **Five-mph bins are evidence bins, not automatically independent gain settings.** Adequate data need repeated directions, road/camber/roll and speed-transition coverage; avoid overfitting a sparse bin or a single bend.
- Separate desired path, transmitted curvature-equivalent, pinion/wheel model and body-yaw response. A wire/request ratio is not direct wheel authority, particularly with path-angle-primary Ford control. Body/wheel agreement is useful but each has calibration/model uncertainty.
- Pinion feedback does not automatically eliminate body-yaw offset or provide tire/path ground truth. Quality flags, source clocks, fixed/learned geometry, steering zero and roll must agree. The 1.20/0.97 owner mapping must retain its original vehicle/scope assumptions.
- Use meaningful-demand thresholds; near-zero ratios can explode. Straight-road/ping-pong review uses absolute motion, wheel rate, lane context and uncertainty rather than “percentage of zero.” Separate entry, steady tracking and unwind.
- Feedback is delayed and quantized. Fresh duplicate values are not independent new response samples. The original angle-frame association study found many ambiguous repeated-value matches; publication time cannot stand in for a unique consumed raw frame.
- Desired curvature motion is not calibration drift. Moving-reference correction needs a validated response envelope for nominal and corrected histories, source timing and uncertainty; the latest pre-action bias model worsened held-out error and is rejected.
- Persistent-error correction must have bounded admission, budgets, monotonic release, ownership/override handling and valid rearming. A speed fade or strong-demand bypass does not erase prior state. Keep transition, abort, delay, quantization, saturation and boundary tests.
- A software deviation/rate limit, an EPS availability flag and actual ECU authority are separate questions. Low-speed parking capability does not prove the driving command channel has unrestricted steering authority.
- The latest 15 mph shortfall and historical 80–85 mph inside-bend events are different regimes. Preserve the full range, including 45 mph, and do not extend a successful local tune across unsupported speeds.

Key sources: [calibration/roll and temporal history in roadmap](NAVIGATOR_ROADMAP.md), [delayed-response investigation](docs/research/navigator-response-resolution-2026-10-27/REPORT.md), [original steering identification](docs/research/navigator-response-resolution-2026-10-27/steering-identification/REPORT.md), [rejected bias refinement](docs/research/navigator-evidence-recovery-2026-10-27/steering-innovation/REPORT.md), [latest all-range road evidence](docs/research/navigator-returned-drive-review-2026-10-28/REPORT.md).

## Longitudinal lessons to retain

- MAX/set speed is an upper bound; lead, model/path demand and planner constraints can keep actual speed below it. Being below MAX does not prove posted-speed-limit following. Inspect the recorded plan source, target, lead and active mode before changing a setting. Alpha, Experimental mode and personality are distinct concepts.
- Aggressive/standard/relaxed planner behavior does not by itself repair Ford brake/propulsion handoff or downstream integral interaction. Preserve the actual recorded personality and source when comparing trips.
- **Inactive gas `-5` is a mode sentinel**, not an acceleration to average with numerical engine requests. Absence of brake/precharge requests can still mean active engine control. Even inactive propulsion plus clear requests does not prove reported brake torque is clear or identify physical free-coast drag. The October 28 metrics correct inherited misleading coasting labels without rewriting frozen historical artifacts.
- Full brake, precharge, command/status clear, actual/arbitrated reported torque and achieved acceleration are separate observations. Preserve the installed received-torque qualification and original timeouts; do not infer clearance just because the software stopped asking for braking.
- Controlled 20 mph braking releases qualified around 1.56–1.58 s, while some highway weak-release sequences are much faster. These different regimes do not justify a universal fixed delay or a larger coast lease. Stopped/creep, interrupted and held phases stay censored.
- Grade’s OEM-fitted ~0.149913 m/s² offset is relative reference alignment, not independently calibrated road slope or proof the ECU/software compensation ownership is resolved. Keep camera/steering calibration separate.
- I integrates signed acceleration error. The four recent I-dominated rebrakes had negative average target-minus-actual error; reducing I was a normal response. Zeroing I or freezing negative error can hide a legitimate slowdown request.
- Grade, allocator, clearance, handoff and I form a feedback loop. Earlier release can freeze positive integration; rebraking can unfreeze it. The latest grade filter changed later strong demand even after bypass and added braking exposure despite fewer transitions. Isolated input smoothing is not a complete fix.
- Preserve allowance/debt across early negative-net exposure and tiny positive crossings; rearm needs the actual required conditions. Merely keeping an allocator class unchanged does not preserve the original authority if its reference input changes. Audit omissions against the unmodified baseline, including locked accounts.
- Forecasting saved acceleration is not an identified counterfactual coast/brake gain. Coissued closed-loop commands, route/grade/gear history, correlated samples and broad uncertainty prevent causal authority claims. Two genuine maneuver sessions were recovered beyond the steering-only corpus; low-speed braking excitation does not establish highway quiet-coast authority.
- RPM quality remains unresolved. Raw engaged-gear code 6 is an engagement state, not sixth gear. Keep actual and target numbered gear separate, and retain the raw QF. OEM predicted-acceleration/target-speed field differences are protocol leads, not proof that transmitting them fixes shifts or pulsing.

Key sources: [relative grade mapping](docs/research/navigator-grade-resolution-2026-10-23/REPORT.md), [response-aware OEM/Alpha study](docs/research/navigator-response-aware-allocator-2026-10-26/REPORT.md), [coupled allocation failure](docs/research/navigator-allocation-response-resolution-2026-10-27/REPORT.md), [controlled maneuver recovery](docs/research/navigator-evidence-recovery-2026-10-27/REPORT.md), [release qualification](docs/research/navigator-maneuver-release-validation-2026-10-28/REPORT.md), [13-event attribution and filter rejection](docs/research/navigator-postclear-rebraking-2026-10-28/REPORT.md).

## Other goals and research

- [Upstream Navigator support plan](docs/research/navigator-upstream-plan-2026-10-19.md): keep a small model/geometry/firmware identity port separate from personal steering and Alpha tuning. Forced Expedition identity is not natural matching. Refresh current upstream and public PR state before acting on historical notes.
- [Active Park Assist hardware investigation](docs/research/navigator-active-park-assist-2026-10-14.md) and [OEM IPMA comparison](docs/research/navigator-ipma-oem-comparison-2026-10-14.md): cached software identifiers and part-number matches are not retrofit compatibility proof. Passive research does not authorize diagnostic/control transmissions.
- [MADS/always-on steering](docs/research/navigator-mads-exploration-2026-10-14.md), [auto calibration](docs/research/navigator-autocal-exploration-2026-10-14.md), [mass normalization](docs/research/navigator-mass-removal-exploration-2026-10-14.md), [fork ideas](docs/research/navigator-fork-ideas-2026-10-14.md) and [QoL priorities](docs/research/navigator-qol-priorities-2026-10-20.md).
- Auto Start/Stop button-press evidence is preserved in the dated roadmap and catalog. Identifying a received button event does not establish a safe transmit feature or approve sending it.
- [Chestnut compatibility background](docs/research/chestnut-egpu-big-model-compatibility.md); the catalog also includes later AGNOS/model recovery, staging, activation, build and screen/parked acceptance records.

## Practical reference checks

For this public export, start with [source reconstruction](docs/navigator-reference/REBUILD.md) and run `python3 scripts/navigator-reference/verify_reference.py`. This checks curated content and links without private recordings or a device. `--openpilot-root /path/to/openpilot` also verifies the pinned source pair and selected source hashes.

Historical study verification/replay commands require the original private inputs and exact environment; many live/backup scripts are deliberately omitted. Curated `PUBLIC_VERIFICATION.json` files summarize outcomes without exporting full private receipts. See the [export policy](docs/navigator-reference/README.md).

## Record format for the next iteration

Keep a dated study directory with owner observation, exact source pair/settings, hypothesis and scope, original-input manifest/hashes, excluded/unknown data, first divergence, candidate source, focused tests, named regression results, actual broader/native/build runs, outcome/rejection and physical limits. Add stage/activation/rollback receipts only when those actions actually occur. Update the roadmap and feature inventory, then refresh the catalog. Preserve earlier failed evidence and distinguish an accepted change from a useful rejected experiment.
