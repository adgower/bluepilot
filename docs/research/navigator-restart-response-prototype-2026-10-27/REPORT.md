<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local restart response diagnosis — 2026-10-27

The saved session proves an unusually late **received target-second-gear selection**, accompanied by sustained positive planner demand. It does not isolate why the TCM selected that target late. No new RPM cap, gear command, or producer shaping module is justified by the OEM contrast. This folder contains a reproducible read-only diagnosis and five observed-event regression assertions; it contains no installable runtime change.

## Exact received timing

These are original CAN receive-event timestamps, with causal past state/control/PID joins, rather than the existing 100 ms CSV's first sampled values:

| Event (CDT) | mph | RPM | actual / target gear | planner / raw / I (m/s²) |
|---|---:|---:|---:|---:|
| <private clock time>, first target second | 18.885 | 3602 | 1 / 2 | .896 / .924 / .028 |
| <private clock time>, RPM peak | 21.154 | 3946 | 1 / 2 | .770 / .851 / .081 |
| <private clock time>, first actual second | 23.373 | 2858 | 2 / 2 | .542 / .540 / −.001 |

Target-to-actual reporting delay is 2.380894 seconds. Peak-RPM telemetry joins are all less than 28 ms old; long control is active and gas/brake pedals are not pressed. Gear target and actual values are received telemetry, not controller commands. A target-field change is not proof of an ECU's internal shift decision timestamp.

At approximately <private clock time>–06, target demand reaches about 1.3–1.4 m/s² and propulsion command about 1.5–1.56 while speed rises through about 7–11 mph. By the RPM peak, planner demand is over nine times the stored integral term. The observed high-RPM event therefore cannot be attributed solely to the roughly .08 integral at the peak. Prior accumulated integral or command history could still influence vehicle/TCM behavior; frozen-input replay cannot resolve that causality.

## OEM comparison and why no additional cap was implemented

The retained October 26 shift-event analysis contains four OEM first-to-second events: target-second at 8.746–9.133 mph, peak RPM 2100–2636, and target-to-actual reporting delay 1.739–2.221 seconds. Eleven older Alpha events target second at 9.025–10.690 mph; six newer examples include five ordinary shifts and one earlier 3946 RPM exception. Today's 18.885 mph target selection is over twice the upper OEM speed; its completion delay is only about 7.2% above the OEM maximum.

The OEM pre-shift propulsion means are approximately 1.62–1.75 m/s² and include higher commands than today's approximately 1.56 m/s² restart peak. Reducing today's acceleration merely because RPM is high has no established threshold or causal justification from those examples. The examples differ in route, grade, lead behavior and history; they are useful structural contrasts, not matched physical trials. The existing prediction/resume-field hypothesis is also insufficient: ordinary Alpha shifts use those same fields.

A separate local producer shaping policy would require an independently justified response objective (for example, measured recovery jerk under matched conditions), a concrete bound earned from observed delivery constraints, and full chronological producer/allocator replay. It must preserve immediate signed braking/downward target response, clearance, and continuity through 3 m/s (~6.7 mph), without resetting integral or forcing gear. The main coordinated coast/recovery experiment already addresses earned command reductions; this diagnosis does not introduce an unsupported second shaping rule.

## Reproduction and limits

Run `analyze_restart.py` using the integration environment Python, then `python -m unittest discover -s <this-folder> -p 'test_*.py' -v`. Analysis verifies SHA-256 of both retained thin and CAN arrays and records the prior comparison-summary digest. Five assertions pass: shift ordering, fresh pedal-free joins, relative target-speed versus delay outlier, planner contribution, and OEM command ordering.

The inputs reside in the already retained private cache referenced by the adjacent road-review manifests; no large arrays were copied. These tests validate the diagnosis only. They are not full controller replay, native safety, physical comfort/RPM improvement, device, or road validation. No paired branch, source controller, SSH session, vehicle, or CAN output was changed. The brief initial received-brake-torque overlaps remain the main replay owner's exact consumed-feedback audit; this report makes no clearance-breach claim from nearest CAN joins.

## Target-speed packet hypothesis: isolated shadow exploration

Inspected current `carcontroller.py` call: `create_acc_msg(...v_ego_kph=V_CRUISE_MAX)` retains the TODO to investigate desired speed. `fordcan.py` sets prediction to −5 and writes the supplied target. The prior 168-segment / 16-route protocol investigation independently recovered cruise setpoints from raw OEM records: the OEM target is closer to measured vehicle speed than setpoint in 82–91% of eligible samples per active route. Its median absolute difference from current speed is 2.2–2.8 km/h. Neither literal setpoint nor an exact measured-speed copy reproduces those semantics; retrospective best horizons vary. No matching decelerating rolling OEM launch exists in that study's selected cohort. The constant Alpha −5/145 packet fields coexist with ordinary and exceptional shifts and zero-to-24-change pulsing windows.

For reviewable exploration, `shadow_target.py` substitutes only the DBC-defined target-speed bits in a local byte buffer when given a finite, independently valid cruise setpoint. Invalid input returns the original packet. This has **no runtime installation hook** and makes no vehicle I/O. It illustrates the proposed literal-setpoint hypothesis without promoting it to a selected fix.

`shadow_native_probe.py` compiles current child native safety locally and compares baseline/shadow packets at 40, 112.65408 and 145 km/h across inactive propulsion, positive propulsion and braking, with synthetic native permission both off and on. All **18 paired native unit cases pass**: decoded target is within its 0.25 km/h quantization tolerance; all other decoded fields and bits remain unchanged; native acceptance equals baseline. The receipt records current child SHA and native/source hashes. Synthetic permission is forced only inside the isolated test library. This is **not recorded native replay**, ECU response, or evidence that substitution improves RPM or shifting. It does not change clearance, 1.20/0.97, longitudinal demand, or braking. An actual runtime target/prediction policy remains blocked on independently identified field semantics or controlled causal evidence.
