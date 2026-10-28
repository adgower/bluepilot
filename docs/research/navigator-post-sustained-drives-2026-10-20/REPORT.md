<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Post-installation drive review — October 20, 2026

No overall improvement is established. The new sustained low-speed term had no activation, so its 15 mph benefit is untested. The 60–70 mph unwind extension ran, but remaining over-response and the matched observations do not establish an improvement. The clearest actionable observations are shortfalls around 23–29 mph.

## Acquisition and configuration

Downloaded all 26 newly available/changed rlog segments relative to the previous archived inventory: three recordings, including one stationary session and two driving sessions. Acquisition re-inventoried the device, verified every downloaded hash and byte count, and found the final remote inventory identical. Raw logs, location and extracted signals remain in the private backup named in [provenance](../../navigator-reference/PRIVATE_ARTIFACTS.md). No device mutations, active ECU queries or CAN transmission were performed.

Installed clean parent `0171b897289be53fd62f330935c55825b86c3c3a`, child `4167433e5c575f620a9dedf8144a0bc7cba14291`; every recorded software revision agrees with the parent. Owner 1.20/0.97 source factors and protected files remain unchanged. Pinion, low-speed, persistent, roll and high-speed options remain enabled; updates disabled; Alpha/Experimental off.

| Recording | Start CDT | Duration | Maximum speed | Lateral active |
|---|---|---:|---:|---:|
| sustained-session-01 | <private wall-clock timestamp> | 282.6s | 0.0 mph | 0.0s |
| sustained-session-02 | <private wall-clock timestamp> | 626.1s | 65.2 mph | 306.4s |
| sustained-session-03 | <private wall-clock timestamp> | 549.6s | 64.7 mph | 319.5s |

## Around 15 mph

There were only 6.65 seconds of lateral activity at 13–17 mph, with no samples meeting the meaningful-turn demand threshold there. The entire 15–20 mph bin supplied only 0.15 seconds of clean meaningful demand and no steady turn. The sustained-extra trace was zero throughout both drives; there were no low-speed command differences from the preceding policy. This is an evidence gap, not proof the fix worked or failed. A normal, legal drive through a familiar broad bend near this speed, with assistance used only while comfortable and safe, is needed; do not delay an intervention to obtain data.

## Around 64 mph

There were 96.2 seconds of clean meaningful demand at 60–65 mph, including 22.95 steady seconds. The new policy changed 69 active/no-driver command frames versus the previous wheel-target policy, all at 60–70 mph; it changed none below 25 mph or at 40–50 mph. This establishes that the extension ran, not that it improved physical tracking.

At 60–65 mph, curve-exit/unwinding median measured body response was 127.0% over 9.9 seconds on the first drive and 129.4% over 6.15 seconds on the second. Steady response was 105.1% and 109.9%, respectively. Curve exit is still the weaker phase.

Outcome-blind matching against all eleven preceding recordings required position within 25 m, heading within 20 degrees, speed within 3 mph, signed demand within 30%, fresh eligible data and globally unique prior timestamps. Same-phase 60–65 mph results:

| Phase | Matched duration | New response | Previous response | New absolute lateral-acceleration error | Previous error |
|---|---:|---:|---:|---:|---:|
| steady | 3.00s | 105.9% | 106.8% | 0.053 m/s² | 0.064 m/s² |
| rising | 4.20s | 102.5% | 99.3% | 0.090 m/s² | 0.117 m/s² |
| unwinding | 4.45s | 129.0% | 127.3% | 0.149 m/s² | 0.147 m/s² |
| transition | 8.25s | 108.9% | 107.5% | 0.073 m/s² | 0.081 m/s² |

The unwind comparison is slightly worse observationally, not a demonstrated patch-caused regression. The matched unwind set is only 4.45 seconds of correlated frames, with unmatched roll, exact demand trajectory, calibration and road conditions. Steady tracking has a small favorable comparison, but it does not resolve the unwind question. Body response during falling demand includes normal motion lag; these percentages are not wheel gain settings.

## Every speed range

Response below is median calibrated body yaw divided by requested curvature × speed, for clean meaningful demand. 100% is the instantaneous reference; transient ratios alone do not establish a gain error. Clean filtering excludes driver input/recent input, braking, blinkers, stale/invalid signals and unhealthy Panda state. Small samples and yaw-estimate uncertainty prevent universal per-speed calibration.

| mph | Active seconds | Clean turning seconds | Steady seconds | Body response median |
|---|---:|---:|---:|---:|
| 0–5 | 10.2 | 0 | 0 | No evidence |
| 5–10 | 7.5 | 0 | 0 | No evidence |
| 10–15 | 9.6 | 0 | 0 | No evidence |
| 15–20 | 15.2 | 0.15 | 0.00 | 54.2% |
| 20–25 | 153.0 | 6.95 | 0.00 | 66.2% |
| 25–30 | 97.0 | 20.70 | 3.35 | 83.1% |
| 30–35 | 41.6 | 0.55 | 0.00 | 78.5% |
| 35–40 | 16.1 | 5.55 | 0.05 | 106.4% |
| 40–45 | 16.2 | 0.95 | 0.00 | 105.5% |
| 45–50 | 9.7 | 0.20 | 0.00 | 127.9% |
| 50–55 | 18.1 | 7.30 | 0.60 | 110.6% |
| 55–60 | 40.3 | 28.95 | 2.90 | 109.6% |
| 60–65 | 191.7 | 96.20 | 22.95 | 110.4% |
| 65–70 | 0.1 | 0.05 | 0.00 | 100.1% |
| 70–75 | 0.0 | 0 | 0 | No evidence |
| 75–80 | 0.0 | 0 | 0 | No evidence |
| 80–85 | 0.0 | 0 | 0 | No evidence |
| 85–90 | 0.0 | 0 | 0 | No evidence |

No new data above 65.23 mph; 70–85 mph remains unassessed in this batch. The 45 mph region also lacks enough clean steady demand to call it optimized.

Four sustained discrepancy episodes met the predefined duration/error thresholds; all were under-response at approximately 25–30 mph. These thresholds exclude many short or confounded events and are not a count of every tracking defect.

## All input/disengagement groups

Twenty groups were detected from lateral disengagements or driver steering pressure while recently active and moving. These are associations, not twenty confirmed safety takeovers. The table uses up to six seconds of clean pre-event demand; absence of qualifying data does not establish normal tracking. Detailed timing, buttons, alerts, model lane estimates and relaxed windows are retained in [incident details](../../navigator-reference/PRIVATE_ARTIFACTS.md) and [takeover review](../../navigator-reference/PRIVATE_ARTIFACTS.md).

| CDT | mph | Association | Clean pre-event seconds | Body response median | Wheel-target absolute error median |
|---|---:|---|---:|---:|---:|
| <private clock time> | 26.3 | steering-pressure-associated, turn-signal-associated | 3.05 | 65.8% | 11.31° |
| <private clock time> | 64.2 | steering-pressure-associated, turn-signal-associated | 3.85 | 106.8% | 0.5° |
| <private clock time> | 45.3 | brake-associated, steering-pressure-associated | 2.50 | 103.2% | 0.48° |
| <private clock time> | 16.3 | brake-associated | 0.00 | Insufficient | — |
| <private clock time> | 24.7 | steering-pressure-associated | 0.00 | Insufficient | — |
| <private clock time> | 23.5 | steering-pressure-associated | 0.00 | Insufficient | — |
| <private clock time> | 23.0 | brake-associated | 0.00 | Insufficient | — |
| <private clock time> | 24.7 | brake-associated, steering-pressure-associated | 0.00 | Insufficient | — |
| <private clock time> | 20.6 | brake-associated | 0.00 | Insufficient | — |
| <private clock time> | 24.4 | brake-associated, steering-pressure-associated | 0.00 | Insufficient | — |
| <private clock time> | 24.1 | brake-associated | 0.00 | Insufficient | — |
| <private clock time> | 23.7 | steering-pressure-associated | 0.00 | Insufficient | — |
| <private clock time> | 23.4 | steering-pressure-associated | 2.30 | 60.6% | 6.3° |
| <private clock time> | 24.1 | brake-associated, steering-pressure-associated | 0.60 | 58.8% | 3.25° |
| <private clock time> | 33.9 | brake-associated, steering-pressure-associated | 0.40 | 90.0% | 1.57° |
| <private clock time> | 29.0 | steering-pressure-associated | 5.80 | 84.3% | 7.76° |
| <private clock time> | 56.6 | brake-associated, steering-pressure-associated, turn-signal-associated | 0.00 | Insufficient | — |
| <private clock time> | 40.7 | brake-associated, steering-pressure-associated | 0.80 | 121.1% | 0.63° |
| <private clock time> | 18.1 | steering-pressure-associated | 0.00 | Insufficient | — |
| <private clock time> | 9.5 | brake-associated, steering-pressure-associated | 0.00 | Insufficient | — |

Priority episodes:

- **<private clock time>, 26.3 mph:** preceding 3.05 clean seconds showed 65.8% response and 11.31° median wheel-target shortfall. Steering pressure and a signal followed. The below-25 correction was out of scope; this is strong evidence to investigate turn-entry demand/limits around 25–30 mph locally.
- **<private clock time>, 23.4 mph:** 2.3 clean seconds showed 60.6% response and 6.30° wheel-target error before steering pressure; the new low-speed extra was not admitted. Investigate the admission trace against wheel/body evidence and remaining budget before changing gains.
- **<private clock time>, 29.0 mph:** 5.8 clean seconds showed 84.3% response and 7.76° wheel-target error before steering pressure, including a shorter 57.9% episode.
- **<private clock time>, 64.2 mph:** steering pressure and signal; preceding six-second clean subset was 106.8% with 0.50° median wheel-target error. The signal confounds interpretation; no hazard or intended maneuver is established.
- **<private clock time>, 40.7 mph:** only 0.8 clean pre-event seconds, 121.1% response; brake and steering pressure. Too little steady data to diagnose oversteer.

## Health and reconstruction limits

No sampled invalid CAN while lateral active, no moving steering-fault episodes, and no active Chestnut supply faults. Startup/stopping exceptions are retained rather than hidden. Three rejected active-mode steering echoes occurred at brake/disengagement transitions (16.3, 20.6 and 33.8 mph); physical brake state is within approximately 11 ms of each. One still had a sampled active CarControl. This timing is consistent with brake cancellation sequencing, but the packet flags alone do not prove the precise Panda rejection cause. Do not bypass brake safety. See [faults/rejections](../../navigator-reference/PRIVATE_ARTIFACTS.md) and [brake timing](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Recorded active/no-driver wire commands agreed with the reconstructed current policy to half a wire step except one frame near 64.47 mph: error 0.00025538 rad against the 0.00025001 tolerance. This small outlier is retained as a replay timing/quantization limitation, not silently classified as an exact match. These offline reconstructions use frozen recorded motion and cannot predict closed-loop handling.

## Next work

1. Investigate saved 23–29 mph episodes, separating low-speed admission, target rise, command slew/authority and physical lag. Keep tuning local and preserve 1.20/0.97.
2. Inspect the saved 60–65 mph unwind windows and exact correction-active frames; quantify calibrated wheel error versus lagged body response before increasing correction.
3. Collect ordinary safe turning data around 13–17 mph when convenient. Further high-speed testing is not required to diagnose these saved episodes.
4. Retain 35–50 mph and all higher-speed bins as evidence gaps where steady demand is insufficient; do not describe subjective 45 mph behavior as objective proof.

[Acquisition](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Analysis](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Focused comparison](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Matched comparison](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Activation windows](../../navigator-reference/PRIVATE_ARTIFACTS.md)
