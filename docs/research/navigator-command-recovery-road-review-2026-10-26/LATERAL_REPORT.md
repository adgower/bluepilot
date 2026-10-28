<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Offline lateral review — October 26, 2026

The new moving session still has transient tracking error and measurable highway oscillation. The negative result is that current gains have not eliminated these residuals; there is insufficient evidence for a new tuning value. These logs do not support a blanket steering gain increase. All conclusions below use only exact parent commit `1dbbc01892616c4b1a5c7c841d132f724ea5132c`; the prior-commit session is excluded from pooled results.

## Evidence and gates

The manifest contains 34 immutable downloaded rlogs across three sessions. Session 01 (<private clock time> CDT, prior commit) and session 02 (<private clock time> CDT, current commit) report 0 mph throughout. Only session 03, starting <private clock time> CDT, contributes moving evidence: 1,108.31 s, maximum 74.51 mph. Thus there is no 75–85 mph evidence and no repeated independent moving route for comparison.

Analysis uses calibrated device body yaw, requested curvature × speed, sent Ford yaw command, measured steering-wheel angle, model lane lines, and validity/health streams. Gates require fresh streams, valid calibrated motion/model/vehicle parameters, healthy panda, valid CAN/control, no steering faults, no driver steering pressure during the previous second, no brake/gas/blinker/lane change, drive gear, ≥5 mph, and ≥2 s continuously lateral active. There are 874.35 eligible seconds; meaningful turns require ≥0.25 m/s² requested lateral acceleration and below 50 mph also curvature >0.001/m, leaving 472.45 s. Prior 1 s request/speed history defines steady/rising/unwinding. Samples are correlated; durations are coverage, not independent experiments.

## Where error remains

Meaningful-turn body/request response median is 107.0% (10th–90th: 84.1–133.8%); steady median is 106.7% (92.1–120.1%). Median absolute lateral-acceleration error is 0.101 m/s² overall. Under-70% response occupies 3.76% and over-120% response 23.72% of meaningful samples. These are observational ratios, not a 100% calibration target: changing path requests, roll compensation, body dynamics and pose uncertainty all contribute. Reported median body-yaw standard deviation is 0.0129 rad/s, so individual small-demand ratios deserve particular caution.

| mph | Meaningful s | Response median % | Steady s / median % | Rising median % | Unwind median % |
|---|---:|---:|---:|---:|---:|
| 20–25 | 4.95 | 71.3 | 0.00 / — | 71.3 | — |
| 25–30 | 6.40 | 90.0 | 0.85 / 88.8 | 69.8 | 105.5 |
| 30–35 | 4.15 | 69.5 | 0.00 / — | 70.8 | — |
| 45–50 | 5.60 | 115.4 | 4.00 / 114.5 | — | 133.4 |
| 50–55 | 75.95 | 110.5 | 29.35 / 112.5 | 103.1 | 125.2 |
| 55–60 | 188.90 | 110.4 | 25.40 / 108.8 | 103.7 | 123.0 |
| 60–65 | 132.75 | 101.8 | 42.65 / 101.0 | 96.6 | 112.6 |
| 65–70 | 31.40 | 103.0 | 7.90 / 98.5 | 95.7 | 123.3 |
| 70–75 | 22.35 | 114.6 | 2.05 / 118.0 | 108.9 | 127.0 |

At 20–35 mph the limited underresponse evidence is mostly rising/transient; there is only 0.85 s of steady meaningful turning. At 60–70 mph steady medians are near 100%, while unwinding medians rise to 112.6–123.3%. At 50–60 mph unwind medians are 123.0–125.2%, versus steadies 108.8–112.5%. This phase pattern is consistent with release lag/transient overshoot, but does not identify a single causal gain or quantify a transport delay. The 70–75 mph steady estimate is only 2.05 s.

Two qualifying underresponse episodes near <private clock time> and <private clock time> lasted 0.55 s each with medians 64.6% and 67.9%, both nonsteady. Thirteen qualifying overresponse episodes lasted 0.50–1.55 s; most were nonsteady. Their exact intervals, signs, speeds and error metrics are in `lateral-analysis.json`.

## Highway oscillation and lanes

Four complete 10 s windows satisfy every gate, confident model lanes (both inner lane probabilities ≥0.7), 60–85 mph, and 95th-percentile requested lateral acceleration <0.4 m/s². At <private clock time> / <private clock time> (65.2 / 69.7 mph), model center peak-to-peak was 0.157 / 0.103 m and smoothed body lateral acceleration peak-to-peak 0.288 / 0.258 m/s². At <private clock time> / <private clock time> (73.9 / 73.9 mph), these grow to 0.124 / 0.437 m and 0.766 / 0.589 m/s², with eight smoothed sign crossings each. This supports residual oscillatory body response in those high-speed windows; it does not establish sustained lane ping-pong, a lane departure, or driver intent. The window rule is conservative and does not classify every second. Model lanes are inferred geometry, not surveyed ground truth.

## Complete speed coverage

| mph | Recorded s | Active s | Eligible s | Confident-lane s | Median absolute model-center offset m |
|---|---:|---:|---:|---:|---:|
| 0–5 | 61.65 | 0.00 | 0.00 | 0.00 | — |
| 5–10 | 15.30 | 1.70 | 1.70 | 0.00 | — |
| 10–15 | 28.55 | 5.85 | 5.65 | 2.70 | 0.024 |
| 15–20 | 20.50 | 10.65 | 4.10 | 2.30 | 0.009 |
| 20–25 | 30.10 | 24.80 | 17.30 | 4.90 | 0.043 |
| 25–30 | 39.40 | 37.95 | 29.00 | 15.80 | 0.186 |
| 30–35 | 33.00 | 31.95 | 17.10 | 14.40 | 0.122 |
| 35–40 | 9.05 | 7.55 | 0.20 | 0.00 | — |
| 40–45 | 8.65 | 6.75 | 0.00 | 0.00 | — |
| 45–50 | 17.15 | 15.40 | 11.95 | 9.45 | 0.688 |
| 50–55 | 130.65 | 128.65 | 111.80 | 108.40 | 0.349 |
| 55–60 | 363.95 | 363.95 | 353.50 | 330.15 | 0.210 |
| 60–65 | 207.05 | 207.05 | 192.10 | 177.80 | 0.159 |
| 65–70 | 64.75 | 64.75 | 62.90 | 58.45 | 0.079 |
| 70–75 | 75.85 | 75.85 | 67.05 | 64.20 | 0.107 |
| 75–80 | 0.00 | 0.00 | 0.00 | 0.00 | — |
| 80–85 | 0.00 | 0.00 | 0.00 | 0.00 | — |
| 85–90 | 0.00 | 0.00 | 0.00 | 0.00 | — |

The sent yaw command exceeds raw curvature × speed because the mapper intentionally transforms it: median wire/request ratios range about 1.27–1.39 at 50–75 mph, versus 1.57–1.65 at 20–35 mph. This is not evidence that measured body yaw should equal the wire command. The JSON also preserves measured wheel-angle distributions and wheel-minus-requested-angle distributions; wheel angles alone cannot establish tire authority or physical steering failure.

## Interventions and health

Nineteen grouped steering-pressure/disengagement associations occur in the moving session. All include steering pressure; six also include turn signals and two include brake pressure. These flags cannot identify an intentional correction, a safety-critical takeover, or its cause. Exact local times and the preceding three-second eligible tracking/lane evidence are recorded in the JSON.

Session 03 has 260 raw carState steering-fault rows, 58 invalid-CAN rows, one chestnut supply-fault sample, no panda Rx-check/invalid/fault/heartbeat samples, and cumulative transmit-block values up to eight. Rejected active lateral-command echoes occur at <private clock time> and <private clock time> CDT (route offsets 558.036 / 1064.037 s). Main control-transition review associates both active rejections with pedalPressed/userDisable; neither should be relabeled controlsMismatch from CAN rejection alone. They do not prove bad physical steering. Startup/shutdown also contain rejected inactive commands. Fault/invalid counts are raw message rows, not seconds or independent incidents. Timing audit places 255 steering-fault rows at startup +2.742–5.398 s and five at shutdown +1108.265–1108.305 s; all are stationary and none are moving lateral-active. All 58 invalid-CAN rows are stationary startup +2.742–3.430 s. The supply-fault sample is startup +0.176 s. Thus these do not establish an active road tracking fault.

No vehicle interaction, tuning, source modification, activation or road test was performed. Reproduction: run `lateral_extract.py` for each manifest session into the private `lateral-cache`, then `lateral_analyze.py`, then `lateral_supplement.py`. Raw logs, extracted GPS and normalized arrays remain in the private cache; public outputs contain no coordinates.

## Steering saturation warning crosscheck

Raw session 03 segment 001 records `steerSaturated/warning` with “take control / turn exceeds limit” at <private clock time> CDT (lateral time origin +98.361 s). This is the same rising low-speed turn as the underresponse episodes: the first threshold-qualified interval ends +98.30 s, 0.061 s before the warning, and the next runs +99.60–100.10 s. The warning is therefore associated with the broader underresponse turn, although its exact first timestamp sits just outside the strict <70% interval. At the nearest 20 Hz sample (+98.35 s), speed is 30.65 mph, requested yaw 0.08767 rad/s, sent wire yaw 0.13950 rad/s, calibrated body yaw 0.06157 rad/s (70.2% of request), and measured wheel angle −22.1°. Steering-pressure/turn-signal input follows around <private clock time> CDT, roughly 2.24 s later; that timing alone does not establish intent. This logged software warning is distinct from the absent moving ECU steering-fault flags and is not proof of a mechanical steering limit.
