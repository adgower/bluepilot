<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Paired calibrated wheel-target/unwind integration

The accepted wheel-target/unwind prototype is integrated and locally committed on both `codex/navigator-tracking-release` branches. Parent `50baa6fd6acf9d37b7e0768e5736efab2a357ddc` pins child `0e65f296260ec16da3c3b814c10ac5f36f8b2e4c`; both checkouts are clean. Starting heads were parent `ff6ff263084a4bc433cf197b44ce3a31f7608851` and child `9d5a3d485085f36beeb9aff7baf53c0d4ea603ee`.

The child adds`lateral_angle_wheel_target.CalibratedWheelTargetReduction`and37prototype regressions with the corrected signed-error helper. The original`lateral_angle_high_speed.HighSpeedReduction`is unchanged and remains the separately advanced installed-policy baseline. The parent changes only factory selection behind the existing prerequisites/default-off`FordPrefHighSpeedTracking`key, updates the selection regression, and documents the paired change. No new key, UI control, producer or card plumbing is introduced.

The class is AST-equivalent to the accepted prototype apart from its exported name; every new test function and helper is also AST-equivalent. Owner1.20/0.97, geometry, fixed pinion, old controller, native safety source/library, parameter registry, card/motion adapter and historical device settings snapshot remain unchanged. The BluePilot workspace's prior dirty state is preserved. No fresh device inventory is claimed.

## Validation status

-139focused integration tests pass, including actual producer/card motion/calibration invalidation, default-off/prerequisite selection and all controller cases. Scoped Ruff and whitespace pass. Independent review found no important issue and independently passed49wheel-target/factory tests.
-Both configured incremental Mac SCons targets pass (`--minimal -j4`, development`-j4`). Full parent suite:1,018passed/343subtests,86skips/1expectedfailure.
- Full child suite: 3,990 passed / 24,673 subtests, with 1,690 skips. Panda target passes. All three incremental targets pass again at the committed pair. [Build results](../../navigator-reference/PRIVATE_ARTIFACTS.md), [post-commit targets](../../navigator-reference/PRIVATE_ARTIFACTS.md), [commits](../../navigator-reference/PRIVATE_ARTIFACTS.md), [preservation/equivalence](../../navigator-reference/PRIVATE_ARTIFACTS.md). Final committed factory/native corpus acceptance passes: see [replay acceptance](../../navigator-reference/PRIVATE_ARTIFACTS.md) and [final verification](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The first focused invocation omitted dependency roots from`PYTHONPATH`and failed in a subprocess importing`tinygrad`; the established full environment passes. The first parent-suite attempt hit sandbox permission errors creating its isolated`~/.comma<UUID>`directories; the successful rerun used the required local filesystem/IPC access, with no test-source workaround. Failed logs are preserved separately and not counted as passing evidence.

The previous prototype's637-segment/native checks establish frozen-input behavior only. Fresh integrated replay will use the actual parent factory for candidates and explicit unchanged installed controllers for references; otherwise factory selection on both sides would accidentally compare the candidate to itself. No Comma/ECU access, CAN transport, push, install, reboot or firmware update occurs in this task.

Local/native/build evidence does not establish physical tracking improvement, lane/tire clearance, ARM/AGNOS boot or road acceptance. The model-predicted near-edge path remains a separate unresolved issue.

Committed exact recorded-timing native check passes for both high-speed drives: 404 encoded steering differences, zero additional rejects, same 32 baseline all-TX rejects retained. Actual-factory send-time command tables match accepted prototype exactly across 83,978 rows. These are frozen-motion checks, not new measured handling improvement.

## Final committed factory replay

All **32 sessions / 637 segments** pass. All **128 whole-stream variant hashes** equal the accepted prototype, across recorded-context and separately labelled causal-calibration fixtures. This includes 3,704,143 controller updates per variant, 503 recorded-context / 558 fixture changed updates, zero changes at or below70mph (including40–50mph), and default-off whole-stream byte parity. Each variant accepts2,387,554configured generatedTXframes with zero rejected;11,829frames precede configuration. The32startup invalid-safety ticks per variant are retained, not counted as continuous RX-validity proof.

Candidates are created through the real parent factory; references explicitly use the unchanged installed controller. All workers agree on final source snapshots and paired HEADs. Protected source hashes remain unchanged and the parent pins the clean child commit. Fresh exact recorded-timing substitution retains the same32baseline all-TX rejects while adding none.

The pair is **locally committed only**. No push, device contact or installation occurred. Main planning status is updated in the BluePilot roadmap and feature inventory. Tests/builds are configured incremental Mac targets and suites; skip/expected-failure counts are stated above. Native debug hooks are unsanitized. No clean-room, ARM/AGNOS boot, physical bus, lane-clearance or road-handling acceptance is claimed.
