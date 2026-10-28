<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator saved-drive review — October 21, 2026

Downloaded all seven new recent recordings / 59 unlocked segments (475,582,190 compressed log bytes). Five moving drives today use parent `db584234805cf2039ee976d856a29b655188ad2a`, paired with unchanged steering child `8ccc6cf0ee123afddddbf6e0a0ea3d3316669a5e` at acquisition. One stationary recording uses the preceding parent; another stationary recording uses the new parent. No device changes, active ECU queries or manual CAN. Owner 1.20/0.97, steering preferences, update pause and stockACC/AlphaOff retained in the acquisition inventory. Raw logs, route identities and GNSS remain in the private acquisition folder.

## Findings

- **22–25 mph turn-entry shortfall remains.** At <private clock time>–<private clock time>, 1.4 clean pre-input seconds yield 35.1% median body response and 40.5% wheel response. Request rises sharply; turn-exceeds-limit/steerSaturated is recorded, followed by steering pressure/brake. A 0.4 s lag sensitivity still gives 56.5% on 0.95 s of eligible overlap. No rejected CAN echo in the focused window. Do not equate the saturation alert with a proven hard EPS limit: inspect the requested path, encoded command, rate/deviation clamps and correction admission locally before choosing a change. Lane confidence is very low here; no lane-crossing inference.

- **Highway excess remains observable around 74 mph.** Before the second input at <private clock time>, 2.8 clean seconds show 127.3% body and 127.1% wheel response. Delaying the reference by 0.25/0.4 s leaves 123.6/121.3% body response. The broader bend has 12.25 clean seconds at 118.7% body response. This warrants source/target/unwind review, but is not a proven regression from merging master. **User explicitly reports avoiding a chunk of tire in the middle of the lane.** Inputs at <private clock time> and <private clock time> are therefore annotated as debris avoidance, not confirmed tracking-failure takeovers. Logs do not establish why debris appeared or prove a lane crossing. No video reviewed.

- **55–65 mph steady response is closer to target than transient response.** 55–60 mph has 13.55 steady seconds at 105.2%; 60–65 mph has 16.10 s at 103.4%. Unwind remains different:64–70 mph has only 4.50 clean unwind seconds across two drives, with per-drive body medians 129.9% and 117.6%. A 0.25 s reference shift reduces those to 109.8% and 103.5%, suggesting timing contributes; it does not demonstrate a control fix or causal improvement.

- **Do not call the remaining speed ranges calibrated.** 13–17 mph has no clean meaningful sample; 15–20 mph has only 0.40 s. 35–50 mph contributes 31.25 clean seconds but only 2.90 steady seconds. Max recorded speed 74.6 mph: no new 75–85 mph evidence.45 mph remains subject to measurement, not assumed perfect.

- **No active steering-fault or CAN-invalid samples.** Seven active-mode steering rejection echoes occur at brake transitions; no active 0x83 echoes. All five moving drives run the big model with zero reported model frame drops during assistance. Keep separate inactive startup/shutdown transient faults, the brief noon low-speed inactive RX-check warning, and startup supply flags; details below.

The master merge did not change the child steering controller. These routes are observational, with different turns, demand, roll and timing. There is no matched before/after trial establishing master improved or worsened physical tracking. Response percentages measure calibrated body yaw relative to requested curvature×speed, not lane safety or a directly usable gain multiplier.

## Recorded sessions

Times are America/Chicago (CDT). Active duration is the 20 Hz observed lateral-active stream, not distance.

|Recording|Start|Duration s|Max mph|Lateral active s|Clean meaningful s|Recorded parent|
|---|---|---:|---:|---:|---:|---|
|master-session-01|<private wall-clock timestamp>|197.9|0.0|0.0|0.00|f7b0c47d2|
|master-session-02|<private wall-clock timestamp>|253.9|0.0|0.0|0.00|db5842348|
|master-session-03|<private wall-clock timestamp>|578.4|74.1|237.1|86.10|db5842348|
|master-session-04|<private wall-clock timestamp>|591.2|74.4|348.6|56.05|db5842348|
|master-session-05|<private wall-clock timestamp>|398.3|35.2|96.7|0.50|db5842348|
|master-session-06|<private wall-clock timestamp>|543.9|74.6|236.4|42.95|db5842348|
|master-session-07|<private wall-clock timestamp>|773.4|69.4|240.4|53.90|db5842348|

New-parent assistance totals 1159.1 s, with 239.50 clean meaningful seconds after filters. These filtered seconds are not the full driving time.

## All speed ranges

100% is equality with the current requested turning at that sample; transient lag, mapping, road roll and sensor uncertainty affect the ratio. Sparse windows cannot establish a tune. All rows below use only the new parent.

|mph|Active s|Clean s|Body median|Steady s|Steady body median|
|---|---:|---:|---:|---:|---:|
|0–5|79.05|0.00|—|0.00|—|
|5–10|16.90|0.00|—|0.00|—|
|10–15|17.10|0.00|—|0.00|—|
|15–20|38.60|0.40|54.8%|0.00|—|
|20–25|170.60|5.00|54.8%|0.00|—|
|25–30|63.30|5.15|85.2%|0.35|81.6%|
|30–35|72.75|3.30|98.0%|0.10|98.4%|
|35–40|97.85|18.80|103.3%|2.00|102.4%|
|40–45|71.65|9.40|112.9%|0.60|122.6%|
|45–50|59.05|3.05|120.6%|0.30|112.9%|
|50–55|60.65|35.85|114.1%|4.25|116.7%|
|55–60|149.65|66.25|109.9%|13.55|105.2%|
|60–65|125.85|59.80|112.3%|16.10|103.4%|
|65–70|64.40|16.40|115.4%|0.80|103.5%|
|70–75|71.70|16.10|120.0%|2.15|123.8%|
|75–80|0.00|0.00|—|0.00|—|
|80–85|0.00|0.00|—|0.00|—|
|85–90|0.00|0.00|—|0.00|—|
|90–95|0.00|0.00|—|0.00|—|
|95–100|0.00|0.00|—|0.00|—|

## All input/disengagement groups

All 40 groups are retained, including brake, turn-signal and planned-maneuver associations. They are not40 proven emergency takeovers. Most lack usable clean pre-input demand, often because lane-change/driver-pressure guards already apply. A dash means no clean meaningful pre-input data. User context is stored separately in human-context.json.

|Recording/event|Time CDT|mph|Recorded associations / human context|Pre-input clean s|Body median|
|---|---|---:|---|---:|---:|
|master-session-03/1|<private clock time>|63.9|steering-pressure-associated, turn-signal-associated|0.60|122.5%|
|master-session-03/2|<private clock time>|63.8|brake-associated|1.30|115.3%|
|master-session-03/3|<private clock time>|33.7|brake-associated|0.00|—|
|master-session-03/4|<private clock time>|23.9|brake-associated|0.00|—|
|master-session-03/5|<private clock time>|24.6|brake-associated|0.00|—|
|master-session-03/6|<private clock time>|23.4|brake-associated|0.00|—|
|master-session-03/7|<private clock time>|24.4|brake-associated, steering-pressure-associated|0.00|—|
|master-session-04/1|<private clock time>|23.1|brake-associated, steering-pressure-associated|0.00|—|
|master-session-04/2|<private clock time>|24.8|steering-pressure-associated|0.00|—|
|master-session-04/3|<private clock time>|24.8|steering-pressure-associated|0.00|—|
|master-session-04/4|<private clock time>|19.9|brake-associated, steering-pressure-associated|0.00|—|
|master-session-04/5|<private clock time>|20.9|steering-pressure-associated|0.00|—|
|master-session-04/6|<private clock time>|11.9|brake-associated, steering-pressure-associated, turn-signal-associated|0.00|—|
|master-session-04/7|<private clock time>|25.7|steering-pressure-associated|0.00|—|
|master-session-04/8|<private clock time>|32.4|brake-associated, steering-pressure-associated|0.00|—|
|master-session-04/9|<private clock time>|45.5|brake-associated, steering-pressure-associated|0.60|121.4%|
|master-session-04/10|<private clock time>|28.2|brake-associated, steering-pressure-associated|0.00|—|
|master-session-05/1|<private clock time>|9.9|brake-associated, steering-pressure-associated|0.00|—|
|master-session-05/2|<private clock time>|34.3|brake-associated, steering-pressure-associated|0.00|—|
|master-session-05/3|<private clock time>|34.1|brake-associated, steering-pressure-associated|0.00|—|
|master-session-05/4|<private clock time>|34.3|steering-pressure-associated, turn-signal-associated|0.00|—|
|master-session-05/5|<private clock time>|33.4|brake-associated, steering-pressure-associated|0.40|107.2%|
|master-session-05/6|<private clock time>|28.9|brake-associated, steering-pressure-associated, turn-signal-associated|0.00|—|
|master-session-06/1|<private clock time>|39.1|steering-pressure-associated|0.00|—|
|master-session-06/2|<private clock time>|36.8|brake-associated, steering-pressure-associated|0.10|-2.1%|
|master-session-06/3|<private clock time>|22.3|brake-associated, steering-pressure-associated|1.40|35.1%|
|master-session-06/4|<private clock time>|19.8|steering-pressure-associated|0.00|—|
|master-session-06/5|<private clock time>|49.9|steering-pressure-associated, turn-signal-associated|0.00|—|
|master-session-06/6|<private clock time>|53.4|steering-pressure-associated, turn-signal-associated|0.00|—|
|master-session-06/7|<private clock time>|60.0|steering-pressure-associated, turn-signal-associated|1.45|110.6%|
|master-session-06/8|<private clock time>|74.1|steering-pressure-associated; user: avoiding tire debris|2.80|110.7%|
|master-session-06/9|<private clock time>|73.9|steering-pressure-associated; user: avoiding tire debris|2.80|127.3%|
|master-session-06/10|<private clock time>|70.7|brake-associated, steering-pressure-associated|0.40|170.5%|
|master-session-06/11|<private clock time>|44.0|brake-associated, steering-pressure-associated, turn-signal-associated|0.50|110.3%|
|master-session-07/1|<private clock time>|29.0|steering-pressure-associated|0.00|—|
|master-session-07/2|<private clock time>|39.0|brake-associated|0.00|—|
|master-session-07/3|<private clock time>|66.8|steering-pressure-associated, turn-signal-associated|2.80|111.2%|
|master-session-07/4|<private clock time>|10.5|brake-associated|0.00|—|
|master-session-07/5|<private clock time>|30.2|steering-pressure-associated|0.00|—|
|master-session-07/6|<private clock time>|40.5|brake-associated, steering-pressure-associated|1.40|120.0%|

## Health and data quality

All 59 selected compressed logs match their device SHA 256/size before and after acquisition. All available segment indices in each recording are contiguous and unlocked; numeric segment order was used for the boundary audit (lexical1,10,2ordering is unsuitable). Largest intersegment car-state gap12.63 ms. Wall-clock offsets are stable (all samples within 100 ms of the final offset). Freshness guards exclude stale startup samples. The final recording ends with endOfSegment rather than endOfRoute: all available unlocked segments were downloaded, but a formal route-end sentinel is absent.

No active steering faults, CAN-invalid samples or permanent steering faults in any recording. Temporary steering-fault samples occur inactive at startup/shutdown, including0/1.4 mph. No Panda hardware faults/heartbeat loss in the sampled streams; the noon recording has nine RX-check-invalid samples at 2.2–2.6 mph with assistance inactive. The preceding stationary old-parent recording and first0.16 s of the <private clock time> new-parent recording have supply flags before fresh carState/carControl exist; speed/active status is unknown there, not falsely treated as active. All moving-drive active model samples report big model, zero drops and median execution 39.4–39.9 ms. Seven active-mode0x3d6 rejected echoes coincide with nearby brake presses; keep cancellation protections intact.

## Next local investigations and evidence gaps

1. Trace 22–25 mph rising-demand episode through planner target, calibration, encoded steering, native deviation/rate limits and correction admission. Alert alone does not identify the limiting layer; preserve safety limits.
2. Review 74 mph calibrated wheel target and unwind using the saved bend, excluding driver-input windows. Preserve the human debris-avoidance explanation separately; any claim of actual lane crossing requires independent video/lane evidence.
3. Keep 64–70 mph unwind open and use lag/phase-matched comparisons. 35–50 mph, especially40–50 mph steady bends, still needs better normal-driving evidence.13–17 mph and 75–85 mph are not validated by these routes; no request for deliberate high-speed testing.

No prototype, settings change or installation performed in this analysis.

Reproducible evidence: acquisition-provenance.json, input-manifest.json, normalized-manifest.json, analysis.json, phase-review.json, focused-episodes.json, focused-health.json, health-context.json, quality-audit.json, interventions.csv and speed-bands.csv. Raw/private path is recorded only in acquisition provenance; no video/GPS exported.
