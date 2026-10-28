<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Remaining ~15 mph steering response and Auto Start/Stop command feasibility

October 14, 2026 local investigation. No SSH, Comma change, ECU query, vehicle CAN transmission, controller/firmware modification, or preference change. Only saved local recordings and pinned source were used for vehicle analysis. Public code research was also checked for an Auto Start/Stop implementation. The paired installed-source checkout remains unchanged at parent `76d78d46fc8713f2f6b1147af02e5aed07bf15a1`, child `f50241ca59d866af275ff6c34fb407b93094e892`. Owner factors **1.20/0.97** remain intact.

## Steering decision

The next repair should target the **Ford curvature-to-path-angle conversion and its response dynamics**. Another uniform percentage increase is not supported as a complete solution: the latest drive contains both a delay-sensitive example and a persistent under-response example.

A useful next local controller comparison is:

1. Retain current feedforward, pinion option and 1.20/0.97. Evaluate a separately bounded, damped **tracking-error correction** in the Ford path-angle stage below ~20 mph, smoothly absent by 25 mph. This would react to the remaining discrepancy instead of multiplying every request equally.
2. Assess request anticipation/response timing separately, because a later turn is consistent with substantial lag. Do not change the global actuator-delay setting or combine an unmeasured lead term with higher gain in one step.
3. Compare with a better low-speed feedforward calibration when sufficient steady turning evidence exists. Adding feedback is a candidate, not proof that feedback is the only or best cure. Vehicle EPS and upstream planning already contain feedback; the absence identified here is specifically continuous wheel/curvature-error correction in this fork's conversion stage.

No best numerical gain, filter or delay is established. A genuine handling fix cannot be certified by replaying fixed recorded vehicle responses. This task identifies the next implementation seam and rejects overly simple explanations; it does not declare the physical issue fixed or introduce a new production controller.

## New discrimination: response delay differs between examples

`probe.py` compares the **same base samples at every tested delay**, excludes driver-detected samples and one second after detected steering input, and requires future comparison samples to remain before the next intervention. It uses independent calibrated motion for actual curvature and full-rate carState/carControl from the prior and post-correction drives.

| New-drive base interval | Common base frames | No shift: actual/requested | +0.5 s | +1.0 s | Interpretation |
| --- | ---: | ---: | ---: | ---: | --- |
| 105.43–106.43 s | 19 | 0.532 | 0.519 | **0.516** | A one-second shift does not explain this persistent shortfall |
| 510.48–511.48 s | 20 | 0.143 | 0.562 | **1.061** | A one-second shift largely aligns this portion of growing demand |

For the late example, median paired diagnostic wheel error falls from 8.06° to 0.73° at +1 s. For the earlier example it remains large (14.81° unshifted, 16.43° at +1 s). These are selected transient probes, not identified factory actuator delays or estimates that every turn needs one second of anticipation. The later interval is the earlier portion of the sharp turn, not the whole 510.48–512.48 s episode analyzed previously.

This refines the earlier observation that delay did not fully explain another selection: it **can explain much of some subintervals**, while it does not explain others. Treating all the instantaneous deficit as missing gain risks excessive command when the response catches up. Conversely, a global delay tweak would leave the sustained earlier deficit.

The preceding raw-data report still establishes significant undertracking before detected input, active EPS/no reached limit in the selected examples, flat local blocked counters and zero recorded lateral safety rejections. No new evidence here points to widening limits or changing the yaw source again.

## Confirmed source mechanism and precise change location

The actual installed-revision strategy was invoked with a fixed 15 mph speed and curvature request 0.006 /m. With actual wheel angle set to 0°, −10° and −25°, it produced the **same path-angle request: 0.0724929 rad** in every case, with equal nonbinding initial limiter state. The low-speed application does not automatically add command as tracking error grows. Pinion feedback is used elsewhere, but the deviation clamp begins only above 9 m/s (~20.1 mph).

`LatControlAngle` computes a diagnostic desired wheel angle and saturation indication; it does not supply a corrective torque for this path. Ford `LateralAngle.update` consumes curvature and constructs the path-angle command. Changing only the diagnostic desired-angle value or saturation threshold would not add the needed wire-level correction. Path-angle radians must not be replaced by desired steering-wheel degrees.

A tracking candidate belongs **after the existing curvature-deviation clip and before inherited path-angle range/rate bounds**. It should use the clipped desired curvature and the paired fixed-model pinion measurement with coherent sign/geometry, reset immediately when inactive or on driver steering, and avoid accumulating state through manual override. Any filter/correction state needs explicit reset behavior and speed-transition tests.

For example, a candidate structure is current feedforward plus a capped, damped term proportional to curvature tracking error and a low-speed fade. This describes an architecture, not a selected coefficient or a tested stability result. Do not add an integrator initially. Preserve normal output when the extra correction is disabled and leave source 1.20/0.97 unchanged. Stronger commands still require full paired controller/native safety replay; passing that replay cannot prove closed-loop stability.

Fade the proposed addition completely to zero by 25 mph, preserving the existing 25–45+ mph map. Require byte-identical ≥45 mph generated streams against the installed baseline and synthetic history/transition coverage. Inherited rate-limiter state means formula equality above the fade alone is not universal output equivalence. No current controller was edited, so the previously validated higher-speed source remains intact.

## Why these recordings do not determine a final feedforward curve

A strict steady-admission check required one second of uninterrupted selected data, speed span <0.5 m/s and path-command span <0.005 rad. Neither drive has admitted samples at 10–20 mph under that check. This is a property of the explicit gate, not proof that every turn was physically unsteady.

Relaxing the requirement to ≥90% selected samples and <0.01 rad command span admits only **16 frames (0.8 s) at 10–15 mph** after the patch, with 14 negative-direction and 2 positive-direction samples. At 15–20 mph it admits 21 frames (1.05 s), all positive-direction. Relaxed/shorter-window counts are retained in `analysis.json`. The direction imbalance, correlated samples and driver interventions make a unique left/right steady gain or deadband fit unjustified. An earlier exploratory first-order fit likewise did not identify a deployable response law.

## Auto Start/Stop: local packet experiment completed; sending integration unresolved

The observed six selected/deselected changes remain strong evidence that actual status is readable on main-bus `Stop_Start` (0x166). The expected direct request signal in main-bus `Compressor_Req_FD1` (0x326) stayed zero during the physical button test. Therefore the recorded status sequence does not identify the genuine request message or which network carries it.

`autostop_probe.py` takes an actual saved 0x326 stock frame and constructs an **offline candidate** with only `StopStrtDrvMde_B_RqBtn` changed from 0 to 1. Native DBC parsing confirms:

- Exactly **one payload bit** changes.
- Every other decoded stock signal remains unchanged.
- Existing matching native Ford safety hooks reject the candidate with artificial local controls permission both false and true. Its address is not in the current TX allowlist.

No packet was transmitted, no sender was wired into CarController, and no permissive Panda rule was added. This proves packet shape and current denial, **not vehicle acceptance, correct timing, gateway routing, checksum/counter handling, repeat behavior or status acknowledgement**. A DBC field name alone is insufficient to call this an integrated on/off control.

Before enabling sending, establish the real OEM request path and applicable message integrity/cadence, then implement a bounded request state machine with fresh valid status, explicit desired selection, press/release semantics if required, acknowledgement/timeout, bounded retries and driver override behavior. The paired safety rule must restrict the intended operation and preserve unrelated payload fields; simply adding the entire shared HVAC-message address as generally writable would be broader than this feature. A status-display integration is supported by the capture; actuation remains unverified.

### Existing public implementation checked

[DASS](https://github.com/ig0ist/DASS) is a public Sync3 modification whose own source/README calls the internal `AL2HMIBridge` Auto Start/Stop button API. It reports testing on Sync3 3.4.23188 and lists Aviator/Explorer 2020. This is a useful indication of an infotainment request path, but it does not provide a raw Comma CAN command or establish support for this 2023 Navigator. No Sync modification or as-built change is recommended or performed here. Searches of the checked local Ford controller implementations found DBC definitions, not a verified sender to port.

## Deliverables, checks and limits

- `probe.py`, `analysis.json`: source sensitivity, equal-cohort delay tests and steady-admission sensitivity.
- `autostop_probe.py`, `autostop-probe.json`: non-transmitting candidate shape and intentional native safety denial.
- `verify.py`: passed mechanism/data assertions. It explicitly does not certify physical response, final calibration or factory command acceptance.

Raw inputs are the already-backed-up 17-segment pre-correction and 10-segment post-correction drives. Temporary anonymous numeric exports are read from `/private/tmp`; raw recordings, GPS/VIN and whole packet payloads are not exported here. The native library is the unchanged matching plain Mac debug build, not sanitizer or complete Panda hardware execution. These diagnostic scripts modify no installed source or source-branch files.

Current next action: a separately scoped local tracking/timing prototype comparison while retaining the installed map and limits. Auto Start/Stop actuation requires protocol confirmation before a deployable sender/allowlist integration can be completed. Neither feature is ready to call an actual handling/control fix from the current evidence.
