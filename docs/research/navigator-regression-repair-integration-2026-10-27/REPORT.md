<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Paired regression repair integration — October 27, 2026

Committed local pair **openpilot `e05e42f43d2907a4f02915a924cfd95a46197e79` / opendbc `5097b993965b2b65ea3fcca7e3769cfa9403d49c`**; parent gitlink matches, both checkouts clean.

Local integration on both existing `codex/navigator-tracking-release` branches. No publication or device activation is authorized or performed in this task. Original bases: openpilot `df788e02719c05595dab2f980e6fd9fb9e464006`, opendbc `1d29e6e78abcbf5c6a80eb397d80b349c6cca960`.

## Integrated behavior

- Production signed-coast allocator and clearance obligation reproduce the accepted signed-coast prototype. Actual brake/precharge flags remain truthful; inactive gas, bounded trial age/debt, three fresh post-coast clearance observations, original timeout and urgent/owner guards remain. Protocol v3 explicitly negotiates this behavior; old/unknown metadata selects nominal fallback. Ordinary ramp integral margins remain unchanged.
- Midrange steering admission uses independent elapsed-time wheel/body evidence and stable targets, directional entry/continuation thresholds and adjacent target-jump release guard. All existing Navigator opt-in prerequisites remain. Existing mapping owners and specialized baseline policies are retained; no recursive runtime monkeypatches.
- New-drive producer-clock repair freezes the secondary pose subscriber before sampling the common producer clock; publishing cannot drain a newer source afterward. Replay retains its original carState clock. Genuine future, stale, unhealthy and primary-invalid input still fail closed; no freshness limit or source timestamp is relaxed.

Owner **1.20/0.97**, geometry, other lateral implementations, native safety sources, models, firmware, launch behavior and opt-in defaults are unchanged. `source-scope.json` audits all tracked source changes against the two original bases. Device settings were not written.

## New current-install drive evidence

[Read-only download and analysis](../navigator-latest-mismatch-review-2026-10-27/REPORT.md): 14 newly completed segments, 118,848,626 bytes, two moving sessions. Hash/size deduplication and before/after device audit passed; the original installed pair remains unchanged.

One controls mismatch was preceded by a healthy pose source **93,749 ns newer than its producer clock**, sequence29270 near20.4mph. The next command was valid. Panda permission loss followed the coordinator fault, rather than initiating it. This explains this particular mismatch; it does not establish every historical mismatch has the same cause. The exact timestamps and real producer-cycle ordering are regression tested locally.

Below40mph pulsing is confirmed by actual outgoing ACC brake bits and received torque, not only allocator phase labels: session02 +160–175s at20.62–24.59mph has **14 brake-bit changes** and14 received torque hysteresis changes. Planner acceleration changes sign while raw demand remains positive and integral/grade terms contribute. No positive outgoing propulsion with brake/precharge overlap was observed in the qualified windows. Physical pulse reduction from the new candidate is **not established**; retain this window as the next road/replay regression.

## Verification status

Minimal/full Mac builds passed. Full parent suite: **1,107 passed,87 skipped,1 expected failure,281 subtests**, one existing capnp repeated-write warning. Initial parent-suite failure is retained separately: older test fixtures used protocol v1 where production-current metadata was required, and an older publication-only fixture expected polling at the old boundary. Fixtures now retain explicit legacy fallback tests and model the new clock boundary. Two inherited child signed-precharge fixtures also hardcoded v1 while asserting current-peer validation; these now use the current protocol constant. Initial child failure log is retained. Production behavior was not weakened to satisfy tests.

Full child suite: **4,733 passed,1,690 skipped,24,693 subtests**. Panda build passed. Native hooks were freshly built from current source without sanitizers on this Mac; no sanitizer or hardware claim.

Production longitudinal replay matches the accepted prototype exactly across **14 drives /237 segments,685,504 consumer callbacks and ACC records,1,311,408 producer records**. All exposed command/feedback/fault/counter fields match. The same **two** historical release-timeout disengagements remain; zero additional faults. Of the237segments,225 have complete active input coverage and12 are diagnostic prefix-gap evidence. Retained native artifact hashes,34safety headers/native C and exact ACC streams establish applicability of prior native replay; **no fresh route-native replay** was performed. The new producer clock fix is independently tested at the real state_control/publish boundary and is outside this frozen-loop replay.

Postcommit minimal/full/Panda builds passed at the exact paired SHAs. Full steering port comparison passed **33 routes /658 segments /3,814,069 recorded controller ticks /762,827 scheduled steering calls per variant**. Verified prototype and production results/admission states match on recorded and calibration-fixture streams (3,051,308 computed strategy calls total). All658raw input hashes and route tick counts match retained evidence. This includes841recorded and1,413fixture admitted frames, not only inactive policy output. Constructor/alias state, context update logic and20 inherited lateral/wire source hashes were checked. The earlier21segment every-tick parity is retained as unscheduled diagnostic evidence; final proof uses actual `STEER_STEP=5` scheduling.

Steering-native evidence is inherited through input/source/strategy parity and graph/context checks; this is **not** a new658segment native or full combined paired-controller replay. New native unit suites, longitudinal frozen controller replay and scheduled steering parity are distinct evidence. No ARM/device/parked/road proof is implied.

Independent review found no actionable runtime defect; optional actual-cycle invalid/future/stale/replay cases were subsequently added and passed. Both paired checkouts are clean. `VERIFICATION.json` binds final artifacts and asserts exact heads/gitlink, source scope, all build gates and both replay totals. See `build-results.json`, `paired-commits.json`, `longitudinal/VERIFICATION.json`, `steering/` and `REVIEW.md` for inspectable evidence.

Mac tests/replay do not establish ARM startup, physical brake clearance, comfort, lane tracking or road safety. No additional drive is required or requested by this local task.
