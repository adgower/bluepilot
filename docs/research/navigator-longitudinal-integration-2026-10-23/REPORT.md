<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Paired Ford longitudinal integration — October23,2026

**Local integration and full configured Mac build/test checks passed.** Both `codex/navigator-tracking-release` branches are committed and clean, with a matching parent gitlink:

- openpilot: `ffebc43497f8015c37be5927800832f2719c7dca`
- opendbc: `0ac9618972dd580281c5e933c7990f186522fbd4`

No push, Comma access, OS/firmware installation, parameter change or active ECU query. Owner **1.20/0.97** mapping is unchanged. This is local build/replay evidence, not ARM/device/road acceptance or a proved shaking/fuel/OEM-equivalence result.

## Integrated behavior

Reviewed Expedition/Navigator Alpha-only handoff withdraws propulsion while braking and bounds resumption. Qualified release resolves the reproduced near-cruise0.2request cap versus old>0.3brake-latch deadlock, including actual stopping→pid restart. Positive raw and pitch-adjusted demand must exceed0.02for60ms; negative net braking immediately relatches. Invalid pitch/data/time preserve prior latch and withdraw propulsion; invalid acceleration holds processed brake output without repeating creep compensation and neutralizes on disengagement. Main exploratory propulsion rise0.5m/s³ and20msbrake-clear qualification retained.

Child adds two standalone helper modules and three test modules. Parent adds a real LongControl/controller-wire integration regression and pins the child. Source cleanup from the reviewed export is limited to imports/local names, merged identical platform guards and helper docstrings. No steering algorithm, calibration, geometry, planner, PID, CAN builder or native safety change.84protected child files preserve exact pre-change hashes; all parent runtime source and Panda gitlink unchanged. These source facts do not establish physical handling/longitudinal behavior.

## Final checks

| Check | Result |
| --- | --- |
| Focused in-tree helper/controller/parent restart tests |33passed,20subtests |
| Changed-source Ruff + Git whitespace checks |passed |
| Configured incremental minimal Mac build |passed |
| Configured incremental full Mac build |passed |
| Full parent suite |1,022passed,87skipped,1expected failure,281subtests |
| Full child suite, fresh unsanitized native Mac debug hooks |4,456passed,1,690skipped,24,693subtests |
| Panda build |passed; artifacts only, no flashing |
| Independent integration review |no actionable findings |
| Exact pair/gitlink, clean checkout and preservation |passed |

The first parent-suite attempt stopped at10PermissionErrors creating normal OpenpilotPrefix test directories under the filesystem sandbox. Its log/results are retained. The complete suite was rerun with normal local test-directory and IPC permissions, preserving prefix isolation. No HOME/shared-root override, test skip or production workaround was introduced. The table describes the final complete run; initial failure remains auditable. Builds use the existing configured environment and incremental cache; this is not a clean-room rebuild or sanitizer proof.

## Production/prototype replay equivalence

Fresh original Alpha extraction, frozen recorded inputs/synthetic100Hz clock: **5,967controller updates,2,984ACC and3,889non-ACC messages exactly match** the frozen reviewed export; returned actuator accel/gas/curvature/angle also match. Both stream hashes are `0dc21b2be8ee9b62380673a0162a852c71bdce81499ef8f04533cea36f90620e`.

Recorded-RX/actual-ACC-slot replay: **239,195RX frames per variant,2,983send slots**, zero RX rejects and valid RX configuration at all TX slots. Integrated production and frozen export match packet bytes and acceptance on every slot. Native permission is not forced. Original recorded packet, baseline, frozen export and integrated candidate each have2,982accepted/one rejected at+48.859173s: driver brake pressed/native permission false while recorded longActive remains true. This is the preserved cancellation boundary, not an added candidate rejection. No relay fault.770packets differ from the old uncorrected baseline in this actual-slot replay; no added rejections.

Limitations: timestamp-sort of934out-of-order adjacent logged pairs, reconstructed50Hz frame phase, explicit initial accel/latch seed, selected past-only state/control≤100ms. RX/timer/tick are exercised; longitudinal TX only. This is not exact full application scheduling, full contemporary steering-context, forwarding/heartbeat/hardware or altered vehicle-response simulation. The prior broader steering evidence is retained through unchanged source and existing suites, not claimed as a fresh whole-corpus integrated drive replay.

## Next stage

Local integration/build gate is complete. Before any road evaluation: separately publish the exact pair, preserve/verify device backup and settings, fresh ARM build/offline acceptance, then ignition-off and powered stationary checks. No authorization for those actions is inferred here from this local-only task. Alpha remains unchanged by this work. The earlier low-speed-first test plan applies after validated installation; no80–85mphshaking reproduction is requested.

Hydraulic release, grade rollback/hold, physical restart, acceleration-lag tradeoff, vibration recurrence, repeated stop/go and fuel economy remain unverified. The0.02/60msnoise qualifier and0.5positive rise are explicit experimental choices, not final OEM-derived calibration. Current integration trusts the standard live CarControl packet/timestamp path; the helper cannot independently establish source orientation sensor age.

## Evidence

[Pair](../../navigator-reference/PRIVATE_ARTIFACTS.md), [build results including initial host failure](../../navigator-reference/PRIVATE_ARTIFACTS.md), [parent suite](../../navigator-reference/PRIVATE_ARTIFACTS.md), [child suite](../../navigator-reference/PRIVATE_ARTIFACTS.md), [Panda](../../navigator-reference/PRIVATE_ARTIFACTS.md), [focused tests](../../navigator-reference/PRIVATE_ARTIFACTS.md), [equivalence](../../navigator-reference/PRIVATE_ARTIFACTS.md), [RX replay](../../navigator-reference/PRIVATE_ARTIFACTS.md), [preservation](../../navigator-reference/PRIVATE_ARTIFACTS.md), [review](REVIEW.md), [execution ledger](EXECUTION.md), [source design](../navigator-longitudinal-release-2026-10-23/DESIGN.md).
