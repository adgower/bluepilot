<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Post-wheel-target drive review — October 19, 2026

**The recordings do not yet establish whether the new high-speed correction improves tracking. It was installed in every session, but changed zero reconstructed commands relative to the previous policy. Low-speed undertracking remains, with a useful new15mph wheel/body-confirmed episode.** No device source, parameters, services, OS, firmware or CAN control state was changed by this review.

## Coverage and provenance

Downloaded all11new sessions/103segments/851,163,756bytes after the prior inventory. Every rlog hash and size was checked. Device source, protected files, selected settings and service state match before/after acquisition. All11sessions’ InitData identify parent`50baa6fd6acf9d37b7e0768e5736efab2a357ddc`; live clean pair pins child`0e65f296260ec16da3c3b814c10ac5f36f8b2e4c`. Existing steering preferences remain enabled and owner1.20/0.97preserved. Raw identities/GPS stay in private Mac cache referenced by acquisition-provenance.json.

98.47recorded minutes,38.10assisted minutes. First session is October18stationary acceptance; the ten October19sessions include manual/low-speed recordings, not ten assisted tests.

| Session | Start CDT | Recorded min | Assisted min | Maximum mph |
| --- | --- | ---: | ---: | ---: |
| wheel-session-01 | <private wall-clock timestamp> | 4.9 | 0.0 | 0.0 |
| wheel-session-02 | <private wall-clock timestamp> | 11.8 | 2.1 | 65.2 |
| wheel-session-03 | <private wall-clock timestamp> | 3.1 | 0.0 | 20.8 |
| wheel-session-04 | <private wall-clock timestamp> | 7.8 | 2.2 | 64.2 |
| wheel-session-05 | <private wall-clock timestamp> | 14.6 | 10.4 | 65.8 |
| wheel-session-06 | <private wall-clock timestamp> | 0.7 | 0.0 | 2.7 |
| wheel-session-07 | <private wall-clock timestamp> | 8.5 | 0.0 | 7.0 |
| wheel-session-08 | <private wall-clock timestamp> | 4.6 | 0.0 | 14.5 |
| wheel-session-09 | <private wall-clock timestamp> | 5.8 | 3.3 | 44.9 |
| wheel-session-10 | <private wall-clock timestamp> | 29.5 | 17.8 | 76.8 |
| wheel-session-11 | <private wall-clock timestamp> | 7.1 | 2.3 | 35.2 |

## High-speed correction verdict

Reconstruction of the actual installed class, original atomic calibration/control packets, recorded sensor motion and send times matches100%of43,934active/no-driver steering packets within half the0.0005rad wire step. Both new and previous-policy commands agree on every one: **zero added command changes**. Replay of frozen motion establishes command consistency, not a counterfactual physical trajectory. It cannot establish that the revised code improved or worsened handling.

The only70mph+recording is the11:37session. It contains12.3s lateral-active above70mph, peaking76.8mph overall, and only1.65s with meaningful requested lateral acceleration. None of that meaningful demand passes all clean tracking guards (freshness/validity, lane keeping, no signals/brake/driver pressure or pressure within1s). There are3.75s otherwise-eligible70mph+samples, but their demand is too small for this metric. No useful75–85mph bend or80mph+travel was recorded. The new wheel-target path never admitted a correction. Do not treat a quiet/straight high-speed passage as success or this absence as an activation bug.

Geographically/direction/speed/signed-demand matched comparison against the three prior high-speed-policy moving drives yields66.10s, all50–70mph: median new/prior body response109.1%/111.5%, median absolute ratio error15.3/14.9percentage points; absolute acceleration errors0.0824/0.0829m/s². The dominant54s60–65mph matched group has absolute ratio errors15.1/14.3points. Mixed, near-flat observational differences below the changed speed scope cannot be credited to the new correction. Prior timestamp is deduplicated per new route; correlated road repeats are not independent trial observations. See matched-comparison.json.

## All speed ranges

100%is calibrated body yaw/requested yaw, not a fitted gain target or independent trajectory truth. Clean meaningful demand requires requested lateral acceleration>=0.25m/s² and, below50mph,|curvature|>0.001/m. Fresh valid lane keeping, no brake/blinker/driver pressure or pressure in prior1s. Strict steady requires continuous past1s eligibility/same sign, curvature span<=10% and speed span<=3mph. Entry/unwind and noisy yaw can distort ratios; sparse cells do not justify per-speed gain changes. Typical reported yaw uncertainty near0.013rad/s is temporally correlated. Wheel-target corroboration is shown separately below.

| mph | Assisted s | Clean meaningful s | Body response median | Strict steady s | Steady median |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0–5 | 261.4 | 0.00 | — | 0.00 | — |
| 5–10 | 47.6 | 0.00 | — | 0.00 | — |
| 10–15 | 53.5 | 7.45 | 50% | 0.75 | 51% |
| 15–20 | 62.9 | 4.25 | 53% | 0.25 | 67% |
| 20–25 | 89.6 | 8.75 | 64% | 0.30 | 68% |
| 25–30 | 127.6 | 3.15 | 72% | 0.00 | — |
| 30–35 | 110.2 | 7.20 | 102% | 0.00 | — |
| 35–40 | 46.8 | 2.15 | 115% | 0.00 | — |
| 40–45 | 231.5 | 0.75 | 113% | 0.00 | — |
| 45–50 | 30.6 | 1.55 | 89% | 0.00 | — |
| 50–55 | 105.0 | 38.35 | 115% | 3.30 | 120% |
| 55–60 | 124.9 | 53.00 | 106% | 8.75 | 103% |
| 60–65 | 966.1 | 293.00 | 111% | 52.35 | 108% |
| 65–70 | 16.2 | 4.75 | 110% | 1.30 | 110% |
| 70–75 | 7.6 | 0.00 | — | 0.00 | — |
| 75–80 | 4.8 | 0.00 | — | 0.00 | — |

- **60–65mph:** strongest evidence,293s clean/52.35s steady, approximately111%/108%body response. Mild aggregate over-response remains; this latest change is identical to the previous policy here.
- **55–60mph:**53s clean/8.75s steady,106%/103%. This is closer to target but not a causal improvement claim.
- **30–50mph:** sparse, changing turns; no strict steady samples. In particular40–50mph is still unvalidated, not certified good.
- **10–30mph:** undertracking persists. The15mph episode is wheel-confirmed, so yaw-estimator disagreement alone cannot explain it. No new blanket gain is inferred.

## All steering inputs and disengagements

Reviewed all50grouped events, including39with steering pressure,22with nearby braking and16with a turn signal (overlapping associations). These are input/disengagement windows, not50proved emergency takeovers. Flags cannot identify intent. [Full chronological event CSV](../../navigator-reference/PRIVATE_ARTIFACTS.md), [all event details](../../navigator-reference/PRIVATE_ARTIFACTS.md), and [strict pre-input review](../../navigator-reference/PRIVATE_ARTIFACTS.md) retain every event. No event was discarded because it had sparse clean evidence.

| Time CDT October19 | mph | Evidence and interpretation |
| --- | ---: | --- |
|<private clock time>|52.4|Steering pressure after2.8s clean tracking around99%body response; absolute wheel-target error0.50°. No clear pre-input tracking deficit established.|
|<private clock time>|63.7|Brake/steering input. Final0.75s clean over-response: body156%, calibrated wheel155%, about1.89°excess wheel angle. At0.25s lag body ratio remains137%. Prior3s median121%. Useful unwind/rearm fixture; not proof of driver intent.|
|<private clock time>|64.1|Pressure plus signal. Pre3s clean body83%, wheel error0.37°; a separate excess-unwind episode occurred11s earlier. Do not merge them into a single causal takeover.|
|<private clock time>|54.2|Pressure plus signal;2.8s clean pre-input body109%, wheel error0.74°. Maneuver association, not confirmed path failure.|
|<private clock time>|66.9|Brake/pressure after recent inputs; no strict clean pre3s evidence. Relaxed current-no-driver window only0.6s shows150%body/122%wheel; diagnostic, confounded by maneuver and recent override.|
|<private clock time>|74.3|Pressure plus signal; no qualifying clean meaningful pre-input evidence. Cannot use this as high-speed tracking validation.|
|<private clock time>|51.7|Brake/pressure;2.8s clean pre-input body115%, wheel error0.51°. Not enough to identify an unwanted steering event.|
|<private clock time>|24.2|Repeated steering input; no strict clean pre-input window. Relaxed1s shows67%body/64%wheel response but is contaminated by recent override.|
|<private clock time>|17.3|Steering pressure with no strict clean pre-input demand. Separate clean15mph deficit follows~12s later; it is not evidence about why this earlier input occurred.|

## Six clean discrepancy episodes

| Time CDT October19 | mph | Duration s | Body response | Calibrated wheel response | Interpretation |
| --- | --- | ---: | ---: | ---: | --- |
| <private clock time> | 63.7–64.0 | 0.75 | 156% | 155% | Excess during changing/unwinding demand |
| <private clock time> | 63.4–64.0 | 1.15 | 161% | 174% | Excess during changing/unwinding demand |
| <private clock time> | 63.7–64.2 | 0.55 | 149% | 146% | Excess during changing/unwinding demand |
| <private clock time> | 28.3–30.9 | 0.70 | 45% | 52% | Undertracking |
| <private clock time> | 14.8–15.0 | 1.55 | 46% | 47% | Undertracking |
| <private clock time> | 14.7–15.1 | 0.60 | 22% | 24% | Undertracking |

Most useful new low-speed fixture: **<private clock time>–<private clock time>.20CDT,14.8–15.0mph**. Body46.5%, wheel46.5%, median21.7°wheel shortfall; body remains49.3%using a0.4s-delayed request. This is not solely a body-yaw discrepancy or ordinary0.25sphase lag. Following opposite-direction demand at13:14:19has22%body/24%wheel response but lasts only0.6s during reversal. Neither is strict steady gain-calibration evidence. High-speed-only policy cannot resolve these lower-speed episodes.

At11:48:35.58around28–31mph,0.7s body45%/wheel52%, median9.60°shortfall; lag0.4s raises body response to58%. This supports retaining the turn-entry/catch-up investigation. The three63–64mph excess episodes have wheel/body agreement, but ratios fall with lag correction; dynamics and unwind timing must be separated from static calibration. No parameter or code adjustment is proposed from these aggregates.

## Safety and power observations

No recorded active-driving temporary/permanent steering fault, active-driving invalid-CAN sample, Panda RX-check/heartbeat/fault episode was found.24temporary-steering-fault episodes occurred inactive at0–2.2mph. Invalid-CAN samples occur inactive/stationary. Hardware TX-block counters do rise:146rejection-marker records, including5active-mode angle echoes;3had the last logged carControl still lateral-active. All5are within9.2ms of a physical brake/cruise RX showing braking. These are disengagement permission edges, not evidence of prolonged lost steering authority.

Native original-traffic replay:23,153,887physical RX,0RX-invalid,373,881configured TX,26rejects. Each route’s initial tick before full RX warmup is invalid (11ticks); this is not an observed sustained hardware fault. Native order does not reproduce every hardware angle echo: only2active-mode rejects are reproduced, while3hardware echoes with the last logged control active remain unreproduced in logged ordering. Counters/echoes/native rejects are not one-to-one. See native session receipts and brake-edge-details.json.

Chestnut supplyFault appears in two **inactive** sessions:09:50:32route5samples while stationary, and09:56:27route410samples across its recording (0–3.4mph at flagged samples). There is no assisted driving in either and no supplyFault in the assisted sessions. This is a separate power/reliability follow-up; sampled flags do not identify cable, harness or power-source cause. Do not describe the whole day as fault-free. See health-context.json.

## Next evidence and work

1. Keep the high-speed result **not yet evaluated in meaningful new bends**. Ordinary supervised familiar-road driving at legal speeds may supply natural bends/entry/exit; no dedicated85mph or lane-edge reproduction is requested. Do not force collection where conditions are unsuitable.
2. Preserve the13:14:15wheel/body-confirmed15mph and11:48:35turn-entry fixtures for local diagnosis of requested→limited command→wheel tracking. No need to assume a new yaw sensor or multiply a gain from46%.
3. Preserve09:08:57,<private clock time>:22and09:37:34around64mph for unwind/lag review below the new policy’s scope.40–50mph steady/both-direction evidence remains missing.
4. Keep supply warnings as a separate reliability card; inspect ordinary power context if they recur. No Comma change made.

[Verification](../../navigator-reference/PRIVATE_ARTIFACTS.md), [speed-band CSV](../../navigator-reference/PRIVATE_ARTIFACTS.md), [reconstruction](../../navigator-reference/PRIVATE_ARTIFACTS.md), [episode diagnostics](../../navigator-reference/PRIVATE_ARTIFACTS.md). Raw/GPS cache stays private. No gains,1.20/0.97, vehicle model, pinion setting, installed code, preference, service, firmware or OS were changed.
