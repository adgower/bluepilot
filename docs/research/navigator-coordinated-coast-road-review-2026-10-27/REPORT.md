<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Coordinated coast/brake road review — October 27, 2026

The new recording confirms **persistent brake/accel cycling, assisted high RPM, and excess turning at 40–50 mph**. It does not establish a physical comfort improvement from the coordinated allocator. No controls-mismatch event or alert, coordination fault, or invalid enabled input was recorded. No tuning, setting, service, firmware or installation changes were made.

## Coverage and identity

All 73 new completed segments across five sessions were downloaded with matching remote/local SHA-256 hashes and sizes; no open segments were deferred. Sessions 01–03 used the previous code, session 04 the new code while stationary. Only session 05 contains moving assistance. It ran about **<private clock time>–<private clock time> CDT**, with roughly 17.4 minutes of qualified Alpha command exposure and maximum qualified assisted speed **69.37 mph**. There is no new 70–85 mph assessment. All original recordings, including parked sessions, are retained in a verified private Mac archive. Disposable decoded parked-session caches were removed to limit Mac disk use; original logs are intact.

Installed and recorded current parent: `df788e02719c05595dab2f980e6fd9fb9e464006`; paired child: `1d29e6e78abcbf5c6a80eb397d80b349c6cca960`. The acquisition inventories found clean source, Alpha/coordination ON, owner steering opt-ins intact and AGNOS 20.1. Personality was Relaxed (stored value 2); ExperimentalMode was unset. The child diff from the preceding installation changes longitudinal precharge allocation/tests, not lateral steering.

## Pulsing: still present

Representative continuously qualified 15-second windows:

| Start, CDT | Speed | Full-brake request bit changes | Reported brake torque range |
|---|---:|---:|---:|
| <private clock time> | 58–60 mph | 17 | 0–60 Nm |
| <private clock time> | 67–69 mph | 14 | 0–204 Nm |
| <private clock time> | 58–60 mph | 12 | 0–84 Nm |

These are bit changes, not complete cycles. Received brake-torque changes corroborate actuator cycling; they are not direct hydraulic pressure or cabin comfort measurements. The first two windows stay in gear 10, so shifts alone cannot explain them. The 67–69 mph window has a positive producer raw acceleration request throughout (0.049–0.470 m/s²) while mapped gravity compensation is negative (approximately −0.40 to −0.16 m/s²). The planner target is near zero and changes sign. This supports further joint review of near-zero demand, grade mapping, coast admission, integral and measured response; it does not establish that road slope caused every switch. Refreshed consumer pitch is not fully reconstructed here.

Above 40 mph, brake onsets occurred with a detected lead (7.78/min over 694 s) and without one (12.13/min over 208 s). This is observational exposure, not a controlled lead/no-lead comparison. Precharge-only allocation appears in 55 intervals totaling 12.09 qualified seconds; its presence is not proof of comfort benefit. The accepted patch was a narrow budget/bit-allocation change and did not remove the broader pulse loop. Earlier saved windows had 14/12/10 changes, but different routes/demands prevent treating that comparison as improvement or regression.

## Restart and high RPM

The approximately **2.17 mph rolling restart at <private clock time>** accelerates continuously through 6.7 and 8 mph. Wire propulsion remains positive around that boundary, without the old brake-bit cutoff. It reaches 15 mph near <private clock time> and 20 mph near <private clock time>. A separate stop/departure also crosses 6.7–8 mph without a brake-bit interruption. These are useful retained boundary regressions; unmatched restarts do not quantify an improvement from this latest allocator.

At **<private clock time>**, Alpha is active, both pedals are released, RPM reaches **3,946 at about 21.2 mph**, actual gear is 1 and target gear is 2. RPM remains at least 3,000 for about 3.28 qualified seconds during the 15.7–22.4 mph portion. At the peak, planner target is about **0.770 m/s²**, raw request **0.851**, integral about **0.08**, and wire propulsion **0.85**. No brake bit is asserted; reported brake torque is zero throughout this high-RPM interval. This is not evidence of braking against acceleration during the RPM peak, nor a large unexplained integral at that instant. The vehicle's shift response and the preceding first-gear demand need investigation together; openpilot's observed target-gear field is received telemetry, not an openpilot gear command. Earlier restart demand rose to roughly 1.5 m/s² while first gear remained reported.

A second brief assisted 3,050–3,296 RPM interval occurs around <private clock time> at 64–65 mph, actual gear 6 with target 7. It is a separate shift episode.

A preliminary causal-as-of join also observes brief nonzero reported brake torque at initial positive propulsion around both departures. That join is not exact ECU-consumed feedback or hydraulic pressure and must be traced against producer/consumer timing before making a clearance claim. Do not relax brake-clearance guards based on this analysis.

## Faults and driver interventions

No controlsMismatch events/alerts or coordination faults occur in the moving current-code session. Panda RX-invalid increments, fault flags, and enabled invalid-input counts are zero. This trip is evidence of no recurrence, not proof all historical mismatch causes are solved.

There are **15 blocked-transmit counter increments**: nine at disabled startup, one at a brake disengagement, one while the accelerator is pressed, and four at the final brake disengagement. Saved rejection echoes and causal pedal state corroborate those boundary associations. They do not establish every exact native rejection reason. Both full disengagements follow the brake pedal: <private clock time> (~20.6 mph) and <private clock time> (~26 mph). Seventeen lateral driver-input/disengagement groups were screened; signaled lane changes and pedal/steering inputs are not automatically failures.

## Lateral: reported oversteer is supported

Meaningful, fresh, assistance-active turns without recent pedals, steering override, signals or lane change show median calibrated body response around **117–118% of requested** at 40–50 mph. There are only about 69 seconds of eligible meaningful turning in those bands, mostly left turns. This ratio is observational and includes roll/calibration/model/dynamic uncertainty; it is not a universal gain target or a tire-authority measurement.

Specific retained episodes:

- **<private clock time>, 42–45 mph:** 1.95 s of excess turning, median response ~129% and signed lateral-acceleration excess ~0.32 m/s².
- **<private clock time>, ~49.7 mph:** excess turning immediately before steering pressure at **<private clock time>**, no turn signal or fault alert. The prior model-estimated nearest lane-line distance reaches about 0.64 m. This supports the reported feel, but does not prove a lane crossing or explain driver intent without video.
- **<private clock time>, ~63.7 mph:** a straight-like 10 s window shows three small body-response zero crossings and model lane-center movement of about 0.59 m peak-to-peak. Unwind response remains above request at 60–70 mph. Other straight-like sections are calmer, so a blanket speed-based gain reduction is not justified.

All observed speed bands were screened; low-speed meaningful-turn evidence is sparse. There is no new >70 mph evidence and no basis to claim 85 mph stability. Lateral code was unchanged by the coast/brake patch.

## Next local priorities

1. Use the 59 and 68 mph windows as regressions for joint coast/grade/integral/response analysis. Evaluate the physical-response timing, not only full-brake-bit counts; preserve strong braking and clearance.
2. Trace the 2.17→22 mph first-gear restart against recorded demand, received gear/torque, and OEM shift behavior. Separate planner demand from residual integral and transmission response. Preserve the now-continuous 6.7 mph boundary.
3. Investigate calibrated wheel/body/path agreement and unwind at 40–50 mph, using the <private clock time> pre-override segment; preserve owner 1.20/0.97 rather than applying a blanket gain change.
4. Keep the startup/pedal-boundary rejection audit open despite zero controlsMismatch on this trip. Exact consumed feedback near initial propulsion also remains a timing-audit item.

This is road-data analysis, not a new controller prototype, safety replay, installation approval or demonstration that the vehicle is safe at a particular speed. No video was downloaded or reviewed.

Evidence: [acquisition](../../navigator-reference/PRIVATE_ARTIFACTS.md), [durable archive receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md), [longitudinal analysis](../../navigator-reference/PRIVATE_ARTIFACTS.md), [pulse audit](../../navigator-reference/PRIVATE_ARTIFACTS.md), [restart windows](../../navigator-reference/PRIVATE_ARTIFACTS.md), [RPM/consumed-state audit](../../navigator-reference/PRIVATE_ARTIFACTS.md), [lateral analysis](../../navigator-reference/PRIVATE_ARTIFACTS.md), [health](../../navigator-reference/PRIVATE_ARTIFACTS.md), and [pedal-boundary CAN join](../../navigator-reference/PRIVATE_ARTIFACTS.md).
