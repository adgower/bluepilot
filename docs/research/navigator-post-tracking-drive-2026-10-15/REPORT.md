<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Latest drive:15mph tracking correction assessment

**No convincing15mph improvement is established.** Broad averages are slightly better, but a tighter matched-road comparison is effectively flat, under-response remains substantial, and the new correction acts only briefly. Nothing on the Comma was changed: SSH/listing/hash/download only; all extraction, reconstruction and safety replay ran locally. No source/settings/service changes, active ECU queries or CAN transmission.

## Coverage and configuration

Downloaded all17 complete available rlog segments (142,713,419bytes), contiguous0–16, verified against device SHA256/size. Recorded command coverage spans981.28s. Both on-device source revisions and recorded startup metadata identify parent74f66e7a0bf1dc0718431532948ece2c4fb0041c / child1b965caadd4a6aea4d09985532bf7cca6c0873ca. Recorded startup Params explicitly confirm tracking, pinion and low-speed preferences enabled. Comparison baseline is the preceding10-segment very-low-speed drive, parent76d78d46fc8713f2f6b1147af02e5aed07bf15a1. Existing1.20/0.97 source is retained.

Command timestamps are strictly increasing, median~50ms, with no>150ms gaps bracketed by qualifying active13–17mph frames. All exported numeric rows finite. Raw source/geographic data remain in the private Mac backup; reports omit coordinates, VIN, route/account/device IDs and images.

## Observed response around15mph

Primary comparison uses outgoing20Hz angle-command frames, past-only joins, lateral requested and wire mode1, no detected driver steering input and>1s since prior detected input, valid CAN/no steering faults, calibrated valid motion/vehicle estimates, lane change off, no blinkers, request magnitude>.001/m and input-age checks. Body response uses calibrated IMU turn rate divided by speed; wheel response uses the installed fixed pinion vehicle model. Neither is an independent lane-position measurement.

|13–17mph cohort|Previous|New|
|---|---:|---:|
|Clean command samples|380|821|
|Median body turn/request|36.9%|41.3%|
|Median wheel-model response/request|45.9%|52.7%|
|Also steady-demand samples|97|214|
|Steady body turn/request|44.4%|45.4%|
|Steady wheel-model response/request|52.6%|53.4%|

The broad+4.4/+6.8 percentage-point changes are descriptive, not a treatment effect. With steady-demand filtering, gains shrink to about+1.1/+0.8 points. New clean frames still have body response below70% of request in86.1% of samples.

A request-magnitude/direction/speed-matched steady cell has body response41.0%→48.9%, wheel51.4%→52.9%, but only44 versus31 serial frames; one other common cell is at20–25mph with discordant IMU/pinion changes. This is insufficient to generalize or infer a causal percentage improvement.

Private GNSS matching within10m, heading20deg, speed1.5mph, same request sign and request-magnitude ratio0.75–1.33 finds42 one-to-one13–17mph clean frame pairs, median separation3.61m. Body response31.6%→32.2%; wheel47.5%→44.5%. None also pass both drives' steady-demand gate. Serial samples from short turns are not42 independent trials. This tighter descriptive comparison does not confirm meaningful improvement; it does not prove the change worsened steering either.

## Did the new correction act?

Yes, detectable added outgoing commands are present. The previous drive has zero visible extra-command frames at the same>1.5mrad screen. The new drive has29/1,730 active13–17mph command frames without detected driver steering input above that screen—about1.45s of86.5s sampled active time. Smaller terms can fall below the screen. Past-input reconstruction of the exact installed strategy predicts31 extra-term frames across active10–20mph samples. In the29 visible frames, actual outgoing versus reconstructed candidate residual is0.000112rad median/0.000206rad95th percentile, comparable to encoding/input-join noise. This supports genuine command activation, not merely an enabled parameter.

These are recorded sendcan requests. They are not direct internal strategy instrumentation, independent confirmation of ECU receipt or a physical steering-authority measurement.

Detectable bursts start near889.73,895.93,897.08,898.68 and909.23s after recording start (roughly14:50–<private clock time>), at13.5–14.5mph. Each lasts only~0.05–0.4s. Encoded residual can slightly exceed the unencoded0.0075rad cap because of quantization/input timing; it is not proof the internal bound was exceeded.

The first weak turn illustrates the limitation: body response is already weak near886.3s, while desired curvature rises from~.001/m to~.015/m. The steady-demand requirement repeatedly prevents admission. Extra command first becomes visible at889.73s; detected driver input starts around890.06s, about0.3s later, resetting the term. The subsequent response rise includes manual steering and cannot be credited to the patch.

Across visible correction frames, only9 retain a clean steady request for the next1s, and zero retain one for2s. This drive therefore does not provide a sustained clean corrected-response interval to establish benefit or closed-loop stability. The most useful next local experiment is admission/release behavior during a ramping turn request, preserving the response-onset, catch-up, driver, freshness and speed guards—not simply raising the global1.20 factor or removing safeguards.

## Health and safety observations

Big model stays selected, no reported model drops in exported samples; maximum sampled GPU51C/memory70C. One supply-fault sample occurs0.278s after route start, before CarState was available; it does not coincide with correction bursts. Brief temporary steering-fault flags occur at stationary startup and~1.4mph shutdown, none in the selected15mph correction intervals. No permanent steering faults or sampled RX-check-invalidity.

Hardware blocked counters are not zero over this drive:7 increments before Ford safety initialization plus7 during Ford mode. The Ford increments occur near409.42,533.12,548.02 and852.51s; none coincide with correction bursts starting889.73s. One is reported while lateral requested at~27.8mph, where the added term is zero by design. They must not be silently described as fixed or harmless.

A local native replay of exact recorded relevant RX/all TX reproduces6 Ford-mode rejections:2 angle0x3d6 frames with controls disallowed and4 button0x83 frames, with zero relevant RX rejected and one initial warmup invalid tick. It does not reproduce the seventh hardware increment (~548s); actual hardware timing/forwarding/permissions are not fully reproduced. Thus attribution remains incomplete. No replay rejection occurs during detected added-correction bouts. Saved-input safety evidence does not prove vehicle-response benefit.

## Artifacts and limits

`analysis.json`, `road-matched.json`, `reconstruction.json`, `detail.json`, `activation-quality.json`, `quality-checks.json` and `recorded-safety-replay.json` contain the counts, cohorts and timing. Scripts and anonymous input manifest are adjacent. Raw logs/metadata are preserved at `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-tracking-release/post-tracking-drive/`; private temporary GPS matching files are not published.

Different requests, road entry/exit, speed, roll and driver interventions confound before/after. The sample sizes are frames, not independent experimental trials; no statistical significance or percentage of causal improvement is claimed. No reliable lane-position/wandering assessment or new45mph conclusion is established by this analysis. No device change was made.
