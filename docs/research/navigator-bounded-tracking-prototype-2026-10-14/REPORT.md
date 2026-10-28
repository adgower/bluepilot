<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator bounded tracking prototype — October 14, 2026

**Implemented locally, default OFF, full saved-input replay completed. Nothing on the Comma was accessed or changed. This is an offline sensitivity experiment, not a validated handling fix or an installation candidate yet.**

## What changed

The [local strategy](../../navigator-reference/PRIVATE_ARTIFACTS.md) subclasses the installed very-low-speed strategy. It retains the current feedforward, including the owner's **1.20/0.97**, pinion geometry, previous low-speed trial and extra 10% through 15 mph. An additional proportional tracking term uses requested curvature minus curvature inferred from steering angle using the same fixed pinion vehicle model.

- Gain **0.5**, first-order error filter **0.30 s**, updated at the existing **20 Hz** steering cadence. No integrator or added prediction/lead compensation.
- Additional path-angle magnitude capped at **0.015 rad** AND **25% of the existing feedforward magnitude**, whichever is smaller. These cap the added pre-limit term, not steering-wheel degrees. They are trial settings, not an identified optimal calibration.
- Full strength **5–15 mph**, smooth fade over **15–25 mph**, exactly zero at/above **25 mph**. Disabled below 5 mph; this lower eligibility boundary is discrete, with output still subject to existing rate limits.
- Filter and correction reset on any detected driver steering, inactive/human-turn override, ineligible speed, unsupported platform/flags, disabled experiment or nonfinite correction inputs. Existing human-turn release behavior remains intact. This does not add a general invalid-input policy to the inherited controller.
- The term is applied **after the unchanged desired-curvature deviation clip and before unchanged DBC range/rate limits**. Shadow curvature stays identical to the baseline. No safety C, allowlist, firmware, Params or selector changes.

The explicit `enabled=True` constructor is used only by offline tests/replay. The report-local copy of the small update sequence isolates this experiment without editing the clean installed-source checkout. A later production implementation should extract a shared pre-limit hook and repeat integration validation; copying this directory to a device is not an installation procedure.

## Validation

| Check | Result |
| --- | ---: |
| Prototype behavioral tests | **21 passed** |
| Regression sensitivity | Both signed tracking tests fail when the correction is bypassed, then pass with it present |
| Existing Ford/controller/native safety suite | **213 passed, 79 skipped, 12,063 subtests passed** |
| Complete cached drives / segments | **5 / 72** |
| Controller updates per stream | **410,939** |
| Physical RX frames per safety instance | **16,377,999** |
| Generated TX accepted after recorded Ford configuration | **242,250** |
| Baseline / candidate generated TX rejected | **0 / 0** |
| Invalid required bus-0 RX messages | **0** |
| Generated messages at ≥25 mph / differing controller updates | **50,567 / 0** |
| Generated messages at ≥45 mph / differing controller updates | **12,425 / 0** |
| Default-OFF stream differences, all controller updates | **0** |

**1,843 generated messages before recorded Ford configuration are excluded from TX acceptance claims.** Five RX-check warmup-invalid ticks occur, one at initialization per drive, in both arms. They are not counted as invalid RX messages or hidden. There are 5,531 differing controller updates; all are below 25 mph. These counts describe complete controller CAN output, not only steering frames.

Coverage comprises three earlier complete drives (33/5/7 segments), the first master drive (17), and the post-very-low-speed drive (10). The intervening partially cached trial route is not claimed as fully replayed. The latest drive reaches about 30 mph; ≥45 mph parity comes from earlier recordings.

Replay feeds physical recorded CAN to two independent copies of the same unchanged native debug Ford safety library, regenerates current controller output from recorded CarControl/CarState, and tests every generated TX once Ford configuration is recorded. Legacy routes use the paired pinion safety configuration while retaining other recorded bits. Permissions are derived through the hooks, never forced on. Boundary-overlapping events are merged chronologically; repeated startup metadata cannot rewind the replay clock. Default-OFF is compared against the current installed VeryLowSpeed strategy, rather than the older pre-10% trial.

## Effect in the two latest slow turns

The same recorded steering feedback is supplied to both streams. During the two pre-intervention 2-second windows:

| Latest-drive time | Frames | Baseline median absolute path angle | Prototype median absolute path angle | Median increase in command magnitude |
| --- | ---: | ---: | ---: | ---: |
| 105.43–107.43 s | 40 | 0.0830 rad | 0.0980 rad | **0.0150 rad** |
| 510.48–512.48 s | 40 | 0.05075 rad | 0.06150 rad | **0.01075 rad** |

This adds command where the prior analysis identified undertracking, without changing the owner's factors. The first window reaches the fixed correction cap. The second includes rising demand and previously identified lag; its command increase must not be interpreted as correction of all apparent error. The cap intentionally prevents chasing a large deficit with an unbounded gain increase.

**No percentage of real steering improvement can be calculated from this replay.** The recorded wheel angle cannot respond to a command that was never sent. Positive feedback through vehicle dynamics, overshoot, oscillation, settling time and any EPS authority limitation remain untested. Recorded ≥25/45 mph byte parity is strong evidence for these recordings, not a universal guarantee for arbitrary speed jumps with different rate-limit history. Independent review reproduced carryover after both 15→25 mph and 24.9→25 mph synthetic transitions. Regression tests now explicitly verify that the added term/filter reset while the inherited rate bound is retained, followed by convergence to baseline under constant demand. Discarding the previous output to force instantaneous parity could bypass that rate bound and is deliberately avoided. This transition behavior remains an integration-review item.

The separate recorded-wire audit's historical button rejects/hardware TX-block counters are not erased or resolved by zero rejects in this regenerated stream. The native library is a plain Mac debug build without sanitizer; replay does not test physical forwarding, firmware timing or a closed-loop vehicle.

## Provenance and reproduction

Pinned source remains clean and unchanged: parent **76d78d46fc8713f2f6b1147af02e5aed07bf15a1**, paired child **f50241ca59d866af275ff6c34fb407b93094e892**, at `${USER_HOME}/Apps/openpilot/.navigator-master-integration-20261014`. No branch switch, commit, publication or device connection occurred for this prototype.

Use the pinned tree's `.venv/bin/python` to run `run_tests.py`, `full_replay.py`, then `summarize.py` and `verify.py` in this directory. Replay requires the existing private local recording caches and compiled dependencies; it has no network/device access. The tests deliberately avoid the older BluePilot checkout's unrelated conftest/runtime imports. Artifacts: [summary](../../navigator-reference/PRIVATE_ARTIFACTS.md), [per-drive replay](../../navigator-reference/PRIVATE_ARTIFACTS.md), [source/library hashes](../../navigator-reference/PRIVATE_ARTIFACTS.md), [native tests](../../navigator-reference/PRIVATE_ARTIFACTS.md), [prototype tests](../../navigator-reference/PRIVATE_ARTIFACTS.md), [behavioral failure check](../../navigator-reference/PRIVATE_ARTIFACTS.md), [latest turn commands](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Next: evaluate closed-loop sensitivity and transient behavior before considering integration or a controlled installation. Keep the current working device baseline. Broader feature research is captured separately in the [fork ideas review](../navigator-fork-ideas-2026-10-14.md).

## Subsequent diagnostic finding

The [stall-rescue comparison](../navigator-stall-rescue-comparison-2026-10-14/REPORT.md) decoded a previously omitted EPS availability field and found a strong low-speed status pattern on the Navigator. This does not invalidate this prototype's saved-input command/safety results, but changes the next investigation: distinguish availability/authority, transient lag and post-press attenuation before considering integration. The tracking prototype remains local and its physical benefit is unproven.

## Subsequent local dynamic screen

The [authority investigation](../navigator-eps-authority-investigation-2026-10-14/REPORT.md) screened this unchanged prototype against 96 hypothetical first-order gain/lag/deadtime cases. An assumed 50% response reaches about 60% with feedback; some other assumed delayed cases overshoot. These are not identified Navigator dynamics or road results. The existing saved-input/native replay still passes as documented, but this screen provides no basis to call the prototype a completed fix or deploy it without further design/validation. Availability is not used as a gain switch.
