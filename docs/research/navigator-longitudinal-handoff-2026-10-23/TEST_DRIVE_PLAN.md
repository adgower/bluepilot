<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# OEM comparison and future Alpha validation

October 23,2026. **Collection plan only. Local prototype is not installed or cleared for road testing. Leave Alpha off now.** Current Comma remains20.1/current paired steering, OEM ACC,1.20/0.97.

## Which mode tests what?

- OEM ACC with Alpha off: useful reference for comfort, speed/following behavior, OEM brake/precharge/propulsion/torque responses and vibration. It does not exercise the handoff prototype or Autospeed gas/brake control.
- Alpha on, after a separately reviewed/authorized installation: enables openpilot's Ford longitudinal actuation. Your current source uses upstream Autospeed planning; the former separate ExperimentalMode toggle is removed. Scene-aware planning and the Ford actuator map are different causes to classify.
- Never enable Alpha on the current install expecting to test this local code. No new user-facing handoff toggle exists. Local files/flags in a replay do not change device behavior.

## Future activation and rollback, after blockers are resolved

The pinned current UI has Settings → Developer → “openpilot Longitudinal Control (Alpha)” on the large UI; the compact UI labels it “alpha longitudinal”. Visibility requires a non-release build and supported CarParams. Its confirmation changes AlphaLongitudinalEnabled and requests an onroad cycle. The UI explicitly warns Alpha may disable AEB. Do not substitute Joystick/Longitudinal Maneuver Mode, or force a hidden preference by SSH.

Change mode only while safely parked and disengaged. After an authorized candidate installation, enable via its normal confirmation, let the requested process cycle finish, and verify actual live CarParams.openpilotLongitudinalControl, expected Ford safety configuration, model/radar/lead health and no faults while stationary. A UI switch alone does not establish the correct active mode. Record exact pair/config for both modes.

To return to OEM: stop safely, disengage, disable Alpha through the same UI, let reinitialization finish, and confirm actual live stock-longitudinal configuration and normal ACC operation before further driving. No settings/reboot interaction while moving. Hardware/source rollback remains separate if runtime cannot return normally.

## Staged progression

1. **Now:** collect ordinary OEM ACC drives on a familiar legal route. Retain owner steering settings, following-distance choice and ordinary supervision. Note approximate time/location/conditions of uncomfortable braking, acceleration or intervention after stopping; do not operate a logging UI while driving.
2. **Before any Alpha road test:** resolve launch/release semantics and missing/stale pitch/timing policy, integrate/review/build, run retained steering and native RX/TX replay, back up and perform actual parked acceptance. Replay does not establish vehicle response.
3. **First physical Alpha stage:** a controlled setting appropriate for low-speed evaluation, clear of people/obstacles, with sufficient room and normal human control. Confirm routine disengagement/braking, modest acceleration, gentle slowing and stop/restart. Do not test collision avoidance or deliberately approach hazards. Any shaking, unexpected surge, delayed braking or unreliable restart ends the trial.
4. **Ordinary low/moderate-speed evaluation:** only after the prior stage is satisfactory, compare routine similar maneuvers with OEM references. Check modest grades, release and following without forcing a set of maneuvers in traffic. Progress by demonstrated behavior, not by a fixed number of minutes or one smooth turn.
5. **Highway last:** only after lower-speed and grade/release evidence is acceptable. No80–85mph reproduction of the historical incident is requested. Follow posted limits. A local replay pass is not clearance for high-speed operation.

If vibration returns: take over/disengage promptly, brake/control manually as necessary and stop in a safe place before any mode changes. Do not keep the feature engaged to collect a longer sample. Preserve logs and mark the approximate event afterward. No test can promise the historical shaking will never recur.

## “At least as good as OEM” scorecard

Use matched phases of repeated trips, not whole-drive averages across different traffic. Match route/direction, speed, grade, lead situation, following setting, tire pressure/load, temperature/warm-up and road surface as practical. Traffic and driver interventions make comparisons observational; report uncertainty and avoid treating individual samples as independent trials.

| Dimension | What to compare | Acceptance interpretation |
| --- | --- | --- |
| Basic control | Faults, unexpected engagement, brake/cancel response, interventions, stopping/restart, lead behavior | Any safety-relevant issue is a blocker; never trade this for comfort/fuel |
| Comfort | Actual longitudinal acceleration and filtered jerk distributions; repeated acceleration/braking cycles and onset/release delay | Improvement must not conceal late braking or excessive acceleration lag |
| Historical shaking | Steering-angle3–15Hz vibration and available IMU/wheel signals, speed/road/brake phase matched | No repeat symptoms; command smoothing alone is insufficient proof |
| Brake/propulsion coordination | Requested deceleration versus valid propulsion; ECU brake-active/torque and propulsion-torque overlap, duration and transitions | Current command contradiction removed; ECU overlap still needs interpretation/response latency and road context |
| Speed/following | Comparable speed error/overshoot, lead-gap behavior and unnecessary braking | Autospeed may intentionally slow for a scene; distinguish intended planning from actuator tracking error |
| Economy | Validated fuel-used/rate over comparable distance and repeated matched legs, or consistent longer-trip vehicle fuel readings | Fewer command overlaps is a proxy only; insufficient data means no fuel-saving claim |

Existing torque signals report ECU estimates, not independently measured brake pressure, engine fuel or wheel force. No validated consumed-fuel channel has been established in this work. Do not use throttle percentage, “no overlap” or one trip-computer snapshot as proof of fuel economy. Fuel instrumentation, if needed, must be separately scoped; this task authorizes no active OBD/ECU query.

There is no honest way to ensure OEM-equivalent performance just by enabling a toggle. Establish non-inferiority on safety/response first, then comfort, then economy, with repeated representative evidence. The initial local spike is not yet ready for this progression.
