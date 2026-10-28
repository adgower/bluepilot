<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Post-regression road review — October 27, 2026

**No controlsMismatch recurrence in the new-code drive. Pulsing is not cured, and selected40–45mph tracking excess remains observed;45–50mph coverage is thin after excluding a planned maneuver.** Moving below40 exposure is too short for a strong improvement claim. No installed-source70–85mph evidence exists. Nothing on the Comma was changed.

## Acquisition and source cohorts

All79new completed segments across9sessions were downloaded and independently hash-verified:668,805,101original bytes. A private durable Mac archive verifies every original. Before/after SSH inventories agree on clean installed `e05e42f43` / `5097b993`, selected settings, protected file hashes and service metadata. Six downloaded sessions are pre-update `df788e027`;07–09 record the installed parent, but only08 contains meaningful assisted driving.07/09 contribute zero active longitudinal exposure. Recorded parent/dirty state is checked in every segment; current child identity comes from installation/acquisition receipts.

The installed drive ran about6:51–7:11p.m.CDT. It has1077.77s raw longitudinal-active exposure; strict fresh/no-override qualification retains974.621s (16.24min). Inactive/faulted/overridden periods are not counted as pulse-free improvement. Original route identities/GNSS remain private.

## Controls mismatch and clock fix

All9new sessions have0controlsMismatch alerts and0coordinator fault episodes. In the installed moving session,102,353active producer commands are protocolV3 with0invalid/future/stale pose samples. Recorded pose age relative to the producer clock spans18.158–87.957ms, below the unchanged100ms limit. This is encouraging evidence for the timestamp-ordering fix on this trip, not a guarantee that every future mismatch or historical release-timeout cause is solved. See [clock audit](../../navigator-reference/PRIVATE_ARTIFACTS.md) and [health scan](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Longitudinal: brief true coast activated, cycling remains

The bounded true-coast path activated:166feedback rows,83distinct consumed requests and18brief runs, totaling1.704s of feedback intervals. All0.3s age and0.01budget guards pass. The separate causal-backward CAN-anchor overlap is1.340s; neither value is an exact physical coasting duration or exact ECU-consumed packet receipt.

During qualified control there are236brake-request-bit changes (14.53/min) and67rapid reversals (<0.6s between edges). An edge is an on/off bit transition, not a complete cycle, stop or severity measurement.

| Saved window, long-session relative seconds | Speed | Brake-bit changes | Physical/context observations |
|---|---|---:|---|
|180.068–195.057|52.24–53.81mph|14|aEgo −0.950..+0.930m/s²; trailing-filter jerk p95≈2.73m/s³|
|383.137–398.118|40.64–49.80mph|14|Planner target and producer request both remain positive; received brake torque0..332Nm|
|316.067–331.047|56.99–58.79mph|12|No fresh lead; producer request remains positive|

Panda controlsAllowed stays true, RX-invalid remains0, blocked-TX counter is unchanged and no rejection echo occurs in these three windows. Thus these cycles are not explained by a controls-mismatch disengagement or repeated Panda rejection. Sent requests and received ECU status/torque remain distinct; torque is not direct hydraulic pressure, and filtered aEgo jerk is not a cabin-comfort measurement.

Below40 has149.640qualified seconds, including79.699s at0–5mph. Only**69.942s moving5–40mph**remain, with7changes and0rapid reversals, versus1068.143s moving5–40 in the V1 comparison. Only36.789s cover20–30mph. The old dense21–25mph condition was not comparably reproduced. The lower observed rapid-cycle count is descriptive, not proof of a cure.

Overall V3 edge rate14.53/min versus V1 8.47/min also does not prove worsening: speed, traffic, grade and exposure mixes differ substantially. Full command/response, lead and speed tables are in [longitudinal report](longitudinal/LONGITUDINAL_REPORT.md). No fuel-economy or qualified engine-restart benefit is established.

## Lateral: planned exit maneuver excluded

The driver confirmed that the road widened from two lanes to three and the input near7:04:48p.m.,49mph was an intentional move into the new rightmost lane for the next exit. This is not classified as a problem takeover. Excluding both ±6s and ±10s around that maneuver leaves the following independent evidence.

40–45mph retains25.25s of meaningful steady turning, with body/request median1.1472.45–50mph retains only4.65steady seconds, with source-time median1.1229 and publication-aligned median1.1272. These selected numerical tracking differences do not establish unexpected oversteer, lane crossing or a universal calibration multiplier. No sustained event survives the additional2×reported-yaw-uncertainty coherent screen.

The calibrated wire-equivalent command includes intentional mapping and owner factors. Wheel/body/request ratios cannot uniquely diagnose a mapping defect or physical plant gain, nor justify changing1.20. Other48–51mph excess windows include unwind, where timing matters; local reconstruction remains appropriate.

The requested [12-second clip](../../navigator-reference/PRIVATE_ARTIFACTS.md) includes both forward cameras; recorded pressure begins around6s. The [local player](http://127.0.0.1:8769/) shows the recorded pressure flag. No lane crossing overlay is synthesized and no cabin video was downloaded. [Maneuver exclusion sensitivity](../../navigator-reference/PRIVATE_ARTIFACTS.md) preserves both exclusion widths and the original measurements.

There are32grouped pressure/disengagement events,17with qualified preceding tracking context. Only2groups contain actual lateral-active falling edges, near11and22.5mph; both associate with pedals, and the latter also a signal. They are not32proven failures. Full event context is in [lateral report](lateral/LATERAL_REPORT.md).

## All-speed evidence

Longitudinal bins use filteredCarState.vEgo; lateral usesvEgoRaw/controller speed, so near-boundary samples differ. Overall maxima are69.23filtered/69.89raw mph; no installed-source70+coverage. Steady ratios below are meaningful-turn screening statistics, not calibration factors. Near-zero-demand ratios are excluded.

| Band mph | Qualified longitudinal s | Brake-bit changes/min | Meaningful steady lateral s | Steady body/request median |
|---|---:|---:|---:|---:|
|0–5|79.70|4.52|0.00|—|
|5–10|8.23|0.00|0.00|—|
|10–15|6.09|0.00|0.00|—|
|15–20|6.30|0.00|0.00|—|
|20–25|16.29|11.05|0.00|—|
|25–30|20.49|5.86|0.00|—|
|30–35|3.45|0.00|0.00|—|
|35–40|9.08|13.21|5.80|1.107|
|40–45|33.63|19.63|25.25|1.147|
|45–50|52.18|13.80|4.65|1.127|
|50–55|103.48|16.24|5.20|1.112|
|55–60|270.28|15.76|30.90|1.036|
|60–65|264.52|16.56|32.35|1.030|
|65–70|100.89|16.65|5.40|1.087|
|70–75|0.00|—|0.00|—|
|75–80|0.00|—|0.00|—|
|80–85|0.00|—|0.00|—|
|85–90|0.00|—|0.00|—|
|90+|0.00|—|0.00|—|

0–25mph lacks meaningful steady-turn coverage;25–35 is also sparse.55–65 selected steady turning is closer to target;65–70 has only5.4steady seconds. Different road conditions prevent blanket improvement claims.

Nineteen qualified5s quiet-demand windows retain straight/gentle-curve observations without near-zero ratios. At+710–714.95s near63mph, wheel-rate p10/p90≈−14/+8deg/s and body lateral-acceleration p10/p90≈−0.35/+0.22m/s². Bank/roll changes and yaw uncertainty coexist. This warrants a low-demand path/roll/wheel review, not a claim of video-proven ping-pong or lane excursion.

## Rejections, health and limitations

There are26rejected-frame echoes:13near startup,6around gas-override/brake-disengagement context, and7near recording end. The in-route echoes are4ACCDATA and2button/cancel frames; no in-route lateral-command rejection is observed. RX-invalid/RX-check-invalid and board/heartbeat-fault samples are0. Associations do not identify every native rejection reason; these are not silently called zero rejections. The adverse pulse windows contain none. See [Panda context](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The installed route logs23,887modelV2 samples with0reported frame drops. Some startup/tail stream records are invalid and excluded by the stated qualification; not every raw record is called valid. Strict longitudinal retention is974.621/975.092fresh active/no-override candidate seconds.

Independent review reproduced the14-edge window,69.94s moving low-speed exposure and key lateral statistics. Qualification wording was corrected: current gas/brake exclusion; preceding1s steering-pressure exclusion;2s active. Adding1s pedal history removes0steady40–50samples. Source-timed body measurements and arrival-timed sensitivity are separate; the arrival check leaves key results unchanged and has0eligible future source/publication samples. Qualified motion delivery max is31.97ms; stale startup source timestamps are excluded. Display CSVs are decimated; hashed full arrays reproduce exact counts.

## Next local priorities

1. Trace the continuing40–70longitudinal cycles through grade-adjusted allocation, integral recovery and received actuator response, retaining the exact positive-request/positive-plan regression. Widening the brief coast lease alone is not established as a safe cure.
2. Reconstruct calibrated wheel-target/admission/unwind behavior on saved40–50episodes while preserving1.20/0.97. Admission mode is not directly logged; observations cannot prove which gate admitted or withheld a correction.
3. Retain60–70quiet-demand steering windows and the missing sustained low-speed/70+coverage in the evidence plan. Use normal lawful driving opportunities; no calibration factor should be inferred from missing or near-zero-demand data.

Only local analysis helpers/artifacts were created. No controller prototype, paired source/branch change, push, installation, device setting/service/OS/firmware change, or custom CAN/ECU query occurred. Camera files were separately read/hash-verified for the requested clip. Results are saved-road observations, not matched-route causal treatment effects or closed-loop proof.
