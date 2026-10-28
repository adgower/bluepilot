<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Ramp-history resolution investigation — October 26, 2026

## Selected result

**Retain the original narrow low-speed ramp anti-windup guard locally, with the owner-approved quantization variation documented. Do not include any post-ramp settling policy.** No paired source or device changes occurred.

This step investigated the two later integral crossovers and tested four attempted repairs. None improved the selected guard's overall regression profile. Further native testing separates the original 27one-increment brake-request differences from actual firmware safety rejection: the original guard adds no native rejection on the full corpus. The strict baseline-identity condition still differs; the owner explicitly accepted this exact variation as the next local candidate. See [decision and scope](DECISION.md) and `SELECTED_CANDIDATE.json`.

## Cause and rejected attempts

Lower initial integral makes some later propulsion ramps reach their reduced target earlier. Returned `limited` clears before the reference, allowing one or two additional positive-integral updates while the reference remains held. In another route, candidate actual braking still integrates signed error while the reference is waiting for release. This produces a small positive crossover in later integral history. A direct below 6.7 mph eligibility limit therefore cannot promise identical commands at every later speed.

A research policy tested 20/40 ms settling after ramp completion, only after a low-speed guard intervention. It preserves signed negative error, target-negative recovery, epoch/freshness validity and all original torque-clearance rules. Deadline uses the original feedback timestamp and does not extend on duplicate drive feedback. Its producer-reset hook clears the policy whenever LongControl resets.

The first policies kept the extra settling behavior available for later ramps in the same engagement. Both add a release-timeout episode near61mph in a retained route, so both are rejected. Narrowing to a single completion per low-speed intervention removes that added fault but worsens the strong-deceleration comparison.

| Research variant | Added coordination fault episodes | Weaker raw samples under strong target | Weaker encoded samples checked |
|---|---:|---:|---:|
| Original narrow guard | 0 | 253 | 27 |
| Repeated20ms settle | 1 | 941 | Not promoted after fault |
| Repeated40ms settle | 1 | 470 | Not promoted after fault |
| One-shot20ms settle | 0 | 1,039 | 328 |
| One-shot40ms settle | 0 | 2,335 | 335 |

Do not optimize the dwell against these particular recordings or count disengagement as smoothness. The new hold mechanisms are not retained as a fix.

## Original guard: fresh native verification

The selected source is byte-identical to the original research guard from the previous investigation. It holds only positive, unattainable-demand integral growth in moving PID operation below 3 m/s, while fresh current-owner protocol 1 feedback truthfully reports a limited engineRamp, no brake/precharge/reference-brake, and nonnegative valid propulsion. It retains signed recovery and every original >=3 m/s predicate. It does not alter planner gains, ramp rate, brake-clearance permission, packet layout, gear fields or steering.

- **41** selected-guard focused tests pass. Separate tests for rejected history policies total 49 passes, but those unit passes do not override their replay failures.
- **162 segments / 472,261 consumer callbacks** in coupled replay: no added coordination faults, inactive changes, gas during brake/precharge, or moving-PID gas with retained measured torque. Two older reconstructed baseline release faults remain unchanged.
- Fresh native replay: **37,796,591 RX and 1,115,518 TX per recorded/baseline/candidate variant**, all 162 segments, zero added candidate rejection or relay malfunction, no forced controls permission. Original RX, non-ACC TX and timers are retained. Existing rejection evidence is not hidden; zero added is not zero total. Plain debug library, no sanitizer/hardware claim.
- The selected variation is 27 encoded brake-acceleration samples one 0.0039 m/s² increment less negative, with gas/brake bits unchanged at those samples. Maximum raw difference is approximately0.0005115m/s² across 253 callbacks with consumed target <= −0.5. This is documented rather than declared bit-identical or a proved physical stopping effect.

The isolated restart evidence remains useful: stored correction falls 0.772 → 0.199 and peak requested propulsion 1.823 → 1.398 m/s² with no new 6–8 mph reacceleration blackout. Recorded RPM, gear, motion and torque are frozen inputs; changed physical shifting/comfort remain unproved.

## Next boundary

This local candidate is selected; paired integration and builds have not been performed. If ported, verify source/wire equivalence to the selected guard and retain the specific variation receipt. A larger or new difference is not pre-approved. No installation is authorized by the selection decision. The independent downhill mode-selection/response problem remains on the roadmap.

## Artifacts

`SELECTED_CANDIDATE.json`, `DECISION.md`, `native-summary.json`, `all-native-low_speed_ramp_antiwindup-results.json`, `native-source-provenance.json`, focused tests/logs, and comparisons for each rejected variant preserve the evidence. `ramp_experiment.py` is the selected implementation; `history_policy.py` is rejected research. Full raw recordings/traces remain private and unchanged. Both paired repositories remain clean at `5b301a944` / `884c9f491`, with 1.20/0.97 preserved.
