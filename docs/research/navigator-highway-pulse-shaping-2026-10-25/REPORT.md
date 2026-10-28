<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Highway pulse investigation and neutral-release prototype

October 25, 2026. **A local prototype reduces rapid command cycling, but the overall comfort fix is not ready for integration or installation.** The Comma was not contacted. Paired source and steering calibration were preserved.

## Result

The selected neutral-release prototype (`release_i2`) reduces rapid brake-state reversals in the newest saved drive's healthy, active, no-pedal 50–70 mph sections from **71 to 59 (16.9%)**, and total brake transitions from **263 to 256**. These compare the same 761.342 seconds of recorded exposure; disengagement/faulted intervals are not counted as improvements.

| Speed | Baseline rapid reversals | Candidate | Brake-command seconds, baseline → candidate |
|---|---:|---:|---:|
| 50–55 mph | 7 | 5 | 28.672 → 30.893 |
| 55–60 mph | 23 | 21 | 61.428 → 69.276 |
| 60–65 mph | 31 | 22 | 53.719 → 57.822 |
| 65–70 mph | 10 | 11 | 50.000 → 49.979 |

A rapid reversal means successive changes of the brake request less than 0.6 seconds apart. **This is a reduction in command cycling, not measured improvement in physical jerk, fuel use or motion sickness.** The candidate also adds about **14.151 seconds** of brake-command activity across those highway sections, and the 65–70 mph bin regresses by one rapid reversal. The older drives do not show a meaningful cycling improvement. Overall comfort acceptance remains **RED**.

## What the investigation established

There are two interacting sources of switching. The longitudinal planner selects the lowest acceleration candidate from radar-following MPC, cruise control and the driving model. Model-derived acceleration changes often reach the controller directly; personality changes do not necessarily remove that selected model request. Separately, the custom release gate can restore propulsion after raw and pitch-adjusted demand exceed only **0.02 m/s² for 60 ms**, despite the underlying brake hysteresis extending to 0.3 m/s². Small grade/demand crossings can therefore repeatedly restore and withdraw propulsion.

The current actual-controller 20-second fixture still reproduces 15 brake transitions and seven rapid reversals. Its original strict cycling assertion was rerun and failed before this work. The source and received torque are available; this is a deterministic software reproduction rather than a report based only on the driver's impression.

A small software threshold does not prove the vehicle is physically applying brakes every time the flag changes. Conversely, holding the flag longer cannot be assumed to be harmless coasting. These distinctions are central to interpreting the results.

## Selected prototype

The reviewable implementation is in **`neutral_candidate.py` and `release_coast.py`**. Other classes in `experiment.py` are retained research probes and harness adapters, not additional features to port.

When braking is already requested, the vehicle is in PID operation above 5 m/s, the consumed planner target is near neutral (−0.2 to +0.2 m/s²), measured acceleration is not more than 0.05 m/s² below that target, and fresh received brake torque is at most 4 Nm, a weak positive demand between 0.02 and 0.08 m/s² receives a brief neutral-release hold. The experimental margin applies for at most 0.2 seconds of continuous qualifying input; the original positive-release qualification and actual measured-clearance observer still follow. This is not a guaranteed 200 ms physical response bound.

Meaningful pickup demand, under-acceleration, nonzero/invalid received torque, low speed, stop/FCW or invalid context use the original release behavior. Requested acceleration, grade calibration, safety limits, stopping/restart handling and actual received-torque thresholds are not altered.

The prototype explicitly labels its intentional hold in returned feedback. Positive integral growth is frozen only for that fresh, valid, same-owner hold with a **current** positive tracking error no larger than 0.05 m/s². Negative error remains free to unwind. A new pickup request bypasses this special freeze even if the previous feedback still describes a neutral hold. No longitudinal gain was changed in the selected candidate. Source feedback remains truthful about the brake actuation flags; the `neutral_coast_hold` marker names an **intent**, not proof of zero physical brake force.

The saved first-divergence sample remains brake-requested with propulsion inactive (`gas = -5`), rather than overriding it with a coasting propulsion command.

## Alternatives tested and not selected

- Broad grade-decision smoothing: 73 → 40 rapid reversals across 20 selected command fixtures, but one older 70–75 mph fixture worsens, and full coupled replay adds release-timeout episodes. This is not a valid 45% overall comfort improvement.
- Narrow grade-entry smoothing: newest highway rapid reversals 71 → 67, but total transitions increase 263 → 266 and brake-command time grows. Raising the smoothing cap from 0.05 to 0.10 m/s² gives the same newest-drive result.
- Tracking-aware entry qualification preserving requested propulsion: little benefit; the version also covering following operation worsens newest highway rapid reversals 71 → 73.
- Filtering the final model-derived feedforward request: adds timeout episodes in coupled replay; rejected.
- Filtering only the model candidate before minimum selection: reconstructed the newest recorded planner target within 1e−5 for 25,444/26,231 eligible plans; unmatched cases retain their original target. It preserves the recorded MPC and reconstructed cruise caps, but uses frozen MPC trajectories and approximate logged input receipt order. On common healthy highway exposure, rapid reversals increase 66 → 74 despite fewer total transitions. Rejected; source receipt and MPC free-run fidelity are additional limitations.
- Lower integral gain: a diagnostic halving of the moving-speed gain, with low-speed fade, adds timeout episodes in frozen-input replay. It was not selected, integrated or installed.

Neither a better point forecast nor fewer total transitions alone established smoother behavior. The neutral-release candidate offers the clearest useful command-level reduction, but it still fails the complete improvement criteria below.

## Replay and guard checks

- **65 research/guard contracts pass**, including original fallback across synthetic 0–85 mph, pickup/stop/FCW/invalid data, bounded neutral holds, negative-error integral recovery, stale coast feedback at pickup, and actual-controller retained-pressure/clearance behavior. Some tests cover rejected probes; passing contracts do not make those probes acceptable.
- Full actual LongControl/CarController replay covers **61 saved Alpha segments / 179,144 consumer callbacks**. It uses consumed plan/state timestamps, causal returned feedback, and recorded torque, pose and driver inputs. All input joint-cache hashes were checked.
- **No added timeout episodes or fault samples** for the selected candidate. The newest original 47.71 mph release timeout remains at the same time. The older current-code baseline timeout episodes also remain. Historical drives replayed through current code are stress cases, not reproductions of their old installed software.
- **Native safety-hook replay:** 14,338,901 recorded RX and 429,929 simulated TX checks per variant; 179,133 reconstructed ACC send slots; zero added candidate rejections and no relay faults. Permission was never forced. Eleven callbacks fall outside original send-slot reconstruction. Existing packet rejections remain. The native build is unsanitized; no sanitizer or hardware validation is claimed.
- No simultaneous brake/precharge request with valid propulsion in the candidate wire checks.
- Extracting the selected implementation into its own module produced **identical complete ACC wire hashes on all three replay routes**. The native results therefore apply to the extracted implementation as well.

The original one-second fault on retained received brake torque still occurs; the prototype does not extend that observer timer or substitute predicted torque for clearance. No CAN was transmitted to hardware.

## Remaining blockers

1. **Extra brake-command exposure is unresolved.** There are about 15.461 seconds of newest highway samples where the candidate requests braking and baseline does not; recorded torque is at most 4 Nm for about 14.389 seconds of them. Only 1.616 seconds are explicitly marked neutral hold. Those are the **original recorded responses**, not responses to candidate commands. They cannot establish that the extra command time is pressure-free coasting or fuel-efficient operation.
2. **65–70 mph regresses slightly.** Aggregate improvement must not hide 10 → 11 rapid reversals in that bin.
3. **Strong-deceleration commands are not bit-identical.** Changed integral history produces 27 newest-drive samples one brake-acceleration quantization count weaker than baseline (one count is 0.0039 m/s²; floating request difference is below 0.001 m/s²). Strong targets and limits are unchanged, but a strict no-weaker-command gate still fails. No stopping-distance equivalence is established.
4. **Physical response is not replayed.** Changed commands cannot change the historical acceleration, arbitrated torque, ECU status or pressure response in this harness. Extra timeout episodes in rejected candidates are software/counterfactual consistency concerns, not proof they would occur at those same times on the car. The archived short-horizon response model does not supply a validated free-running vehicle plant or clearance authority.
5. **75–85 mph remains unvalidated.** Raw active Alpha coverage reaches approximately 74 mph; there is no basis for claiming the requested upper range is tuned.

Before integration, the next useful work is explicit coast/precharge/braking state and ECU-response validation, rather than simply increasing smoothing or dwell. In particular, preserve the meaningful cycling reduction while separating true friction-brake demand from neutral/precharge intent and resolving the remaining strong-command/upper-bin differences. The existing OEM/Alpha recordings can inform that local work, but they cannot certify a new command sequence's physical response.

## Reproduction and provenance

Use the paired checkout's `.venv/bin/python` from this report directory:

```sh
python -m pytest -o addopts='' -q --confcutdir=. test_experiment.py
PULSE_VARIANT=release JOINT_VARIANT=release_i2 python joint_replay.py
PULSE_VARIANT=release JOINT_VARIANT=release_i2 JOINT_MANIFEST=older-inputs.json JOINT_PREFIX=older- python joint_replay.py
JOINT_CANDIDATE=release_i2 python compare_joint.py
JOINT_CANDIDATE=release_i2 python wire_check.py
JOINT_CANDIDATE=release_i2 python native_replay.py
JOINT_CANDIDATE=release_i2 JOINT_PREFIX=older- python native_replay.py
JOINT_CANDIDATE=release_i2 python acceptance.py --assert-fix
```

The final command intentionally remains red for the unresolved overall criteria. Detailed evidence is in `joint-comparison-release_i2.json`, `wire-check-release_i2.json`, `coast-exposure.json`, native results and `acceptance.json`. Private recordings/caches are referenced by manifests and were not published. The paired parent/child trees remain clean at `74eaa6a60d344f141d06da16f4dbe10d3de49c0e` / `3a5fe9fe5a296d44b7f898b580c2d3afafe6bfd1`. Steering **1.20/0.97** is unchanged. No paired integration, push, ARM/device build, settings change, reboot, installation or road validation was performed.
