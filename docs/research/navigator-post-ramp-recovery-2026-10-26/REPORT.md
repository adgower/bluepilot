<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Post-ramp recovery investigation — October 26, 2026

**Rejected after the full controller replay. Do not integrate or install.** The old 61.23 mph timeout is removed, but a new 20.59 mph timeout remains and encoded strong-demand braking becomes weaker elsewhere. Highway pulsing is unresolved. No Comma access or paired source changes were made; 1.20/0.97 remains intact.

## Diagnosis and prototypes

The earlier rolling guard's omitted-growth budget did not bound later integral divergence. At the 61 mph failure its integral was about 0.0616 higher than reference: different brake/release phases allowed different subsequent integration. This is a control-history problem, not evidence to extend a brake-release deadline.

Implemented an explicit recovery account with fresh same-owner drive feedback, positive demand, no driver pedals or urgent demand, and recovery only at 3–12 m/s. Recovery is capped at 0.1 per second, 0.001 per update, native integral capacity and available headroom. Negative-error recovery can only reduce an existing negative native increment. Positive recovery cannot bypass actual brake/precharge/limited feedback. Actual PID reset clears the account; ordinary moving qualification does not. New rolling holds are blocked while an earlier account is pending.

The first full run exposed an enum integration error: numeric phase values were compared through string conversion. That run is archived only as inactive-recovery debugging evidence. Actual-wrapper tests now use explicit PID-state comparison.

Corrected flat recovery removed the old 61 mph fault but produced a new 20.59 mph timeout and 409 weaker encoded strong-target brake rows, maximum 0.1053 m/s². Rejected.

The final clipping-aware version advances a gated same-input comparison integral from actual I plus pending debt using the exact installed freeze/native PID, then revalues contributions affected by clipping/freeze. It reads no recorded reference I or wire output. This is auxiliary counterfactual accounting, not a vehicle model or a continuously advanced native reference history. Positive-growth trimming is subject to CAN, ownership, freshness, callback timing, pedal, urgent/stop and speed/context gates. Signed native revaluation closes the algebraic account; account conservation is not proof of physical recovery or a bound on later command divergence.

## Full controller replay

All **197 segments / 12 routes / 570,269 callbacks** processed. Source bindings were checked before and after execution. 185 segments have no active atomic-input gap. One retained 12-segment route has five missing active prefix inputs and remains diagnostic-only; it is not used to clear a gate.

Final candidate:

- Old 61.23 mph alpha-comfort timeout: absent.
- New **20.5901 mph release-timeout at route-relative 1482.258 s**, highway-pulsing-session-02; 104 callbacks lose activity. Retained 69.71 mph timeout in that route is unchanged.
- **472 weaker encoded strong-target braking rows** out of 33,194 checked. Maximum difference **0.1014 m/s²**: 366 rows in precharge-road-session-02, 24 in maneuver-followup-session-02 and 82 in alpha-comfort-session-01. These are encoded requests, not measured physical deceleration.
- Two new positive-gas rows with fresh valid retained torque; no moving >=3 m/s gas-with-retained-torque rows, and no gas under commanded brake/precharge. The low-speed cases remain a gate failure, not a physical clearance claim.
- 17,882 changed wire rows; zero disabled-owner wire changes.
- All routes end with zero pending account; account residuals are below numerical tolerance and measured reference crossings are zero. Nevertheless the later control trajectory still diverges. Zero debt is therefore insufficient as an exit criterion.

At 1478–1482 s before the new timeout, candidate raw demand and integral sit about **0.1803 m/s² above reference despite zero pending debt**. At the fault reference is braking (~−0.2263 raw), candidate is waiting for observed pressure clearance (~−0.0460 raw), with retained torque. This points to history accumulated through changed actuator modes after repayment. Keep pressure clearance and disengagement safeguards authoritative; do not suppress the timeout to call this fixed. See timeout-20mph-detail.json.

## City, restart and highway results

| Frozen-response fixture | Reference | Final candidate |
|---|---:|---:|
| City 25 mph brake changes | 17 | 17 |
| City brake-command exposure | 21.5329 s | 21.5329 s |
| Original 63 mph highway changes / 15 s | 20 | 20 |
| Newer highway window 1 / 20 s | 22 | 22 |
| Newer highway window 2 / 20 s | 12 | 12 |
| Earlier high-RPM window peak raw request | 2.000 | 1.859 |
| Latest high-RPM window peak raw request | 2.000 | 1.765 |
| Normal stopped-launch peak raw request | 1.440 | 1.440 |

The entire city route's wire output is unchanged. Restart command peaks improve locally; earlier/latest restart brake exposure also falls 1.940→1.559 s and 1.100→0.462 s in the selected windows. RPM, motion, shifts and received torque are frozen: these are not physical comfort or gear-shift improvements. Aggregate brake changes 1434→1429 do not clear any gate or establish highway comfort.

**Highway pulsing has not improved in the named highway regressions.** Do not label this rolling-restart account as highway smoothing. The remaining work is joint coast/brake-mode and integral feedback design across braking/release, with an explicit bound on post-recovery command history. Saved response identification can constrain that design, but frozen motion/torque cannot validate changed ECU pressure response. A deployable candidate must first clear every complete-route software regression, not just these selected windows.

## Evidence and next gate

91 focused tests pass, including actual production-PID integration, partial clipping headroom, account conservation, reset, stale feedback, epoch/pedals/CAN gates, native hold budget and independent encoded-braking comparisons. Independent review found no additional blocking gate defect, but notes that signed account revaluation is not physical evidence and ownership tests could force a stronger would-have-trim crossing.

Fresh native replay completed all 197 segments: 570,178 replacement ACC slots, zero added TX rejections or relay faults, with no forced permission. Reference has 134 TX rejections; candidate has 133 (zero added). Recorded original RX, non-ACC TX and timers are retained. Debug hooks were compiled from the current exact child; no sanitizer or hardware validation. Results are recorded separately in native-summary.json and native-recovery-results.json. Native acceptance cannot override the controller rejection. No road-readiness, ARM build or hardware proof is claimed.

Preserved clean pair: parent 2ca969e45afee229d7ec5c03c8768e137410c8d1; child bcd706d02fd6b8159b1eadcb6b2a56b504f69567. Earlier broad local guard remains uninstalled. No push, integration, device access, settings, CAN, firmware or OS operation.
