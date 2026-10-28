<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Command-recovery road review — October 26, 2026

## Result

The new drive does **not establish whether command recovery improves rolling restarts or high RPM**: Alpha never became active below 9.65 mph, while the new reduction admits only below 6.7 mph. No controlsMismatch or Navigator coordination fault was recorded. Highway brake/coast cycling remains, alongside some lateral turn-entry shortfall and unwind/straight-section oscillation. No tuning or device changes were made.

## Acquisition and cohort

Downloaded all 34 new completed rlog segments across three sessions, verified sizes and SHA-256 hashes, and retained a verified private Mac archive. No locked/open segments were deferred. Two sessions were stationary (one on the previous installation); only session 03 was a moving current-code drive. That drive ran approximately **<private clock time>–<private clock time> CDT**, reaching 74.51 mph. Qualified Alpha exposure was approximately 16 minutes. There is no 75–85 mph evidence in this acquisition.

The device pair was `1dbbc01892616c4b1a5c7c841d132f724ea5132c` / `beb10c25770471534261606072c131db5eefa117`, AGNOS 20.1. Alpha, DisableUpdates and owner 1.20/0.97 settings were preserved. Recorded driving personality was **Relaxed** throughout the moving session. Raw logs remain private; no video was downloaded or reviewed.

## Rolling restart and RPM

Exact consumed-state checks found zero missing/invalid active state inputs and zero active samples below 3 m/s. The minimum was **9.6469 mph** near <private clock time> Controls were disabled before initial engagement, so there was no retained correction entering this drive. The new rolling-recovery admission condition was never met.

The fresh CAN RPM maximum was **3,358 RPM at <private clock time>, 65.8 mph**, with longitudinal assistance inactive and the accelerator pressed. The assisted/no-pedal maximum was **2,870 RPM**, immediately after that manual acceleration during a shift. No assisted samples reached 3,000 RPM. This trip did not reproduce the previous assisted 4,000 RPM complaint, but its lack of a qualifying slow restart prevents attributing that to the fix. The raw RPM quality field is not independently interpretable as validity here: the DBC documents it as not transmitted on gas/HEV vehicles.

[Consumed-state and RPM audit](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Highway pulsing

Cycling persists in both lead-following and no-lead sections, including these representative 15-second windows:

| Start, CDT | Speed | Brake-request bit changes | Reported brake torque |
|---|---:|---:|---:|
| <private clock time> | 58–62 mph | 14 | 0–156 Nm |
| <private clock time> | 62–64 mph | 12 | 0–116 Nm |
| <private clock time> | about 74 mph | 10 | 0–80 Nm |

These counts are changes, not complete cycles. Fresh received torque samples corroborate actuator cycling. All three windows remained in gear 10. The last two had no detected lead; the approximately 74 mph window had a positive planner acceleration target throughout, yet brake allocation still switched. That makes the coast/grade/integral allocation interaction a useful next local investigation, rather than assuming the planner alone asks for alternating braking.

Across 48,067 qualified command samples, there were zero positive-gas commands simultaneously carrying brake/precharge request bits, and zero positive-gas samples paired with latest causal reported brake torque above 4 Nm. This supports alternating allocation, not simultaneous commanded gas/brake in these samples. Received torque is not direct hydraulic pressure or exact consumed-torque evidence.

The producer pitch and logged offset only estimate mapped gravity compensation; the refreshed consumer pitch is not captured here. These recordings therefore do not prove that downhill grade caused any particular transition. Wheel-derived acceleration extrema are also not direct body-acceleration measurements. There is no matched before/after comfort comparison.

[Window audit](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [All observed speed bands](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Faults and disengagements

There were **zero controlsMismatch events/alerts and zero Navigator coordination faults** in the new moving session. Two full disengagements followed the brake pedal, at approximately **<private clock time> /54 mph** and **<private clock time> /26 mph**. Their driver intent is unknown.

Panda recorded 14 additional blocked-transmit increments: six at startup and eight associated with accelerator/brake override boundaries and queued-command timing. These did not produce a controlsMismatch event. The association does not identify every exact rejection reason and does not establish that all historical mismatch causes are resolved. Temporary steering faults, invalid-CAN startup samples and the single Chestnut supply fault occurred while stationary/disabled, not during moving assistance.

[Detailed health report](HEALTH_REPORT.md) · [CAN boundary join](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Lateral control

All observed speed ranges were screened. The clearest low-speed issue was a rising turn around **<private clock time>, 30.65 mph**: calibrated body yaw was approximately **70% of requested yaw**, with a software `steerSaturated` warning. Steering input and a turn signal followed about 2.24 seconds later. This does not independently prove a physical EPS limit or establish why the driver intervened.

Steady meaningful turns at 60–70 mph were generally near requested response in this recording. Unwind sections still showed excess response, and straight-like windows near 74 mph showed repeated small corrections and lateral motion. These support residual tracking/oscillation concerns, not a confirmed lane departure. Model lane positions and uncertain yaw ratios cannot substitute for video or ground truth. Nineteen steering-input-associated episodes were reviewed; they are not all classified as controller failures.

Low-speed steady-turn evidence remains sparse, and there is **no 75–85 mph coverage**. These data do not justify a blanket steering gain increase.

[Full lateral report and speed table](LATERAL_REPORT.md)

## Next evidence and local priorities

1. Obtain a naturally occurring assisted rolling slowdown/restart below 6.7 mph before judging this fix; do not force a maneuver to trigger it. Review RPM, gear, demand and brake clearance together.
2. Prioritize the persistent highway coast/brake/feedback interaction, using the three windows above as regressions. Preserve strong braking and brake-clearance behavior.
3. Review the approximately 31 mph rising-turn saturation and highway unwind/straight-section corrections separately. Preserve 1.20/0.97; do not infer a universal per-speed gain from unmatched turns.

The Comma installation, settings, services and firmware were left unchanged. Offline validation checked acquisition completeness, hashes, exact source cohort, causal input joins and analysis invariants; it is not a new controller safety replay or proof of improved road behavior.

[Verification receipt](PUBLIC_VERIFICATION.json) · [Acquisition provenance](../../navigator-reference/PRIVATE_ARTIFACTS.md)
