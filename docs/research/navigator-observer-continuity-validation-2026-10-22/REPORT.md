<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Observer continuity broader validation — October 22, 2026

Local offline validation completed. Paired branches and Comma unchanged; owner **1.20 / 0.97** preserved. This validates a revised highway prototype and replay timing, not physical steering improvement or deployment readiness.

## Result

- **71 recordings / 1,015 segments**, all saved input hashes verified; **5,805,897 controller invocations per variant** and 232,333,840 physical RX frames. Historical recordings provide regression coverage, not uniformly current-tune road evidence.
- Four independent native safety lanes: recorded reference/candidate and separately timestamped calibration-fixture reference/candidate. Controls permission comes from recorded RX; it is never forced.
- **No additional native rejection.** Each lane has the same 392 existing rejection events (348 button-address 0x83, 44 steering-address 0x3d6). Complete event lists, full rejection counts, generated TX counts and RX-invalid outcomes match for each route. These are shared baseline events, not zero absolute rejection.
- Recorded candidate changes 811 packed steering updates: 364 at 70–75 mph and 447 at 75–80 mph. Fixture candidate changes 892. Both preserve all commands below 70 mph and at/above 80 mph, including 40–50 mph. No phase/counter mismatch. All per-route source fingerprints match final source.
- **71 focused tests**, **6 timing transport tests**, and **196 timing/transition/abort scenarios / 15,680 frames** pass. Stress receipt matches the replayed candidate hash.

## Timing blockers resolved

The earlier harness invoked CarController on carControl publications. Card actually applies already-sampled inputs on vehicle cycles. The corrected replay invokes on every recorded sendcan event, including empty sends; it freezes deeply copied topic inputs at the preceding carOutput publication and associates the next carState. Steering phase/counter starts from recorded traffic. Original packets retain original publication clocks; synthetic fixtures use their own creation clock.

On the two current target drives, output-snapshot timing reduces baseline half-wire-step mismatches from 11 to 7 and 39 to 13. Across 38,867 active comparisons, **20 baseline timing mismatches remain; the candidate changes none of those frames**. It changes 43 and 125 other packed sends, respectively. Exact SubMaster receipt/application times are not logged, so bit-perfect whole-route reconstruction is not claimed. Historical corpus baseline mismatches are likewise not evidence of physical tracking errors.

## Candidate narrowed after broader evidence

The initial candidate modified existing policy history/shared low-speed budgets. Broader testing exposed low-speed boundary effects and six changes above 80 mph. That run was stopped and retained as failed evidence. The final candidate is an independent output overlay over untouched installed policy. It keeps source-ordered wheel observation, requires current confirmation from the actually selected production body observer, and retains withdrawal, slew, direction, provenance and driver guards. Combined trim is bounded by the existing 0.01 rad / 15% cap and 0.0003 rad/frame onset. Scope fades in at 70–71 mph and out at 79–80 mph.

**New low-speed actuation was withdrawn.** Original-target observation remains diagnostic. Existing low-speed commands/budgets are unchanged, and severe 23–24 mph clipping remains unresolved. The prototype cannot create authority beyond unchanged command headroom.

## Limits and next gate

Frozen-input native replay cannot demonstrate closed-loop damping, reduced lane error, EPS acceptance, or 80–85 mph stability. No ARM/device build, firmware action, publication, branch integration or installation occurred. Existing Mac debug native safety library was reused; no new sanitizer build is claimed. Default-off full-stream evidence is retained from the earlier two-target-route run, not rerun over this entire corpus.

Next is a separately authorized paired integration and build validation of this narrowed candidate, with exact implementation/provenance parity and retained rollback evidence before any device decision. Low-speed saturation needs its own diagnosis/design; this pass does not close it.

## Inspectable evidence

- [Machine-readable validation receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Full route results](../../navigator-reference/PRIVATE_ARTIFACTS.md) and [source snapshot](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Target timing review](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Timing stress receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Execution history, including discarded runs](EXECUTION.md)
- [Final prototype](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Evidence hashes](../../navigator-reference/PRIVATE_ARTIFACTS.md)
