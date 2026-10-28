<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# AGNOS 20 drive review — October 22, 2026

Downloaded all 11 new recordings / 137 completed segments: 1,117,905,795 compressed log bytes. Every downloaded hash and final remote inventory matches. Seven recordings identify AGNOS 20 and parent `26b3416a6b` in initData; four identify AGNOS 19.9 and the prior parent. Current live child `fe59e50338` and both clean source trees verified at acquisition. Seven AGNOS 20 recordings include five with assistance active, one short manual drive and one parked recording. Raw route identifiers/GNSS stay in the private acquisition directory. Device mutations: zero.

## Findings

- **Runtime behaved well in the available AGNOS 20 recordings.** No recorded unexpected process stops; thermal status stays `ok`; UI p99 frame time is about 16.7 ms in the three long recordings, with maximum inter-message gap under 80 ms. No sustained recurrence of the prior UI stall is observed. All assistance-active model samples use the big model with zero reported frame drops. One short manual recording has a startup drop reading up to 16.0%; assistance never activates there. This establishes recorded behavior, not absence of every possible runtime issue.

- **23–24 mph remains the clearest low-speed problem.** At about <private clock time>–<private clock time>, the focused window has 2.75 clean seconds at 50.8% median body response and 60.8% wheel response. Another window about <private clock time>–<private clock time> has 1.90 clean seconds at 47.9% body / 52.8% wheel. `steerSaturated` is recorded near both, followed by steering/brake input. A 0.4 s reference shift increases response to 75.8% / 71.5%, so lag explains part but not all. At <private clock time>–<private clock time>, a separate 24 mph window has 4.2 clean seconds at 66.5% body / 68.9% wheel; shifting the reference changes little. Saturation does not by itself identify a software clamp versus EPS authority.

- **70–79 mph excess turning is still present.** The 77–79 mph window around <private clock time>–<private clock time> has 14.35 clean seconds at 123.1% body / 133.7% wheel response, with no rejected steering echo in the window. A 0.25/0.4 s reference shift gives 125.9/126.7%, so simple time lag does not explain the whole window. Lane-change events occur nearby and are excluded from the clean sample mask; this does not prove a lane crossing or a tracking-failure takeover. The 72 mph pre-input window around <private clock time>–<private clock time> has 3.8 clean seconds at 140.7% body / 141.1% wheel, with turn-signal/lane-change context near the input.

- **40–50 mph should remain in the investigation.** 40–45 mph contributes 7.25 steady seconds at 116.5% body response; 45–50 mph contributes 21.8 steady seconds at 113.1%. In the latter band wheel response is 114.8% on the main contributing drive and delay sensitivity leaves the excess. This is useful evidence of bias on these routes, not a reason to divide the steering gain by that percentage.

- **64–70 mph unwind is not resolved.** Per-drive clean unwind medians are 115.8%, 117.3% and 122.5%, but the first two contain only 0.40 / 0.25 s. The third has 6.05 s and falls to 116.0% / 112.3% with a 0.25 / 0.4 s reference shift. Timing contributes, with remaining disagreement. These different-route observations cannot establish the new onset correction improved or worsened tracking.

- **15 mph and 85 mph remain unproved.** 10–15 mph has only 1.30 clean meaningful seconds, median 39.6%; 15–20 mph has none. Highest recorded speed is about 80.0 mph, with no meaningful clean 80–85 mph sample and no 85 mph evidence. Do not extrapolate the highway results into a claim of stability at 85.

The OS update coincided with a master/source and steering-policy update, and the roads/demands differ from previous drives. There is no matched OS-only before/after experiment. Runtime appears healthy; steering is neither uniformly perfect nor proven worse because of AGNOS 20.

## Recorded sessions

Times are America/Chicago. Only exact AGNOS20/parent-matched recordings are listed here.

|Recording|Start|Duration s|Max mph|Active s|Clean meaningful s|
|---|---|---:|---:|---:|---:|
|agnos20-session-05|<private wall-clock timestamp>|439.6|31.1|188.6|3.00|
|agnos20-session-06|<private wall-clock timestamp>|66.4|12.1|0.0|0.00|
|agnos20-session-07|<private wall-clock timestamp>|192.4|43.8|100.1|0.75|
|agnos20-session-08|<private wall-clock timestamp>|877.4|0.0|0.0|0.00|
|agnos20-session-09|<private wall-clock timestamp>|2382.1|74.9|306.2|78.95|
|agnos20-session-10|<private wall-clock timestamp>|1379.9|74.4|802.3|140.70|
|agnos20-session-11|<private wall-clock timestamp>|1456.2|80.0|1228.0|140.10|

Assistance-active time: 2625.2 s; clean meaningful evidence: 363.50 s. These are time samples, not independent trials.

## All recorded speed ranges

Body response = calibrated body yaw / (requested curvature × speed). 100% means equality to the current request, not lane safety. Low-demand/near-zero targets are excluded. Sparse rows remain uncertain.

|mph|Active s|Clean s|Body median|Steady s|Steady body median|
|---|---:|---:|---:|---:|---:|
|0–5|387.40|0.00|—|0.00|—|
|5–10|164.00|0.00|—|0.00|—|
|10–15|132.55|1.30|39.6%|0.15|48.7%|
|15–20|106.05|0.00|—|0.00|—|
|20–25|212.00|30.65|67.4%|5.70|73.6%|
|25–30|280.75|13.80|81.3%|1.30|85.9%|
|30–35|76.55|6.35|98.5%|0.50|107.9%|
|35–40|149.40|4.95|116.8%|0.90|109.8%|
|40–45|63.20|17.70|116.4%|7.25|116.5%|
|45–50|71.95|37.50|112.5%|21.80|113.1%|
|50–55|71.45|30.70|111.2%|2.75|113.9%|
|55–60|182.80|46.50|102.7%|10.85|103.8%|
|60–65|295.65|64.55|110.3%|11.30|107.2%|
|65–70|175.65|39.90|108.3%|13.35|107.4%|
|70–75|184.65|57.10|123.1%|2.70|119.2%|
|75–80|71.10|12.50|127.8%|0.70|129.4%|
|80–85|0.05|0.00|—|0.00|—|

## Inputs and disengagements

Owner follow-up: “i think avoiding some thing?” This is uncertain possible obstacle avoidance, without identifying which queried event (<private clock time> or <private clock time>–<private clock time>). Do not attribute all inputs to an obstacle or label them confirmed tracking-failure takeovers. The measured pre-input shortfall/excess remains separate evidence. See [human context](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Reviewed all 83 detected input/disengagement groups, including 67 on AGNOS 20. These include routine brake/cancel/lane changes and steering pressure; they are not 67 confirmed failures. No video was reviewed; the owner tentatively recalls avoiding something, without identifying an exact event. Full event list: [interventions.csv](../../navigator-reference/PRIVATE_ARTIFACTS.md); the AGNOS20 event list follows.

|Recording / event|Local time|mph|Association|Pre-input clean s / body median|
|---|---|---:|---|---|
|agnos20-session-05 / 1|<private clock time>|29.2|brake-associated|0.00 / —|
|agnos20-session-05 / 2|<private clock time>|22.5|brake-associated|0.00 / —|
|agnos20-session-05 / 3|<private clock time>|9.6|brake-associated, steering-pressure-associated|0.00 / —|
|agnos20-session-05 / 4|<private clock time>|25.5|steering-pressure-associated|0.15 / 86.0%|
|agnos20-session-05 / 5|<private clock time>|28.0|steering-pressure-associated|0.35 / 68.9%|
|agnos20-session-05 / 6|<private clock time>|26.4|brake-associated, steering-pressure-associated|0.50 / 72.2%|
|agnos20-session-05 / 7|<private clock time>|21.1|steering-pressure-associated|0.00 / —|
|agnos20-session-05 / 8|<private clock time>|29.2|brake-associated, steering-pressure-associated|0.00 / —|
|agnos20-session-07 / 1|<private clock time>|29.4|steering-pressure-associated, turn-signal-associated|0.00 / —|
|agnos20-session-07 / 2|<private clock time>|23.2|steering-pressure-associated|0.00 / —|
|agnos20-session-07 / 3|<private clock time>|20.8|brake-associated, steering-pressure-associated, turn-signal-associated|0.00 / —|
|agnos20-session-07 / 4|<private clock time>|36.4|steering-pressure-associated|0.00 / —|
|agnos20-session-07 / 5|<private clock time>|35.8|brake-associated|0.00 / —|
|agnos20-session-07 / 6|<private clock time>|31.6|brake-associated, steering-pressure-associated, turn-signal-associated|0.00 / —|
|agnos20-session-09 / 1|<private clock time>|27.9|steering-pressure-associated|0.00 / —|
|agnos20-session-09 / 2|<private clock time>|20.1|steering-pressure-associated|0.00 / —|
|agnos20-session-09 / 3|<private clock time>|29.1|steering-pressure-associated, turn-signal-associated|2.80 / 71.6%|
|agnos20-session-09 / 4|<private clock time>|61.0|steering-pressure-associated, turn-signal-associated|1.15 / 140.3%|
|agnos20-session-09 / 5|<private clock time>|58.1|brake-associated, steering-pressure-associated|0.60 / 117.2%|
|agnos20-session-09 / 6|<private clock time>|27.9|brake-associated|0.00 / —|
|agnos20-session-09 / 7|<private clock time>|27.1|steering-pressure-associated|0.00 / —|
|agnos20-session-09 / 8|<private clock time>|28.7|brake-associated|0.00 / —|
|agnos20-session-09 / 9|<private clock time>|29.5|brake-associated, steering-pressure-associated|0.00 / —|
|agnos20-session-09 / 10|<private clock time>|28.6|brake-associated|0.00 / —|
|agnos20-session-10 / 1|<private clock time>|25.0|steering-pressure-associated|0.00 / —|
|agnos20-session-10 / 2|<private clock time>|21.3|brake-associated|0.00 / —|
|agnos20-session-10 / 3|<private clock time>|23.6|brake-associated, steering-pressure-associated|2.55 / 50.8%|
|agnos20-session-10 / 4|<private clock time>|23.6|brake-associated, steering-pressure-associated|1.70 / 48.7%|
|agnos20-session-10 / 5|<private clock time>|60.6|steering-pressure-associated|0.00 / —|
|agnos20-session-10 / 6|<private clock time>|47.6|steering-pressure-associated|2.80 / 114.2%|
|agnos20-session-10 / 7|<private clock time>|43.0|steering-pressure-associated|2.80 / 117.3%|
|agnos20-session-10 / 8|<private clock time>|59.9|steering-pressure-associated, turn-signal-associated|2.80 / 102.7%|
|agnos20-session-10 / 9|<private clock time>|59.7|brake-associated, steering-pressure-associated, turn-signal-associated|0.00 / —|
|agnos20-session-10 / 10|<private clock time>|43.2|steering-pressure-associated|0.00 / —|
|agnos20-session-10 / 11|<private clock time>|55.4|steering-pressure-associated|2.80 / 98.8%|
|agnos20-session-10 / 12|<private clock time>|52.9|steering-pressure-associated|1.75 / 100.1%|
|agnos20-session-10 / 13|<private clock time>|51.1|steering-pressure-associated|1.65 / 105.1%|
|agnos20-session-10 / 14|<private clock time>|48.1|steering-pressure-associated|2.80 / 112.7%|
|agnos20-session-10 / 15|<private clock time>|47.8|steering-pressure-associated|2.80 / 111.6%|
|agnos20-session-10 / 16|<private clock time>|47.5|steering-pressure-associated|2.80 / 114.1%|
|agnos20-session-10 / 17|<private clock time>|45.4|steering-pressure-associated|1.60 / 111.1%|
|agnos20-session-10 / 18|<private clock time>|69.4|steering-pressure-associated|0.25 / 82.0%|
|agnos20-session-10 / 19|<private clock time>|73.8|steering-pressure-associated, turn-signal-associated|2.80 / 128.6%|
|agnos20-session-10 / 20|<private clock time>|73.7|steering-pressure-associated|0.00 / —|
|agnos20-session-10 / 21|<private clock time>|73.9|brake-associated|0.00 / —|
|agnos20-session-10 / 22|<private clock time>|39.2|brake-associated|0.00 / —|
|agnos20-session-10 / 23|<private clock time>|25.1|steering-pressure-associated|0.00 / —|
|agnos20-session-10 / 24|<private clock time>|38.9|brake-associated|0.00 / —|
|agnos20-session-11 / 1|<private clock time>|24.4|brake-associated, steering-pressure-associated|2.80 / 67.4%|
|agnos20-session-11 / 2|<private clock time>|28.6|brake-associated|0.00 / —|
|agnos20-session-11 / 3|<private clock time>|9.8|steering-pressure-associated|0.00 / —|
|agnos20-session-11 / 4|<private clock time>|13.8|brake-associated, steering-pressure-associated|0.00 / —|
|agnos20-session-11 / 5|<private clock time>|30.8|steering-pressure-associated|2.15 / 83.9%|
|agnos20-session-11 / 6|<private clock time>|40.2|brake-associated, steering-pressure-associated|1.45 / 119.8%|
|agnos20-session-11 / 7|<private clock time>|72.2|steering-pressure-associated, turn-signal-associated|2.80 / 144.2%|
|agnos20-session-11 / 8|<private clock time>|64.1|steering-pressure-associated, turn-signal-associated|0.00 / —|
|agnos20-session-11 / 9|<private clock time>|66.5|steering-pressure-associated, turn-signal-associated|0.00 / —|
|agnos20-session-11 / 10|<private clock time>|57.0|steering-pressure-associated|2.80 / 96.6%|
|agnos20-session-11 / 11|<private clock time>|40.7|steering-pressure-associated, turn-signal-associated|2.80 / 114.6%|
|agnos20-session-11 / 12|<private clock time>|54.9|steering-pressure-associated, turn-signal-associated|0.00 / —|
|agnos20-session-11 / 13|<private clock time>|66.2|steering-pressure-associated, turn-signal-associated|0.00 / —|
|agnos20-session-11 / 14|<private clock time>|79.0|steering-pressure-associated, turn-signal-associated|0.00 / —|
|agnos20-session-11 / 15|<private clock time>|79.5|brake-associated|0.00 / —|
|agnos20-session-11 / 16|<private clock time>|6.1|brake-associated|0.00 / —|
|agnos20-session-11 / 17|<private clock time>|51.7|brake-associated, steering-pressure-associated|2.80 / 117.3%|
|agnos20-session-11 / 18|<private clock time>|25.1|steering-pressure-associated|0.05 / 87.7%|
|agnos20-session-11 / 19|<private clock time>|29.0|brake-associated, steering-pressure-associated, turn-signal-associated|0.00 / —|

Notable cases: <private clock time> / <private clock time> at 23–24 mph follow measured shortfall. Repeated pressure at <private clock time> and <private clock time>–<private clock time> spans 45–48 mph with roughly 111–114% clean pre-input response. The <private clock time> input at 72 mph and <private clock time> input at 79 mph have turn-signal associations; the latter has no clean three-second pre-input sample. Their intent must not be inferred from tracking ratios.

## Safety/runtime context and integrity

No AGNOS20 active-mode steering fault or CAN-invalid samples. Eight active mode-1 steering rejection echoes occur at or immediately around braking; all are brake-associated within the inspected transition window. No active 0x83 rejection. Inactive temporary steering-fault flags occur at startup/shutdown and one brief low-speed inactive transition, without permanent-fault samples. No Panda or Chestnut supply-fault samples in the normalized sessions. See [focused health](../../navigator-reference/PRIVATE_ARTIFACTS.md), [health context](../../navigator-reference/PRIVATE_ARTIFACTS.md) and [runtime review](../../navigator-reference/PRIVATE_ARTIFACTS.md).

All routes have contiguous segment indices, unlocked finalized files and verified hashes. Startup state gaps reach about 0.14 s; eligibility rejects stale state. Two early recordings have large wall-clock adjustments; the last stable clock cluster is used, and one pre-update route remains dated July 28 by its own clocks. Do not use that wall date to infer chronology. Target highway recordings 09–11 have stable wall clocks. One pre-update short runtime-only recording lacks core tracking streams and is explicitly excluded. Historical `prior` fields in analysis.json refer to an older descriptive baseline, not a matched AGNOS comparison.

## Next work

1. Investigate the 23–24 mph saturation windows locally: desired curvature, calibrated wheel target, command rate/deviation clamp, correction admission and actual wheel response. Preserve the request/command distinction.
2. Investigate the 70–79 mph body/wheel excess and unwind using these windows, including the 40–50 mph steady bias; avoid a blanket gain change from pooled ratios.
3. Keep the 64–70 mph timing issue open. Do not label 15 mph or 85 mph calibrated without representative clean evidence. No special high-speed collection is requested.
4. Preserve 1.20/0.97 and current device configuration. No tuning, service restart, update, firmware action, active ECU query or manual CAN was performed.

Evidence: [acquisition](../../navigator-reference/PRIVATE_ARTIFACTS.md), [quality audit](../../navigator-reference/PRIVATE_ARTIFACTS.md), [analysis](../../navigator-reference/PRIVATE_ARTIFACTS.md), [focused episodes](../../navigator-reference/PRIVATE_ARTIFACTS.md), [phase review](../../navigator-reference/PRIVATE_ARTIFACTS.md).
