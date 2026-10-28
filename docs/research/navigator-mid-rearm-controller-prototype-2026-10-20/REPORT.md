<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator 26 mph rearming and full controller replay

October 20, 2026. **Local prototype accepted for controller replay; not integrated, built as a paired release, installed or road validated.** No device access or changes. Owner factors **1.20/0.97** remain unchanged.

## Result

The saved 26 mph rearming blocker is resolved. The old quiet detector repeatedly discarded a genuinely near-neutral interval because wheel quantization and body-yaw jitter exceeded its sample-to-sample tolerance. Of 156 samples within the absolute neutral bounds, it accumulated at most two consecutive samples toward the required second.

The new detector confirms a full second of fresh, distinct, near-neutral observations using bounded resolution-aware tolerances. In `sustained-session-02`, both recorded-context and separately labelled causal calibration-fixture replay rearm at **158.7595054 s**, 26.53 mph, after **21 frames spanning 1.000409338 s**. The following turn produces **seven changed packed steering commands** from 163.958885–164.259384 s. The added term peaks at **0.0025 rad**, then withdraws on predicted catch-up; native deviation clipping still limits later effort. This resolves admission/rearming, not the complete physical tracking shortfall.

## Bounds and guards

The absolute requested/wheel/body curvature bounds remain 0.0005/m and the dwell remains one second. Invalid, duplicate, stale or non-neutral evidence clears the quiet window. Source cadence and age guards remain enforced. A sliding window avoids letting an old disturbance poison later settled evidence.

Wheel tolerance derives from the validated model's curvature equivalent of a 0.1-degree wheel step. Adjacent wheel change is limited to the smaller of 0.00008/m and the old slope allowance plus two resolution steps; whole-window wheel spread is capped at 0.0002/m. Body tolerances use bounded yaw uncertainty, with adjacent extra allowance capped at 0.00025/m and whole-window extra allowance at 0.0003/m. First-five versus last-five medians of requested, wheel and body curvature must each differ by no more than 0.0001/m. These are engineering bounds; correlated body uncertainty does not establish a statistical confidence interval or zero physical motion.

Only a confirmed quiet interval rearms the episode. Turns, aborts and resets do not refill it. Existing 0.0025-rad, five-percent path, 0.0015-rad-second and 0.75-second episode bounds remain. A lifetime exposure counter verifies the allowance across rearms. Driver/fault/withdrawal guards, native pinion/shadow/deviation/range/slew limits and speed scope remain unchanged. Independent review found a non-finite-input gap; an explicit finite guard and regression test resolved it before the full replay. Review then found no remaining material issue.

## Verification

See [acceptance.json](../../navigator-reference/PRIVATE_ARTIFACTS.md), [episode results](../../navigator-reference/PRIVATE_ARTIFACTS.md), [rearming receipts](../../navigator-reference/PRIVATE_ARTIFACTS.md) and [full replay](../../navigator-reference/PRIVATE_ARTIFACTS.md).

| Check | Result |
| --- | --- |
| Saved corpus | 46 recordings, 766 segments; input hashes verified |
| Generated CarController evaluations | 4,432,831 updates per compared variant |
| Independent native streams | Recorded reference/candidate and causal-fixture reference/candidate |
| Native configured physical RX | 176,310,196 per stream |
| Generated TX | 2,870,369 per stream; 2,853,385 accepted, 16,982 before Ford configuration, two rejected |
| Additional native rejections | Zero |
| Focused tests | 91 passed |
| Transition checks | 714 cases, 228,480 frames passed |
| Active-correction abort checks | 128 cases passed; extra command tail at most 0.10 s after neutral request |
| Default-off parity | Whole generated stream identical on every evaluated recorded-control update |
| Protected output | Byte parity at 30–60 mph, including 40–50 mph, and at/above 75 mph; below 5 mph also unchanged |

The two shared rejections are 0x83 on buses 2 and 0 at 116.941513 s in `wheel-session-10`: assistance inactive, controls not allowed, RX valid, 28.9 mph. Exact rejection lists match reference and candidate. There is no controls-permission override. Earlier original-send-time replay reported 232 shared rejections; that is a different replay method and must not be presented as a before/after reduction caused by this fix.

Real CarController calls run at recorded CarControl times with original physical RX, timers and motion/model events. Recorded atomic calibration packets are preserved. A separate causal fixture supplies the latest saved calibration snapshot without changing targets or synthesizing vehicle motion. Missing or invalid inputs remain guarded. The corpus includes stationary recordings; it is not 46 moving drives. Compared with the installed-policy reference, the combined prototype changes 847 generated updates in recorded context and 2,185 in fixture context; these include the preceding calibrated/mid/unwind work, not solely rearming.

## Provenance and next gate

Paired source remains clean and unchanged: openpilot `0171b897289be53fd62f330935c55825b86c3c3a`, opendbc `4167433e5c575f620a9dedf8144a0bc7cba14291`. Frozen prototype SHA-256: `2fa2cfa5729c0bd5dc5c6d9552cdc049f11f3fd108b31be442c79570c1f4ec73`. Replay receipts contain dependency/source snapshots and input manifests. `checks/audit.py` verifies them and the exact rejection lists.

Next: paired integration and build validation, retaining the existing factors and native limits. Hardware acceptance and road comparison remain separate gates. Offline command changes do not prove improved steering, lane tracking or actuator response; no installation is authorized by this local task.
