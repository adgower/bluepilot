<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator master integration implementation plan

> Execute inline using executing-plans; perform one independent whole-branch review after verification.

**Goal:** create clean paired branches from current public master and its pinned opendbc, preserving the installed Navigator trial without changing the Comma.

**Architecture:** independent local clones preserve existing checkouts and the old trial. Port existing commits in dependency order, adapt normalized vehicle parameters, and pin the exact custom child revision in the parent. Keep AGNOS, firmware and models at the new master's supported versions; carry only the deliberate vehicle selector, not old build workarounds.

**Spec:** ../../research/navigator-migration-settings-2026-10-14.md and ../../../NAVIGATOR_ROADMAP.md NAV-10. User explicitly authorized this implementation after reviewing the paired-branch design.

**Global constraints:** no device access/mutations; retain owner 1.20/0.97, geometry 3.1115 m and ratio 19.6, optional fixed pinion and low-speed trial, unchanged steering limits and >=45mph mapping; no MADS, auto calibration or longitudinal candidate; no publication/PR/deployment in this implementation request.

## Review focus

- Normalized geometry guard must agree with fixed Panda curvature despite removed mass/rear-steer fields.
- Pinion missing, stale, invalid-quality/counter data must fail closed.
- Options off preserve the original fork angle mapping and avoid affecting other Ford platforms.
- Trial requires supported fixed pinion geometry and preserves high-speed mapping.
- Parent/submodule pin and both UI settings must survive a clean clone/build.

## Tasks

1. **Isolation and baseline:** query/fetch latest master, record exact parent and child bases, create `codex/navigator-master-integration` in independent clones, inspect instructions and build dependencies. Run unmodified targeted Ford tests as a baseline. Record environmental limitations separately.
2. **Child port:** first port regression tests for Navigator geometry, angle control/ordering, preserved 1.20/0.97, pinion and trial behavior; observe failures on upstream. Apply existing implementations in order, adapt mass-normalized field checks with equivalence tests, and run the Ford/controller/safety suites plus lint/build. Commit reviewable changes in opendbc.
3. **Parent integration:** port parameter/startup/UI tests first, confirm upstream lacks the options, apply settings/startup changes with current interfaces and forced vehicle selection, update the fork dependency URL and exact gitlink. Preserve master AGNOS pin and model/firmware requirements. Run UI/startup contracts and relevant builds/tests. Commit parent integration.
4. **Replay and review:** adapt recorded replay harness paths/schema under the new dependency; replay prior full dataset and latest drive where available, verify >=45mph trial-neutral comparison and independent old/new fixed-model equivalence. Perform one fresh-context review, fix substantive findings, and rerun affected checks.
5. **Handoff:** write exact SHAs, branch locations, check counts, replay results and build limitations; update roadmap. Keep installation pending. Never describe local checks as device/road validation.

## Execution ledger

- Started: isolation and upstream fetch. Native worktree tool is attached to the BluePilot project rather than the target openpilot/opendbc repositories; independent clones inside allowed workspace roots avoid modifying their original Git metadata or dirty source.
- Ruling: the user has explicitly approved the prior migration design and requested execution; proceed inline without a repeated design approval gate.
- Baseline pinned: openpilot 6eb63e045469a582f4c7b406705543e891113606, opendbc b3bd79a659dae961af169a3baac723961f720133. Upstream Ford baseline: 6 tests passed. Initial migration regression: 10 assertion failures as expected (geometry/model/option absent). Parent UI contracts: 6 failures before port.
- Child commits ported in order. Ruling: retain upstream automatic Ford checksum generation (d22436e8) rather than resurrect the removed manual checksum helper. Preserve upstream bus-qualified safety RX structure while adding the existing pinion guard.
- Ruling: upstream now uses FordFlags.HAS_BSM=2, which collides with the old trial's PINION_CURVATURE=2. Added failing regression, then allocated PINION_CURVATURE=4 and LOW_SPEED_GAIN=8. Panda safety parameter values remain unchanged; runtime flags are internal and must be regenerated, not copied from an old CarParams blob.
- Adapted pinion guard to mass-normalized stiffness fields and removed obsolete rear-steer/mass fields; fixed Panda formula remains the preserved algebraically equivalent model. Tests and native safety suite running.
- Native H7 build passed, native Params/messaging build passed. Six UI contracts passed; 13 real Params tests passed after granting their isolated temporary-prefix filesystem access. Full minimal Mac build stops at Metal command-queue creation during model warp compilation; no dummy/prebuilt artifacts substituted.
- First full child suite: 3746 passed, 1690 skipped, 3 MISRA mutation setup failures. Direct MISRA isolated real pre-existing angle-port conversion findings. Replaced composite/narrowing casts and float shadow scaling with equivalent signed decode/integer scaling; exhaustive 65536-value comparison preserves behavior. Direct MISRA and normal mutation tests now pass. Final whole suite rerunning.
- First 45-segment new-controller replay produced byte-identical complete CAN streams against the prior trial on all three drives; 148765 TX accepted and zero rejected, 10082330 RX. Latest-drive exact recorded replay retains the same 2 angle and 8 button rejections. Final replay uses actual opt-in selector with the new internal flags and final native safety library.
- Tasks 1–3 complete locally. Final child suite green: 3746 passed, 1690 skipped, 24673 subtests. Focused parent native/UI/startup: 23 passed. Matching H7/native Params/messaging build and changed Python lint pass. Independent source review: no important actionable findings.
- Task 4 replay complete: trial-on all-three-drive CAN streams byte-identical to old trial; options-off all-three-drive streams byte-identical to preserved baseline; no new safety rejections. Trial-on final replay148765TX accepted/zero rejected,12425high-speedmessages identical. Existing latest-drive recorded rejection pattern unchanged.
- Task 5 complete: final parentc16168b9f772a7beb2991a7265dc420dcfe05550 pins childc09baff5c2cdd7c887e25c2d88b671f403e1ed9d. Durable independent clones and verified delta bundles preserved. Roadmap and report updated.
- Validation blocker: full Mac build first fails sandbox Metal queue; normal GPU retry reaches missing LLVM library. Full parent pytest collection lacks generated acados solver, rednose EKF and jeepney. No full-build/full-parent-suite or device/road success claim. Next step is supported-environment validation; no publication or deployment in this task.

## Build validation follow-up

Completed full minimal/development Mac builds and project-scoped parent suite (957 passed, 343 passing subtests). Recorded dependencies, verified model artifacts, reviewed test-only portability fixes and evidence in parent 6ae31161b73de2ce5043f708569759ac5f55f283. Child and vehicle control code unchanged. Refreshed roadmap/report/bundles; no device operations. Remaining publication and AGNOS/device validation are tracked in NAV-02/NAV-10.
