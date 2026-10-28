<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Latest post-high-speed-trial drives — October 18, 2026

**The new correction is installed and working, but these drives do not establish an overall tracking improvement. High-speed over-response remains; the unwind/rearm guard blocks correction in several concerning windows.** No Comma code, parameters, services, OS or firmware were changed.

## Download and source coverage

Downloaded all four sessions after the previous route inventory: **97 segments /841,980,293bytes**. Every rlog and both forward-camera files for each of the requested two video segments were hash-verified; remote rlog inventory/source/settings/service state matched before and after. Raw route identities, GPS and original video stay in private cache `${USER_HOME}/CommaBackups/<private timestamp identifier>-post-highspeed-drive-analysis`. Exact clean installed pair: openpilot `ff6ff263084a4bc433cf197b44ce3a31f7608851`, opendbc `9d5a3d485085f36beeb9aff7baf53c0d4ea603ee`. InitData confirms the new preference in every session.

| Session | Start CDT | Recorded min | Assisted min | Max mph |
| --- | --- | ---: | ---: | ---: |
| highspeed-session-01 | <private clock time> | 4.4 | 0.0 | 0.0 |
| highspeed-session-02 | <private clock time> | 20.6 | 11.7 | 66.2 |
| highspeed-session-03 | <private clock time> | 48.3 | 30.2 | 85.0 |
| highspeed-session-04 | <private clock time> | 22.0 | 16.8 | 84.6 |

The first session is the stationary acceptance/startup recording. Three moving drives contain58.74minutes of lateral-active recording. Their start times are08:41,<private clock time> and15:01CDT.

## Did it improve tracking?

Actual installed-candidate reconstruction matches **100% of 67,726 active/no-driver wire packets within half a0.0005rad encoding step**. Previous roll-mapping reference differs on 299 encoded packets; the new trial changes 343 unquantized frames (**17.15s**), across77short correction windows. Below60mph it adds zero changes. This proves the new path executes; reconstruction uses recorded sensor motion and publication time as receipt proxy, so it does not predict an alternative vehicle trajectory.

Geographically/direction/speed/demand-matched comparison against the immediate prior installed drive yields only **41.35s**, almost entirely60–65mph. New/prior median body response are both about108.8%; median absolute ratio error13.1% versus14.8%. Only **0.65s** of those matched samples received nonzero correction. There is no useful matched70–85mph comparison, and only3.95s where both recordings satisfy the strict steady criterion. The small aggregate difference cannot be credited to this trial.

## All speed ranges

Response is calibrated body yaw divided by the request curvature×speed;100% is the instantaneous target. Ratios during entry/unwind are not a calibrated gain estimate. These use a calibrated pose yaw estimate, not independent ground truth. Its typical reported yaw standard deviation near0.0125rad/s corresponds to about0.46m/s² at82mph; values are temporally correlated, so samples are not independent confirmations. Wheel-target, video and model agreement must be considered separately. Clean turns require requested lateral acceleration≥0.25m/s² at every speed, plus |curvature|>.001/m below50mph; gentle highway curves are included. Fresh/valid/no-driver/no-brake/no-blinker/no-fault lane keeping only. Steady requires a past1s continuous eligible same-sign window,≤10% curvature span and≤3mph speed span.

| mph | Assisted s | Clean turn s | Body response median | Strict steady s | Steady median |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0–5 | 135.9 | 0.00 | — | 0.00 | — |
| 5–10 | 13.7 | 0.00 | — | 0.00 | — |
| 10–15 | 22.6 | 0.75 | 41% | 0.00 | — |
| 15–20 | 105.7 | 10.75 | 55% | 2.20 | 54% |
| 20–25 | 89.5 | 1.90 | 74% | 0.00 | — |
| 25–30 | 61.4 | 2.75 | 47% | 0.00 | — |
| 30–35 | 79.1 | 8.50 | 90% | 0.25 | 101% |
| 35–40 | 93.5 | 8.25 | 111% | 1.60 | 111% |
| 40–45 | 285.5 | 5.85 | 121% | 0.00 | — |
| 45–50 | 32.0 | 4.20 | 111% | 0.00 | — |
| 50–55 | 108.4 | 12.90 | 116% | 2.35 | 116% |
| 55–60 | 168.4 | 61.50 | 114% | 16.45 | 116% |
| 60–65 | 779.1 | 226.45 | 109% | 48.70 | 103% |
| 65–70 | 564.5 | 126.80 | 113% | 27.75 | 112% |
| 70–75 | 590.5 | 68.35 | 122% | 5.40 | 125% |
| 75–80 | 176.4 | 43.70 | 133% | 1.65 | 131% |
| 80–85 | 218.7 | 61.05 | 133% | 0.35 | 116% |
| 85–90 | 0.1 | 0.00 | — | 0.00 | — |

- **60–65mph:** strongest new steady evidence:48.7s,median102.8%. This is close to request but not matched proof of a correction benefit.
- **65–70mph:**27.75s steady,median111.9%; residual over-response remains.
- **70–85mph:** all-clean-turn medians122–133%, with transient/short steady support dominating. Do not choose a new global factor from these ratios. The80–85 steady cell has only0.35s.
- **35–50mph:** response medians111–121% in sparse changing turns;40–50 has no strict steady support. This range is not certified perfect by previous subjective feedback.
- **13–19mph:** at11:04:30.95CDT a5.7s clean under-response episode has median53.4%, with2.2s strict steady. The lower-speed issue remains open, and this high-speed-only change cannot fix it.

## Driver input and disengagements

**62 input/disengagement groups**, not62 proven safety-critical takeovers:21 include lateral disengagement,21 have nearby brake input and19 have turn signals/lane-change context (categories overlap). All are in [interventions.csv](../../navigator-reference/PRIVATE_ARTIFACTS.md), with pre-event clean response, correction activity and controller reasons in [incident details](../../navigator-reference/PRIVATE_ARTIFACTS.md). Manual steering without recent assistance is excluded.

| Time CDT | mph | Observation before input | Correction / interpretation |
| --- | ---: | --- | --- |
|<private clock time>|83.0|2.8s clean response median136%;140% with0.25s lag comparison|Brake-associated disengagement; only1of56pre-input frames corrected,32blocked awaiting rising confirmation. Model-estimated center-to-line minimum0.35m is not measured tire clearance. |
|<private clock time>|81.1|2.8s clean response median144%, also144% with0.25s lag|Driver pressure;22of56frames corrected but excess remained. Cause/intent unconfirmed. |
|<private clock time>|82.4|2.8s clean response median169%;159% with0.25s lag|0of56frames corrected;39frames body-confirmed but blocked by unwind/rising confirmation. After viewing clip, owner reports apparent oversteering near/past the line and possible metal/debris avoidance. Treat as owner-reported path/clearance intervention; object, tire crossing and controller causation remain unverified. |

### Requested video

[20-second forward + wide road clip](../../navigator-reference/PRIVATE_ARTIFACTS.md),<private clock time>–<private clock time>:09CDT. Driver input is approximately10s in. [Synchronized steering overlay](../../navigator-reference/PRIVATE_ARTIFACTS.md) shows recorded requested/measured wheel angle, driver pressure/torque, speed and lateral-active status. Orange timeline bands mark pressure; reconstruction-derived guard/correction values are explicitly labelled. Selected decoded frames show adjacent cars, a median barrier and changing road curvature, not a nearby semi. Owner subsequently clarified a lane-edge/path concern and possible metal/debris avoidance. The footage review does not independently identify that object or establish tire crossing. It cannot establish steering intent, surveyed lane crossing or clearance. Raw capture/encode timestamps align both cameras; labels are added but no synthetic lane/HUD overlay. Only road cameras were downloaded, no cabin video. [Video alignment](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Safety and health

All10temporary-steering-fault episodes occur while lateral assistance is inactive, at0–4.8mph/startup/stopping; no recorded permanent steering fault during active travel. No Panda RX-invalid or RX-check/heartbeat/fault issue is observed. Historical TX-blocked counters increase, so “zero blocked TX” would be false. Actual logs contain85rejection-marker records, including7active-angle echoes; all7are within~10ms of a physical brake/cruise RX record and associated disengagement.

Original-packet native replay processed22,703,325physical RX frames with no RX invalids. It reproduces4active-angle rejects with controls disallowed after braking;3hardware angle echoes are not reproduced in the logged TX/RX order. Their brake record is in the same logged timestamp batch. Keep the difference explicit: native log ordering is not full hardware-bus ordering. It also rejects34cancel packets; marker/counter/native counts are not assumed one-to-one. No rejected frame is used as proof of persistent high-speed steering-authority loss. [Brake-edge details](../../navigator-reference/PRIVATE_ARTIFACTS.md), [faults/echoes](../../navigator-reference/PRIVATE_ARTIFACTS.md), per-session native receipts.

## What to focus on next

1. Use the saved10:32:28,<private clock time> and15:19:59windows to investigate the high-speed unwind/rearm admission and residual tracking. Separate deliberate clearance inputs and planned lane changes from unintended path correction. Do not weaken the withdrawal safeguards merely because they prevented admission.
2. Keep the11:04:31low-speed sustained deficit as its own fixture. Examine wheel-target/body response and remaining catch-up/calibration limitations independently of the highway trial.
3. Continue35–50mph ordinary-drive evidence; the new recordings still lack steady40–50mph coverage. No special85mph reproduction drive is needed.

No gain,1.20/0.97,vehicle geometry, pinion/yaw option, installed code, preference, service, firmware or OS was changed. Findings are observational, not a causal gain calibration or a proved fix.
