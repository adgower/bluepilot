<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator paired master integration

October 14, 2026. The requested current-trial port is committed in two isolated local branches. No SSH connection, source/parameter write, reboot, firmware flash, or installation on the Comma occurred during this implementation. The original implementation was local only. In the subsequent authorized publication step, both branches were pushed and clean remote cloning was verified; no PRs were opened.

## Branches and provenance

Both branches are named **`codex/navigator-master-integration`**.

| Repository | Isolated checkout | Base | Final head |
| --- | --- | --- | --- |
| openpilot | `${USER_HOME}/Apps/openpilot/.navigator-master-integration-20261014` | `6eb63e045469a582f4c7b406705543e891113606` | `6ae31161b73de2ce5043f708569759ac5f55f283` |
| opendbc | `${USER_HOME}/Apps/opendbc/.navigator-master-integration-20261014` | `b3bd79a659dae961af169a3baac723961f720133` | `c09baff5c2cdd7c887e25c2d88b671f403e1ed9d` |

The parent pins that exact child commit and changes the dependency URL to Alex's opendbc fork. Its nested child checkout matches the standalone child branch. Both checkouts are clean. The original openpilot/opendbc working files and older trial commits were preserved. Fresh fetching at implementation start advanced the audited parent target from `690fa743b` to `6eb63e045`; the opendbc base stayed the same.

The review covered parent implementation commit `21fd666e2` and child `c09baff5`; the later parent commit adds verification documentation/scripts only. Delta Git bundles and binary-capable patches are saved beside this report. The bundles require the listed upstream bases and were verified locally. Both branches are now published at the exact listed SHAs. A clean remote clone resolves every pinned submodule, including the custom child; see `publication-verification.json`.

## Preserved features

- Forced Expedition selection for this Navigator, 3.1115 m wheelbase, fixed ratio 19.6 and equivalent normalized dynamics. This is still a personal profile override, not first-party Navigator support.
- Existing angle-control command mapping and engagement ordering.
- Owner **1.20/0.97** high-curvature factors, unchanged.
- Opt-in paired fixed-model pinion feedback and low-speed trial, with original signal, rate/range/deviation and driver-override protections.
- Original trial multipliers, curvature blend and 30–45 mph fade; at or above 45 mph the trial contributes no additional gain.
- Both persistent settings, startup wiring, and offroad-only standard/MICI controls. Fresh parameter storage defaults both options off; existing device preferences were inventoried but not changed or copied to a device.

The new base retains AGNOS **19.9**, current Chestnut firmware/model expectations and automatic Ford checksum generation. Old AGNOS pinning, prebuilt marker and staging-path workaround were not imported. MADS, automatic calibration, anti-weave smoothing and the separate longitudinal coordination candidate were not added.

## Compatibility changes

1. **Mass normalization:** the pinion guard now checks the equivalent `tireStiffnessFrontPerMass` / `tireStiffnessRearPerMass` fields. Obsolete mass and rear-steer accesses were removed. Panda's fixed model remains algebraically equivalent.
2. **Flag collision:** upstream `HAS_BSM=2` conflicts with the old pinion bit. Runtime pinion/trial flags are now **4/8**, protected by a regression test. Persistent parameter names and Panda safety values are unchanged. Startup regenerates CarParams; do not transplant old runtime flags.
3. **Ford checksums:** retained upstream automatic checksum computation instead of restoring the removed manual helper.
4. **Safety RX structure:** preserved upstream bus-qualified RX matching while adding the existing pinion lifecycle checks.
5. **MISRA:** corrected inherited shadow decode/conversion casts and reduced variable scope. All 65536 signed shadow values were checked to preserve the old float-scaling conversion result.
6. **Settings UI:** retained current upstream experimental-mode behavior and descriptions while adding the two guarded trial controls.

## Verification

| Check | Result |
| --- | --- |
| Unmodified upstream Ford baseline | 6 passed |
| New geometry/option regressions before port | Failed as expected; preserved red logs |
| Flag-alias regression before fix | Failed as expected |
| Parent UI contracts before port | 6 failed as expected |
| Full final opendbc suite | **3746 passed, 1690 skipped, 24673 subtests passed** |
| Normal MISRA mutation checks | Passed, including 3 subtests |
| Parent UI, real Params and startup combination checks | **23 passed** |
| Changed production Python / relevant tests lint | Passed |
| Matching H7 firmware build | Passed locally; not flashed |
| Native Params and messaging build | Passed |
| 45-segment trial replay | **252406 updates; 10082330 RX; 148765 accepted TX; zero TX rejected** |
| Old/new complete trial CAN stream comparison | Byte-identical on all three drives |
| Trial-neutral >=45 mph comparison | **12425 messages; zero differences** |
| Options-off complete CAN comparison | Byte-identical to preserved original baseline on all three drives; existing one-angle rejection unchanged |
| Latest-drive recorded relevant RX / all TX replay | Same **2 angle + 8 button rejections** as previous reconstruction; no new checked RX invalidity |
| Fresh-context independent source review | No important actionable findings |
| Full minimal and development openpilot Mac builds | **Passed**; native solvers, real model compilation, Cabana included |
| Complete parent project suite (`pytest openpilot`) | **957 passed, 86 skipped, 1 xfailed, 343 subtests passed** |

Each old-route replay has one initial RX warmup invalid tick and excludes pre-Ford-configuration TX. Native safety verification on this Mac uses an unsanitized debug build; no sanitizer coverage is claimed. Replays do not reproduce complete forwarding/hardware behavior or changed vehicle response. The latest-drive replay uses the complete compact recording rather than incomplete downloaded raw rlogs. Hardware blocked counters remain a separate unresolved attribution question.

H7 artifact built from implementation parent `21fd666e2` and final child code: SHA256 **`5a10a6119110b3c41a03d381c4bdd3bea4e05c3a7164bef515b42df7054c466e`**. It remains in the isolated parent's `panda/board/obj/panda_h7.bin.signed`. Subsequent parent changes are tests and documentation only; production steering source is unchanged. Rebuild and re-identify artifacts before any later deployment.

## Build follow-up and remaining installation steps

The earlier LLVM, generated solver/localizer and optional dependency blockers are resolved. Full minimal and full development Mac builds now pass with real model compilation. Git LFS model files were verified against committed pointer sizes and SHA256; actual fonts/images also load in the real Comma 4 UI startup test. No model/source bypass was introduced.

The complete parent project suite passes: **957 passed, 86 skipped, 1 expected failure, 343 passing subtests** (170.44 seconds). Focused messaging passes 222 tests; Athena/uploader/real UI startup passes 38. Five test files needed reviewed macOS spawn, socket readiness, xattr portability and CLI-helper collection fixes. The paired child and production steering code are unchanged, including 1.20/0.97. Earlier failed logs are historical, superseded by the committed `validation-*` logs and `MAC_VALIDATION.md` reproduction notes.

Local Mac build blockers are cleared. Publication and clean remote cloning are complete. The backed-up, parked AGNOS 19.9/firmware/model procedure is documented in [the installation plan](INSTALLATION_PLAN.md); fresh device inventory, backup and recovery verification remain before migration. Mac success does not prove an AGNOS build, Chestnut runtime, device boot or improved road handling. Existing application backups do not establish OS downgrade capability. No Comma access, publication, flashing or installation occurred during this follow-up.

## Evidence locations

- This directory: replay scripts/results, command comparisons, summary, verified delta bundles and patches.
- Isolated parent `docs/navigator-integration/`: settings snapshot, reproduction notes, native/full-build logs, parent test logs, environment list and provenance.
- Isolated child `docs/navigator-integration/`: red/green migration evidence, full-suite and MISRA results.
- [Migration settings inventory](../navigator-migration-settings-2026-10-14.md).
- [Main roadmap](../../../NAVIGATOR_ROADMAP.md).

## Publication follow-up

Both remote heads match the validated local revisions. The clean clone resolves all six pinned submodules and has a clean working tree. Its real driver-monitoring model download matches the LFS pointer, and Chestnut firmware matches its committed Git blob. The complete LFS pointer inventory is identical to upstream master, so no model upload was required; the inherited Hugging Face upload hook was skipped after that check. This is not a new full build or complete model provisioning of the clean clone. No PR, device access or installation occurred.

## Device preparation follow-up

After separate authorization, private backups and inert source staging on the Comma are complete. See [backup](DEVICE_BACKUP.md), [stage verification](STAGING_STATUS.md) and [recovery assessment](RECOVERY_OPTIONS.md). Current installation, preferences, calibration, 1.20/0.97, OS, slot and firmware remain unchanged. No updates or activation were started.

## Installed-state update

The subsequent authorized migration completed successfully: clean native AGNOS19.9 build, matching Chestnut/Panda firmware and final normal offroad reboot. See [execution and limits](MIGRATION_EXECUTION.md). Both repos are clean at the published SHAs; 1.20/0.97, steering preferences and calibration are preserved. Alpha/Experimental mode remain off and application updates paused. Full-power/onroad and road evaluation are not yet established. Earlier non-installation statements above describe the earlier implementation/preparation stages.
