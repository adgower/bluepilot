<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Alpha road review — October 23, 2026

## Finding

The drive supports Alex's report of repeated braking/acceleration and poor smoothness. **The current Alpha candidate should not advance to further road evaluation until the handoff cycling is resolved locally.** The earlier parked/build/native passes verified configuration and software contracts; they did not establish comfortable or stable closed-loop longitudinal behavior. No device changes were made in this review. Alpha was still enabled at the final read-only inventory.

The new handoff prevented concurrent brake request and valid propulsion, but the brake mode repeatedly switched. Each brake re-entry withdraws propulsion and resets its resumption ramp. Pitch-adjusted demand repeatedly crosses the narrow brake/release region; the current 0.02 m/s², 60 ms positive-release qualification does not prevent this cycling. This is the leading software mechanism supported by source and recorded commands. Exact hydraulic response and physical root cause are not established by these logs.

## Acquisition and coverage

Downloaded **all 32 new completed rlogs / three sessions / 244,771,022 bytes**, verified each hash and final unchanged remote inventory. No open segments deferred. Existing acquisitions were identified by segment identity plus hash, not filename alone. Private raw data: `${PRIVATE_CACHE}` (temporary storage; not a permanent archive).

| Session | Local time CDT | Configuration | Coverage |
|---|---|---|---|
| 01 | <private clock time>–<private clock time> | Prior parent 24e981d6d, stock longitudinal | Stationary; no active longitudinal |
| 02 | <private clock time>–<private clock time> | New parent ffebc4349, stock longitudinal | Stationary; no active longitudinal |
| 03 | <private clock time>–<private clock time> | New parent ffebc4349, Alpha true | 23 segments; 13.44 minutes active; maximum 73.94 mph |

Live source matched published parent `ffebc43497f8015c37be5927800832f2719c7dca` / child `0ac9618972dd580281c5e933c7990f186522fbd4`, clean; retained settings/protected files unchanged across acquisition. Driving log initData confirms parent and live CarParams confirms Alpha. All raw identities and location-bearing data remain in the private cache.

[Acquisition receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md), [input hashes](../../navigator-reference/PRIVATE_ARTIFACTS.md), [extraction counts](../../navigator-reference/PRIVATE_ARTIFACTS.md), [analysis](../../navigator-reference/PRIVATE_ARTIFACTS.md), [full-rate command review](../../navigator-reference/PRIVATE_ARTIFACTS.md), [stop/input review](../../navigator-reference/PRIVATE_ARTIFACTS.md), [runtime health](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Repeated cycling

There are **209 full-rate brake-request bit transitions** during active longitudinal control above 5 mph without driver pedal input. This counts both on and off edges, not 209 complete cycles. Frozen 20-second windows below use as-of topic alignment and show no driver pedals.

| Window CDT | Median speed | Full-rate brake edges | Planner acceleration p05–p95 | Actual acceleration p05–p95 |
|---|---:|---:|---:|---:|
| <private clock time>–<private clock time> | 68.8 mph | 33 | −0.069 to +0.171 m/s² | −0.693 to +0.709 m/s² |
| <private clock time>–<private clock time> (overlaps above) | 70.5 mph | 25 | +0.005 to +0.244 | −0.504 to +0.787 |
| <private clock time>–<private clock time> | 21.7 mph | 24 | −0.133 to +0.110 | −0.446 to +0.544 |

At 68.8 mph, controller acceleration median was +0.373 m/s² (p05 +0.098, p95 +0.618), whereas planner median was only +0.073. Actual acceleration spanned −1.40 to +1.12 m/s². Median brake-on intervals were about 0.413 s and clear intervals 0.317 s. Only 43.4% of command frames in this window had positive valid propulsion; repeated withdrawal/qualification/ramp resets prevent continuous propulsion response. The full command stream confirms the bit changes; 20 Hz sampling is not their source. The overlapping second window has 25 full-rate edges versus 24 observable at the state sampling cadence.

The low-speed example has median brake-on/clear intervals around 0.376/0.498 s and positive propulsion on only 32.2% of frames. Its actual acceleration spans −0.95 to +1.23 m/s². This matches repeated mild braking/surging rather than one isolated restart event.

Pitch contribution in the highway window varies approximately −0.613 to −0.041 m/s². Wire acceleration plus as-of pitch lies near the zero/positive-release thresholds at many transitions, despite positive raw controller demand. Pitch here is the controller's orientation input, **not independently measured road grade**. Body motion, grade estimate, controller feedback, lead changes and planner demand remain coupled. Radar lead is present in 60.8% of the first window and 70.5% of the low-speed window; neither is a matched steady-road experiment.

### What the installed change did accomplish

**Zero recorded active braking commands had a simultaneously valid propulsion request.** The explicit command conflict was removed, but this contract alone was insufficient: withdrawing propulsion and restarting a slow ramp at every short brake interval can itself participate in a closed-loop oscillation. The integrated controller starts brake mode below zero net demand; the new release gate can clear it above 0.02 after 60 ms; propulsion then requalifies and rises at 0.5 m/s³. The observed intervals are short relative to a useful uninterrupted ramp.

Source: `opendbc/car/ford/carcontroller.py` longitudinal block, `longitudinal_release.py`, `longitudinal_handoff.py` at the exact paired child. No controller modifications or counterfactual road-benefit claim in this review.

## Stops and driver interventions

Nine active low-speed intervals below 0.8 mph lasted at least one second. These are **stationary/creep intervals, not necessarily nine independent traffic stops**: two pairs include creeping within the same stop context.

- Six intervals subsequently crossed 3 mph while control remained active, before any observed pedal input. Typical crossing time after leaving the <0.8 mph interval was about 1.2–1.35 s; one took 6.8 s. This is not release latency from lead departure.
- At **<private clock time>**, after roughly 38 seconds stationary, driver accelerator input overrode longitudinal control. The logs do not establish whether the lead had moved or whether this was impatience, a planned maneuver or failed restart.
- Two short stop/creep intervals did not exceed 3 mph within the next 12 seconds, then continued into further stop context. Do not count them as failed restarts without scene/lead review.

| Longitudinal active → inactive | Speed | Recorded trigger |
|---|---:|---|
| <private clock time> | 0 mph | Accelerator override, steering input |
| <private clock time> | 11.1 mph | Brake pedal / user disable |
| <private clock time> | 6.2 mph | Brake pedal / user disable |
| <private clock time> | 19.8 mph | Brake pedal / user disable, steering input |

There are also 22 steering-input episodes beginning with longitudinal active within the preceding second. They are driver inputs, not automatically longitudinal failures. `take control` warnings in the recorded selfdriveState resolve to **steerSaturated/warning**, not a proven longitudinal fault. No intent attribution beyond Alex's general poor-smoothness report.

## Speed coverage

Pedal-free active moving evidence: 5–15 mph 62.3 s; 15–25 158.6 s; 25–35 112.9 s; 35–45 84.8 s; 45–55 44.5 s; 55–65 70.5 s; 65–75 67.5 s. Different roads/scenes/lead conditions mean these are coverage totals, not a ranking of calibrations. No 75–85 mph Alpha evidence in this drive. Do not request a high-speed reproduction of the historical shaking.

## Runtime and rejection boundaries

No recorded Panda faults, safety RX-invalid/check failures, heartbeat/SPI errors or radar errors in the reviewed runtime scan. No invalid carState CAN samples during active longitudinal. However, **blocked TX was not zero on the road**: after an initial stale 8→0 startup counter reset, it rose 0→1 at accelerator override, 1→4 at the 11 mph brake disengagement, 4→7 at the 6 mph brake disengagement, and 7→8 at the final brake disengagement. These are cumulative counter edges, not thousands of separate faults. Their exact rejected message/address is not established here. Counters remained unchanged through the sustained highway cycling; this is not evidence that Panda repeatedly rejected those brake/propulsion commands.

## Next local work

1. Preserve this drive as the regression case; reproduce the 69 mph and 22 mph cycling with a production-controller command replay and explicit internal brake/release/handoff state reasons. Record sampling/timing limits rather than assuming exact original scheduling.
2. Resolve brake-mode chatter and repeated ramp resets around pitch-adjusted near-zero demand. Evaluate a coherent coast/brake/propulsion decision and bounded, state-aware handoff; preserve prompt genuine braking, driver overrides, stopping and grade holds. A blanket brake delay or larger acceleration gains is not justified.
3. Check whether pitch/body-motion feedback and the integral acceleration offset amplify cycling. Compare planner target, controller output, pitch and ECU torque over transitions with timing/lag accounted for. Do not tune planner and actuator gain together without isolating the mechanism.
4. Replay override/disengagement boundaries and identify the eight new blocked frames before calling rejection handling resolved. Maintain the low-speed restart fix without reintroducing its prior deadlock.
5. Only after local regressions/builds pass should another separately authorized candidate be installed. Current recommendation is OEM ACC for ordinary driving while this is investigated; switching mode is the owner's parked UI action, not an unrequested SSH change.

## Method and limitations

Exact executable analysis is retained in acquire.py, extract.py, analyze.py, focused.py and episodes.py. Raw commands decoded with the paired Ford DBC; raw full-rate sendcan is used for the 209 edges and zero-overlap check. State/plan/controls are retained around 20 Hz; as-of joining caps topic age at 250 ms in the broad sweep. Full-rate focused pitch joins use the most recent retained carControl; this can be tens of milliseconds old, so net values are threshold-context proxies, not exact per-update internal state. Acceleration is logged filtered aEgo, not an independent physical sensor calibration. There is no matched OEM road comparison, validated fuel measurement, physical brake-pressure measurement or proof of lead-departure timing. Planner/lead/environment contributions remain possible; the source-and-command mechanism is a strong working diagnosis, not a demonstrated closed-loop cure.
