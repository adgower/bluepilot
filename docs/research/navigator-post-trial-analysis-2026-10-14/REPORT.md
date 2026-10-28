<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# First Navigator steering-trial drive — observed response

2026-10-14, America/Chicago. Complete anonymous signal extraction from all **11** saved segments of the new drive, compared with the three earlier saved drives. No settings/source/firmware changes, active ECU queries, or onroad tests were performed by the investigator.

## Answer

The logs provide **partial support for better gentle-turn tracking**, but do not establish a uniform improvement or an overall improvement percentage. The remaining slower-speed tracking weakness is visible before recorded driver inputs. The initial cause in the highlighted examples is not the manual-turn override or sustained safety rejection.

## What actually ran

Recorded CarParams: flags **7**, safety parameter **10**, angle control, fixed steer ratio 19.6, wheelbase 3.1115 m, mass 2878 kg. This confirms the paired pinion setting and low-speed trial selector were configured for this drive. SSH also confirmed both persistent settings enabled after parking. The drive reached only **35.47 mph**, so it supplies no new road evidence for 45 mph behavior.

## Comparison: useful but mixed

Same eligibility/matching rules applied to old and new recordings: active steering requested and active angle mode on wire, no registered driver press, valid calibrated motion and learned parameters, valid car CAN, closely matched sample timestamps, speed≥5 mph, requested yaw magnitude≥0.005 rad/s. A secondary local demand-change gate reduces transient contamination. Matching strata use speed band, requested curvature magnitude, and direction sign.

Example shared group: **20–30 mph**, |requested curvature| **0.00035–0.0007 /m**, negative sign:

| Comparator | Eligible frames | Median actual/requested curvature |
|---|---:|---:|
| Earlier drive 1 | 33 | 0.625 |
| Earlier drive 2 | 46 | 0.729 |
| Older long drive | 25 | 0.647 |
| New trial drive | 56 | **0.924** |

The new group tracks closer to request, consistent with the user's feeling of improvement. These are only approximately 1.25–2.8 seconds of selected samples per group, scattered across the respective drives, not repeated matched road tests. Other shared groups improve less or worsen; for example some positive-sign and medium-curvature groups do not improve. Speed bands alone mix different curvature demands, turns, road roll, transitions and time history. Do not turn 0.729→0.924 into a claim of a 19.5% overall handling improvement.

In the new drive, broad 20–30 mph selected-response median is 0.471, versus 0.477/0.584/0.704 in different previous drives. This shows why an overall before/after percentage is unsupported: route mix dominates. The new 30–40 mph selected-response median is 0.828, with substantially more samples than the earlier short drives. It does not validate every speed or prove a causal gain effect.

## Remaining slower-speed moments

Times below are relative to the start of the saved route, not wall-clock timestamps.

### Around <private clock time>–<private clock time>, approximately 20 mph

At 534.25 seconds, requested wheel angle was **−7.9°**, actual **−2.7°**, with no registered driver press and active steering mode on wire. At 534.75 seconds, actual wheel angle moved to −6.6°; at 535.25 it moved to +0.2° while desired wheel angle remained −5.3°. This is inconsistent tracking/wheel movement rather than a clean sustained turn deficit alone. A recorded driver steering input begins at 535.75 seconds (~19.6 mph).

The paired wheel-angle mismatch exists **before** that input. Received EPS status remains control-in-progress, with limit-not-reached through the selected window. The offline safety replay has no steering rejection there. Driver hands may still exert torque below the registered-press threshold; these logs do not prove every wheel movement was caused solely by software.

### Around <private clock time>–<private clock time>, approximately 16 mph

At 562.2 seconds (~15.8 mph), desired wheel angle was **−4.6°**, actual **−2.6°**. Driver press begins at 562.7 seconds (~15.6 mph), then wheel angle increases as the driver turns. Brake press is recorded around 563.0 seconds and lateral activation becomes false; by 563.2 seconds wheel angle is about −53°. This is a manual takeover with subsequent normal brake disengagement. It must not be described as the controller spontaneously shutting off before the driver intervention.

Neither initial press occurs with wheel angle above the manual-turn detector's 45° threshold. Thus that detector is not the initial explanation for these two weak moments. The user did not identify exact locations/times; these recorded inputs may or may not correspond to the specific zigzags they remember.

Below 15 mph, broader samples also show substantial undertracking, but most are transient and there is little comparable slow-changing-demand coverage. Ratios are not used below 5 mph because curvature estimation divides by small speed and becomes unreliable. No sub-5-mph numerical improvement claim is made.

## Safety evidence

- Recorded Panda receive-check-invalid flags: **zero** selected samples across the full extracted drive.
- Four temporary CarState steering-fault samples occur stopped at startup/end; no permanent fault samples. They do not explain the highlighted moving episodes.
- Offline native replay of exact recorded safety-relevant RX and all recorded TX: **296,638 relevant RX frames**, **35,056 evaluated TX messages**, zero RX invalid frames, one initial warmup invalid tick; **515** TX frames precede the first recorded Ford configuration and are excluded.
- Reconstructed TX rejects: **2 angle frames** and **8 button frames**. Both angle rejects occur when controls_allowed is already false, at ~73.27 s (23.2 mph) and ~309.50 s (28.2 mph). No angle reject is reconstructed around the highlighted 531–565 s low-speed moments.
- Hardware health counters are cumulative across safety modes/resets. The route's maximum counter is 16 and positive increments across all modes sum to 23. These do **not** reconcile one-for-one with the 10 replay rejects. Actual firmware timing, nonlogged/forwarded traffic and transitions are not fully reproduced. Do not claim every hardware reject is classified or that the replay proves all actual transmissions accepted.

This does not support sustained pinion-receive failure or repeated native steering rejection as the initial cause of the selected weak moments. It is not hardware/forwarding equivalence or a road-safety certification.

## Recommended next investigation

Investigate **response and damping below ~20 mph** separately from the current broad low-speed map. Below 30 mph the current trial already has full added weight, so it does not add progressively more assistance as speed falls. The underlying command still scales with speed. Also inspect tracking dynamics: a larger feedforward multiplier alone could worsen the inconsistent wheel movement visible around the ~20 mph input.

Use these newly identified pre-input windows for local controller/response evaluation, preserve the current 20–35 mph behavior and ≥45 mph gain boundary, and evaluate command delay/steady tracking/oscillation separately. No further gain increase or device change is made from this observational result.

## Method and data fitness

Wi-Fi interrupted bulk transfer. The alternative executed `extract_remote_readonly.py` against saved rlogs in memory with bytecode writes disabled; it exported only compressed anonymous numeric signals. All 11 segments decoded successfully. A second in-memory extraction exported only exact safety-relevant RX addresses plus all TX for local native replay. Raw newer rlogs were not completely downloaded; the private partial bulk transfer is not analyzed.

CS, CC, TX and Panda timestamps are monotonic without duplicates. Sixteen duplicate motion measurement timestamps occur only in invalid startup samples and are excluded. Median CS/CC/TX spacing is approximately 50 ms; Panda is approximately 100 ms. Motion validity is ~99.85%. Learned parameters are flagged valid throughout; median learned angle offset is ~−2.04°, ratio ~22.42, stiffness ~1.001, roll ~0.033 rad. Those flags do not establish perfect physical calibration.

Nearest-time joins are one-to-one selections on TX timestamps with explicit skew gates. Measurements are calibrated road-frame Comma motion, not the biased CAN yaw signal; controller-sign actual curvature is calibrated z yaw divided by speed. Request ratios during changing demand do not fully compensate response delay or future-path anticipation. Samples are temporally correlated. There is no direct lane-deviation metric, exact road matching, randomized A/B trial, or proof of reduced wandering. Apparent common-band improvements remain observational.

Verified claims: `verify.py` passed checks for coverage/configuration, sample-level wheel errors before input, brake timing, receive flags, safety transition locations and highlighted comparison membership. Independent nearest-sample inspection confirms the 4–5° pre-input wheel errors. Arithmetic/methodology should be shared with these caveats.

## Artifacts

`signals-before.json`, `signals-after.json`, `signals.json`, `analysis.json`, `recorded-safety-replay.json`, `manifest.json`, extraction/replay scripts, console outputs and `verify.py`. Output excludes GPS, VIN, cabin imagery and credentials. Private compressed signal/safety exports are in `${PRIVATE_CACHE}`.
