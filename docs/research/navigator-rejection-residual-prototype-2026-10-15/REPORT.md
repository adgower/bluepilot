<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator: stale intent rejection and bounded turn-exit correction

Local prototype, 2026-10-15. Nothing on the Comma was accessed or changed. Installed paired source remains parent `74f66e7a0bf1dc0718431532948ece2c4fb0041c`, opendbc `1b965caadd4a6aea4d09985532bf7cca6c0873ca`. This folder is an offline adapter, not an installed or published branch patch.

## Why the 28.44 mph command was rejected

At saved-drive time 547.984205 s, the unchanged native Panda safety implementation rejects `0x3d6` because its advertised shadow curvature is stale. The angle request itself passes the path-angle rate/range and controls-permission checks. RX is valid and controls are allowed.

The previous marker encodes 1606, converted by the C integer scale to 80. The received pinion sample window is 187–200; the unchanged deviation check allows 86–301. The controller's current true clipped intent would encode 1975, converted to 98, inside that band. Thus the previous marker fails while the current intent passes. See [rejection trace](../../navigator-reference/PRIVATE_ARTIFACTS.md), [diagnostic source](../../navigator-reference/PRIVATE_ARTIFACTS.md), and [diagnostic log](../../navigator-reference/PRIVATE_ARTIFACTS.md). Diagnostic inspection covers the latest drive through 550 s; its duration field reflects the route extent, not processed coverage. Instrumented and original safety verdicts agree in that diagnostic window.

The original controller schedules steering at20Hz and regular markers at33Hz, but refreshes a marker immediately before steering only on coincident slots or a mode transition. [Synchronized controller](../../navigator-reference/PRIVATE_ARTIFACTS.md) supplies the truthful current marker immediately before each active Expedition/pinion angle command. It leaves actuation packets and inactive handoff ordering unchanged. It does not substitute measured curvature, relax Panda limits, or modify safety C.

## Reducing residual after aborted turns

[Limited correction](../../navigator-reference/PRIVATE_ARTIFACTS.md) retains the previous rising-demand admission and recovery veto, then caps the absolute accumulated extra path-angle command at `.001 rad*s` for a rising-demand episode. The cap remains in force through a later steady plateau. Temporary invalid context, cadence, feedback or driver interruptions suspend correction without replenishing the budget. Only demand falling to the existing `.001` floor or reversing sign starts a fresh budget. Pure steady weak-demand episodes retain the installed steady correction.

This keeps the early admission but limits how much extra command can enter a delayed response. It does not send opposite steering or pulse the steering mode. It preserves1.20/0.97, geometry, pinion calculation, existing feedforward and fade to zero by25mph. Sustained ramp assistance is intentionally smaller; a budget chosen from hypothetical plants may provide too little assistance on the vehicle.

The budget bounds the additional term before final range/rate limiting, not tire force, final actuator residual or an entire physical turn spanning multiple demand-floor/sign boundaries. A noisy or invalid demand boundary can rearm it. These boundaries need further validation before treating this as a deployable controller.

## Evidence and scope

Final corrected-code replay: six drives,89 segments,20,227,501 physical RX frames;322,306 configured TX accepted,zero rejected,zero required RX-invalid frames. Baseline accepts299,496 and reproduces one rejection at28.44mph. The prototype adds22,809 metadata frames across the dataset. Both source checkouts remain clean at the pinned revisions. All89 input hashes were checked after replay.

Final numerical results are in [summary](../../navigator-reference/PRIVATE_ARTIFACTS.md), [verification](../../navigator-reference/PRIVATE_ARTIFACTS.md), [full replay](../../navigator-reference/PRIVATE_ARTIFACTS.md), [unit tests](../../navigator-reference/PRIVATE_ARTIFACTS.md), and [300-case changing-demand screen](../../navigator-reference/PRIVATE_ARTIFACTS.md). The replay feeds recorded physical CAN into the original native safety library without forcing controls permission. All89 compressed input hashes are verified in [input manifest](../../navigator-reference/PRIVATE_ARTIFACTS.md); source, prototype dependencies and safety-library hashes are in [provenance](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The saved weak turn begins receiving extra command0.9473s earlier than the installed correction, at888.7800s rather than889.7273s, before driver input at890.0580s. This is command reconstruction from recorded inputs, not a prediction that the driver intervention would be avoided.

In the300-case assumed gain/lag/delay grid, the worst unit-gain increase in turn-exit excess falls from1.3270914 percentage points of peak requested magnitude to0.0076105 points, a99.43% reduction of that added residual. It is still nonzero. The plant is hypothetical and lacks an identified EPS model, outer planner, road/friction behavior and realistic noise. These figures are not a percentage improvement in actual steering. Original96-step and expanded210 stress screens are retained separately; their steady-input behavior is not newly improved by the ramp budget.

Recorded high-speed **actuation** parity excludes only `0x3ca` metadata: all remaining messages are identical at≥25mph, including≥45mph. Full CAN streams intentionally differ because metadata is refreshed more often. Default-OFF tracking matches the feedforward reference with the same marker fix, not the original unsynchronized stream. Additional marker traffic requires later hardware/bus timing validation.

Focused behavioral suite:51 passed. Native Ford suite:213 passed,79 skipped,12,063 subtests. Focused tests include inherited guards, marker ordering/actuation parity, integrated budget, negative demand, alternating40/60ms cadence, steady plateau and invalid-context re-admission. The review-discovered budget-reset bypass was reproduced with a failing test before correction; see [review](REVIEW.md).

## Remaining work

No road fix or hardware validation is claimed. Next work is reviewable paired branch integration plus assessment of marker frequency and actual residual after final command limiting. Any installation, parked acceptance or road comparison requires a separate device step; this task performs none.
