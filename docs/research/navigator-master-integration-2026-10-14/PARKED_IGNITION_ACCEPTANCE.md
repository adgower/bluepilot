<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Parked ignition-on acceptance — October 14, 2026

User confirmed being stationary in the driveway on Wi-Fi and authorized ignition-on checks. Tests consumed existing runtime topics and files only; no extra diagnostic ECU requests, engagement requests or steering test commands were injected. No source or driving preference was changed. Vehicle remained in Park at 0 m/s; assistance/controls remained disabled.

## Findings

- Live manager/source: `6ae31161b73de2ce5043f708569759ac5f55f283`, `codex/navigator-master-integration`; parent and child source clean. Owner 1.20/0.97 constants reconfirmed unchanged.
- Actual live CarParams identify the forced `FORD_EXPEDITION_MK4` profile, Navigator wheelbase 3.1115 m and ratio 19.6. Flags **15** include both pinion feedback and low-speed trial. Live Panda and CarParams both select **Ford / safetyParam 10**. Stock longitudinal remains selected.
- All 11 observed topics are alive and valid at the end of the 59.67-second window, including live CarParams, cameras/model-dependent states, controls, calibration and driver monitoring. No unexpectedly stopped required process.
- CAN valid, no timeout. No reported temporary/permanent steering fault, ACC fault, noncritical car fault, invalid vehicle sensor or car-not-ready flag. Calibration reports calibrated. No selfdrive alert text.
- **Big-model inference confirmed** across all 120 sampled model messages: approximately **20.00 frames/s**, **39.43 ms** mean sampled execution time, **0% reported frame drops** in those samples. This resolves the earlier USB-identity-only uncertainty for this stationary test.
- Powered accelerator telemetry at the final sample: GPU 50 C, memory 70 C, 29 W, 52% GPU utilization, PCIe LTSSM 120 (0x78/L0), supply 13.91 V, no supply fault.
- Separate 16-sample passive Panda window: zero RX-invalid and TX-blocked counters throughout; no RX-check invalidity, heartbeat loss, SPI errors or Panda faults. This is stationary evidence, not a resolution of earlier drive-counter attribution.
- DisableUpdates and both Ford options remain enabled. Alpha and Experimental mode remain off. No new steering tuning or mode changes.

## Limits and next work

The first short probe used current CarParams storage because the slow CarParams topic had not published into its observation window. The longer probe received the actual live topic. An initial instrumentation attempt referenced the retired liveCalibration service; it was corrected to extrinsicsCalibration before data collection and changed no device state.

This establishes powered stationary startup and big-model operation for about one minute, not engagement behavior, wheel response, sustained thermal reliability or improvement in 20–40 mph/sub-20 mph handling. No road test or actuation test was performed. Subsequent road data and comparison remain separate; the current low-speed trial remains experimental.

Detailed raw evidence is private on device and Mac under the existing pre-migration backup, in `parked-ignition-check-60s.json` and `parked-panda-check.json`. No VIN, device identity or credentials are included here.
