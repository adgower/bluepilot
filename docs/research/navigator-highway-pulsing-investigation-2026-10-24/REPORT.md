<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Highway pulsing: local investigation — October 24, 2026

The current `49be383b2` / `d459133a` pair still reproduces the saved highway cycling. The 6.7 mph continuity repair does not address it. No device contact, settings changes, paired-source edits, installation or CAN transmission occurred in this investigation. Owner 1.20/0.97 and clean paired sources are retained.

## Reproduced symptom

`reproduce.py` runs the actual current production controller over the earlier saved moving session, using recorded control requests, latest-published carState and decoded torque at 60,656 consumer slots. Four checked feedback fields match at 60,517 slots; 139 differ from the older install, which predates the restart fix. This is reconstructed controller behavior, not exact consumed-state replay, full feedback-byte equality, native safety replay or vehicle simulation.

The selected near-60-mph window reproduces **39 brake-command edges in 20 seconds**, including **32 adjacent reversals less than 600 ms apart**. Raw acceleration demand exceeds +0.02 m/s² for 94.8% of the window. No fault occurs in that window. These are command transitions, not independently measured physical brake applications or a comfort score.

`pulse_diagnostic.py --assert-no-repeated-cycling` fails deterministically on this episode (two runs). The three-rapid-reversals alarm identifies the observed command-cycling symptom; it is not a physical safety or comfort threshold. Existing saved-data source provenance is retained in the earlier [road review](../navigator-brake-release-road-review-2026-10-24/REPORT.md).

All 20 brake entries in the window occur with small calculated negative residuals, from -0.0429 to -0.00287 m/s² (median -0.0156). Sixteen entries have positive raw demand and sixteen have reported torque <=4 Nm. Brake command is active for 32.9% of the window, but propulsion is inactive for **49.7%**. Measured-clearance waits account for 2.24 seconds. The handoff also repeatedly returns through qualification and its acceleration rise limit.

## Ranked hypotheses and tests

1. Pitch/reference variation moves residual demand through the brake threshold. Prediction: changing only the pitch-decision reference changes the edges. Confirmed as a sensitivity; synthetic pitch variation alone also reproduces cycling.
2. Planner/controller demand varies near that threshold. Prediction: filtering only demand changes edges. Confirmed as a sensitivity, so pitch is not the only contributor.
3. Release qualification and repeated handoff reset amplify an entry into a propulsion interruption. Source trace and reason durations confirm this chain. This does not justify bypassing clearance.

The minimal actual-controller diagnostic holds speed at 26.8 m/s, requested acceleration at +0.1 m/s² and reported torque at zero. After reference warmup, a synthetic 2-Hz, ±0.04 m/s² pitch-gravity variation around the decision boundary produces **76 brake edges in 19 seconds**, 84% inactive propulsion, and no faults. Its constant-pitch control produces zero edges and uninterrupted propulsion. It removes planner, lead, gear and actual vehicle response variation; it is a software reproduction, not a claim that the real sensor has that exact waveform. `minimal_repro.py --assert-no-repeated-cycling` is intentionally RED. The initial synthetic fixture's sub-nanosecond floating timestamp mismatch was corrected by using one integer-nanosecond clock; no production guard was changed.

## Simple filters rejected

Diagnostic 0.3-second causal low-pass interventions run in memory only. The same saved vehicle response and torque are retained, so this is a frozen-response sensitivity, not a causal prediction of the modified vehicle.

| Intervention | Window brake edges | Inactive propulsion | Later route timeout in frozen response |
|---|---:|---:|---|
| Current production | 39 | 49.7% | No |
| Pitch-decision low-pass only | 19 | 36.0% | Yes |
| Raw demand low-pass only | 24 | 45.4% | Yes |
| Both | 11 | 32.4% | Yes |

**None is an installation candidate.** The reduced counts after a latched fault cannot count as improvement. The timeouts do not prove the physical counterfactual would fault, because changed commands would change feedback; they prevent claiming this replay validates a fix. Filtering raw demand can delay actual deceleration and is particularly unsuitable as a blanket remedy. These choices were diagnostic probes, not a parameter search or selected tune. Intervention-reset behavior was checked and corrected before producing these results.

## Recommended correction design

Use a coherent residual-demand coast/brake allocator, with a stable causal reference and bumpless propulsion handling. The current nominal 40 ms mild-entry admission, positive-release dwell and subsequent independent clearance/rise reset can form a fast repeated cycle. Merely making a dwell longer or widening release hysteresis can also hold brakes longer, so transition count alone must not select the design.

1. **Stable decision reference:** keep reference-zero mapping separate from short-period attitude movement. Bound any causal filtering's residual and integrated speed-error effect, explicitly reset/reacquire on bad chronology or reference loss, and retain fast handling of genuine demand/grade changes. Do not filter, overwrite or reset global calibration. Existing +0.149913 m/s² mapping is an empirical relative-reference fit, not surveyed grade or known PCM semantics.
2. **Bounded coast region:** when a new entry is weak and ambiguous, qualify persistent signed residual demand with an explicit accumulated speed-error budget and packet-deadline bound. Let short opposite residuals cancel according to a specified causal policy. Preserve immediate takeover of meaningful deceleration, unsafe context, low speed/stop phases and urgent braking. No numerical deadband/debt/delay is approved by this investigation; derive and test it rather than choosing a comfortable-looking trace.
3. **Continuous propulsion handling:** while still genuinely clear and only qualifying a new weak entry, avoid treating every sample as a fresh brake-to-drive episode. Cap any retained request according to the qualified coast contract; never keep positive propulsion through actual braking or non-clear feedback. After actual braking, retain distinct received-sample clearance and the existing fault deadline. The 6.7 mph fix and stock rise limit remain intact.
4. **Separate protocol question:** OEM recordings show precharge-only, negative propulsion without braking, and other distinctions the current single brake/precharge boolean cannot express. That supports further passive analysis, but precharge is real actuation and is not automatically equivalent to free coasting. Do not copy OEM overlap or ignore torque clearance based on message names.

Alternatives considered: blanket low-pass is rejected by the diagnostic outcomes and deceleration-lag concern; changing raw acceleration gains is unsupported and would not repair the state transition; a bounded allocator is the recommended next local prototype. This is a design recommendation, not implemented paired-source behavior.

## Acceptance before integration

- Lock the real saved pulsing episode and minimal actual-controller reproducer as regression fixtures; preserve provenance and baseline failures.
- Check all available OEM/Alpha routes and the incoming current-pair drive, counting active coverage and faults, not just edges. OEM lacks the same Alpha planner inputs; unmatched-route comfort/fuel comparisons are not valid.
- Compare meaningful/urgent braking onset, brake acceleration, stopping behavior, speed-error integral, request continuity and commanded jerk. Require explicit bounds for deferred weak braking at actual send slots, including gaps and boundary samples.
- Retain stale/non-clear torque, deadline, override, ownership, pose/reference loss, stop/restart, grade reversals and inactive/default-off checks. Both prior release-timeout episodes remain separate blockers; do not silence them or raise their torque threshold.
- Parent-in-the-loop checks must model changed actuator response and expose uncertainty; frozen-response results alone cannot establish closed-loop comfort. Run full controller/native safety replay, integration/build, isolated ARM and parked gates before any later activation.

The new drive is needed to confirm today's exact signature, lead/speed targets, grade-reference behavior and whether controls mismatch returned. It is not necessary to continue uncomfortable Alpha testing: the existing data already reproduces the software problem. Physical comfort, braking adequacy and fuel improvement remain unproven.

Evidence: [edge analysis](../../navigator-reference/PRIVATE_ARTIFACTS.md), [sensitivities](../../navigator-reference/PRIVATE_ARTIFACTS.md), [minimal reproduction](../../navigator-reference/PRIVATE_ARTIFACTS.md), [production source receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md). Raw locations and road identifiers are not included.
