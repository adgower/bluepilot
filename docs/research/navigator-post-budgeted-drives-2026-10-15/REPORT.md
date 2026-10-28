<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator: drives after 1 a.m., October 15 — budgeted correction

**Improvement around 15 mph is not established.** Most travel at that speed occurred with assistance disabled; there is only one second of clean, meaningful-demand evidence and no steady or matched-road comparison. The clearest remaining response shortfall is a roughly 22 mph turn. Its reconstructed correction repeatedly waits/withdraws while response remains below request; the rising-demand budget never activates in this drive. This supports investigating admission/recovery behavior locally, not increasing the budget or changing1.20/0.97 from these data.

No Comma source/settings changes, restart, active ECU queries or injected CAN/control commands occurred during this analysis. Downloads, parsing, reconstruction, plotting and native replay were performed on the Mac.

## Scope, software and completeness

Time cutoff: October15 at <private clock time> Chicago/CDT =06:00UTC. All currently retained onboard rlogs meeting that cutoff were copied: **71 segments,561,270,925 bytes**, with every local SHA-256 equal to the device file hash. Recorded clocks confirm these sessions are wholly after the cutoff. This describes retained evidence; it cannot establish that no earlier deleted recording ever existed.

| Session | Chicago time | Coverage |
|---|---|---|
| drive-01 |<private clock time>–<private clock time>|16 segments, entirely stationary; excluded from steering-response comparison|
| drive-02 |<private clock time>–<private clock time>|55 segments, four moving stretches separated by stops of at least60 s; max65.8 mph|

Moving stretches, with brief stops under60 s merged:08:28:33–<private clock time>(max65.8 mph),<private clock time>–<private clock time>(max32.8 mph),<private clock time>–<private clock time>(max30.3 mph),<private clock time>–<private clock time>(max59.6 mph). These are movement groups, not inferred ignition cycles.

Both recordings identify parent `0cc74c94f3c6dafa3790c303be9ef345878bd792` and the preserved pinion/low-speed/tracking options. Its committed child pin is `d64ffcfa4e4a7556151962ca304d223a0a323375`. Recorded geometry remains3.1115m/19.6, flags 15, Ford safety 10; Alpha/Experimental remain off. Live read-only inspection after download confirms both exact heads and clean repositories. The forced Expedition identity remains the Navigator compatibility path.

The logs' `dirty=true` flag requires qualification: this local branch has no upstream configured, and current version code treats a missing upstream as dirty. The logged1857-byte GitDiff is identical to the pre-activation cached parameter, containing historical settings already committed into the branch. It is not a fresh worktree diff. See [source provenance](../../navigator-reference/PRIVATE_ARTIFACTS.md), [input hashes](../../navigator-reference/PRIVATE_ARTIFACTS.md), and [scope/provenance](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Historical baselines are the 17-segment release-correction drive at 00:08CDT Oct 15 and 10-segment very-low-speed drive at 22:00CDT Oct 14. They supply context, not additional post01:00 test drives. One software revision change cannot be treated as a controlled road experiment.

## What happened around 15 mph

In13–17 mph,1532 outgoing angle-message samples represent about76.6 s of travel. At 1436 samples(~71.8 s), the latest control flag was inactive, stock cruise was disabled, and selfdrive state was disabled with no alert text. This is93.7% of the sampled time in that band. The profile's minimum **enable** speed is20 mph; its minimum **steer** speed is0. Thus low-speed travel without engaged stock cruise is an availability/engagement question, distinct from tracking while active. Continuing below an enable threshold and initially enabling below it are separate behaviors; no factory engagement rule was altered.

Only 58 samples(~2.9 s) had an active outgoing angle request with no detected driver steering. Strict clean/fresh meaningful-demand filtering leaves **20 samples(~1.0 s)** and **zero steady samples**. The reconstructed added correction is zero throughout those58 samples. No same-road/same-direction/similar-speed/demand13–17 mph pairs match the historical baseline.

The raw clean median body response is79.5% of requested curvature, versus41.3% in the previous drive, but this is **not an improvement estimate**: new usable duration is1.0 s versus41.05 s; median demand magnitude is0.00137/m versus0.00293/m, and neither road nor phase is matched. The previous drive had10.7 s steady coverage; the current drive has none. Do not read these raw medians as a gain percentage.

## Remaining undertracking and candidate mechanism

The most useful new fixture is around **<private clock time>–<private clock time>**, median21.9 mph. In that0.70 s clean interval, median body curvature is59.4% of request and the fixed-model wheel estimate is63.6%. The broader eligible pre-input window has roughly 66.5% body response. Detected driver steering begins around <private clock time>, at 23.6 mph. No rejected steering echo occurs in this response-shortfall window. Simple lag sensitivity does not eliminate the deficit, though clean follow-up becomes sparse.

[Private/local visualization omitted](../../navigator-reference/PRIVATE_ARTIFACTS.md)

Reconstruction at actual saved20Hz send times shows:

- Existing steady-error correction adds small pulses at 20.8–21.9 mph; it then withdraws under the fractional catch-up veto and restarts its hold.
- Steering-derived measured curvature stays near 0.0025/m while requested magnitude fluctuates around 0.004/m. Small request reductions raise the measured/requested ratio and can look like projected recovery even when measured curvature is nearly flat. That is a plausible explanation for the withdrawal; whether continued correction would improve physical response requires a separate controlled validation.
- Across the whole drive there are only **7 reconstructed extra-command frames(~0.35 s)** below 25 mph and **zero rising-admission frames**. The ramp budget is never spent and never rearms. Enlarging that budget would not change this reconstructed case.
- The new strategy differs from the former release strategy at 9 distinguishable frames, all near 21–22 mph. In these frames it requests0.88–1.45 mrad **less** added path angle than the former strategy. Observed wire output fits the new prediction much better(p50/p95 error0.117/0.211 mrad versus1.368/1.522 mrad for the former strategy). This is command-level evidence, not proof of worse or better road handling.
- Global active reconstruction p95 error is0.238 mrad, close to the half-step of the 0.5 mrad wire quantization. Internal admission/budget values are reconstructed; no direct internal telemetry was recorded.

A second brief shortfall occurs near <private clock time> at 11.8 mph, with only 0.75 s clean evidence. Relative response is poor, but median lateral-acceleration error is only 0.055m/s² because the request is small. The correction reaches a single steady-error frame and then returns to waiting as demand varies. It is useful for testing admission continuity, not for prescribing a large low-speed gain.

[Reconstruction](../../navigator-reference/PRIVATE_ARTIFACTS.md), [guard context](../../navigator-reference/PRIVATE_ARTIFACTS.md), [distinguishable-frame check](../../navigator-reference/PRIVATE_ARTIFACTS.md), [coverage](../../navigator-reference/PRIVATE_ARTIFACTS.md), and [details/matching](../../navigator-reference/PRIVATE_ARTIFACTS.md) preserve these results.

## Other speeds and highway

Clean frames require active angle mode, no driver input or recent input, no blinkers/lane change, valid/fresh control/state/model/IMU, valid CAN/vehicle parameters, speed≥5 mph and |requested curvature|>0.001/m. These are descriptive proxies, not lane-position or wandering measurements.

|Speed|Usable time|Median body/request|Median wheel estimate/request|
|---|---:|---:|---:|
|10–13 mph|0.75 s|6.7%|26.7%|
|13–17 mph|1.0 s|79.5%|87.0%|
|17–20 mph|1.15 s|88.1%|87.6%|
|20–25 mph|5.5 s|77.1%|79.4%|
|25–40 mph|13.1 s|102.1%|137.1%|
|40–50 mph|5.95 s|110.8%|111.3%|
|50–70 mph|19.9 s|106.3%|143.3%|

The highway data do not show a general persistent steering shortfall in the eligible meaningful bends. Some transient overshoot/phase mismatch remains. One apparent38.8 mph deficit changes markedly with 250 ms response alignment and has very little uncontaminated follow-up before driver input; it is not a strong gain-calibration fixture. The wheel estimate is a fixed-geometry model and differs from measured body motion, particularly at higher speed; treat it as a second proxy, not ground truth.

Reconstructed new-versus-former actuation is identical at/above 25 mph in this recording. There is no basis here for retuning the good45 mph behavior or the 0.97 setting. The historical release baseline only reached29.9 mph, so it is not a comparable highway before/after drive.

## Actual rejections: counters fully attributed

The driving session has **20 Ford-mode TX-blocked increments while moving**. Actual Panda rejected-frame echoes identify all 20:

- **18 cancel-button packets** at 0x83, with cancel asserted after stock cruise permission has gone away.
- **2 active steering packets** at 0x3d6, around 29.5mph(<private clock time>) and 44.3mph(<private clock time>), at driver-brake/disengagement edges.

At the 29.5 mph event, physical PCM brake/cruise-off is logged at 2173.531208 s, carState reflects it at 2173.533289 s, and an active steering packet using the preceding control state is sent at 2173.534154 s. Selfdrive disables at 2173.536213 s; the next control message is inactive. Panda correctly rejects the stale active request.

At 44.3 mph, host sendcan is stamped2948.633008 s; the brake RX and actual rejected echo arrive together around 2948.639345 s, followed by controlsAllowed=false. This illustrates why host-time offline replay cannot reproduce every actual USB/CAN arrival ordering.

The all-physical-RX/exact-recorded-TX native replay processes13,054,876 physical RX with zero rejected RX and 200,375 configured TX:200,362 accepted,13 rejected(12 cancel,1 steering). The actual echoes resolve the additional6 cancel and 1 steering rejection not reproduced by host-order replay. They are no longer unattributed counter increments. There are also11 stationary startup/shutdown rejection echoes around safety-mode changes, outside the 20 moving-event count. Do not combine these populations or call native timing replay hardware validation.

No active steering rejection is found in the 22 mph/12 mph undertracking windows. No steady-driving shadow-intent-limit rejection is established in these logs. The correct direction is to suppress stale/redundant outgoing requests at disengagement, retaining all Panda permission/steering limits.

See [actual echoes](../../navigator-reference/PRIVATE_ARTIFACTS.md), [counter reconciliation](../../navigator-reference/PRIVATE_ARTIFACTS.md), [native replay](../../navigator-reference/PRIVATE_ARTIFACTS.md), and [29mph](../../navigator-reference/PRIVATE_ARTIFACTS.md)/[44mph](../../navigator-reference/PRIVATE_ARTIFACTS.md) transition timelines. Echo flag decoding is backed by pandad's CAN_REJECTED_BUS_OFFSET handling in panda.cc.

## Runtime health and next local work

The moving session has zero RX-invalid samples, Panda faults, heartbeat loss, permanent steering faults or Chestnut supply faults. All 438 temporary-steering-fault state samples occur while stationary; none occurs while moving or at an active angle frame. Sampled models remain the big model with zero reported frame drops; maximum sampled GPU47 °C/memory68 °C. These observations do not prove closed-loop stability or performance under every condition.

Recommended local investigation, with device unchanged:

1. Use the 22 mph and 12 mph snippets as new admission/recovery fixtures. Examine small-demand jitter, hold resets and ratio-based catch-up withdrawal. Test filtered recovery/hysteresis while preserving immediate genuine-unwind, driver, freshness and lane-change release, existing budget retention/rearm rules, final slew limits and aborted-turn residual checks. No new numeric gain is justified yet.
2. Add direct diagnostic fields for admission reason, extra term, budget, freshness and requested/measured curvature before the next controller experiment, so reconstruction is not the only evidence.
3. Investigate conservative brake/cruise-off gating and redundant-cancel suppression locally; verify main-off/brake/cancel behavior without loosening firmware safety. A packet already in transit can still be rejected, so do not promise zero edge rejection.
4. Require adequate naturally occurring **assist-active**15 mph steady-turn coverage to evaluate improvement. Most low-speed travel here is an engagement-availability issue; NAV-04 MADS-style lateral independence is relevant research, with separate application/UI/Panda design. Changing an enable-speed constant alone is not that feature.

Keep1.20/0.97, pinion feedback, the good45 mph behavior and the active device untouched during this follow-up. [Verification assertions](../../navigator-reference/PRIVATE_ARTIFACTS.md) recompute key counts and reconciliation from numeric arrays; all pass. Frame observations are serially correlated and are not independent trial counts. Exact road response to any unimplemented controller cannot be inferred from replay.
