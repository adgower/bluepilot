<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Longitudinal maneuver follow-up — October 25, 2026

## Outcome

**The targeted progressing-release timeout fix worked in this test.** The new installation completed the full seven-type, 21-run tool sequence and reached “Maneuvers Finished,” with no recorded ControlsMismatch event, mismatch alert or coordination fault. Nineteen runs were uninterrupted, CAN-valid and pedal-free. One creep run and the first +2 m/s² run included pedal input and loss of longitudinal activity, so they are excluded from response calibration.

The new recordings also contain a separate **pre-installation** ControlsMismatch around <private clock time>, near 40.9 mph, with reason `invalid_pose_or_accel`. This is one fault episode with repeated alert-state transitions, not three separate failures. It was on parent `74eaa6a60`, before the new pair. No new-code normal active highway driving was recorded, so the current tests do not establish that the separate highway pose issue is resolved.

## Acquisition and source

Downloaded all 93 newly available completed segments across six sessions: 792,708,644 raw bytes, unique hashes verified, final remote inventory matched, zero open segments deferred. Source, selected settings, protected file hashes and running service matched before/after acquisition. No Comma source/settings changes, service actions, ECU queries or CAN transmission were performed. All subsequent work was offline on the Mac; plotting dependencies were installed only into a temporary Mac folder.

Three sessions precede activation and three use clean parent `ead00c30e` / child `d4a20125`. Two post-installation sessions contain no active longitudinal control; the third is the maneuver session. Pre-installation normal-driving data remain useful for comfort diagnosis because the installed patch changes release timeout handling, not the existing planner, integral, grade mapping or handoff ramp. They are not presented as a post-installation comfort comparison.

## Full test coverage

“Uninterrupted” means longitudinal activity throughout the marked run, valid CAN and no driver pedals. It does not require a settled initial actuator state or sufficient cruise-speed headroom, so it is not the same as pure gain-calibration eligibility.

| Maneuver | Tool runs | Uninterrupted valid |
|---|---:|---:|
| come to stop | 3 | 3 |
| start from stop | 3 | 3 |
| creep: alternate between +1m/s^2 and -1m/s^2 | 3 | 2 |
| brake step response: -1m/s^2 from 20mph | 3 | 3 |
| brake step response: -3.5m/s^2 from 20mph | 3 | 3 |
| gas step response: +1m/s^2 from 20mph | 3 | 3 |
| gas step response: +2m/s^2 from 20mph | 3 | 2 |

## Direct evidence that the timeout repair worked

After the three -1 m/s² braking steps from 20 mph, original transmitted brake requests turned OFF while reported actual brake torque remained approximately 972, 1,036 and 968 Nm. Distinct received samples met the existing <=4 Nm, three-sample/40 ms clearance criterion after **1.556, 1.576 and 1.563 seconds**. First positive propulsion requests followed at **1.599, 1.640 and 1.616 seconds**. There was no fault or driver intervention in these runs. The original one-second wait would have expired while pressure estimates were still releasing.

This is moving recorded evidence of the intended correction, beyond the earlier frozen-input replay. It is still one completed test session, not proof that every possible ControlsMismatch cause is gone. These are ECU-reported torque estimates, not direct hydraulic-pressure measurements. The existing below-3 m/s stop/creep path is separate and must not be described as enforcing the moving-release rule universally.

[Private/local visualization omitted](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Acceleration results: distinguish demand from what was actually sent

The three moderate brake runs reached final-second wheel-based acceleration means of about **-1.10, -1.15 and -1.10 m/s²** for a -1 target. The three hard-brake runs reached about **-3.35, -3.36 and -3.21 m/s²** near the end of a -3.5 command. The approach to a stop and input ramps affect those averages; these are not standalone brake-gain estimates.

The +1 m/s² trials expose a benchmark constraint. In the first two runs, recorded cruise speed was **25 mph**. Ford's existing `get_pid_accel_limits` reduces available positive acceleration while approaching cruise speed; it clipped the controller request near the end of those runs. Final-second measured means were approximately **0.64 and 0.62 m/s²**. In the third run, cruise speed was approximately **31 mph**, no near-cruise clipping was observed, and the corresponding mean was **0.97 m/s²**. Raising a global engine gain from the first two ratios would misdiagnose a software limit as weak vehicle response. Different initial integral and actuator states also contribute; this was not a randomized experiment.

The two uninterrupted +2 m/s² trials had cruise headroom, but the controller's approximately 1.9 m/s² request was not sent immediately. Recorded release-wait time occupied about **0.62 and 1.26 seconds** of the three-second action windows. After clearance, the existing **0.5 m/s² per second** propulsion rise limit governed the transmitted request. Maximum transmitted gas requests were only about **1.17 and 0.86 m/s²**. Final-second wheel-acceleration means were approximately **1.00 and 0.55 m/s²**. These results show clearance and resumption constraints; they do not demonstrate that the engine cannot produce 2 m/s².

All three start-from-stop runs were uninterrupted. Half-response observations were about **0.80–1.28 seconds**, including the installed ramp and measurement filtering. Terminal speeds differed from the earlier partial test, but different cruise settings and initial conditions prevent crediting that change to this timeout-only patch.

[Private/local visualization omitted](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Highway pulsing: useful new evidence from the pre-installation drives

Exact control epoch/sequence, corresponding consumed planner timestamps and latest causal state were matched. Pedals, faults, stale/invalid inputs and deliberate maneuvers were excluded. The two normal-driving sessions provide approximately **35.7 minutes of qualified active data**, reaching about **65 mph**. Five-mph results and lead/no-lead splits are in `road-metrics.json`; the new data do not validate 65–85 mph.

One approximately 55 mph, 15-second episode has:

- Planner target only **+0.005 to +0.203 m/s²**—gentle positive demand, rather than repeated requested hard braking.
- **24 actual transmitted brake-bit transitions**, matching the feedback trace.
- Reported brake torque spanning **0–464 Nm**, with propulsion torque spanning approximately **-96 to +580 Nm**.
- A stable reported **10th gear**, no brake-disable or brake-denial flags, and no detected lead for about **98%** of the window.

Another no-lead episode has 15 transmitted transitions in 15 seconds with the target approximately **-0.002 to +0.179 m/s²**, stable 10th gear and no brake denial. Selected lead-present episodes also cycle. This confirms that following behavior or gear hunting alone does not explain the problem. Brake-bit counts are not equivalent to equally many hydraulic pressure cycles; actual torque channels independently show substantial propulsion and brake changes.

[Private/local visualization omitted](../../navigator-reference/PRIVATE_ARTIFACTS.md)

The wheel-derived acceleration estimate has large fast fluctuations, so its spikes must not be treated as independently measured passenger acceleration or used alone to fit gains. ECU torque cycling is separate evidence that the issue is more than a displayed acceleration artifact. The grade-reference comparison has a small median residual in the selected windows but wide changing residuals. It does not support another blanket pitch-offset adjustment or identify an absolute road-grade sensor truth.

Lead/no-lead counts also do not support blaming only cars ahead. In one session, brake onsets were approximately 9.2/min with a lead and 9.3/min without; in the other, approximately 6.8/min and 8.5/min. These are observational route/demand groups, not a causal experiment. Lead-present periods spent more time requesting braking, but switching occurs in both groups.

## Next local work

Prioritize stable coast/brake/propulsion selection around near-zero demand, coupled to the integral, grade-reference dynamics and measured actuator response. A short brake request can withdraw propulsion and restart qualification/ramping; actual pressure then takes additional time to release. Repeating that sequence can amplify otherwise small demand changes. The saved wire/torque traces support testing that interaction; they do not yet isolate a single proven dominant cause.

Use the new uninterrupted trials and the saved highway windows together in the coupled controller replay. Preserve measured moving brake clearance and urgent braking. Evaluate release/ramp-aware, bumpless recovery instead of blindly increasing propulsion gain, lowering the clearance requirement, resetting global calibration or applying a generic planner filter. Prior rejected coast prototypes remain rejected; these observations do not establish that their forecasting/admission strategy has become safe or effective.

There is no need to repeat the entire factory maneuver suite just to investigate the present pulsing. Some trials are limited for gain fitting, but they already expose the software constraints. More normal active highway evidence on the new pair would evaluate physical comfort at those speeds; it is not required to continue local diagnosis from the existing pre-installation highway data.

## Reproduction and receipts

`acquisition-provenance.json`, `input-manifest.json`, `quick-inventory.json`, `quick-health.json`, `extraction.json`, `partial-test-results.json`, `maneuver-detail.json`, `maneuver-can-metrics.json`, `road-metrics.json`, `road-physics.json` and `verification.json` retain source, timing and data-quality evidence. The first compact extraction hit an empty startup radar message; it was repaired to distinguish absent/invalid startup data and to use this schema's `leadOne.present` field. The final road analysis verifies that the matched consumed control request equals the recorded feedback request.

Raw routes, coordinates and full recordings remain private. CSV episodes and PNG/SVG plots are deidentified. `health_extract.py`, `quick_health.py`, `thin.py`, `partial_results.py`, `maneuver_can_metrics.py`, `maneuver_detail.py`, `road_metrics.py`, `road_can.py`, `road_physics.py` and `plot_findings.py` reproduce the analysis from the manifests with the paired checkout's Python. No replay or physical comfort improvement is claimed for a new unimplemented pulsing correction.
