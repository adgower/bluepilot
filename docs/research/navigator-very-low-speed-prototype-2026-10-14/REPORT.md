<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator very-low-speed correction prototype — local only

October 14, 2026. Prototype and validation artifacts only. No SSH, Comma file/parameter changes, reboot, firmware changes, OS changes, ECU queries, publication or installation. The existing paired master-integration source remains clean and unchanged: openpilot `6ae31161b73de2ce5043f708569759ac5f55f283`, opendbc `c09baff5c2cdd7c887e25c2d88b671f403e1ed9d`.

## Result

A separate **10% very-low-speed feedforward experiment** was implemented locally and replayed against all **62 segments from four complete locally cached drives**. Both the current installed-trial baseline and prototype generated **zero native safety TX rejections**, with zero checked RX-invalid frames. Default-OFF output matches the current trial at every controller update. All replayed messages at/above 25 mph match the current trial byte for byte, including 12,425 messages at/above 45 mph.

This verifies recorded-input command compatibility, **not a steering handling fix**. The chosen 10% is a modest sensitivity experiment, not a fitted or demonstrated cure for the large observed response deficit. No vehicle response, lane-wandering improvement, stability, native device build or road evaluation of the new prototype has occurred.

## Behavior

`VeryLowSpeedGainPrototype` subclasses the existing `LowSpeedGainPrototype`. It is default OFF and has **no installed selector, Params key, UI toggle or normal-controller wiring**. Only this local replay explicitly enables it.

- Requires the Expedition fingerprint currently used for the Navigator, plus the existing pinion and low-speed-trial flags. As with the prior trial, the temporary fingerprint cannot distinguish a native Expedition from this forced Navigator definition; it is not a generic Expedition tuning recommendation.
- Keeps the owner's **1.20/0.97** constants and existing gain map authoritative.
- Additional multiplier **1.10** at/below 15 mph, fading by smoothstep over 15–25 mph, exactly **1.00** at/above 25 mph.
- At 20 mph the extra multiplier is **1.05**. It continues tapering above 20, as requested, until fully absent at 25.
- Applies to both gentle and tight curvature arms. At 15 mph, gentle endpoint is 1.15 × 1.10 = **1.265**; tight endpoint is 1.30 × 1.20 × 1.05 × 1.10 = **1.8018**. These are path-angle conversion factors, not steering-wheel angles or predicted handling gains.
- Leaves the previously installed 30–45 mph fade intact. There is no new PID, integrator, tracking-error feedback, yaw correction, steering-ratio change or global delay change.
- Inherits the existing deviation clipping, path-angle range, rate bounds, human override, pinion feedback and shadow-curvature rules without alteration. Panda safety code is unchanged.

The encoded command in the 40 selected no-driver-input frames immediately before the late 15 mph intervention increases by median **10.0%** (median current path angle 0.071 rad, candidate 0.078 rad). Recorded wheel/IMU response was held fixed; it must not be presented as 10% better actual steering.

## Full controller/native safety replay

`full_replay.py` executes the pinned current CarController at every saved carControl event with saved carState and stock-message values parsed from physical CAN. It runs current-trial and candidate controllers side by side, plus a default-OFF controller for byte comparison. Two independent copies of the same matching native debug safety library validate baseline and candidate separately. Their independence is checked through distinct safety parameters before replay initialization. Controls permission is derived from saved RX traffic; it is never forced on during replay.

| Evidence | Result |
| --- | ---: |
| Complete cached drives / expected segments | 4 / **62** (33 + 5 + 7 + 17) |
| Controller updates per controller | **353,029** |
| Physical RX frames supplied to each safety instance | **14,084,237** |
| Candidate generated TX messages | **209,663** |
| Candidate TX evaluated and accepted after Ford configuration | **208,186** |
| Active candidate angle TX messages | **20,104** |
| Baseline / candidate TX rejections | **0 / 0** |
| Checked relevant RX-invalid frames | **0** |
| Default-OFF differing controller updates | **0** |
| Compared messages at ≥25 mph / differing updates | **41,285 / 0** |
| Compared messages at ≥45 mph / differing updates | **12,425 / 0** |

There are **1,477 generated messages before the first recorded Ford safety configuration**, explicitly excluded from acceptance totals, and **four initial RX-check warmup invalid ticks** (one per drive). They are not counted as accepted transmissions or hidden. All generated TX message types are validated, not only steering. Relevant RX invalid results are tracked for the required Ford addresses on bus 0; the harness supplies all physical received frames on buses below 3 to the hooks.

Legacy recordings are evaluated with paired pinion mode by adding its existing safety bit to recorded Ford configurations; other recorded safety bits are retained. Current source normalizes vehicle dynamics per mass. No limits or safety code were changed for this experiment.

### Coverage and ordering qualifications

The intervening 11-segment trial has only its first raw rlog cached locally, so it is **not included as a fully replayed drive**. Its anonymous full-drive signal/safety exports do not substitute for full-rate raw controller inputs. The four included drives contain every expected raw segment, including the new 17-segment master-integration drive with the reported 15 mph example. No device access was used to retrieve the missing recording.

A first ordering assertion caught repeated initData metadata with the original startup timestamp in later segments. The completed harness advances hooks only from required input topics (can/carState/carControl/pandaStates), merges a five-second boundary tail chronologically, and asserts global monotonic time. It discards no required controller/safety input events. This avoids rewinding the safety timer due to repeated metadata.

Generated replay is **not the original recorded TX stream**: controller cadence, event alignment and generated command ordering can differ. The previously documented three recorded lateral permission-transition rejections on the latest drive remain historical findings; zero generated rejections here does not mean those original events were fixed. Both the unchanged baseline and candidate pass the same generated replay.

Byte identity above 25/45 mph is established for these saved trajectories. The gain formula is also universally unchanged there, but inherited rate-limiter history could carry a difference into an arbitrary hypothetical speed transition. No universal closed-loop equivalence is claimed. Only the older drive supplies ≥45 mph coverage; the latest drive reached approximately 35 mph.

Native library SHA and prototype SHA are recorded in `provenance.json`. The library is the previously verified matching plain debug Mac build, without sanitizer validation. Complete Panda hardware/firmware execution and forwarding hooks are not reproduced.

## Tests and limitations

Test-first validation initially produced **12 expected assertion failures / 22 passes** when the existing trial was used without the correction. After implementation, the expanded prototype suite passes **36 tests**. Coverage includes gain/fade for both signs and curvature arms; default OFF; flag/platform scope; dense bounded/no-weakening and symmetry sweeps; fade-endpoint smoothness; inherited range/rate/driver override; preserved factors; and high-speed parity after a disengagement reset. These tests verify controller behavior, not physical response.

The broad unchanged opendbc suite attempt produced **3,746 passed, 1,690 skipped, 24,670 passing subtests**, and **three failed MISRA mutation subtests**. An uncaptured-output diagnostic identified their checker bootstrap failing before analysis with:

```
failed to open file ${USER_HOME}/.cache/uv/sdists-v9/.git: Operation not permitted
```

The failed mutation cases were the unmutated control, a `subaru.h` `misra-c2012-14.2` probe and a `psa.h` `misra-c2012-13.3` probe. The script sources setup.sh/uv sync and returns code 2 with empty checker stdout. This broad suite is **not fully green**; no unrelated tool/bootstrap/source change was made to conceal the failure. Current Ford/native safety tests in that run passed. The new Python-only experiment does not modify safety C code.

Critical Python syntax/error lint and compilation checks passed. Source cleanliness was checked separately. There was no parent integration change requiring an openpilot rebuild; the new experiment is a standalone local module and portable add-file patch, not an installed branch update.

## Files and reproduction

- `lateral_angle_very_low_speed_prototype.py`: default-OFF standalone experiment.
- `opendbc-prototype.patch`: portable add-file patch only; applying it does not select or deploy the experiment.
- `test_prototype.py`, `test-red.txt`, `test-green.txt`: test-first evidence.
- `full_replay.py`, `replay-console.txt`, `full-replay.json`: complete replay and per-drive baseline/candidate results.
- `late-command-comparison.json`, `summary.json`, `summarize.py`: anonymous command comparisons and acceptance assertions.
- `opendbc-suite.txt`, `misra-diagnostic.txt`: broad-suite failure and bootstrap diagnosis, retained honestly.
- `provenance.json`: source artifact hashes.

Run scripts with the existing master-integration Python 3.12 virtualenv. `full_replay.py` and the test module pin imports to that untouched source tree; the replay reads existing private raw-log paths on this Mac and does not open a network connection. `summarize.py` asserts coverage, zero hook rejections and high-speed parity. Raw location/VIN/images/device identifiers are not exported into these report files.

## Decision

Keep this as an explicitly selected local experiment. It increases commands in the requested range and passes the complete available recorded-input safety replay while preserving the covered higher-speed commands. The degree of actual improvement remains unknown. Any future device installation still needs separately authorized integration/build validation and subsequent vehicle-response assessment; this report does not authorize installation.

## Subsequent installation

The user later authorized installation. See the [installation report](../navigator-very-low-speed-installation-2026-10-14/REPORT.md) for integrated commits, backup verification, repeated final-selector replay, native build and offroad acceptance. The local-only statements above describe the original prototype task, not current device status.
