<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# First master-integration drive: observed steering response

Recorded October 14, 2026 local time; analyzed October 15 UTC. Read-only saved-log analysis. No device settings, source, firmware or control messages changed for this analysis.

## Finding

The late approximately 15 mph segment supports the reported insufficient steering. The current trial already applies its full low-speed weighting below 30 mph, including 15 mph. Extending its speed coverage would not change this case. A separate low-speed response/conversion investigation is justified; this recording does not establish a safe replacement gain.

At 936.03–938.03 seconds from recording start, 40 selected 20 Hz samples had median speed 14.79 mph, no detected driver steering, valid calibrated motion measurements, active steering request and wire mode 1. Median measured/requested curvature was **0.359**, and median absolute diagnostic wheel-target error was **17.04 degrees**. This is a local response ratio during increasing turn demand, not a general percentage of steering capability or a recommended gain multiplier.

| Relative time | Speed | Diagnostic wheel target | Actual wheel | Transmitted path angle | Driver steering detected |
| --- | --- | --- | --- | --- | --- |
| 933.98 s | 14.61 mph | −7.57° | −2.90° | 0.0165 rad | No |
| 935.98 s | 14.78 mph | −17.66° | −7.10° | 0.0430 rad | No |
| 936.98 s | 14.79 mph | −27.34° | −10.40° | 0.0690 rad | No |
| 937.98 s | 14.83 mph | −38.27° | −17.80° | 0.0980 rad | No |
| 938.08 s | 14.81 mph | −36.75° | −24.20° | 0.0940 rad | Yes |
| 938.98 s | 14.57 mph | −65.99° | −66.00° | 0, mode 0 | Yes |

The wheel target is an upstream model-derived diagnostic, not the direct Ford wire command. The actual command is the path-angle signal shown. Curvature response is independently estimated from calibrated IMU yaw divided by speed, rather than the CAN yaw signal under investigation.

Driver detection begins at 938.03 s. Mode 0 follows while the driver steers beyond the existing human-turn threshold; it did not initiate the earlier shortfall. Later wheel agreement includes manual input and is not evidence that autonomous response recovered. Earlier discrepancies around 927–935 s also precede detected intervention; this is not solely one instantaneous reversal. Below-threshold driver torque remains a confounder.

## Limits and safety evidence

In the two seconds before intervention, EPS status was consistently continuous lateral control in progress, limit not reached, extended mode available. The hardware blocked-message counter remained 17 throughout 920–948 s. The matching native offline safety replay rejected no messages in that window.

The largest absolute transmitted path angle in the selected two seconds was 0.102 rad, well inside the DBC range −0.5 to +0.5235 rad. Largest adjacent step was 0.015 rad, below the local 0.055 rad/frame soft rate bound. The curvature-deviation clip only applies above 9 m/s (20.13 mph), so it is inactive at 15 mph. These observations do not support increasing safety/rate limits to address this episode. Transmitted-command observations are not a complete internal-state reconstruction or proof that every unreported EPS constraint is absent.

Whole-drive native replay processed **500,196 relevant RX frames**, with zero RX rejections, and **59,420 TX frames** after Ford configuration. It rejected **3 lateral messages** (546.33, 574.13, 882.48 s) and **14 button messages**, all with replay controls permission false. There was one initial invalid tick while RX checks populated. These transition findings remain separate from the 15 mph episode and deserve follow-up; this is not an all-clear replay. Hardware blocked counter maximum was 19 with positive increments totaling 23 across counter resets/configuration transitions. Offline counts do not fully reconcile hardware counters, and replay excludes hardware forwarding/timing reproduction.

Two downsampled temporary steering-fault samples occurred near 10.95 and 1017.32 s, outside the selected episode; zero permanent-fault samples and zero Panda RX-invalid samples were observed. Do not infer their cause solely from their timing.

## Overall drive and comparison

All **17 contiguous saved rlogs** were copied to the private Mac backup and each compressed file checked against its device SHA-256 and byte count. Approximately 17 minutes were recorded; the command stream spans 1000.16 s. Maximum analyzed speed was **35.08 mph**, so this drive does not validate 45 mph behavior.

Recorded configuration confirms Navigator geometry **3.1115 m wheelbase / 19.6 ratio**, angle control, flags **15** (including pinion and low-speed trial), and Ford safety parameter **10**. The previously verified installed source retains the owner's **1.20/0.97** calibration; this analysis did not re-read or change device source. At 15 mph its gentle endpoint multiplier is 1.15 and tight endpoint is 1.638 (1.30 × 1.20 × 1.05), with full trial weight; it does not add another increase specifically below 20 mph.

Selected active, no-detected-driver-input, valid-motion samples with meaningful turn demand:

| Speed | Selected time, approximate | Median actual/requested curvature | Median absolute wheel-target error |
| --- | --- | --- | --- |
| 10–15 mph | 12.10 s | 0.315 | 5.56° |
| 15–20 mph | 38.70 s | 0.446 | 4.00° |
| 20–30 mph | 48.45 s | 0.485 | 1.65° |
| 30–40 mph | 7.10 s | 0.746 | 0.85° |

These bins contain different curves, directions and transients; they do not measure a causal speed effect, lane wandering, or an improvement percentage. Very short selected coverage at higher speeds limits conclusions.

Against the earlier trial drive, only two slowly changing demand strata met the minimum 20-frame coverage in both recordings. Both were positive-curvature 20–30 mph turns: response ratios rose from 0.186 to 0.346 (gentler stratum) and 0.354 to 0.556 (next stratum). Each comparison has only 2.55–4.20 s per drive, different roads/roll/transients, and a changed upstream model/software baseline. This is limited encouraging evidence, not proof of overall improvement. There were no qualifying matched low-speed strata to establish improvement at 15 mph.

Chestnut used the big model in **19,678/19,678 sampled model messages**, with model execution median **39.61 ms**, p95 **40.37 ms**, and reported frame-drop percentage **0 throughout**. GPU temperature maximum was 51°C, memory maximum 70°C, and no sampled supply faults occurred. This supplies road evidence for this recording, not long-term reliability certification. No model fallback or compute dropout is evident as an explanation of the selected turn.

## Next investigation

Keep the current settings and limits intact while comparing the low-speed curvature-to-path-angle conversion against actual wheel response, steady turns versus growing demand, and response delay around 10–20 mph. A separately bounded local low-speed response experiment could then be evaluated against these recordings and prior 20–40/45+ mph replay coverage. Do not infer a gain by taking the reciprocal of a transient response ratio. Existing replay can verify command compatibility/limits but cannot establish the vehicle response to hypothetical stronger commands.

Also classify the three transition-time lateral safety rejections before calling the migration fully validated. This analysis does not authorize a new deployment or claim the low-speed issue fixed.

## Reproduction and evidence

Private raw recordings remain under the pre-migration Mac backup, outside Git; route identifiers, GPS, images and VIN are not exported here. `extract.py` reads a directory of `segment-XX/rlog.zst`, emits anonymous compressed signals; `analyze.py` compares those signals with the earlier anonymous export; `detail.py` produces the selected-window timeline. `extract_safety.py` exports exact relevant RX/all TX for local `replay_recorded.py`, using the matching master-integration debug safety library. Intermediate input locations currently use `/private/tmp`; retain the raw backup to reproduce after temporary-file cleanup.

Supporting outputs: [analysis](../../navigator-reference/PRIVATE_ARTIFACTS.md), [drive health](../../navigator-reference/PRIVATE_ARTIFACTS.md), [late-turn details](../../navigator-reference/PRIVATE_ARTIFACTS.md), [two-second late windows](../../navigator-reference/PRIVATE_ARTIFACTS.md), [native recorded safety replay](../../navigator-reference/PRIVATE_ARTIFACTS.md). Sampling gates and speed/curvature strata are explicit in `analyze.py`. Samples are temporally correlated, so sample counts are not independent trial counts. Matching uses nearest topic timestamps with bounded skew, not exact controller input replay.
