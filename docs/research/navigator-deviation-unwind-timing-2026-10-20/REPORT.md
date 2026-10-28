<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local investigation: 28 mph deviation and 64–70 mph unwind

October 20, 2026. Saved logs only. No SSH/device access, settings changes, CAN transmission, paired source edits, or installation. Owner **1.20/0.97** preserved. Installed source remains clean at parent `f750d756ca`, child `de70d4f945`.

**Finding:** The tight 28 mph episode contains both real tracking deficit and a fixed-versus-calibrated model mismatch. The native deviation check is active, but calibration mismatch alone does not explain the missing steering. Highway correction suffers serial confirmation and a gradual onset; many short admission opportunities end before any correction appears. The next useful prototype is bounded highway onset timing, not a general gain increase or a wider native deviation limit.

## Evidence and reproducibility

Inputs are the two moving new-code recordings from the [35-segment review](../navigator-post-calibrated-rearm-drives-2026-10-20/REPORT.md), anonymized sessions04/05. Raw files are preserved privately; this folder publishes no coordinates or raw route identities.

`reproduce.py` runs in the paired-build Python environment and deliberately returns1 for the saved symptoms:28mph entry32 clean samples,67.8% median body response;67mph unwind10 clean samples,136.1%. This is an observational regression signal, not a simulated vehicle that can prove a future fix. It remains red because no control fix was attempted.

`trace.py` replays the actual installed factory on original send times and atomic calibration packets. It wraps the fraction calculation for instrumentation, captures incoming wheel/body/calibration, each admission/persistence stage, output residual, and uses the actual CANPacker/fordcan message builder offline. `validate.py` confirms instrumentation leaves every floating output identical to the preceding reconstruction, the source pair stays clean, and quoted episode wire parity holds. Session05 matches all3340 active/unpressed mode1 packed requests exactly. Session04 matches5705/5742; the32-update28mph window matches exactly, including the transmitted shadow-curvature metadata. Unmatched portions of session04 are not used for exact causal timing claims.

## 28 mph: three separate effects

At14:43:27.815–<private clock time>.415CDT, before driver pressure, the vehicle is entering a sharp bend and steering demand is still rising. Median values at original send times:

| Quantity | Median |
| --- | ---: |
| Speed |28.36mph|
| Requested lateral acceleration |2.832m/s²|
| Measured calibrated body acceleration |1.887m/s²|
| Acceleration inferred from calibrated wheel |1.933m/s²|
| Acceleration inferred from fixed native pinion model |2.221m/s²|
| Requested curvature |0.017644/m|
| Fixed-model measured curvature |0.013882/m|
| Calibrated-wheel measured curvature |0.012083/m|
| Curvature after native deviation clip |0.015882/m|
| Actual / requested steering angle |−52.7° /−76.4°|
| Learned / fixed steering ratio |22.003 /19.6|
| Learned angle offset |−2.725°|

Medians are separately calculated, so subtracting displayed medians need not reproduce median paired differences.

1. **Real tracking deficit:** Body and calibrated-wheel estimates agree near1.9m/s², well below2.83 requested. This is not explained by a bad body-yaw reading alone. The fixed model estimates *more* response, not less, and is therefore more permissive during this deficit. A hypothetical equivalent clip based on the calibrated measurement would still clip all32 updates, more strongly.
2. **Actual clipping:** The existing ±0.002/m fixed-pinion deviation band clips all32 updates and the mid-speed addition reports `native_deviation_clip` throughout. Median curvature reduction corresponds to0.297m/s² at recorded speed. This is a request-space calculation, not a claim that removing the clip would add0.297m/s² of physical response. All32 emitted shadow values agree with this clipped curvature at1e−6/m wire resolution. No new native rejection is needed for the host-side clip to limit steering.
3. **Independent model mismatch:** Even if the wheel instantaneously reached the calibrated requested angle, its curvature interpreted by the fixed native model would differ from requested curvature by a median0.002483/m—outside the0.002 band in30/32 samples. Learned ratio, offset, roll, and fixed-model assumptions therefore need reconciliation independently of the real deficit. At the actual measured wheel, fixed-minus-calibrated curvature is0.001799/m; removing offset alone changes the calibrated estimate by+0.000639/m, removing roll by−0.000358/m. These partial changes do not add into an isolated causal parameter attribution; ratio/model-speed effects also matter.

The Ford controller source comments describe roughly2m/s² EPS authority, consistent with the observed response range (body10th–90th percentiles1.65–2.08m/s²). **This is not proof of a hard Navigator EPS ceiling:** this is a1.6s rising-demand entry, not a settled saturation test. Neither an EPS torque limit nor receiver acceptance/actuator internals is measured here. A calibration fix alone cannot be assumed to recover the remaining response; more gain cannot be assumed to overcome an authority limit.

Do not generalize this sharp-turn episode to the entire band. Across clean original-send samples at23–29mph with requested acceleration below1.5m/s², median body response is83.1% over121 updates and **none hit the native deviation clip**.78 of those updates report spent/aborted mid allowance,16 duplicate evidence, with five earlier bounded-correction updates. That is a different lifecycle/evidence problem. Simply widening the deviation limit would not resolve these unclipped deficits either.

## 64–70 mph: where the time goes

The exact-parity session05 separates three serial stages:

1. Current wheel excess must exceed0.5°, with a nontrivial valid calibrated target and fresh inputs.
2. Body acceleration excess must exceed `max(0.1m/s²,10% of demand)`, with a sustained median history; independent wheel history must also establish excess and predict it is not already closing away.
3. The combined fraction must remain positive for five20Hz updates before onset. Correction then increases by at most0.0003rad per update. A CAN path-angle increment is0.0005rad.

The extra combined persistence is applied after the wheel and body histories have already confirmed evidence. Quantization can add another frame before the first effective output change. This is distinct from transport delay or final slew clipping.

### 67 mph episode before the63.5mph steering input

Times below are seconds from the15:01:26.734868CDT recording start:

| Time | Stage | Effect relative to untrimmed roll-aware reference |
| --- | --- | --- |
|411.136|Current body excess0.119m/s² crosses0.100 margin; history not yet confirmed|No correction|
|411.236|Combined wheel/body admission; persistence1/5|No correction|
|411.436|Persistence5/5; floating correction0.0003rad|Same encoded command|
|411.485|Floating correction0.0006rad|First0.0005rad encoded reduction|
|411.686|Floating correction reaches0.0018rad|0.0015rad encoded reduction|
|411.736|Predictive wheel excess shrinks as wheel catches up|Correction decreases|
|411.785|Floating correction0.000163rad|Encoded reduction is zero|

Thus approximately**0.35s** elapses from the first current body-margin crossing to the first encoded correction; approximately0.25s follows fully combined admission. The earlier50ms floating change rounds to the same command. These are trace timings, not an identified vehicle delay constant. During the quoted0.5s excess episode, the installed output is also identical to the previous policy, explaining why the latest history fix does not improve that particular episode.

### 69 mph excess episode

At351.335s current body excess exceeds the margin, but the sustained-history check has not passed. Combined admission begins351.435s; the first encoded reduction appears351.635s. The admission burst lasts six updates, producing only two nonzero reduction updates, both about one encoded step. By351.735s the wheel prediction is closing and the unwind latch is set; withdrawal occurs while body motion still lags. Retaining body-only correction here would risk fighting the wheel's recovery, so this is not evidence to remove predictive release.

### Entire drive, not only selected episodes

Session05 contains29 active/unpressed64–70mph positive-fraction admission bursts;20 are shorter than five updates. Nine bursts produce a reduction and an encoded change. Within471 clean meaningful high-speed updates,130 have a positive fraction but77 of those still produce no floating reduction.53 produce some floating reduction;43 produce a smaller encoded magnitude than the untrimmed reference. Only16 of the471 have a different packed command from the preceding installed policy. These counts are correlated update coverage, not independent driving trials.

The final prototype slew guard and release-pending state are not active in those clean updates. No native deviation clipping occurs in the clean64–70mph samples. The main restriction is therefore admission/persistence/onset and protective withdrawal, not the final soft-rate limiter. Quantization suppresses some small effects but does not explain the full lack of improvement.

## Hypotheses: results and limits

| Hypothesis | Result |
| --- | --- |
|28mph is only a fixed/calibrated model mismatch|Rejected as a complete explanation. Mismatch exists, but wheel/body confirm a genuine deficit and calibrated-reference clipping would also occur.|
|Unwind waits too long after evidence agrees|Supported: repeated short bursts and an additional~200ms combined persistence delay before floating onset.|
|Final slew or repeated speed weighting blocks all output|Final slew not binding in the inspected clean high-speed samples. Installed candidate has the once-faded wheel term; no additional speed-factor bug was demonstrated.|
|Quantization erases the correction|Partly supported; some small reductions disappear, including the first67mph onset frame. Most restriction precedes encoding.|
|EPS saturation/physical lag explains the rest|Plausible, not proved. High-demand entry and delayed body recovery support further investigation, not a hardware-limit or causal-response claim.|

## Recommended next design

- **28mph:** retain native limits and1.20/0.97. Treat sharp high-demand entry separately from the lower-demand spent/aborted allowance. Establish a consistent calibrated target/native-reference diagnostic contract before considering any control change; do not substitute a learned model into Panda or enlarge the native error band on this evidence. Trace lower-demand budget abort/distinct-source history independently if improving the whole23–29mph band.
- **64–70mph:** prototype reusing already confirmed, distinct wheel/body history for onset rather than adding an independent five-update wait after that confirmation. Preserve current valid-data checks, wheel/body agreement,0.5° deadband, body margins, bounded magnitude/rate, driver withdrawal, and predictive catch-up release. First evaluate earlier effective packed onset, not merely more floating correction. No minimum-step push or larger cap is justified yet.
- For such a prototype, require the full generated-controller/native replay, transition and abort cases, exact source pinning, no additional native rejects, and protected lower-speed/40–50mph/>=75mph parity. Frozen-log output changes would still not prove improved physical tracking. No prototype, paired integration or device activation was performed in this task.

## Files and rerun

`trace.py` takes private anonymized recording directory and output directory; run through `../navigator-paired-calibrated-rearm-build-2026-10-20/run.py` to use the pinned environment. Run both traces first, then `summarize.py`, `targeted_metrics.py`, and `validate.py`. `reproduce.py` intentionally remains a red saved-symptom check. Evidence is in `findings.json`, `targeted-metrics.json`, `validation.json`, and per-session `detail.json`/`trace.csv`/scene results. The scripts parse logs and pack messages into local memory only; they contain no transmission path.
