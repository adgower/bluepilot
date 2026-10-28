<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator feedback/admission investigation — October 16, 2026

## Outcome

The reasons for non-activation are reproduced locally, and much of the pinion/body discrepancy is explained by comparing a **fixed, uncalibrated wheel proxy** with calibrated vehicle motion. These are not equivalent measurements. The physical low-speed undertracking is also corroborated independently and is not eliminated by correcting the comparison.

An unselected local prototype separates fresh body-motion tracking feedback from the unchanged fixed pinion safety proxy. Its conservative version does not supply a useful correction in the target14/19–21mph windows. Earlier-admission variants shift a small correction earlier but do not establish a physical fix. **No deployable all-speed steering fix is demonstrated. No Comma or paired release-branch changes were made.**

The feedback-only prototype completed335 segments/19 sessions:77,170,084 physical RX,1,219,156 configured candidate TX accepted, zero candidate or baseline rejections; default-OFF full-stream byte parity and ≥25/45mph actuation parity. Eleven focused tests and552 modeled cases pass for this version. Native debug hooks run in memory, without forwarding or hardware timing reproduction; earlier-admission variants were not full-native-replayed. No new native build or firmware compilation was required because paired source and safety code were unchanged. The validation summary is in [verification.json](../../navigator-reference/PRIVATE_ARTIFACTS.md). The raw replay and plant outputs distinguish native safety acceptance, hypothetical behavior and frozen measured road response; none is a new road test.

[Private/local visualization omitted](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Exact reason the14mph addition barely activates

`admission_trace.py` runs the installed strategy's actual correction code on compact saved inputs and captures its branch locals. The earlier actual-send reconstruction independently agrees on three added samples. State, model and control freshness pass in the selected turn; budget is not exhausted. The new term requires all of the following, not merely a low speed:

- Demand magnitude above0.001/m, same-direction observed response of at least10% of demand, valid context and feedback, and no driver override/lane change.
- Eleven samples representing approximately0.5s of same-sign demand, less than0.5m/s speed spread, and stable demand or an admitted bounded rise.
- For stable demand, window range no more than25% of the median magnitude.
- Six consecutive qualifying deficit samples; a predicted recovery to70% vetoes the extra term.

Drive-01 near10:56:16CDT:

| Route elapsed | Demand-window range/median | Stable | Hold count | Result |
| ---: | ---: | --- | ---: | --- |
| 87.743s | 44.0% | No | 0 | Waiting |
| 87.890s | 29.9% | No | 0 | Waiting |
| 87.943s | 22.9% | Yes | 1 | Waiting |
| 88.043s | 12.0% | Yes | 3 | Waiting |
| 88.191s | 11.9% | Yes | 6 | First extra term |
| 88.290s | 22.2% | Yes | 8 | Third extra term |
| 88.343s | 26.6% | No | 0 | Waiting/reset |
| 88.391s | 29.2% | No | 0 | Projected catch-up veto |

Thus request changes prevent persistence, then genuine demand withdrawal/recovery releases the correction. Raising the area budget does not alter these gates. At the11mph accelerating window, the0.5s speed spread reaches approximately0.73–0.90m/s, exceeding the0.5m/s gate. At19–21mph, fixed pinion feedback is already near the request, projected recovery vetoes frequently, and speed change further limits admission. These are concrete branch decisions; non-activation alone is not proof of an implementation error.

## Pinion versus body yaw: what explains the difference

The installed pinion option uses `VehicleModel` with the paired fixed geometry: steer ratio19.6, raw wheel angle, zero learned angle offset and zero roll. This is also the native safety proxy. It is not a calibrated yaw sensor, despite the common nickname.

Saved vehicle-parameter estimates around the12:40turn are ratio22.45 and angle offset approximately−2.1°. For controller-sign curvature, the comparison must use the corresponding sign and `-(wheel_angle - angle_offset)` through the model. Parameter calibration changes wheel-to-curvature conversion, not actual wheel motion. Representative calculations:

| Window | Body/request | Fixed wheel proxy/request | Learned ratio+offset, zero roll/request |
| --- | ---: | ---: | ---: |
| ~13.7mph,<private clock time> | 49.8% | 33.6% | 68.2% |
| ~21.2mph,<private clock time> | 48.3% | 96.9% | 47.4% |
| ~19.5mph,<private clock time> | 56.9% | 87.2% | 55.6% |

The14mph estimate moves to44.9% when the recorded learned roll is included, versus49.8% body response. Learned roll does not universally improve each transient; at19.5mph it moves the estimate to62.6%. These estimates partly learn from body motion themselves, so agreement is not independent proof. Tiny selected-window boundary differences account for rounded values differing from the preceding report.

The broader ten-session audit compares fixed, offset-only, ratio-only and learned models across5–80mph on unchanged samples. It frequently reduces wheel/body disagreement, but short/one-direction speed bins do not identify a new universal steering ratio or a reliable speed-dependent calibration. The1s smoothness selection is descriptive, not a controlled steady-state experiment.

### Independent check: the vehicle CAN yaw still has a baseline

The raw CAN yaw remains biased while stopped: about−0.0168rad/s in drive-01 and−0.0160rad/s in drive-02. Moving CAN-versus-body fits have slopes approximately−1.001 and−1.006 and intercepts−0.01667 and−0.01634rad/s. This supports compatible dynamic units/signs with a nonzero baseline, consistent with the earlier investigation.

Removing each drive's measured stationary baseline **for analysis only** yields independent CAN/request ratios of50.4% at the14mph weak turn,46.1% near21mph and59.1% near19.5mph. Body-yaw ratios in those same windows are49.8%,48.3% and56.9%. Median yaw disagreement is approximately0.0008–0.0017rad/s. Thus the physical undertracking cannot be dismissed as merely an IMU scale or fixed-model artifact. This is not authorization to hardcode a yaw offset or modify the universal Ford DBC/safety conversion.

### Local resolution of the feedback interpretation

Keep the fixed pinion model as the coherent app/native safety proxy. A separate tracking feedback channel can observe physical response, with explicit freshness/validity, without changing the native shadow curvature, curvature-deviation limiter, geometry or firmware. The local `BodyFeedbackPrototype` demonstrates this separation and fails closed on missing/stale/future/invalid motion. Both observed body response and observed same-direction pinion response remain necessary: it is not silent-EPS stall rescue.

This resolves the conceptual/source mismatch locally, but **does not make calibrated body feedback a proven control solution**. Native fixed geometry was not changed to learned values; doing so would require a separate paired safety design and would affect more than the target speed band.

## Speed-range survey

Ten retained sessions on the current installation, strict eligible meaningful-demand samples. Times are approximate20Hz sample counts; samples are correlated and roads/demand/directions are unmatched.

| Speed | Clean exposure | Stable subset | Median body/request | Interpretation |
| --- | ---: | ---: | ---: | --- |
| 5–10mph | 2.95s | 0 | 13.6% | Very short low-demand transients; no steady gain identification |
| 10–13mph | 1.40s | 0 | 39.4% | Acceleration/delay and demand changes confounded |
| 13–17mph | 1.80s | 0.30s | 47.5% | Real short deficit, almost entirely one direction |
| 17–20mph | 1.60s | 0.85s | 57.5% | One-direction turn, fixed proxy overestimates body response |
| 20–25mph | 3.60s | 0.05s | 66.6% | Transient demand/deceleration dominates |
| 25–40mph | 19.05s | 8.05s | 105.8% | No broad understeer multiplier justified |
| 40–50mph | 24.35s | 15.45s | 118.2% | Mostly right-hand samples; do not boost; preserve owner's calibration |
| 50–70mph | 174.40s | 106.25s | 111.7% | Both directions; no broad gain increase supported |
| 70–80mph | 8.35s | 4.80s | 115.4% | One-direction subset; no speed-only retune justified |

Ratios above100% include delay, offset, model, banking and request evolution. They are not automatically persistent oversteer. No lane-position error inference is made from these ratios. Simply scaling each band by inverse median would both overfit this data and alter already satisfactory behavior.

## Local prototypes and limits

All prototypes live only beside this report, not in paired source or device selection:

1. **Body feedback, existing six-frame confirmation:** extra feedback channel only; original feedforward,1.20/.97, speed fade, caps, budget/rearm, override and range/slew behavior retained. Eleven focused tests pass. In the latest four-drive signal replay it removes the previous three tiny14mph additions and does not add in the19–21mph target: corrected feedback alone does not fix admission timing.
2. **Body feedback, three-frame confirmation:** three14mph samples start at88.043s, approximately0.148s earlier than installed88.191s. Four small samples near19mph, peak0.000345rad. No useful addition in the11mph acceleration window. It increases worst modeled unit-gain peak excess by0.0006345 of request amplitude, approximately0.063 percentage points.
3. **Earlier confirmation with half proportional gain:** same earlier timing, smaller terms; worst additional modeled unit-gain peak excess0.00008533 of request amplitude, approximately0.0085percentage points.

The last two fail the previous strict zero-increase peak criterion. Those numerical changes are small and **do not themselves establish unstable or unsafe behavior**. They also do not establish meaningful physical benefit: frozen measured response does not change, the terms are brief and often around/below wire quantization, and sensor-delay/feedback-error robustness needs its own validation. Neither is promoted to the release pair.

Each plant screen covers540 cases plus two saturation cases and ten forced aborted turns (552 total), using actual range/slew-limited outputs in hypothetical delayed first-order plants. All settle and45mph parity holds. The feedback-only version has zero added unit-gain peak excess in this tested grid. This grid assumes ideal body feedback consistent with the modeled physical response; it is not comprehensive sensor-failure, uncertainty or hardware validation.

### Why another small correction cannot fully repair this deficit

The existing maximum relative extra is12.5% of feedforward before the speed fade, with a0.0075rad absolute cap and0.00025rad·s rising-episode budget. In a **hypothetical linear steady plant** producing50% of requested curvature, even a continuously applied12.5% increase would reach only56.25%, not100%. Near20mph the fade permits less. This is a bound illustration, not an identified Navigator plant or a prediction of the vehicle.

The present addition was designed as a modest bounded transient correction. Asking it to repair a much larger steady command/response discrepancy is a different control problem. Removing persistence or increasing its budget does not provide a defensible all-speed calibration.

## Next implementation decision

The evidence supports a design that treats the following separately:

- **Measurement:** calibrated physical-response feedback with explicit validity, plus coherent unchanged native safety feedback. The local prototype is a diagnostic seam, not a production sensor policy.
- **Steady command map:** derive recommendation-only feedforward estimates from sufficiently sustained, matched left/right observations, with offset/ratio/roll and uncertainty separated. Do not learn a gain from1.8s of mostly one-direction transients or automatically write new settings. The current snapshots support a deficit below25mph, not an exact replacement map.
- **Transient response:** identify delay versus gain and evaluate demand prediction/withdrawal explicitly. Earlier proportional pulses alone do not establish tracking improvement and can retain effort into an aborted turn.

After the three evaluated local approaches, no fourth gain/timer tweak is justified without revisiting that design. The [systematic-debugging skill](../../navigator-reference/PRIVATE_ARTIFACTS.md) says “If ≥ 3: STOP and question architecture (step 5 below)”. That applies to these repeated unsuccessful target fixes. The technical reasons are the failed target behavior, bounded authority and uncertainty above, not lack of user authorization. A concrete [next design](DESIGN.md) separates calibration identification from transient control. The user has authorized local repair work; no additional SSH or install authorization is needed for local analysis, but no on-device action is part of this task.

## Reproduce

Use the explicit paired-worktree Python environment. `admission_trace.py`, `feedback_audit.py`, `speed_audit.py`, `signal_replay.py`, `test_feedback.py`, `plant_screen.py` and `full_replay.py` are retained here. All run offline from existing private caches. `test_feedback.py` uses pytest with `-c /dev/null --confcutdir=<this directory>` to avoid unrelated older BluePilot root conftest/native imports. Initial red outputs show three feedback-seam failures against the installed strategy and a separate missing-pinion-response guard failure before correction; final results are retained.

See [branch decisions](../../navigator-reference/PRIVATE_ARTIFACTS.md), [feedback audit](../../navigator-reference/PRIVATE_ARTIFACTS.md), [speed audit/CAN cross-check](../../navigator-reference/PRIVATE_ARTIFACTS.md), [signal replay](../../navigator-reference/PRIVATE_ARTIFACTS.md), [full native replay](../../navigator-reference/PRIVATE_ARTIFACTS.md), and [verification](../../navigator-reference/PRIVATE_ARTIFACTS.md). Original GPS/identity-bearing extracted logs remain private. Final paired Git state and installed source remain unchanged. No active ECU queries, SSH mutations, restarts, OS/firmware actions or parameter writes.
