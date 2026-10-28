<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# First road review of calibrated/mid/unwind/rearm pair — October 20, 2026

The new correction is running, but **23–29 mph tracking and 64–70 mph unwind are not resolved**. A small matched steady-highway sample is closer to demand; matched unwinding does not improve. No gain or device change was made. Owner 1.20/0.97 and settings remain unchanged.

## Acquisition and revision separation

Downloaded all five newly hash-identified recordings / 35 segments / 297,157,263 compressed bytes relative to the preceding complete inventory. Raw identities, GNSS, and extracted logs are retained in the private CommaBackups directory referenced by acquisition-provenance.json; public tables use anonymous labels. Every route starts at segment 0, includes every segment present in the remote inventory, is contiguous and unlocked, and has a terminal logger endOfRoute sentinel. Local SHA-256/size checks pass. Final remote inventory/source/settings/protected file/service checks equal their initial snapshots. Zero device mutations, active queries, CAN injections, installations, or restarts.

| Recording | Start CDT | Code | Duration | Maximum | Lateral active |
| --- | --- | --- | ---: | ---: | ---: |
| calibrated-session-01 | <private clock time> | Previous 0171/4167 | 355.1s | 35.1 mph | 193.7s |
| calibrated-session-02 | <private clock time> | Previous 0171/4167 | 343.6s | 35.0 mph | 121.1s |
| calibrated-session-03 | <private clock time> | New f750/de70 | 194.7s | 0.0 mph | 0.0s |
| calibrated-session-04 | <private clock time> | New f750/de70 | 571.5s | 69.3 mph | 328.8s |
| calibrated-session-05 | <private clock time> | New f750/de70 | 536.5s | 69.6 mph | 173.5s |

Only sessions 04 and 05 are moving tests of the new pair. Session 03 is stationary. Sessions 01/02 are additional previous-code evidence, not new-code failures. Source metadata is clean and the relevant preferences are enabled. The parent revision pins the documented child revision; child provenance additionally verified by read-only current device inventory.

## 23–29 mph: shortfall remains

Session 04 provides 7.4 seconds of clean meaningful demand: median calibrated body response **78.6%**, offset-corrected wheel/command response **79.1%**. Only 0.65 seconds meets the steady-window definition (body 89.7%, wheel 89.7%); this is too little to calibrate the entire range. Session 05 has no usable meaningful demand in this exact band. There are no spatially matched previous/new clean samples in 23–29 mph under the declared matching tolerances, so improvement is not established.

At **<private clock time> CDT**, 27.5–29.5 mph, 1.65 seconds before/through the beginning of steering pressure shows body response **67.7%** and median lateral acceleration deficit **0.939 m/s²**, against demand 2.838 m/s². Pressure begins <private clock time> at 27.7 mph; a turn signal is associated with the larger input episode. This is a real recorded tracking shortfall, but the driver's reason is not inferred from flags.

At original send times 103.0–104.6 seconds, reconstruction matches all 32 active unpressed wire commands to half a wire quantization step. The mid-speed addition is withheld by **native_deviation_clip** at all 32 updates and output equals the previous strategy. More mid-speed gain would not cure this particular guarded episode. Preserve the native envelope; next investigate the requested/calibrated wheel model versus fixed-pinion native deviation reference and actual steering response, rather than bypassing that envelope.

The new addition did activate earlier: five bounded updates around <private clock time>–<private clock time>, up to 0.0025 rad path-angle difference, followed by catch-up withdrawal. Those seven surrounding active updates also have full half-step wire parity. This establishes brief activation, not a measured benefit attributable to it. One mid rearm was reconstructed in session 04; none in session 05.

## 64–70 mph: steady hint, unwind unresolved

Across both new drives there are **11.2 clean unwinding seconds**, median current-request body response **127.8%**, median absolute lateral-acceleration error **0.173 m/s²**. Session 04: 6.8s, body 128.2%, wheel 120.1%; session 05: 4.4s, body 127.4%, wheel 114.7%. Wheel ratios use nontrivial offset-corrected wheel targets, so wheel sample coverage differs from body coverage. Wheel/body excess agrees in these samples, but a shrinking target and physical delay contribute to instantaneous ratios.

An outcome-blind spatial comparison uses four immediate previous-policy recordings (the earlier two reviewed drives plus today's two newly downloaded previous-code drives). It requires distance <=25m, heading <=20 degrees, speed <=3 mph, signed curvature within30%, equal turn phase, roll within0.01rad, and fresh GPS with accuracy <10m. Prior timestamps are deduplicated globally. Samples are correlated observations, not independent trials or causal estimates.

| Matched 64–70 phase | Paired time | Previous body response | New body response | Previous median absolute error | New median absolute error |
| --- | ---: | ---: | ---: | ---: | ---: |
| steady | 3.00s | 114.1% | 107.3% | 0.135 m/s² | 0.084 m/s² |
| rising | 0.65s | 99.9% | 87.8% | 0.049 m/s² | 0.068 m/s² |
| unwinding | 1.95s | 129.0% | 132.7% | 0.148 m/s² | 0.160 m/s² |
| transition | 4.25s | 120.5% | 116.4% | 0.110 m/s² | 0.082 m/s² |

The 3.0-second steady subset is encouraging (114.1% to107.3%). The 1.95-second matched unwind subset is not (129.0% to132.7%, error0.148 to0.160m/s²). Different samples and phases must not be pooled into a claim that unwind is fixed. The matched rising subset also looks worse, but only0.65s is available.

On session05 the entire active/unpressed mode1 command reconstruction has half-step wire parity. Relative to the previous strategy, only26 strategy updates differ, all at65–70mph; none differ at60–65mph. At15:07:18.135 (~69mph), a0.5s excess episode has136.7% body response and0.326m/s² median error. The unwind logic is admitted/reducing during part of it, with two differing strategy updates. At15:08:18.035 (~67mph), another0.5s excess episode has136.1% response and0.263m/s² error; reconstructed output equals the previous strategy across those ten updates despite target-excess admission. This is insufficient effective additional authority, not evidence that the option is wholly disabled.

Lag sensitivity: session05 unwind response becomes119.0%,112.4%,108.3% when compared against requests0.10,0.25,0.40s earlier. These are sensitivity checks, not identified delays or permission to shift measurements until they appear perfect. Next diagnosis should separate physical wheel/body lag, demand prediction, current admission/release limits and quantized transmitted effect before changing strength.

## Every speed range

Only new-code sessions04/05 are included below. Response is calibrated body yaw divided by requested curvature times speed.100% means instantaneous body response equals requested curvature; it does not establish correct lane placement. Clean meaningful sample and steady durations explicitly limit what can be concluded.

| Speed mph | Active time | Clean meaningful time | Median response | Steady time | Steady response |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0–5 | 0.0s | 0.00s | No usable demand | 0.00s | No usable demand |
| 5–10 | 3.5s | 0.00s | No usable demand | 0.00s | No usable demand |
| 10–15 | 7.9s | 2.30s | 52.2% | 1.40s | 52.0% |
| 15–20 | 15.2s | 1.20s | 55.1% | 0.00s | No usable demand |
| 20–25 | 102.7s | 1.85s | 72.1% | 0.00s | No usable demand |
| 25–30 | 53.2s | 8.25s | 79.7% | 0.95s | 90.7% |
| 30–35 | 41.9s | 7.00s | 88.0% | 0.00s | No usable demand |
| 35–40 | 8.1s | 0.25s | 99.3% | 0.00s | No usable demand |
| 40–45 | 7.1s | 1.25s | 108.0% | 0.00s | No usable demand |
| 45–50 | 13.7s | 0.00s | No usable demand | 0.00s | No usable demand |
| 50–55 | 41.6s | 9.65s | 109.1% | 0.25s | 125.5% |
| 55–60 | 71.2s | 42.95s | 111.3% | 10.35s | 109.0% |
| 60–65 | 51.4s | 25.75s | 108.1% | 3.05s | 102.8% |
| 65–70 | 85.1s | 51.00s | 114.9% | 9.65s | 112.7% |
| 70–75 | 0.0s | 0.00s | No usable demand | 0.00s | No usable demand |
| 75–80 | 0.0s | 0.00s | No usable demand | 0.00s | No usable demand |
| 80–85 | 0.0s | 0.00s | No usable demand | 0.00s | No usable demand |
| 85–90 | 0.0s | 0.00s | No usable demand | 0.00s | No usable demand |
| 90–95 | 0.0s | 0.00s | No usable demand | 0.00s | No usable demand |
| 95–100 | 0.0s | 0.00s | No usable demand | 0.00s | No usable demand |

Below20mph remains undertracking in the available turns, not a completed calibration.13–17mph has only2.25 clean meaningful seconds in one drive,0.55steady seconds at52.4% body response; sensor uncertainty and scant coverage preclude selecting a global factor.35–50mph remains poorly covered, particularly45–50mph with no meaningful clean demand.55–60mph steady response is109.0% over10.35s, so retain this as a separate excess-response investigation rather than assuming only64mph matters. No new evidence exists at70mph or above; this batch cannot validate75–85mph behavior.

## All input/disengagement groups

The two new-code moving drives contain17 grouped events:14 groups include driver pressure and8 include lateral disengagement (overlapping). All groups and earlier-code groups are retained in interventions.csv; associations are descriptive and do not classify intent or safety-critical takeover. The27.7mph event above is the clearest pre-input low-speed shortfall. At15:08:20.535, pressure at63.5mph follows the67mph excess episode, then braking/disengagement. Its preceding2.8clean seconds have115.0% median body response but range widely; this warrants review, not a claim that the earlier overshoot caused the input.

| CDT | Speed | Signals associated |
| --- | ---: | --- |
| <private clock time> | 21.5 mph | steering-pressure-associated |
| <private clock time> | 27.7 mph | steering-pressure-associated, turn-signal-associated |
| <private clock time> | 37.4 mph | steering-pressure-associated, turn-signal-associated |
| <private clock time> | 43.9 mph | steering-pressure-associated |
| <private clock time> | 63.9 mph | steering-pressure-associated, turn-signal-associated |
| <private clock time> | 43.6 mph | steering-pressure-associated |
| <private clock time> | 33.5 mph | steering-pressure-associated |
| <private clock time> | 36.5 mph | brake-associated, steering-pressure-associated |
| <private clock time> | 16.6 mph | brake-associated, steering-pressure-associated, turn-signal-associated |
| <private clock time> | 24.6 mph | steering-pressure-associated |
| <private clock time> | 24.2 mph | brake-associated, turn-signal-associated |
| <private clock time> | 18.3 mph | steering-pressure-associated |
| <private clock time> | 23.9 mph | brake-associated |
| <private clock time> | 23.7 mph | brake-associated, steering-pressure-associated |
| <private clock time> | 33.1 mph | brake-associated, steering-pressure-associated |
| <private clock time> | 66.4 mph | brake-associated |
| <private clock time> | 63.5 mph | brake-associated, steering-pressure-associated |

The43.9mph pressure event has1.05s of clean preceding demand near105.0% body response; do not classify it as a control failure without driver/video context. Other input episodes often lack a clean pre-window because of straight/low demand, blinkers, pressure or disengagement. No lane crossing, obstacle or driver intention is established by this numerical audit; model lane estimates are not surveyed tire clearance.

## Health and evidence quality

No active steering faults or invalid-CAN samples, permanent steering faults, Panda faults or RX-invalid counts. Temporary steering faults occur inactive at0mph startup/shutdown. Session04 has one Chestnut supply-fault sample at0.163s,0mph, assistance inactive, with an8.703V sample; it is not a driving steering fault but is retained rather than called absent. One active-mode0x3d6 rejection echo in session04 is brake-transition-associated; no active0x83 rejection. Preserve normal native cancellation behavior.

All routes have terminal endOfRoute markers;carState boundary gaps are8–13ms. Maximum within-route state gaps are83–141ms and affected samples are excluded by freshness checks. Wallclock offset spans are1.5–7.3ms and every clock sample is within100ms of the final cluster. Per-signal eligibility handles sensor/control/model freshness and disagreement. Body yaw's reported standard deviation is around0.013rad/s, materially relevant to gentle/low-demand ratios; ratios are descriptive estimates, not exact calibrated truths.

Reconstruction is diagnostic strategy replay on frozen recorded motion, not a full generated-controller/native safety replay or a prediction of handling. Session04 has99.36% half-step parity over active/unpressed mode1 updates (37 mismatches), so unmatched portions cannot establish exact causal guard timing. The quoted low-speed windows have100% parity. Session05 has100% parity. Replayed differing floating strategy updates are not automatically distinct packed CAN messages. No new control code or safety-limit changes were made, so no new build/safety certification is claimed.

The optional native CommaLab latest-three import independently confirmed the newest route's logger completion/hash checks before the app became unavailable; full native-job completion was not confirmed. All five downloads and quality checks above were independently completed using the directly authorized read-only SSH evidence path.

## Next work / open evidence

1. Locally trace the28mph native deviation clip against calibrated wheel target and actual wheel/body response. Preserve native limits and1.20/0.97; do not broaden gain across the entire band from this single high-demand turn.
2. Locally trace65–70mph admission, release and encoded effect using session05's exact-parity episodes; compare matched falling-demand curves and rising-demand transitions separately. The small steady improvement does not close the unwind issue.
3. Keep15mph,35–50mph and>=70mph evidence gaps open. Collect ordinary supervised repeatable curves in both directions and steady/entry/exit phases at legal appropriate speeds; do not pursue85mph or provoke a takeover to fill a table.
4. Preserve all17 event timestamps and user/video review as a separate evidence layer. No additional Comma modification is proposed as completed.

## Reproduce / inspect

Scripts: acquire.py (read-only SSH acquisition), extract.py/process.py, analyze.py, phase_review.py, extra_review.py, match.py, reconstruct.py, episode_review.py, quality.py, write_report.py. Use the pinned paired-build run.py environment. Private raw route mappings/GNSS stay outside this report. Public evidence: acquisition-provenance.json,input-manifest.json,normalized-manifest.json,quality-audit.json,analysis.json,phase-review.json,focused-health.json,matched-comparison.json,matched-pairs.json,episode-review.json,interventions.csv and per-session reconstruction artifacts. Matches are chosen without looking at outcome; reuse of a previous timestamp is prohibited. No randomized or confidence-interval claim is made from correlated20Hz samples.
