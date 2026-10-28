<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# First drive with the very-low-speed correction; Auto Start/Stop capture

October 14, 2026 local time. Read-only saved-recording analysis. No Comma source/setting changes, restart, firmware operation, active ECU query or transmitted test commands. All decoding/replay after the download ran locally on the Mac.

## Conclusions

1. **The Auto Start/Stop button test is visible through the vehicle's selected/deselected status.** Six rapid alternating state changes appear at 90.88–94.78 seconds, consistent with the user's approximate five-press description. This is strong evidence of the effect of the test, not a literal physical-button edge count. The engine remains on during this sequence. A direct button-request pulse was not identified in the expected main-bus signal, so a Comma on/off control is not established yet.
2. **The new steering revision ran, but the ~15 mph shortfall remains.** At 511.98 seconds and 14.96 mph, diagnostic desired wheel angle is −27.89°, actual wheel −11.90°, before detected driver input at 512.48 seconds. Command mode remains active. This recording does not demonstrate that the added 10% fixed or consistently improved the issue.
3. **No lateral TX rejection explains the selected weak-steering examples.** Local recorded-stream replay rejects zero lateral messages; selected EPS state is active control/limit not reached, and hardware blocked counters stay flat in those examples. This is not a clean bill for every message/counter in the drive.

## Capture and configuration

All **10 contiguous completed segments** were copied into the private Mac backup and individually checked against device SHA256/byte counts: **89,174,053 compressed bytes**. The route spans approximately 590 seconds; its transmitted-command stream spans 573.06 seconds. Maximum speed from full-rate carState is **30.18 mph**, so this drive provides no fresh ~45 mph road comparison.

Recorded initData identifies parent **76d78d46fc8713f2f6b1147af02e5aed07bf15a1**, branch `codex/navigator-very-low-speed-trial`; this parent pins the deployed child. CarParams confirms flags **15**, Ford safety parameter **10**, angle control, wheelbase **3.1115 m**, ratio **19.6**, and the current forced Expedition fingerprint. This is the installed +10%-through-15-mph trial, not the previous master-drive baseline.

The command reconstruction using the new strategy agrees with recorded commands to median absolute error **0.000145 rad** in 481 selected 10–15 mph samples, versus **0.004073 rad** with the preceding trial. The wire encoding step is 0.0005 rad. The new reconstruction's p95 error is **0.003179 rad**: timing/downsampling and state alignment still matter in fast transients, so this is not exact original controller-state reproduction. The same held-input calculation yields median new/old command ratio **1.10**; that confirms the intended command increment, not physical improvement.

Raw rlogs remain private under the latest pre-trial backup's `post-vlow-drive` directory. No route identifiers, GPS, images, odometer values, VIN or device serials are exported here.

## Auto Start/Stop: observed state sequence

User confirmed pressing the **Auto Start/Stop disable button**, not the ignition button. The captured main-bus message is `Stop_Start`, decimal address **358 / 0x166**, signal `StopStrtDrvMde_D_Indic`. Its existing DBC values are 0 = selected, 1 = deselected, 2 = indirect deselection, 3 = unused. All main-bus frames here use 0/1.

| Time from recording start | Auto Start/Stop selection | Speed | Engine operating state |
| --- | --- | --- | --- |
| <private clock time>.88 | Selected / enabled | 15.37 mph | On |
| <private clock time>.38 | Deselected / disabled | 15.30 mph | On |
| <private clock time>.18 | Selected / enabled | 15.19 mph | On |
| <private clock time>.88 | Deselected / disabled | 15.17 mph | On |
| <private clock time>.58 | Selected / enabled | 15.13 mph | On |
| <private clock time>.78 | Deselected / disabled | 15.14 mph | On |

The state remains deselected for the rest of driving until ignition shutdown. An initial transition at 3.68 s and the final shutdown clearing are kept separate; neither is counted as a deliberate button press. Recorded engine state (`VehicleOperatingModes`, 0x167) is On throughout the six-change burst. Selection status is not proof that automatic stopping would occur: the vehicle was moving, and other vehicle conditions govern engine shutdown.

Native DBC parser cross-checks agree with the extracted fields on **5,901 main-bus Stop_Start frames**, **5,901 Compressor_Req_FD1 frames**, and both received main-bus APIM request frames.

### What this establishes for a future Comma control

- **State visibility:** good evidence. Reading actual selected/deselected state is a useful foundation for status display and confirmation of a future command.
- **Physical request / writable command:** unresolved. `Compressor_Req_FD1` (0x326), `StopStrtDrvMde_B_RqBtn`, stays 0 in all 5,901 main-bus frames, including the burst. `APIM_Request_Signals_FD1` (0x105), `StopStrtDrvMde_B_RqBtn3`, appears only twice on the main bus and stays 0. Same-address traffic on bus 1 is not assumed to have the main-bus DBC meaning; its constant high bit is not a stream of button presses.
- **Current support:** the paired Ford Panda TX allowlist does not permit either candidate request address, and the current controller has no Auto Start/Stop actuation path. A UI preference alone would not switch the factory feature.

Next research is to identify the genuine OEM request path, network visibility and message integrity/interaction, then design narrowly scoped controller/safety support with reliable status confirmation if the hardware path permits it. Do not treat the status bit as a transmit command or assume a named DBC request is proven writable. No implementation or active probing was performed.

## Steering after the +10% correction

Both the prior 17-segment master drive and this drive were re-extracted using full-rate **100 Hz carState/carControl**, retaining the calibrated motion and TX grids. This improves rapid-transient matching compared with the earlier 20 Hz state/control export. Small numerical differences from earlier reports reflect this refinement; their original files were not overwritten.

Selection requires lateral request active, transmitted mode 1, no detected steering press, valid CAN/calibrated motion/vehicle parameters, bounded timestamp skew, ≥5 mph and meaningful requested yaw. Actual curvature uses calibrated Comma IMU yaw divided by speed rather than the biased CAN-yaw field.

Two useful windows before the first detected press in each episode:

| Relative time | Median speed | Selected time | Median actual/requested curvature | Median absolute wheel-target error |
| --- | --- | --- | --- | --- |
| 105.43–107.43 s | 13.79 mph | 2.00 s | **0.531** | **15.17°** |
| 510.48–512.48 s | 14.93 mph | 2.00 s | **0.295** | **11.43°** |

These ratios describe growing/transient requests, not a recommended gain multiplier. They must not be inverted into a 2–3× tuning change. Below-threshold driver torque and imperfect time alignment remain possible confounders.

At 106.98 s, desired/actual wheel are approximately **+29.63° / +14.40°**, before first detected press at 107.43 s. At 511.98 s, they are **−27.89° / −11.90°**. The desired wheel value is an upstream model-derived diagnostic; the Ford wire command is path angle, not that wheel-angle target.

In both two-second windows, EPS reports continuous lateral control in progress, limit not reached, extended capability available. Blocked counter stays respectively **0** and **14**. Peak transmitted path angles are 0.089 and 0.107 rad, well inside −0.5/+0.5235; largest per-frame steps are 0.006 and 0.012 rad, below the local 0.055 bound. The deviation clip only starts above 9 m/s (~20.1 mph), so it is inactive here. This again points toward insufficient effective conversion/response rather than those limits as the explanation.

A third inspected 14.76 mph window at 163.93–165.93 s overlaps recovery from a preceding manual override, with EPS available→active and a rate-bound-sized step. It is not used as a clean pre-intervention calibration example. Later mode-0 intervals in the sharp-turn episodes follow detected driver steering/large wheel angle; they must not be mistaken for the cause of the earlier shortfall.

### Before/after comparison: mixed, not a measured handling improvement

| Selected speed bin | Prior actual/requested median | New median | Prior/new median absolute wheel-target error |
| --- | --- | --- | --- |
| 10–15 mph | 0.325 | 0.394 | 5.56° / 10.29° |
| 15–20 mph | 0.438 | 0.366 | 3.91° / 3.49° |
| 20–30 mph | 0.492 | 0.605 | 1.61° / 1.50° |

The new 10–15 mph selection has 24.05 s of meaningful turn demand versus 11.95 s before, and different request magnitudes/turn shapes. These aggregate changes are **not causal improvements or regressions**. Higher ratio alongside larger wheel error is one sign of differing turn composition.

After matching speed, turn magnitude/direction and slower demand change with ≥20 frames in each drive, **no sub-20 mph stratum qualifies**. Only two 20–30 mph positive-direction strata remain; one ratio decreases (0.347→0.320), one increases (0.552→0.640). They contain only a few seconds each and are not verified identical roads. This is insufficient to claim an overall improvement. The strongest supported conclusion is that the patch is active and substantial low-speed undertracking remains.

## Drive health and recorded native safety replay

- Big model: **11,336 / 11,336** sampled messages; execution median **39.59 ms**, p95 **40.27 ms**; reported frame drops **0 throughout**.
- GPU maximum 51°C; memory maximum 70°C; no sampled supply faults. No model fallback is evident as an explanation of the selected turns.
- Five temporary steering-fault samples near startup/end (10.86, 580.46/580.51, 590.06/590.12 s), outside the selected examples; no permanent fault samples. Their causes are not established here.
- Panda RX-invalid samples: zero. Hardware blocked maximum 14, positive counter increments totaling 18 across resets/configuration changes.
- Matching native recorded-stream replay: **286,561 relevant RX**, zero RX rejections; **34,066 TX** after Ford configuration, **zero lateral rejections** and **10 button-message rejections** at five permission-false transitions (each repeated on buses 0/2). One initial RX-check warmup invalid tick; 486 TX before Ford configuration excluded.

The hardware counters and offline rejection count are not fully reconciled. No claim is made that every hardware counter increment was a button rejection. Replay does not reproduce forwarding/hardware timing or prove all vehicle commands accepted. No lateral rejection or counter increment coincides with the two selected weak-steering windows.

## Artifacts and verification

`extract.py` decodes anonymous numeric/status fields; `analyze.py` reproduces selection and before/after strata; `detail.py` cross-checks DBC decoding, command reconstruction and selected windows. `extract_safety.py` and `replay_recorded.py` operate exclusively on saved files using the existing matching native library. `verify.py` passed assertions for revision/configuration, six state changes, DBC cross-checks, residual undertracking, selected limiter/status observations and model/safety results.

Supporting outputs: [analysis](../../navigator-reference/PRIVATE_ARTIFACTS.md), [detailed state/steering evidence](../../navigator-reference/PRIVATE_ARTIFACTS.md), [drive health](../../navigator-reference/PRIVATE_ARTIFACTS.md), [recorded safety replay](../../navigator-reference/PRIVATE_ARTIFACTS.md). Temporary compressed numeric exports are in `/private/tmp`; retain private raw backups for future reproduction. Sample counts are correlated time samples, not independent road trials. All conclusions remain limited to the observed recording.
