<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local midrange roll-target mapping spike — October27,2026

Status: diagnostic prototype complete; full replay completed. No installation/integration recommendation. Paired source and owner1.20/.97 remain unchanged. No SSH, device, CAN transmission, publication, or settings writes.

## Recorded symptom and mechanism

`trace.py` replays24,285 normalized20Hz frames from the latest moving session05 and reproduces positive signed excess lateral acceleration above0.1m/s² in40–50mph. Freshness, assistance, driver/pedal/signal/lane-change exclusions are inherited from the road review.

| Band | Eligible meaningful turn time | Body/request median | Wheel-model/request median |
|---|---:|---:|---:|
|40–45mph|32.45s|117.43%|117.71%|
|45–50mph|36.20s|118.37%|119.32%|

At10:15:59.9–<private clock time> body/request median129.48%, wheel-model124.52%, actual wheel exceeds target by4.45deg median. At10:23:05.0–<private clock time> before recorded override, body125.04%, wheel-model122.49%, wheel exceeds target by1.86deg. Wheel/body agreement supports a real steering response excess; it does not prove the learned vehicle model is physically exact.

The requested steering-wheel target agrees with the roll-aware vehicle-model inverse (median error−0.0020deg and−0.00025deg in those windows). Thus target generation mismatch is not supported. Learned ratio is22.23/22.29, stiffness about0.999/0.997, roll−0.0189/−0.0496rad. Existing roll-aware path mapping has zero weight below50mph. Converting that existing wheel target through the same vehicle model without roll yields97.70% and87.20% of requested raw curvature in the two windows. This is an evidenced mapping seam, not evidence for a blanket17% gain change.

Ranked hypotheses tested: (1) wheel/path mapping disagreement is supported by wheel/body excess; (2) omission of the existing roll-target mapping below50mph is supported by source and target decomposition; (3) body-only calibration artifact is weakened by wheel agreement; (4) incorrect wheel-target generation is contradicted by inverse-model agreement. Transient plant dynamics, learned-model error and road bank remain confounders. The first window's~2.3% roll-target difference is far smaller than its~29% body excess; extending roll mapping alone cannot be claimed to solve all observed excess.

## Throwaway experiment

`prototype.py` subclasses the exact installed `ObserverContinuity` policy and changes only existing nested `RollAwareMapping` leaves. Its weight smoothly rises35–40mph, stays1 through50mph, blends back to the existing mapping by55mph, then exactly retains the original speed-weight curve. Existing0.01rad/15% mapping bounds, calibration/context freshness, target agreement, driver/signal/lane-change releases, and final range/slew remain inherited. Highway observer/body/wheel evidence policies, low-speed policies and owner1.20/.97 are retained.

This is a static engineering experiment, not a fitted17% reduction. Roll-target mapping can increase or decrease path command depending on roll/direction; replay output must be reviewed for both outcomes. New35–40mph changes are transition exposure and do not have strong independent road evidence. Fresh-history55–85mph equality tests do not establish that every transition is byte-identical; full history replay is needed.

A rejected initial experiment inherited obsolete `HighSpeedReduction`, while the installed policy is `ObserverContinuity`. Its full latest-session replay exposed unexpected changes60–70mph and a few low-speed frames. It is retained as `rejected-obsolete-baseline-*`, and its73test results do not validate the final candidate. The first harness also failed on an obsolete `handoff_pending` property; `harness-obsolete-property-failure.log` is retained. Final harness uses the current `release_pending` property.

## Validation and limits

Final candidate: 71 installed observer/highway checks pass (`actual-highway-tests.log`);21 candidate-specific cap, validity/abort, continuity and fresh-history speed parity checks pass (`midrange-tests.log`). An additional 14 full `CarController` stream-equality checks pass: both turn directions at 55, 60, 65, 70, 75, 80 and 85 mph, with sustained demand, unwind and driver abort, against a separately constructed exact `ObserverContinuity` baseline. Total: 106 final-candidate checks. These are synthetic checks and cannot measure comfort or vehicle stability.

Historic corpus:32 routes637 segments; latest moving drive:1 route21 segments, total33 routes658 distinct segments. `run_full.py` runs full raw chronological RX/timers and generated TX through independent native safety hooks for recorded atomic snapshots and separately labelled past-only calibration fixtures. `full-progress.json`, per-route worker logs and per-route `full-replay.json` are durable progress/results. No controls permission is forced. Historic routes retain their actual recorded non-pinion safety bits while applying the paired pinion configuration as in the established harness. Historical generated controls are compatibility fixtures, not historical installed-code reproduction.

All 658 raw segment hashes match the original evidence manifests (`manifest-verification.json`). Raw inputs are referenced in place, not copied. The paired source snapshots are clean parent `df788e02719c05595dab2f980e6fd9fb9e464006` and child `1d29e6e78abcbf5c6a80eb397d80b349c6cca960`; imported Ford modules, vehicle model, tracking seam and native safety library are hash-bound in `source-snapshot.json`. Full replay completed all 33 routes / 658 distinct segments: 3,814,069 controller updates and 152,312,756 physical RX frames. Every comparison variant generated 2,476,839 TX frames; 2,464,642 per variant were tested after native Ford safety configuration and all were accepted. The remaining 12,197 generated frames per variant precede Ford safety configuration and are explicitly excluded from the native TX pass claim; 33 invalid safety ticks occur at initialization across 33 routes. There are zero added native rejections, and default-off full-stream equality holds across every route.

Changed angle-frame counts by speed band are recorded atomic: 35–40: 365; 40–45: 1,184; 45–50: 1,290; 50–55: 1,152. Causal calibration fixtures: 35–40: 1,707; 40–45: 2,768; 45–50: 3,317; 50–55: 1,958. Every band below 35 mph or at/above 55 mph has zero changed angle frames in both comparisons, including all retained 55–85 mph exposure and transitions. Independent full-controller synthetic tests additionally verify exact generated full-CAN equality at 55–85 mph in both directions through unwind/driver abort. This preservation is command-level evidence, not proof of physical highway stability.

`acceptance.json` confirms original-manifest hashes, source hashes/SHAs unchanged, clean paired repositories and full default-off equality. Across the full corpus, recorded atomic commands decrease magnitude in 3,884 slots and increase in 107; causal calibration fixtures decrease in 9,396 and increase in 354. Maximum absolute generated delta is 0.009 rad recorded / 0.010 rad causal fixture. These comparisons are separate fixtures, not additive independent exposure. Historical fixtures reproduce current policy against saved historical state with causal calibration, not historical physical performance. Frozen saved response is not counterfactual body response or proof of physical improvement. Latest trip has no>70mph evidence;85mph evidence remains synthetic/historical only.

## Latest generated-command result

The full latest 21-segment session replay completed with 2,001 changed generated updates and zero additional native TX rejections against the independent current baseline. Recorded atomic calibration and separately reconstructed causal calibration fixtures give identical comparisons on this current-source trip. All latest changed angle frames are within 35–55 mph; none change at 55–70 mph.

At <private clock time>–<private clock time>, generated path magnitude is 98.08% of baseline (median path −0.1035→−0.1010 rad). At <private clock time>–<private clock time> it is 93.27% (−0.0520→−0.04825 rad), with maximum absolute delta 0.007 rad. These are generated commands on frozen observed state, not changed observed body response.

The observational risk screen also finds 16 eligible 40–50 mph slots where command magnitude decreases while observed body response is below 80% of request, and 2 where it increases while observed response is above 120%. These are screening associations rather than counterfactual regressions, but they prevent presenting this unconditional mapping extension as a solved, integration-ready correction. A further bounded, body/wheel-confirmed admission experiment would need its own replay. No such change is integrated here.

`risk-detail.json` classifies those slots using the road review's strict preceding one-second phase gate. Of the 16 reductions, 13 are transition-classified (<private clock time>–05.533 and <private clock time>–34.267), while 3 are rising (<private clock time>–21.137 and <private clock time>). None are classified steady or unwinding. Median body/wheel-model ratios for these four groups are respectively 71.8%/89.6%, 71.6%/95.9%, 79.9%/116.9%, and 79.5%/100.4%; this disagreement is consistent with lag/confounding rather than a proved controller regression. Their requested absolute lateral accelerations range about 0.35–0.87 m/s². The two increases are isolated transition-classified slots at <private clock time> and <private clock time>, each one 0.0005-rad wire quantum, with body/wheel-model ratios 128.1%/116.9% and 153.7%/166.6%. `transition` means the strict phase classifier did not establish a continuous one-second rising/steady/unwinding history; it is not a physical diagnosis.

## Commands

Use `${USER_HOME}/Apps/openpilot/.navigator-master-integration-20261014/.venv/bin/python` as`$PY`; run pytest from`/private/tmp` to avoid the BluePilot import shadow. `$P` is this directory. Source repository and safety-library hashes are retained in`source-snapshot.json`.

```sh
$PY "$P/trace.py"
$PY "$P/build_corpus.py"
$PY "$P/prepare_worker.py"
$PY "$P/run_full.py"
$PY "$P/summarize.py"
$PY "$P/finalize.py"
$PY "$P/command_audit.py"
PYTHONPATH=${USER_HOME}/Apps/openpilot/.navigator-master-integration-20261014/opendbc_repo:${USER_HOME}/Apps/openpilot/.navigator-master-integration-20261014 "$PY" -m pytest -o addopts='' --confcutdir="$P" -q "$P/test_actual_highway.py" "$P/test_midrange.py" "$P/test_full_controller.py"
```
