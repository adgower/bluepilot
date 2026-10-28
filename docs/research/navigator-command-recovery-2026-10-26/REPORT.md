<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Command recovery and local-constraint anti-windup — October 26, 2026

**The final local candidate clears the previously added 20.6 mph/61 mph timeout and weaker strong-braking replay regressions. Highway pulsing remains unresolved.** The paired branches and Comma are unchanged, with steering 1.20/0.97 preserved. This is an offline candidate, not an installed or road-validated fix.

## What caused the failures

The previous recovery account measured omitted increments, not the complete change in native integral and actuator-mode history. Its first positive crossover in highway-pulsing-session-02 occurs at producer-relative1455.638s: the candidate adds0.001 to I while0.17986 remains pending, overtaking reference. About26seconds later it waits for pressure clearance while reference continues braking, then faults at20.5901mph. Empty debt did not imply command-state recovery. Evidence: prior-first-positive-crossover.json and the previous report.

The first new design removed synthetic I repayment and used a bounded reduction of positive rolling-restart demand. This removed both added timeouts and large weaker-braking differences, but the full replay still found106one-increment weaker encoded strong-braking samples (24maneuver-followup-session-02,82alpha-comfort-session-01).

Their first divergence exposes a second cause: the reduced command reaches unlimited-drive feedback earlier, while the native producer still wants its higher unreduced request. It integrates positive error when the reference is still ramp-limited. Tiny persistent I differences (+0.000345/+0.002989) then cross packet quantization boundaries. See residual-first-crossovers.json. No artificial repayment causes this second failure.

## Final local design

- Retain the narrow moving-restart qualification: prior movement, fresh low-speed braking, then positive limited engine-ramp demand at0.3–3m/s; actual-stop launches are excluded.
- Accumulate a transient negative command reduction from eligible native positive growth, maximum0.25m/s² and three seconds of rolling admission. Observed maximum0.249130. Do not replace, copy or reseed native I and do not maintain a baseline-controller output oracle.
- Apply reduction only to positive requested propulsion with positive planner target and fresh valid same-owner protocol feedback, valid CAN/atomic source, no pedals or urgent/stop demand, no brake/precharge/reference-brake, and numerical nonnegative gas authority. Never turn positive output into negative demand; the0.02positive floor prevents that.
- Unwind reduction only with fresh unlimited-drive feedback at3–12m/s, maximum0.1m/s³ and0.001per update. Real PID reset clears it. Clock/epoch/sequence discontinuity invalidates it without resetting native I. Invalid-input native fallback is not a comfort guarantee.
- **Account for the local output constraint in anti-windup.** Alongside the installed actual-actuator freeze, freeze positive I growth while its own reduction is active at3–12m/s and unreduced wanted demand exceeds actual numerical gas by the existing0.011resolution. Require valid context, positive error/target and no braking/precharge. Negative-error integration remains available. No feedback fields or pressure permission are fabricated.

Native state transitions/PID mechanics and real feedback remain in use; positive-growth freeze now acknowledges both actuator and software output constraints. This is explicitly different from the initial transient-only native-integration variant. It adds no integral repayment, release timeout, pressure-clearance exception, planner change, CAN range change, protocol field, steering or geometry adjustment.

## Full controller replay

All **197segments /12routes /570,269callbacks** processed. Hash-bound inputs and source bindings are checked.185segments have no active atomic-input gap. One12-segment route contains five missing active prefix inputs and remains diagnostic-only; incomplete rows do not clear a gate.

| Gate | Final result |
|---|---:|
| Added release-timeout events | **0** |
| Lost/gained active callbacks | **0 /0** |
| Weaker raw strong-target requests | **0** |
| Weaker encoded strong-target requests | **0 /33,194 checked** |
| New positive-gas rows with fresh retained torque | **0** |
| Moving gas with retained torque | **0** |
| Gas under commanded brake/precharge | **0** |
| Disabled-owner wire changes | **0** |
| Command reduction remaining at route end | **0 for every route** |

The previous20.6mph and61.23mph episodes now remain in actual braking, without fault. At their old fault instants, candidate raw demand is respectively0.004099 and0.001212m/s² more negative than reference. No timeout or pressure gate was disabled. Evidence: old-timeout-regressions.json.

Two **preexisting reference** release-timeouts remain unchanged at63.52mph and69.71mph. This candidate does not resolve every recorded controls-mismatch cause.

This is not a proof that all post-recovery history is identical or globally bounded: I still follows changed feedback. The explicit audit observes post-overlay I differences from−0.053825 to+0.013960 across eligible complete rows. The formerly failing20.6mph route has−0.004099 post-overlay difference instead of the old~+0.1803. All declared strong-braking and timeout gates clear in the saved corpus. See post-recovery-audit.json.

## City, restart and highway regressions

| Fixture | Reference | Final candidate |
|---|---:|---:|
| City25mph brake changes |17|17|
| City brake-command exposure |21.5329s|21.5329s|
| Original63mph highway changes /15s |20|20|
| Newer highway window1 changes /20s |22|22|
| Newer highway window2 changes /20s |12|12|
| Earlier high-RPM rolling window peak raw request |2.000|1.751|
| Latest high-RPM rolling window peak raw request |2.000|1.753|
| Normal stopped-launch peak raw request |1.440|1.440|

Entire named city route wire output is byte-identical. Normal stopped launch is unchanged. Earlier rolling-window brake exposure grows1.940→1.978s; latest remains1.100s. Actual RPM, gear, motion, planner and torque are frozen, so lower requested propulsion does not prove better shifting or physical smoothness.

Across the common-active corpus, brake changes remain1434→1434 and brake-command exposure rises2528.025→2532.374s (**+4.349s**).22,383wire rows change. This is not a demonstrated comfort improvement: stronger/longer braking is a material tradeoff requiring further review and eventual controlled response evidence. Do not advertise this patch as highway smoothing.

**Named highway pulsing regressions are unchanged.** Coherent anti-windup clears the rolling-recovery regressions; it has not fixed highway coast/brake cycling. Do not copy these claims across to coast-response or planner experiments.

## Verification and scope

58focused tests pass: qualification, deadline/budget, actual PID integration, same-feedback signed recovery, local output-constraint anti-windup, brake/urgent suppression, stale/invalid owner data, rollback and independent encoded-braking comparison. Red tests are retained. Independent review reproduced the sequence rollback gap, verified its fix and the added local-constraint freeze; no further concrete focused finding.

Fresh native replay completed all197segments: 570,178 replacement ACC slots; 45,641,383 original RX with zero RX rejections; reference/candidate TX rejections 134/134, **zero added TX rejections or relay faults**, no forced permission. Original non-ACC TX and timers retained. Full native results and receipt: native-summary.json, native-recovery-results.json, native-source-provenance.json. Native acceptance does not establish physical clearance or comfort. Debug native hooks, no sanitizer/hardware/ARM validation is claimed here.

Source remains clean at parent2ca969e45afee229d7ec5c03c8768e137410c8d1 /childbcd706d02fd6b8159b1eadcb6b2a56b504f69567.1.20/0.97 unchanged. No integration, push, SSH, device settings, install, reboot, CAN, OS or firmware action. The earlier broad guard remains uninstalled. The new candidate is retained separately from rejected account and transient-only variants.
