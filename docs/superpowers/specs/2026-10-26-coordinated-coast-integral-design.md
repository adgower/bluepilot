<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Coordinated coast selection and integral recovery — proposed local design

Status: approved by owner on 2026-10-26 for local research. No device authorization.

## Intent

Reduce the owner's uncomfortable brake/accel cycling while preserving speed/following response, signed integral recovery, stop/restart behavior and existing safety limits. Preserve steering, 1.20/0.97, Navigator geometry and the selected narrow low-speed guard. Start from local parent `2ca969e45afee229d7ec5c03c8768e137410c8d1` / child `bcd706d02fd6b8159b1eadcb6b2a56b504f69567`.

## Approaches

1. **Coordinated mode selection and integral recovery (recommended direction).** Keep the planner unchanged. Evaluate coasting against a causally supported acceleration envelope and return command-authority feedback in the same units as the producer request. More work, but addresses both the observed switching and its subsequent integral history.
2. **Planner-only filtering.** Smaller change, but positive planner targets already coexist with the downhill brake transitions; filtering can delay real following deceleration without repairing the grade/actuator boundary. Retain only as a diagnostic ablation, not the proposed fix.
3. **Longer precharge or wider brake deadband.** Reject as a runtime direction: the finite allocator already exhausted its budget, prior point-forecast coasting worsened coupled replay, and thresholds alone do not establish physical coast capability.

This is a proposed engineering design, not a claim that the owner approved new gains, changed safety limits or installation.

## Current verified behavior

The declared downhill regression has 20 commanded brake changes in 15 seconds, all with positive planner targets and fresh lead context. The allocator falls back to nominal policy after spending its bounded budget. Current release qualification accepts sustained positive raw/net intent, but the physical observer still independently requires received torque clearance. Short propulsion intervals then terminate at another compensated braking request.

Current producer uses `target - measured acceleration` as PID error and adds its integral to target. Its anti-windup primarily holds positive error when returned commands are limited. `gas=-5` is an inactive sentinel, not acceleration delivered. Neither that value nor recorded measured acceleration can be substituted as a counterfactual applied command.

## Work in two explicit stages

### A. Offline authority identification and feasibility gate

Use the saved OEM/Alpha received state, actual/arbitrated brake torque, gear/RPM, grade, command history and lead context. Reuse existing route split roles; previously inspected routes are development/regression evidence, not new blind validation.

Identify separate command modes: inactive propulsion, valid engine coast, propulsion ramp, precharge, friction brake and release. Keep inactive sentinel distinct from valid zero/negative acceleration commands. Estimate the range of net coast acceleration only from causal known inputs and supported mode/gear/grade/history strata. Do not train on future measurements that would be unavailable at a decision time. Offline future outcomes may be used only as labeled evaluation targets.

An existing 200ms point forecast is insufficient: all 54 prior conservative interval comparisons overlapped. Before a policy patch, report calibration/coverage and error by mode and speed, and whether a conservative coast choice is actually identifiable. If no supported choice remains, stop with that result; do not shrink uncertainty merely to admit coast. No numeric performance bound is invented in advance of measuring the model's error.

### B. Research policy only if Stage A supports a choice

Desired net acceleration remains the consumed planner target plus producer correction. The consumer's mode selector compares this demand with the supported coast envelope, retaining current ownership, timestamp, phase, pose and actuator eligibility. An uncertain or out-of-support comparison returns the complete baseline path with no stale candidate state. A coast preference is never a brake-clearance permission.

Keep the bounded precharge allocator separate and its limits unchanged. Do not reset its budget on candidate coast/drive transitions. A new experimental coast decision has its own explicit finite intervention/debt bounds and measured-clear, positive-demand recovery; its values must be justified by Stage A error, not tuned to one recording. There is no indefinite weak-brake suppression or new timeout extension.

For lead following, require fresh valid range/relative speed and reject model/lead disagreement, closing/urgent scenarios, FCW, stop demand and missing context. Exact supported margins are a Stage A deliverable, not values inferred from the 74–101m downhill example. Missing lead data is never interpreted as clear road. For this first candidate, missing context falls back to baseline even if the planner says no lead.

Return truthful selected-mode, request, command limitation and command-domain bounds under the current owner/sequence/freshness contract. If the existing version-1 metadata cannot represent a finite coast authority bound, add a separately versioned producer/consumer extension with safe unknown-version fallback; do not overload existing fields. Any extension is local research until paired integration is separately requested.

Compare existing conditional integral hold with bounded back-calculation toward a valid command-domain bound. Never use measured acceleration, forecast torque, or the inactive sentinel as that bound. Preserve signed error that drives demand back toward available authority and stopping reset. Back-calculation is a candidate to measure, not an assumed improvement; select its rate only after timing and recovery analysis, with explicit limits and tests.

## Required experiment matrix

Run baseline, consumer-only, integral-only and coordinated variants against the same chronological inputs, clocks and causal returned feedback. Report whether a coordinated effect exists rather than attributing all changes to the mode selector. Keep runtime source unchanged until the research comparison passes.

Primary fixtures:
- The 15-second downhill 62–64mph lead-following episode, including the full preceding budget history.
- The earlier 21.39mph first-divergence fixture with mild negative target but large positive measured acceleration; preserve full subsequent integral history.
- Rolling restart and first-to-second-gear event used for the integrated low-speed guard.
- Retained release-timeout episodes, stronger deceleration, stale/unknown feedback, pedal override and ownership transitions.
- No-lead and following episodes in each supported speed band; do not extrapolate the 27 seconds above70mph to75–85mph validation.

## Gates and evidence

1. Reproduce the committed baseline before variants; retain raw hashes, exact pins and private full traces.
2. No added coordination fault, inactive-path change, gas under commanded brake/precharge, propulsion before received clearance, forced permission or allocator-rearming loophole.
3. Strong-deceleration command behavior must not worsen relative to the committed baseline. The prior owner-approved 27 one-increment differences belong to the integrated baseline; they are not a waiver for new differences.
4. Evaluate switching, valid propulsion exposure, command jerk/ramp and full downstream integral behavior together. A lower transition count caused by disengagement, prolonged braking or lost acceleration is failure.
5. Following safety and physical comfort cannot be proved by frozen-response replay. Simulated tracking must be labeled model-based and its uncertainty retained; do not claim improved gap, braking distance, RPM or road comfort from recorded motion.
6. After successful research: full162-segment coupled and native command replay, transition/abort/fallback tests and paired build checks. Native debug acceptance is distinct from ARM/hardware/road validation.

## Scope boundary and deliverables

Deliver a reproducible feasibility report, experiment matrix and, only if supported, a local research prototype with explicit rejected outcomes. Update the roadmap. No push, SSH/device staging, install, settings change, reboot, firmware or CAN transmission. Preserve the committed low-speed guard and 1.20/0.97. Device activation requires a separate request after concrete validation evidence.
