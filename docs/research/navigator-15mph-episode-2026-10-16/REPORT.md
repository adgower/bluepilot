<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Why the 12-second 15 mph episode undertracks

October 16, 2026; local saved-data investigation only. No device access or changes, controller tuning, branch integration or installation. Owner factors 1.20/0.97 remain unchanged; paired tracked source is clean.

## Finding

The existing command map is delivered faithfully but produces insufficient measured wheel steering and body turning in this episode. The corrective term adds nothing. Three contributors are supported: the feedforward-to-response mismatch; a fixed pinion proxy that overstates actual turning; and a reconstructed correction budget spent earlier in the session without rearming. This is not evidence that Panda discards 59% of the command, or that the correct gain is simply 1/0.41.

The episode begins at <private clock time> CDT (elapsed 1532 s in collection-drive-02), with speed 13.94–15.48 mph. The earlier reported ~41% is the contemporaneous median of body yaw divided by request in its ~9.85 s meaningful-demand subset. It is not a steady-state transfer gain: request changes substantially, including a reversal near the end.

## 1. The host sends the intended command

At actual send timestamps, the installed strategy was reconstructed from the full session's saved state, control and lane-change-context streams, preserving its state before the episode. The 12-second interval contains 241 send samples; all are active mode 1, with no recorded driver steering, brake or steering fault. Of those, 227 have meaningful requested curvature.

- Every reconstructed path-angle output agrees with recorded transmitted path angle within **0.000250 rad**, the half-step tolerance for the 0.0005 rad wire quantization.
- The recorded command also agrees with **feedforward alone** within that same tolerance for every sample. Extra correction is zero throughout the interval in the reconstruction.
- For meaningful samples, transmitted/feedforward command ratio median is **99.98%**, with 10th–90th percentiles about 99.19–100.62%; quantization contributes proportionally more at small commands.
- The median feedforward factor is **1.8018**, consistent with the existing tight-turn low-speed combination `1.30 × 1.20 × 1.05 × 1.10`. The requested map is `path_angle = curvature × speed × factor`; path angle is not a requested steering-wheel angle.
- Maximum command magnitude in the interval is below 0.15 rad, comfortably inside the existing DBC range. Recorded speed stays below 6.92 m/s, so the deviation clip that applies only above 9 m/s is inactive. Matching unclipped feedforward confirms final slew/range clipping is not reducing this episode's command.
- Panda's historical TX-blocked counter stays at 25 throughout the interval, with no increment. This does not explain earlier session rejects, but gives no evidence of a new hardware transmission block in this episode.

The deficit therefore occurs after the planner-to-transmitted-command map: the full mapped command does not produce the wheel angle/body turn that would satisfy planner curvature. These observations alone cannot separate feedforward calibration from undocumented internal EPS behavior or establish an exact inverse map.

## 2. Wheel steering and body yaw agree on the deficit; the fixed proxy overstates it

| Response / request | Full episode's meaningful samples: median | Inner weak window: median |
| --- | ---: | ---: |
| Calibrated body curvature | **39.8%** | **40.7%** |
| Wheel curvature with recorded learned ratio/offset | **39.8%** | **40.5%** |
| Learned wheel model including roll | **40.7%** | **41.1%** |
| Fixed pinion model used by correction | **56.1%** | **57.6%** |

At the actual wheel angle, applying the recorded learned steering ratio (~22.58) and angle offset (~−1.58°) brings the wheel estimate into close agreement with body yaw. The correction instead uses fixed nominal ratio 19.6 and zero angle offset. The previously saved independent, stationary-debiased OEM yaw check gives ~44.9% in the inner window, also corroborating weak physical turning.

This supports insufficient actual wheel steering for the requested turn, rather than an apparent 59% deficit caused solely by the body sensor. It also shows why the fixed proxy can make recovery look better than it is. It does not establish tire slip, ECU torque saturation, or a new ratio/offset to install. No native safety interpretation, DBC or sensor calibration was changed.

A representative snapshot at elapsed 1541 s (~<private clock time>) has requested curvature **0.01023/m**, transmitted path angle **0.1175 rad**, wheel angle **−21.1°**, body curvature **0.00494/m**, learned-wheel curvature **0.00479/m**, and fixed-proxy curvature **0.00591/m**. These quantities describe different stages; the path-angle value must not be interpreted as a wheel-angle setpoint.

## 3. The small correction allowance was spent before this turn

The full-session controller-state reconstruction spends its entire **0.00025 rad·s pre-limiter correction budget** at elapsed 430.70–430.85 s, around **<private clock time> CDT**, at about 6 mph. Four small extra-command frames consume the allowance. No quiet rearm occurs in the reconstruction before the later 15 mph episode. Spending persists across ordinary tracking resets by design.

At the 12-second episode, all 241 reconstructed samples have spent budget and zero extra correction. Among the 227 meaningful samples:

- 119 are waiting on admission/hold conditions;
- 56 are rejected by predictive catch-up;
- 37 reach the spent-budget veto;
- 15 are otherwise ineligible/reset (`none`).

Thus exhausted budget directly blocks 37 otherwise-admitted samples, while request variation/recovery gates suppress the rest. Budget exhaustion alone is not the explanation for every frame, and simply replenishing it would not establish a full fix.

### Why it did not rearm

Rearming requires one continuous second of fresh, valid, quiet low-speed demand and measured response, including very small measured slope/range. Across the full-session reconstruction, the longest surviving quiet dwell is only **0.4005 s**; rearm count is zero. The diagnostic wrapper, which delegates unchanged to the original method, records 307 quiet starts and 266 measured-slope resets, alongside demand, fixed-proxy and context disqualifications.

At 15 mph, the slope threshold permits only about **0.0358° of steering-wheel change per 50 ms** under the fixed vehicle model. A **0.1°** wheel change implies ~0.00002794/m curvature change, exceeding the permitted 0.00001/m per frame. The recorded nonzero wheel changes in the episode commonly occur in 0.1°-or-larger increments. This exposes a mismatch between quiet-dwell slope sensitivity and available wheel signal resolution/motion; it is a concrete rearming design issue to evaluate, not a reason to remove the dwell or enlarge the budget blindly.

Budget and admission state are inferred by replay, not directly logged on-device telemetry. Physical send-time alignment is not proof of identical online receive timing. The sub-half-wire-step target reconstruction strongly supports the resulting zero-extra output, while exact earlier live internal state is still not independently recorded.

## 4. Ordinary timing alignment does not explain away the deficit

Using the same inner-window requests and eligible samples, comparing with body response later gives:

| Body-response shift | Median response / original request |
| --- | ---: |
| 0 s | 40.7% |
| +0.25 s | 45.5% |
| +0.50 s | 47.1% |
| +1.00 s | 46.6% |

These are fixed, diagnostic shifts, not an optimized delay estimate. They show the deficit persists under several ordinary alignments; they do not exclude all nonlinear dynamics or establish exact latency.

## Supported next work

1. Evaluate a **sensor-resolution-aware, bounded rearm design** against these actual recordings and aborted-turn cases. Preserve continuous-validity and quiet-demand requirements and cumulative correction safeguards. Do not silently reset spent state at every pause or increase the budget as a shortcut.
2. Keep fixed native safety feedback separate from a calibrated application-side body/wheel estimate. This scene supports the learned estimate diagnostically; it does not authorize changing firmware safety geometry.
3. Identify a low-speed feedforward map using repeated whole-drive evidence, rather than asking a small transient correction to carry a sustained large deficit. The existing correction cap is 25% of feedforward (rising terms are further halved), so it cannot be assumed to compensate a ~59% steady shortfall even with fresh budget. No new multiplier is justified by this one changing-demand scene.
4. Preserve the collection plan: another one or two separate drives, both turn directions, transition coverage and a normal 40–50 mph reference. The saved episode is already useful for rearm/admission regression work; additional data are for generalization/calibration, not a prerequisite to investigate this software behavior.

## Evidence and verification

`investigate.py` reproduces the full-session frozen-input strategy trace and a read-only wrapper around its original quiet-dwell method. `trace.json`, `summary.json`, `budget-events.json`, `quiet-rearm.json` and `lag-check.json` retain the findings. `provenance.json` hashes the private signal input, script and controller strategy sources. `verify.py` checks command reconstruction/feedforward parity, physical response discrepancy, proxy disagreement, unchanged in-window blocked counter and spent/no-rearm state. It passed.

This is diagnosis, not a controller change, native safety replay, new build or physical validation. No SSH was needed. Tracked paired sources remain clean; 1.20/0.97, settings and device installation remain unchanged.
