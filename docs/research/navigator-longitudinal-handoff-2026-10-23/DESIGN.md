<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local brake/propulsion handoff prototype

Owner requested local design/prototype and replay on October 23, 2026. This is a report-local experimental spike, not paired integration or installation. Current pair and 1.20/0.97 stay unchanged.

## Approach

Compare baseline, simple brake-latch propulsion withdrawal, and stateful withdrawal/resumption. Choose the stateful variant as the main spike because simple withdrawal leaves an unbounded valid-request handoff. Defer separate precharge/deceleration thresholds and brake-release changes: their hydraulic/grade implications are not established. This choice is the investigator's proposal under the authorized local prototype scope, not owner approval to deploy.

## Interface and states

A pure Handoff object consumes monotonic seconds, longActive, baseline brake latch, baseline gas request, finite pitch validity and stopping state. It returns wire propulsion and explicit state/reason. Modes: inactive, braking, coast, qualify, resume, drive. Disabled/invalid input clears all handoff state and returns inactive sentinel -5. Braking and stopping always withdraw propulsion; genuine invalid/missing pitch also withdraws propulsion without modifying brake output. No stale cached pitch is substituted. Timestamp gaps >100 ms, repeated/backward time and invalid numeric data reset resumption history. No request is transmitted from this module.

After braking/inactive, require at least two consecutive eligible brake-clear samples spanning20ms. First resumed valid request is at most zero (negative engine-deceleration request may pass immediately); positive propulsion rises from the actual previously emitted valid request with nominal0.5m/s³ bound. Reductions and renewed braking/stop/disengagement are immediate. Keep bounding positive increases while active rather than declaring the ramp finished on a single near-zero target; this prevents near-zero targets bypassing the handoff bound on the next sample. Sentinel is never subtracted or treated as physical acceleration. The0.5rate and20msqualification are explicit exploratory constants; sweep0.25/0.5/1.0rates and20/60/100msqualifications. No fuel/comfort claim follows.

The baseline brake acceleration, jerk limiting, creep/pitch compensation, precharge/deceleration bits, stopping flag, predicted acceleration, target speed, native safety and steering remain identical for the main prototype. Scope only Expedition+openpilot longitudinal. Other platforms/OEM mode bypass the helper.

## Known limitation to expose

Old brake latch release still needs pitch-adjusted accel>0.3m/s². Small positive restart requests can therefore remain in braking mode. Tests must reproduce and label this limitation, not mark launch fixed. No artificial timer clears brakes. Brake latch release thresholds and an OEM-feedback-confirmed release design are separate work requiring more evidence; prototype cannot be recommended for installation while launch/release and physical outcomes remain unvalidated.

## Gates

Test absent feature first; then mutual exclusion, immediate withdrawal/decrease, sentinel handling, demand changes/reversals, finite/missing pitch, invalid times/gaps, bounded resume, flat/positive/negative grade, stop/restart and small-positive blocked restart. Controller-to-wire tests must preserve all non-propulsion fields and stock/other-platform behavior. Replay current production controller with frozen past-only recorded inputs and candidate-only helper; validate emitted ACC frames under current native TX hooks including disabled permission. Reuse original Alpha and35saved OEM segments as evidence; keep recorded response separate from counterfactual output. No closed-loop vehicle, fuel, full native RX/forwarding replay or current steering-context coverage claim.
