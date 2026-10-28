<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Actuator timing and mode selection: full local replay

**Decision: rejected for integration. Remaining pulsing and integral blockers are not resolved.** No Comma access, settings changes, paired-source edits, installation, CAN transmission, reboot or push occurred. Steering settings 1.20/0.97 remain untouched.

## What was investigated

The previous spike admitted almost no coasting because it required brake torque to be near zero before withdrawing the weak brake command. This experiment separates requesting release from permission to propel. The actual installed pressure-clearance observer remains the only authority for propulsion; its distinct-sample qualification and stalled/progressing timeouts are unchanged.

A continuous planner-integrated speed reference and causal 200 ms acceleration-error filter select RELEASE, COAST or DRIVE. A 250 ms bounded projection anticipates response; actual speed error above 0.04 m/s overrides that projection. These values are experimental hypotheses, not identified vehicle parameters. The local selector is restricted to weak demand, independent fresh no-lead radar, reported brake/arbitrated torque at most 500 Nm, moving PID operation from 3 m/s through 70 mph, and low lateral acceleration. Lead, FCW, stopping, invalid inputs and stronger requests return to the original policy. Low-speed restart and 70–85 mph behavior receive no direct new tuning.

The combined ablation adds a positive-integral recovery hold of at most 250 ms per admitted authority transition; negative error and stronger deceleration retain immediate integration. It uses only causal returned feedback. The mode-only ablation omits this hold.

## Failure found and corrected within the experiment

The unrestricted retained-pressure release trial produced an added timeout near 63.9 mph: the candidate withdrew its brake bit while the recorded response stayed at 48 Nm for over a second. It was never permitted to propel. This is both a real watchdog obligation and a frozen-response replay limitation: recorded pressure belongs to the original command, not to the counterfactual candidate command.

The revised selector backs out when reported maximum actual/arbitrated pressure rises by over 4 Nm or fails to fall by over 4 Nm within 100 ms. It then requires sustained positive intent and clear pressure before retrying. This removed added faults in the full revised replay. It is a conservative experiment backout, not an ECU response model and not a replacement for the original timeouts.

## Full replay result

All 137 cached segments were processed through chronological actual LongControl and CarController callbacks: **401,970 consumer callbacks**. Producer integral state evolves continuously; candidate feedback is returned only at causal recorded publication times. Planner, vehicle response, torque, pose and driver actions remain recorded/frozen. This is software comparison, not a closed-loop comfort simulation.

Across identical common healthy active samples in five-mph bands:

| Metric | Current baseline | Combined trial |
|---|---:|---:|
| Matched active exposure | 4,210.259 s | 4,210.259 s |
| Brake-bit transitions within bands | 992 | 1,050 |
| Successive transitions less than 0.6 s apart | 218 | 275 |
| Brake-command time | 1,485.477 s | 1,552.969 s |
| Propulsion-inactive time | 1,601.837 s | 1,668.303 s |

These are controller callback/band metrics, not counts from the earlier raw transmitted-CAN episode report; window boundary and reconstruction differences mean those earlier counts must not be substituted here.

The named ~55 mph 15-second window improves from 22 to 19 reconstructed transitions but spends more time braking (262 to 288 callbacks). Another window worsens from 8 to 13, and the named second-route highway window worsens from 15 to 17. Several other named windows do not improve. The mode-only ablation also regresses; the extra integral hold is not a solution.

No added coordination fault or inactive-control change was found in the revised full replay. Both pre-existing reconstructed older-route release faults remain. The maneuver route and all 61 older segments produce **byte-identical generated ACC wire streams** to the current-stack baseline because required independent context keeps the new selector out of scope there. Their replay still ran; this is not new comfort coverage.

## Remaining integral blocker is on the wire

In the second recent highway route, 653 common active consumer samples with planner target at or below -0.5 m/s² have a weaker raw acceleration command, by at most 0.008311 m/s². Decoding generated ACC messages confirms **588 weaker brake-acceleration wire requests**, maximum delta **0.0117 m/s²**. This cannot be dismissed as exclusively below wire quantization.

The first raw divergence of this kind is at route-relative 453.188 s / 31.24 mph, after the selector has already fallen back to ordinary lead following:

- consumed planner target: -0.516158 m/s² in both;
- baseline integral: +0.126381; candidate integral: +0.129722;
- baseline raw request: -0.389778; candidate: -0.386436;
- both brake bits are active and both use the same recorded vehicle acceleration.

Immediate fallback on a lead does not undo prior integral history. A longer coast grace, indefinite freeze or relaxed pressure watchdog would conceal this interaction rather than resolve it. No such changes were made.

## Verification and limits

- 14 focused tests passed: retained-pressure release, pressure-progress backout, no micro-rearming, speed debt, reference continuity, scope fallback, bounded integral hold and actual-controller pressure-clearance/timeouts.
- 157 retained Ford tests and 20 subtests passed against the local controller overlay.
- The old admission policy fails four of the new policy regressions (three others pass), retained in `regression-red.log`. Initial test harness configuration errors are retained separately and are not counted as RED evidence.
- Fresh plain-debug native safety replay across all 137 segments processed 32,171,016 RX and 951,332 TX per variant, with zero added rejection and no relay fault or forced permission. Existing recorded/baseline rejected messages remain visible in the receipts; this is not a claim of zero total rejections. Results are recorded in `RESULT.json` and the native receipts. Native acceptance is not comfort, stopping-distance, ARM, hardware or road proof. No sanitizer run in this experiment.
- The baseline reconstruction retains the known hidden consumer IPC/pose receipt-order limitation; the old recorded pose fault cannot be claimed fixed from this replay.
- Above ~65 mph, these new highway recordings do not provide active longitudinal evidence. There is no new 70–85 mph comfort claim.

## What must change next

Retain the pressure-progress regression and first later lead-braking divergence as blockers. Reject this mode selector and integral recovery hold as installation candidates.

The next useful design needs an identified **effective coast/engine-braking response**, including the response to valid zero/nonpositive propulsion versus inactive propulsion, plus brake apply/release timing. A nominal zero acceleration message is not proof of zero wheel force. Fit that response by gear and grade with uncertainty and held-out OEM/Alpha episodes, then evaluate the command selector and authority-aware integral together against a dynamic response model. The existing frozen replay remains necessary for CAN/fault/transition checks, but cannot certify the changed physical trajectory. Do not call fewer command transitions alone a comfort fix.

No new drive is required to finish the diagnosis above. Saved data can further constrain that response model; an eventual controlled actuator identification test would need a separate plan and authorization. This result does not ask the owner to repeat the same highway trial or install another unproven tune.

Evidence: `joint-comparison-combined_progress.json`, `episodes-combined_progress.json`, `wire-comparison.json`, `first-divergence.json`, focused/retained test logs, paired preservation receipt and native replay receipts. Exact private cached inputs are hash checked by each replay.
