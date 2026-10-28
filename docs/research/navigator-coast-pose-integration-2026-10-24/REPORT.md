<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Coasting and pose integration — October 24, 2026

The coasting and pose-expiry fixes are integrated and committed locally on the paired `codex/navigator-tracking-release` branches. Full local builds and suites pass. No push, device contact, installation, parameter write or OS/firmware update occurred. Owner **1.20/0.97**, steering/geometry source and existing brake-clearance protections are preserved. The quiet-release experiment is excluded.

## Integrated behavior

**Child:** `BoundedCoastAdmission` replaces the prior weak-entry admission constructor for the existing Navigator coordination path. Brief weak residuals can retain clear propulsion rather than repeatedly resetting its handoff. Persistent residual demand still admits braking at the sampled signed-demand/time bounds. Outside the existing eligible, fresh, clear, moving-PID scope, baseline admission remains. No meaningful-braking, measured-clearance or timeout bypass is introduced.

The experimental thresholds remain 0.01 m/s signed residual-demand integral and 0.3 seconds from the first observed negative sample. Sampling permits a debt increment of less than 0.002 m/s and up to one eligible callback beyond the deadline. These are software decision bounds, not physical speed-error or stopping guarantees.

**Parent:** an independent pose subscriber/calibrator is created only for the enabled Navigator/Alpha coordination path. If the published pose would exceed 100 ms at consumption, the helper can recover a copied command using a coherent fresh snapshot. It retains producer identity/timestamp, invalidity, reference validity, source chronology and lateral calibration/actuator fields. Reusing a previously measured source does not restamp or extend it. Ordinary healthy commands retain the existing path, except for maintaining monotonic consumption after recovery.

Live integration captures the clock after subscriber drain and after calibration work, revalidates source/producer age, and shares that final timestamp with tracking context and `CI.apply`. Actual constructor, replay-mode consumer and live fake-clock consumer tests cover this lifecycle. The single-drain frozen snapshot prevents a second read from changing data after validation.

## Verification

| Gate | Result |
|---|---|
| Minimal Mac build | Passed |
| Full Mac build | Passed |
| Entire parent suite | 1,059 passed, 87 skipped, 1 expected failure; 281 subtests passed |
| Entire opendbc suite | 4,570 passed, 1,690 skipped; 24,693 subtests passed |
| Panda compilation | Passed |
| Changed-file lint and diff checks | Passed |
| Four-drive actual-source controller replay | 247,765 extracted callback rows exactly match the accepted prototype |
| Native recorded traffic comparison | No added integrated rejections or relay faults |
| Independent review | No remaining blocking findings |

The initial sandboxed parent attempt could not create temporary `.comma` test directories. The authorized host test run reached the changed tests. Two existing constructor-bypassing fixtures needed the newly required isolated consumer state. Three child admission assertions encoded the superseded withdrawal/short-qualification policy; they were replaced by propulsion-continuity and bounded eventual-admission contracts. Existing legacy admission and clearance tests remain. The complete parent and child suites subsequently passed. No runtime change was made merely to suppress those failures.

## Replay scope and outcomes

The integrated class matches the accepted coasting prototype AST. All four fresh actual-source replay traces match the final accepted pose/coasting prototype across 247,765 callbacks. The optional live-clock integration is separately exercised by permanent consumer tests; saved replay uses the recorded deterministic callback clock.

Native replay processes **19,834,859 received packets and 597,172 transmitted packets per variant** across the four moving saved drives. It retains **349,435 original non-ACC transmissions** and substitutes generated ACC at **247,737 actual send slots**. Recorded, baseline and integrated variants use the original RX and native timers; permission is never forced. Baseline/integrated share **35 rejected transmissions** with **zero added integrated rejections** and no relay faults.

ACC substitution uses the latest preceding reconstructed callback within 40 ms; the observed maximum lag is 21.81 ms. Callback and transmit counts differ because of eligibility and send-slot mapping. This is broader than the earlier ACC-TX-only hook check, but it still does not model forwarding/heartbeat injection, changed vehicle response or physical braking. Existing reconstruction limitations, including partial first-route warmup and recorded parent fault reactions, remain.

The recorded 62 mph pose-expiry fault does not initiate in the integrated replay. All **four known release timeouts remain** at their original reproduced times. Their measured-clearance guard and fault deadline are unchanged. Integration does not claim to resolve those timeouts or prove physical comfort.

The earlier bounded-coast replay result—29.3% fewer command edges across available new 60–74 mph samples, with a worst selected 26→12 edge window—is a command-level finding, not a road comfort or fuel-economy result. No new 75–85 mph validation or lateral tuning is claimed.

## Preserved scope and next gates

The child `fordcan.py`, torque observer/restart guard, steering source and vehicle values retain their prior hashes. Resume packing remains unchanged, so this pair does **not** include the quiet-resume hypothesis. No new preference default or user-visible toggle was added.

Publication, isolated device ARM validation, parked checks and activation are separate future steps. No device/ARM/parked/road result is claimed for this pair. Release-feedback/ECU response and residual pulsing remain unresolved physical concerns.

Exact local commits and gate details: [validation receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md). Supporting artifacts include source-equivalence.json, build-results.json, parent-tests.xml, child-tests.xml, full-native-results.json, old-full-native-results.json and REVIEW.md. Raw saved routes/GNSS remain private.
