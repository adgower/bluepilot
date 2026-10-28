<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator low-speed gain prototype — local only

2026-10-14. Prototype implemented and committed locally on `codex/navigator-low-speed-prototype`. Openpilot `6ab602fdd`; opendbc `fe85f3f7`. Isolated checkout: `${PRIVATE_CACHE}`. No device access, update, parameter change, restart, flash, active ECU query, push, or deployment in this task. Owner settings remain **1.20/0.97**.

## Prototype design

The regular controller retains its behavior. Its gain calculation was extracted into a method without changing its arithmetic. `LowSpeedGainPrototype` is a separate, explicitly selected local subclass. Only the local replay harness selects it; the normal controller and existing pinion UI toggle do not enable this calibration.

- Navigator/Expedition fingerprint only; other platforms unchanged.
- Gentle endpoint: existing gain × **1.15**.
- Tight endpoint: existing gain × **1.05**, still derived from the owner's 1.20/0.97 endpoint gains.
- Smoothstep blend over |curvature| **0.00025–0.00125 /m**, replacing the narrow original 0.0007–0.001 transition inside the experiment.
- Added effect has full weight below 30 mph, smoothly decreasing blend weight from 30 to 45 mph, zero at/above 45 mph.
- No PID/integrator or new feedback correction added. The replay uses the already-reviewed **pinion-enabled baseline** and paired native safety code.
- Feedback clipping, override behavior, signal limits, rate limits, and safety code unchanged.

Trial values explore command behavior; they are not fitted or certified vehicle tuning. The broadened blend begins earlier, so **15%/5% describe endpoint increases, not an overall maximum**. Peak map uplift is approximately **35.75%** near curvature 0.0007 /m below 30 mph. Independent dense review found no map weakening and monotone command magnitude. Added blend weight decays monotonically; percentage uplift can briefly rise at particular curvatures because original endpoint gains also vary with speed.

The initial trial's blend reduced command strength in part of the transition. A new no-weakening sweep failed on it. Moving the blend earlier fixed that test; the final code and full replay use the corrected bounds above.

## Command examples

| Speed | Curvature /m | Baseline gain | Trial gain |
|---|---:|---:|---:|
| 25 mph | 0.0002 | 1.0000 | 1.1500 |
| 25 mph | 0.0007 | 1.0000 | 1.3575 |
| 25 mph | 0.00085 | 1.2800 | 1.4662 |
| 25 mph | 0.002 | 1.5600 | 1.6380 |
| 40 mph | 0.0002 | 1.1398 | 1.1841 |
| 45 mph | 0.0002 | 1.2111 | 1.2111 |
| 45 mph | 0.002 | 1.4717 | 1.4717 |

In the latest saved stronger-turn window, encoded command magnitude increased by a median **5.07%**. In the gentler-turn window it increased by **20%**. These are command changes with saved inputs held fixed; they are not improvements in actual turning or wandering. A 5% command increase is not demonstrated to overcome the previously observed ~39% response shortfall in the strongest turn.

## Full saved-stream native safety replay

All expected segments were asserted and processed chronologically: **33 + 5 + 7 = 45**, across three drives.

| Evidence | Result |
|---|---:|
| Controller updates | 252,406 |
| Physical received CAN frames | 10,082,330 |
| Accepted generated TX messages | 148,765 |
| Active angle messages | 14,475 |
| TX rejections in final prototype replay | **0** |
| Checked RX invalid frames | **0** |
| Compared generated messages at ≥45 mph | **12,425** |
| Differing controller updates at ≥45 mph | **0** |

Native hooks derive controls_allowed from recorded receive traffic; it is not forced on. All generated TX types are checked, not just steering. Native safety code was not changed for this experiment. There are **1,109** generated frames before the first recorded Ford safety configuration (369/371/369), explicitly excluded from hook evaluation. Each drive has one initial receive-check warmup invalid tick. These exclusions remain visible in JSON rather than being counted as accepted safety transmissions.

The regular pinion baseline was replayed after the helper extraction. Its complete generated CAN hashes and counts match the previous pinion implementation on all three drives. The prototype comparator runs a second regular pinion controller on the same inputs. All saved ≥45 mph generated messages match this baseline byte for byte; 3,474 selected active/no-driver steering-angle frames are included in that region. Only the earlier drive supplies ≥45 mph coverage.

The gain formula is universally identical at/above 45 mph. Exact transmitted parity is established for these recordings, not every hypothetical transition: inherited rate limiting can retain prior low-speed command history in an arbitrary synthetic trajectory.

## Tests and review

- **180 tests passed**, **77 skipped**, **12,000 subtests passed** in the targeted controller/pinion/native Ford suites.
- Seven new prototype tests cover endpoint changes, exact high-speed gain, unaffected platforms, smooth fade/odd monotone commands, lower transition peak sensitivity, no weakening, and inherited clipping/rate/range/override behavior.
- Changed Python/new tests passed Ruff; diff whitespace checks passed.
- Independent code review and dense gain sweep found no blocking issues. Review explicitly distinguished gain equality from universal stateful transmission equality.

## Limits and decision

The prototype answers the local command/safety-compatibility question: it strengthens the intended low-speed commands, reduces the sharp transition sensitivity, retains the recorded ≥45 mph baseline, and introduces no native RX/TX rejection in these saved drives.

It **does not establish a vehicle handling fix or closed-loop stability**. Saved planner inputs, wheel angles, CAN traffic and motion do not change in response to the trial commands. No lane-wandering reduction or new physical turning ratio can be inferred. It does not reproduce complete Panda firmware/hardware or forwarding-hook behavior. The native C library uses the existing plain debug build because macOS rejected sanitizer loading in the prior implementation work. No device build or road validation was performed.

Keep this as a reviewable local experiment. It is not automatically selected in the installed-code path. Any later implementation/deployment needs a deliberate selection mechanism and separate device/vehicle response evidence.

## Files and rerun

`full_replay.py`, `summarize.py`, `*-replay.json`, `*-command-comparison.json`, and console logs provide inspectable evidence. Portable local commit patches accompany this report. Raw rlogs remain in the private local recording folder; output contains anonymous numeric signal comparisons, not VIN/GPS fields.

From `${USER_HOME}/Apps/bluepilot`:

```sh
${PRIVATE_CACHE} docs/research/navigator-low-speed-prototype-2026-10-14/full_replay.py low-speed-prototype
${PRIVATE_CACHE} docs/research/navigator-low-speed-prototype-2026-10-14/summarize.py
```
