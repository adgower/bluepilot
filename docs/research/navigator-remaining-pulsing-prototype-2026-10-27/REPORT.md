<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Remaining longitudinal pulsing: local prototype and full replay

**Pulsing is not fixed. Reject this prototype as a pulsing treatment.** The narrow pending-pressure withdrawal role never activates in the saved corpus. All 903,645 consumer outputs, wire packets, raw requests and callback integral histories remain identical. No integration or installation is recommended.

## Boundary diagnosis

The installed road observations remain 14 / 14 / 12 brake-bit changes in the three named 53 / 40–50 / 58 mph windows. Current-source coupled reconstruction yields 14 / 15 / 12, all active; the 40–50 difference is disclosed rather than presented as exact road reproduction. Its raw-request error against recording has median 0.00156, p95 0.01848 and maximum 0.05261 m/s². Original recorded state, pose, torque and driver response remain frozen; the hidden consumer receive order is not logged.

The relevant boundary is producer → grade-adjusted allocation → observed release → returned integral authority. The nominal controller uses brake-entry net acceleration below zero and release above +0.3. Its qualified release gate can release an ongoing request much earlier: positive raw/net above +0.02 for 60 ms. Recorded falling edges often have net +0.027 to +0.063; brief reentries occur near −0.001 to −0.03 before measured pressure clearance. That creates a much narrower effective release/reentry band than the nominal +0.3 suggests. It is a software mechanism consistent with the observed command cycling, not proof of its physical cause.

In the 40–50 window the planner target stays +0.145..+0.551 and producer +0.214..+0.503 m/s² while effective grade compensation is negative and I changes −0.103..+0.170. Positive producer intent alone cannot justify removing downhill braking: actual acceleration also varies, and many full-brake rows have positive target-minus-actual error. Saved OEM evidence remains observational. Software applies gravity to bit selection while keeping the transmitted acceleration separate, consistent with its comment that the PCM compensates acceleration. **Ford ECU internal grade/pressure semantics and the necessary physical brake effort are not identified by this replay; software inspection does not rule out an ECU compensation interaction.**

Across active 40–70 mph session08 callbacks there are 13,570 full-brake rows: 7,534 `budget_reference`, 6,019 `strong_reference`, and 17 others. Of 1,614 positive-raw/positive-target rows with weak net −0.05..0, **1,600 already have a locked shared account**. The other 14 are committed/invalid-entry cases, not free permission to restart the account. This explains why extending a weak-entry-only path cannot resolve most full-brake cycling within its present constraints.

[Recorded boundaries](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Coupled boundaries](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Isolated experiment

[prototype.py](../../navigator-reference/PRIVATE_ARTIFACTS.md) and [standalone local patch](../../navigator-reference/PRIVATE_ARTIFACTS.md) add a distinct pending-pressure withdrawal role, only for an existing weak precharge-only decision. It never overrides a full-brake, strong-demand, committed or spent-budget reference. The installed **same** 0.01 demand-area / 0.3-second account remains authoritative; no independent account, reset or earned-rearm bypass exists.

Entry requires valid active 40–70 mph scope, positive raw/target, weak net above −0.05, no pedals/FCW, current protocol/target and fresh valid measured torque. Unlike the existing clear-entry coast lease, this role may retain an already-pending ordinary release. It invokes the original restart/release observer without resetting its timeout origin, clear samples, pressure history or debt. Freshness/reversal, ordinary timeout and three distinct clear readings remain required. It returns propulsion permission false throughout withdrawal. Strong/FCW/invalid scope falls straight back to the installed decision.

The existing installed clear-entry path is the within-contract control. The experimental extension has **zero activations** across the entire saved corpus and therefore changes nothing. Synthetic activation demonstrates its contract plumbing only; it is not evidence of a useful treatment. No further budget widening, release-margin increase, threshold swap, gravity removal or integral erasure was attempted. Earlier downhill-off/BP-threshold experiments already failed; those rejected hypotheses were read, not repeated.

## Complete software comparison

Fresh baseline and candidate cover **316 unique segments / 23 routes**, comprising all prior 237/14 plus all nine newly saved sessions/79 segments. There is no original-segment hash overlap. Six new sessions predate the update; only session08 supplies meaningful installed-source assisted exposure. They are not all labelled V3 road evidence.

Both variants process **903,645 consumer callbacks** and recompute **1,725,152 producer steps**. There are 304 segments without active atomic-input gaps. One retained historical 12-segment route has five missing active-prefix inputs and remains diagnostic-only, not a gate-clearing route. Two consumer clocks have no corresponding saved consumed control and are omitted in both variants: one recorded-inactive alpha prefix and one recorded-active prefix in the already-diagnostic route. There are zero future-publication skips. No replacement control is fabricated. Inactive fallback and absent streams are disclosed. Session09 has no longitudinalPlan/deviceMotion and zero active callbacks: a separately versioned resume processes its 421 inactive callbacks after the original runner raised KeyError. Both original 315-segment runs end with that error; the complete result is explicitly a verified resume, not a single exit-zero execution. See [execution receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md).

| Software gate | Baseline → candidate |
|---|---:|
| Changed wire/raw/gas/I at consumer callbacks | 0 |
| Changed fault history / lost or gained activity | 0 / 0 |
| Full-brake bit changes | 2,463 → 2,463 |
| Full-brake exposure | 4,519.896 → 4,519.896 s |
| Brake/precharge union exposure | 4,612.005 → 4,612.005 s |
| Weaker strong-target raw/encoded rows, 55,593 checked | 0 / 0 |
| Lost weak-target brake / weaker weak-target raw | 0 / 0 |
| New gas under commanded brake/precharge or retained torque | 0 |
| Changed disabled/inactive outputs | 0 |

The two old timeout histories remain exactly equal: historical diagnostic session01 at 63.515 mph / +91.538 s and session02 at 69.713 mph / +458.271 s. There is no new timeout in session08. These are not assertions that every historical timeout cause is solved.

| Protected fixture | Brake changes, both variants |
|---|---:|
| City 25 mph | 17 |
| Original 63 mph highway | 20 |
| Newer 20-second highway windows | 20 / 12 |
| Previous latest highway windows | 17 / 14 / 12 |
| New session08 53 / 40–50 / 58 mph windows | 14 / 15 / 12 |

The two retained earlier rolling high-RPM fixtures remain at peaks 1.751 / 1.753, latest first-gear restart 1.561 and normal stopped launch 1.440 m/s²; all gas/brake and request timing is unchanged. No fuel, RPM, shift, comfort or stopping-distance improvement is inferred. The callback audit does not independently hash every recomputed producer step; it checks every consumed callback's raw/I/freeze/phase and both complete wire streams.

[Full comparison](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Supplemental audit](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Input/cohort/dedup audit](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Tests, native replay and limits

The first two pending-role tests fail against installed behavior; the final **11 focused checks pass**, including shared spent/deadline fallback, signed weak withdrawal, unchanged ordinary release origin, timeout still firing, stale pressure, mid-owner changes, disabled-owner reset and no propulsion while establishing clear readings.

The full Ford test directory under the prototype passes **1,033 tests and 75 subtests** with freshly compiled unsanitized native hooks. The initial default hook build produced 54 failures / 1,015 passes / 39 passing subtests because macOS refused its UBSan runtime; that failing log remains. The successful rerun preloads the ordinary debug build. This is not a claim of a passing entire openpilot suite, UBSan, ARM or hardware validation.

Fresh native saved-traffic replay completes **316 segments / 23 routes / 903,463 replacement ACC slots** with original RX, non-ACC TX and timers. Baseline/candidate each have 205 TX rejections; **zero added rejections and zero relay faults**, with no forced permission. Native acceptance cannot turn an inactive prototype into a comfort improvement.

[Native summary](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Native provenance](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Focused results](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Ford directory results](../../navigator-reference/PRIVATE_ARTIFACTS.md)

Paired sources remain at parent `e05e42f43` / child `5097b993`; protected source hashes were checked before and after execution. Only this research directory and task-specific private caches were written. No SSH, network/device operation, source integration, commit, push, setting/service, calibration, OS, firmware or CAN transmission occurred. Owner 1.20/0.97 is preserved. Remaining work requires an explicit actuator-response identification/model and joint producer/allocation design that preserves needed braking and clearance; the present weak account cannot be enlarged merely to obtain fewer edges.


## Concrete next local design

The zero-change constraint is precise: the new role may withdraw only an **already-admitted precharge-only** request; 99.1% of the positive weak full-brake rows already have a locked shared account, while most other full-brake rows use the strong/reference path. Reopening those accounts would increase the authorized deferral. Holding the brake until a larger positive release margin would instead increase brake exposure. Neither is a valid success shortcut.

The saved extractor retains gear actual/target/engagement (374), engine RPM/quality (516), received brake/precharge status (531), measured and arbitrated brake torque (125), wheel propulsion torque actual/request (359/512), pose/grade and actual/target acceleration. These can identify **observed conditional** request-to-status/torque transition intervals and separate gear changes from no-shift events. They cannot identify the pressure/propulsion response to an unissued sustained coast command, exact ECU packet consumption, hydraulic pressure or ECU internal grade compensation. Recorded response belongs to the recorded command; it must not be substituted as a counterfactual plant when the command changes.

This builds on the existing [gear/grade/coast investigation](../navigator-gear-grade-coast-2026-10-25/REPORT.md), rather than restarting it. That work already fitted observational net-response models, reviewed 277 brake-release episodes and rejected a support-gated valid-propulsion bridge: brake edges increased 992→1,008 and 430 later strong-demand requests became weaker. Its held-out Alpha net-request RMSE of 0.0849 m/s² beat added/subtracted-gravity alternatives at 0.2026 / 0.1433. This supports further testing of ECU compensation semantics; it does not justify naive gravity removal. Another gear table or repetition of that rejected bridge would not fill the missing capability.

The **new** capability needed is a validated dynamic transition model, with whole-session held-out transition tests and explicit unsupported regions for Alpha no-brake/inactive-propulsion. The prior settled-input selection yielded no qualified Alpha windows in that mode and zero strict isolated coast steps; its zero fitted added lag therefore cannot identify transition dynamics. The model must also include integrated returned authority and subsequent integral/recovery history, carrying the rejected bridge's later strong-braking divergence as an explicit regression, rather than validating only the coast instant.

The next bounded local artifact should extend those retained fits into a response-state model with explicit drive, brake, precharge and pending-release transitions, trained and held out by complete session/episode with separate gear/grade regimes and declared unsupported regions. First reproduce observed 531/125/359 timing and actual acceleration error in unchanged-command episodes; preserve uncertainty bounds instead of extrapolating a never-observed coast response. The resulting allocator contract should take target-minus-actual acceleration, cumulative actual speed error, grade and fresh measured actuator state as separate inputs, rather than interpreting positive raw demand alone as permission to remove downhill braking. It needs one shared signed deficit account, an immediate strong/stop/FCW path, truthful returned authority and the original independent measured-clearance/timeout barrier. Only a modeled, supported weak transition may spend that account. Unsupported or unidentifiable response uses the exact installed reference. A coupled synthetic plant can then test whether the revised joint producer/allocator settles without cycling; recorded replay still supplies the complete software regression gates, not physical comfort proof.

Source anchors: [grade/bit selection and admission](../../navigator-reference/PRIVATE_ARTIFACTS.md), [qualified positive release](../../navigator-reference/PRIVATE_ARTIFACTS.md), [shared sampled-demand account](../../navigator-reference/PRIVATE_ARTIFACTS.md), [ordinary producer error/integral](../../navigator-reference/PRIVATE_ARTIFACTS.md).
