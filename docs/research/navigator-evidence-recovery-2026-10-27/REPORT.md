<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator maneuver evidence recovery

Completed October 28, 2026; investigation directory retains its October 27 start date. Offline only; no controller or device changes.

## Recovered original evidence

The bounded inventory now covers **1,669 unique original segments**, 127 source/alias groups and 14,045,246,890 compressed bytes. It recovers **two genuine longitudinal maneuver sessions (20 and 22 segments)** missed by the earlier 737-segment steering corpus. The 20-segment session reaches Finished; the 22-segment session is partial. No lateral maneuver execution was observed in this retained set. Missing mode parameters and recording gaps remain unknown; this does not establish that a lateral test was never performed.

Source-bound mode and actual CAN command checks separate PID braking, stopping resets, interrupted phases and release/setup commands. The completed session contains repeated clean 20 mph braking phases. First-two-to-third response templates have acceleration RMSE of 0.173, 0.084 and 0.240 m/s² for weak-stop, −1 and −3.5 planned-reference phases. These are closed-loop reference responses, not actuator gains. Two earlier clean −1 repeats predict three later repeats with RMSE 0.144–0.197 m/s². The matching raw engaged-gear code is not evidence of a numbered transmission gear.

Command/status clearance precedes measured torque clearance. Setup commands and overrides prevent treating those intervals as isolated coast experiments. Retain measured-torque clearance; these data do not identify highway coast authority, grade compensation or a 0–85 mph response model. Stop-mode integral resets must not be fitted as moving PID authority.

## Steering refinement rejected

A single predeclared, pre-action shared-error correction was evaluated without tuning on the held-out session. Moving-target held-out RMSE worsened from **1.016 to 1.171 degrees** across 314 anchors in three islands; calibration q90 widened from 1.724 to 1.959 degrees. The paired block interval for change in mean squared error is entirely positive. This refinement is rejected; no validated moving-reference response provider was produced.

## Decision and remaining work

Neither control blocker is resolved and no new controller is selected for integration. The next longitudinal work can use source-bound PID/release/torque-clearance fixtures from the recovered tests, while returning unsupported outside their observed domain. Highway coast authority and steering response discrimination still require evidence; broad gain changes are not justified by this pass. No new full controller/native replay is claimed because this pass changes evidence and evaluates an observer, not an accepted controller candidate.

The paired source heads remain e05e42f43d2907a4f02915a924cfd95a46197e79 / 5097b993965b2b65ea3fcca7e3769cfa9403d49c. Owner 1.20/0.97 settings, installed software and original recordings were untouched.

## Inspectable evidence

- [Original inventory and phase audit](maneuver-audit/REPORT.md)
- [Controlled longitudinal response support](longitudinal-maneuver-support/REPORT.md)
- [Steering assessment](steering-innovation/REPORT.md)
- [Independent review](REVIEW.md)
- [Artifact/source verification](PUBLIC_VERIFICATION.json)

Artifact verification establishes recorded-file integrity and unchanged source, not physical comfort, ECU authority or road validation.
