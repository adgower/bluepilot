<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Paired high-speed integration — October 18, 2026

Local integration of the body-confirmed high-speed reduction, cumulative unwind latch, rising-demand rearm and bounded driver-pressure release into the existing paired `codex/navigator-tracking-release` branches. Parent `ff6ff263084a4bc433cf197b44ce3a31f7608851` pins child `9d5a3d485085f36beeb9aff7baf53c0d4ea603ee`. Both commits are local and the paired checkouts are clean.

The child owns the portable controller and 73 controller regressions. The parent owns a separate persistent/default-off `FordPrefHighSpeedTracking` key, prerequisite-aware factory selection, real subscriber receipt/source/publication separation, invalid-calibration revocation, and actual producer/card capture tests. No new UI control is added. Existing preferences are not modified.

Owner **1.20/0.97**, Navigator geometry, fixed pinion model, existing roll map, Ford controller and native safety source/library are unchanged, verified against the pre-integration SHA256 receipt. The historical device settings snapshot is unchanged; no fresh device inventory is claimed.

## Replay evidence

Fresh integrated factory/module replay covers **28 sessions / 540 segments**, **124,787,149 physical RX frames** and **3,134,371 controller updates**. All route results and all four variant TX-stream hashes are identical to the final validated prototype. Each variant has **2,004,203 configured generated TX accepted and zero rejected**. Default-off, below-60 mph and 40–50 mph streams remain identical. All 12 controller methods are AST-equivalent to the validated prototype, allowing explicit `zip(strict=False)` and normal package imports.

The exact original recorded-timing check processes 5,881,370 RX frames and 99,445 configured recorded TX. Candidate changes 110 encoded steering packets, including 28 in the reported bend, and adds **zero native rejections**. The same seven historical rejects remain (six cancel, one steering after braking). The scene reconstruction changes 31/130 unquantized eligible bend frames and none of 1,567 active 40–50 mph frames. Reference reconstruction matches recorded wire within half a step.

These are frozen-motion command and native-hook checks, **not measured handling improvement**, lane-clearance proof or full physical bus validation. The Mac debug safety library is unsanitized. Separate ARM/AGNOS build/boot, hardware timing, powered parked checks and road evaluation remain necessary before claiming device or road acceptance.

## Build results

Both normal incremental Mac SCons targets pass (`--minimal -j4` and development `-j4`). The complete project-scoped parent suite passes **1,018 tests / 343 subtests**, with **86 skips and one expected failure**. The complete child suite passes **3,953 tests / 24,673 subtests**, with **1,690 skips**. The local Panda SCons target passes, including H7 recompilation at the final commits. Both openpilot build targets also pass again at the final paired revisions. Scoped Ruff and whitespace checks pass. Independent review found no important actionable issues.

These are full configured targets and suites in the existing checkout, not clean-room rebuilds. Build/test failures from the test-import isolation issue are retained and explained rather than counted as passing runs.

## Build and source receipts

- [Build and full-suite results](../../navigator-reference/PRIVATE_ARTIFACTS.md), [post-commit builds](../../navigator-reference/PRIVATE_ARTIFACTS.md), [paired commits](../../navigator-reference/PRIVATE_ARTIFACTS.md), [verification](../../navigator-reference/PRIVATE_ARTIFACTS.md).
- [Independent source review](REVIEW.md), [test isolation diagnosis](TEST_ISOLATION.md), [scoped lint](../../navigator-reference/PRIVATE_ARTIFACTS.md), [method equivalence](../../navigator-reference/PRIVATE_ARTIFACTS.md).
- [Fresh corpus replay](../../navigator-reference/PRIVATE_ARTIFACTS.md), [source snapshot](../../navigator-reference/PRIVATE_ARTIFACTS.md), [scene](../../navigator-reference/PRIVATE_ARTIFACTS.md), [exact recorded native timing](../../navigator-reference/PRIVATE_ARTIFACTS.md).
- [Preserved starting heads/settings/source hashes](../../navigator-reference/PRIVATE_ARTIFACTS.md) and `backup/` copies permit reviewing the exact starting state.

The new actual producer/card test is subprocess-isolated because importing process modules in the suite parent leaked cached live-mode startup into later forked replay tests. The integration pipeline plus formerly blocked radar replay passes together; no runtime workaround was added. Interrupted diagnostic runs are retained separately from the final complete run.

No publication, Comma contact, parameter writes, installation, reboot, firmware flash or physical CAN transmission occurred. Paired commits remain local.

Final preservation/source/pin checks pass after the commits. The first final-Panda invocation omitted the virtualenv ARM-toolchain PATH and failed before compilation; `post-commit-panda-final.log` records the successful repeat with the established build environment. No source workaround or package installation was needed.
