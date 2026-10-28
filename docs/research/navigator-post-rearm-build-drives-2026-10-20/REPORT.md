<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# New drives recorded during local integration

October20,2026. Passive download and observational analysis only; **no device mutations**. Two moving recordings,18segments,160,565,513raw bytes, all hashes verified. Raw identities/GNSS remain in the private CommaBackups cache. Inventory/source/settings were identical before and after acquisition.

Installed code remains parent`0171b897289be53fd62f330935c55825b86c3c3a`/child`4167433e5c575f620a9dedf8144a0bc7cba14291`. Both source trees were clean. Existing high-speed/roll/tracking/pinion/low-speed preferences and update pause were on; Alpha longitudinal was off. Protected steering/geometry/firmware/launch files matched across acquisition. This is evidence about the existing installation, **not a test of the newly integrated calibrated/mid/rearm policy**.

## Coverage and findings

Recordings start10:48:25and11:00:08CDT, last540.24and511.72seconds, with278.9and318.6seconds of lateral engagement; maximum speeds70.47and65.65mph.

| mph | Active seconds | Clean meaningful seconds | Median body response | Steady seconds |
| --- | ---: | ---: | ---: | ---: |
| 0–5 | 37.8 | 0 | — | 0 |
| 5–10 | 7.3 | 0 | — | 0 |
| 10–15 | 6.8 | 0 | — | 0 |
| 15–20 | 16.6 | 0 | — | 0 |
| 20–25 | 128.2 | 4.70 | 69.0% | 0.00 |
| 25–30 | 46.5 | 3.55 | 94.8% | 0.00 |
| 30–35 | 49.0 | 8.45 | 95.0% | 0.50 |
| 35–40 | 23.9 | 6.70 | 103.9% | 0.05 |
| 40–45 | 17.2 | 0.20 | 89.4% | 0.00 |
| 45–50 | 14.6 | 0.20 | 95.5% | 0.00 |
| 50–55 | 31.1 | 16.65 | 115.4% | 1.90 |
| 55–60 | 84.9 | 36.75 | 115.7% | 3.35 |
| 60–65 | 30.8 | 15.05 | 104.2% | 3.80 |
| 65–70 | 103.0 | 57.05 | 114.5% | 13.05 |
| 70–75 | 0.1 | 0.05 | 90.0% | 0.00 |

Body response means calibrated body yaw divided by requested curvature×speed, excluding nearzero targets. It is not lane accuracy, steering authority or a direct gain recommendation.20Hz past-only alignment requires fresh valid active lane-keeping data and excludes brake/blinker/fault/driver-pressure context (including recent pressure). Meaningful target requires>=0.25m/s² and additionally |curvature|>0.001/m below50mph. Steady requires a full prior second of stable demand/speed/sign. See[analysis](../../navigator-reference/PRIVATE_ARTIFACTS.md) for exact definitions.

- **15mph remains untested:** no clean meaningful13–17mph demand. Active time alone does not fill that gap.
- **20–25mph remains the strongest shortfall:**4.7clean meaningful seconds, pooled median69.0%, no steady window. At10:55:14.400CDT around24.4mph,1.7clean seconds before steering input have median70.4% body response; preceding brake-associated input at10:55:22 has0.5s at65.1%. The upcoming policy addresses experimental admission, but no causal improvement is established.
- **25–30mph:**3.55clean meaningful seconds, median94.8%, no steady window. This does not disprove the earlier26mph rearming failure; suitable repeated same-phase turns remain sparse.
- **35–50mph:** very limited steady evidence;40–50mph has only0.4clean meaningful seconds total. Preserve the tune and keep gathering ordinary matched data.
- **37.5–38.0mph:** one0.55s transient at10:54:26.382CDT reaches148.4% median body response, with0.303m/s² median excess. It is not a steady calibration sample or proven lane crossing.
- **63–65mph:** first recording has1.6steady seconds at98.6% body/98.5% wheel response. Unwind evidence in that narrow range is only0.1s and0.2s across the two recordings, too little to validate the64mph fix.
- **65–70mph:** first recording provides13.05steady seconds at113.0% body/115.5% offset-corrected wheel response and10.8unwinding seconds at131.0% body/122.4% wheel. A0.25s lag sensitivity reduces unwind body response to118.1%;0.4s gives113.5%. Timing explains part, not all, of the apparent excess. These are observational sensitivity checks, not an identified delay or a proven controller cause. Retain this episode for post-install matched comparison.
- **75–85mph:** no new coverage.

## Inputs, disengagements and health

All22input/disengagement groups are retained in[interventions.csv](../../navigator-reference/PRIVATE_ARTIFACTS.md) and[analysis.json](../../navigator-reference/PRIVATE_ARTIFACTS.md), with brake/turn-signal/steering-pressure associations and pre-input evidence. Flags alone cannot establish driver intention or classify every event as an emergency takeover. Notable pressure-associated windows include61mph at10:51:13.581,69mph at10:51:49.281,24.4mph at10:55:14.400and47.9mph at11:06:36.507CDT.

No Panda/supply faults or permanent steering faults were recorded. CAN-invalid and temporary steering-fault samples occur only while inactive; temporary fault episodes are stationary startup/shutdown. Four active mode1 rejected0x3d6 echoes are near brake transitions; active0x83 echoes are absent. Preserve cancellation behavior; do not bypass safety gating based on these counts. See[health and rejection details](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Next evidence

Finish the authorized paired integration/build checks independently of these observations. After separate installation/parked acceptance authorization, compare ordinary safe turns around23–29mph and the65–70mph unwind against these saved episodes. Obtain broad safe13–17mph demand only when naturally available; do not hold engagement or force speeds/turns to collect it.35–50mph steady evidence and upper-speed evidence remain incomplete. No new gain or budget change was made from these recordings.

[Acquisition provenance](../../navigator-reference/PRIVATE_ARTIFACTS.md),[input manifest](../../navigator-reference/PRIVATE_ARTIFACTS.md),[phase/wheel/lag details](../../navigator-reference/PRIVATE_ARTIFACTS.md).
