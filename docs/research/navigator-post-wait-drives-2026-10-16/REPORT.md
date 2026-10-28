<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator post-install drive review — October 16, 2026

The installed wait/catch-up correction has **not yet been tested by an engaged low-speed drive** in the retained recordings. There is no defensible improvement percentage for 15 or 22 mph. The two active highway sessions show no rejected active steering messages, but do not establish low-speed benefit or a matched before/after handling result.

## Recording coverage

All 84 retained segments were copied read-only and independently hash-verified (714,859,171 bytes). Dates below are America/Chicago (CDT). Durations and active time are approximate; active time counts recorded 20 Hz angle-command samples.

| Session | Start | Segments | Duration | Steering assistance |
| --- | --- | ---: | ---: | --- |
| drive-01 | Oct 15, <private clock time> | 5 | 254 s | Parked; never active |
| drive-02 | Oct 15, <private clock time> | 7 | 396 s | Manual; never active |
| drive-03 | Oct 15, <private clock time> | 7 | 409 s | Manual; never active |
| drive-04 | Oct 16, <private clock time> | 26 | 1,531 s | 229.6 s active, 55.4–66.9 mph |
| drive-05 | Oct 16, <private clock time> | 17 | 1,017 s | 305.2 s active, 60.3–69.0 mph |
| drive-06 | Oct 16, <private clock time> | 22 | 1,268 s | Manual; never active; owner confirmed |

There are zero active 5–25 mph frames, including zero at 13–17 mph. There is also no engaged 40–50 mph comparison. Manual low-speed travel cannot be classified as an openpilot tracking failure. No engagement failure is inferred from the latest manual drive.

## Steering response and controller reconstruction

The reconstruction admits no extra tracking correction, spends no correction budget and rearms no episode in any session. Thus these drives do not exercise the new wait/catch-up behavior. Installed candidate, preceding budget strategy and feedforward reconstruction have identical outputs on the covered inputs. This is code-path parity, not a physical low-speed road test.

In clean highway bends above 0.0003/m requested curvature, drive-04 provides 18.6 s and drive-05 58.4 s. Median body-yaw/request ratios are about 1.17 and 1.16; median absolute lateral-acceleration errors are 0.116 and 0.113 m/s² (95th percentiles 0.229 and 0.325). At the stricter 0.001/m demand threshold only drive-05 contributes: 16.4 s, median body ratio 1.13 and pinion ratio 1.08, median absolute acceleration error 0.130 m/s². No clean meaningful-demand weak-response episode persists for at least 0.5 s. Small-request ratios are sensitive to timing and offsets and are not evidence for another gain increase.

Eligibility requires fresh aligned state/control/IMU/model/parameters, active valid lateral control, no driver steering input or recent override, no lane change/blinker, and valid dynamics signals. Stable subsets require 0.5 s of same-sign relatively stable demand/speed. See analyze.py for exact masks. Roads, demand and intervention patterns are unmatched, so these numbers do not establish causal improvement over the preceding installation.

The earlier 15 mph body-versus-pinion response discrepancy remains unresolved. Pinion feedback is installed/enabled; that does not prove the body-yaw discrepancy was fixed or that the vehicle achieves the requested curvature at low speed.

## Rejections and runtime health

Actual rejected-frame echoes contain zero active-mode angle messages across these sessions. Inactive angle/startup/shutdown rejects are separate. The only Ford-configured moving counter increase is two messages in drive-05 near elapsed 769.7 s, around 66.8 mph: both are 0x83 cruise-cancel packets on buses 0 and 2. Exact recorded-transmit native replay reproduces both rejects: 63,891 configured TX, 63,889 accepted, two cancel rejects, zero RX-invalid. This supports the cancel diagnosis; offline replay does not reproduce physical transport timing.

No sampled Panda faults, heartbeat loss, RX-invalid conditions, permanent steering faults or reported model frame drops were found. Big-model inference remained selected. Brief Chestnut supply-fault flags occur only during the first approximately two seconds of drive-03 through drive-06 and clear; there are none later in those sessions. Temporary steering flags are principally stationary startup/shutdown/reverse, with four additional reverse parking samples around 1.9 mph in drive-04. None occur during active highway assistance. These observations do not prove long-term hardware reliability.

## Current status and next step

- Installed pair: parent 9da98d0c91f0559efa976e3ffb221f2584fd0b88, opendbc 18175406d0cc5af8233afde70a5d121aedf8de44. All six init records identify this parent. Logged dirty metadata is distinct from live Git status; both live checkouts were clean at the beginning and end of this review.
- Existing 1.20/0.97 source calibration is retained in the installed pair. Recorded configuration retains Navigator wheelbase 3.1115 m and steering ratio 19.6; pinion, low-speed and persistent-tracking preferences and update pause are enabled. Alpha longitudinal remains off. A recorded ExperimentalMode preference alone does not establish openpilot longitudinal operation.
- Installation/build/parked acceptance is complete in the preceding installation report. This review supplies highway observation, not validation of the low-speed correction.
- Next useful evidence is an ordinary drive where assistance is actually engaged through the relevant 15–25 mph bends. Record approximate time and any intervention. Low-speed engagement availability remains a separate limitation; if engagement is unavailable there, do not treat that as insufficient steering gain. MADS remains a separate roadmap feature.
- Keep the current calibration and controller unchanged until there is relevant engaged exposure; further gain tuning is unsupported by this batch.

No source/settings writes, ECU queries, restarts, firmware actions or activation were performed on the Comma. Final SSH check found the same clean paired revisions, offroad. This task ran a recorded-message diagnostic replay, not another full candidate validation suite, because no candidate code changed.

## Evidence and reproducibility

[Analysis](../../navigator-reference/PRIVATE_ARTIFACTS.md), [controller reconstruction](../../navigator-reference/PRIVATE_ARTIFACTS.md), [actual rejected echoes](../../navigator-reference/PRIVATE_ARTIFACTS.md), [health detail](../../navigator-reference/PRIVATE_ARTIFACTS.md), [native recorded replay](../../navigator-reference/PRIVATE_ARTIFACTS.md), [verification](../../navigator-reference/PRIVATE_ARTIFACTS.md), and [anonymized input manifest](../../navigator-reference/PRIVATE_ARTIFACTS.md). Scripts are retained beside these outputs. Private raw recordings and route mapping: `${USER_HOME}/CommaBackups/<private timestamp identifier>-post-wait-drives`; extracted raw signals remain private. Public-facing report artifacts omit GPS and device identifiers. The native replay library hash and timing limitations are recorded in its JSON.
