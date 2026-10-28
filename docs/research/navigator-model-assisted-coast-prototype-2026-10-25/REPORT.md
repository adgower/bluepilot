<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Model-assisted coasting experiment — rejected for integration

October 25, 2026. Local research only. The Comma was not contacted or changed.

The improved response model was used to choose between hypothetical weak friction-braking and valid engine-coasting requests. This is an implemented, replayed prototype, **not a working fix for pulsing**. Full coupled controller replay worsens several highway bands and changes brake-release fault timing. Do not integrate or install it.

## What was built

`policy.py` adds a bounded coast trial when the planner requests only mild acceleration/deceleration, actual received and arbitrated brake torque are fresh and at most 4 Nm, existing eligibility/clearance permits it, and a supported 200 ms response forecast favors coasting. A 0.05 m/s measured tracking-error budget, 200 ms trial, measured-tracking continuation and latched recovery prevent unlimited deferral. The first regression caught a budget-rearming loophole through the original qualifier; the final policy closes that loop.

`experiment.py` loads the current CarController into an isolated Python namespace. It changes one gas-selection seam in memory to permit a valid, bounded coast request. The existing observer must still allow propulsion at that point. Existing brake-release clearance, one-second timeout, stop/restart, ownership, pose and handoff logic remain present. Planner targets and PID/integral implementation are unchanged. No parent or child source files were edited.

The model receives current recorded physical context, the candidate's own past generated ACC commands, and an explicitly hypothetical 200 ms future command prefix. Recorded future commands, torque or acceleration are not selection inputs. Model predictions never supply measured clearance. The model is a short-horizon conditional forecaster, not a validated vehicle simulator.

New behavior is restricted to no-lead operation because this cache lacks independently replayed radar gap/closing-speed context. Following operation retains the baseline policy. New model admission is disabled above 70 mph and below 3 m/s; five-mph synthetic tests cover fallback through 85 mph. Previous controller state can still affect later speeds, so this speed restriction does not prove subsequent commands are identical.

## Evidence

Forty local tests pass, including unsupported-forecast baseline equivalence at 0, 5, …, 85 mph; retained/invalid torque; stop/FCW/lead/arbitration gates; budget lockout; and actual-controller pressure tests with deliberately optimistic forecasts. Real retained pressure still withholds propulsion and faults at the existing one-second timeout. Actual clearance is required before propulsion resumes.

The actual LongControl and CarController were replayed together across all 61 saved Alpha segments: **179,144 consumer callbacks**, with consumed planner/state timestamps, causal returned software feedback, recorded received torque and pose. Baseline comparisons use the previously verified current-pair replay, whose newest-drive outputs reproduce all 135,449 producer computations and 67,687 feedback callbacks. All raw joint-cache hashes were rechecked. This is frozen-vehicle-response replay: changed commands cannot change the historical physical response, so results test software consistency and identify regressions; they do not predict actual ride comfort.

Latest drive, common healthy active samples only:

| Speed | Baseline rapid brake reversals | Candidate | Outcome |
|---|---:|---:|---|
| 20–25 mph | 3 | 3 | No improvement |
| 25–30 mph | 4 | 5 | Worse |
| 45–50 mph | 3 | 8 | Worse |
| 50–55 mph | 7 | 16 | Worse |
| 55–60 mph | 7 | 16 | Worse |
| 60–65 mph | 25 | 24 | Small isolated reduction, more braking time |
| 65–70 mph | 10 | 24 | Worse |

A rapid reversal means successive brake-bit transitions less than 0.6 seconds apart. Faulted/inactive candidate intervals are excluded from these comparisons; disengagement is not counted as a comfort improvement. Full five-mph results are in `joint-comparison-model_coast.json`.

The newest baseline has one release-timeout episode at 47.71 mph. The candidate has episodes at **61.23 and 65.95 mph** instead. Across common healthy samples, the changed integral history also produces 841 samples with weaker raw deceleration while the unchanged planner target is at most −0.5 m/s². These are command regressions in frozen-input replay, not measured stopping-distance results. The older drive with zero model admissions remains identical to its current-code baseline. The other older drive also worsens cycling in the 60s and changes timeout timing.

Native RX/original non-ACC TX/timer replay also completed all 61 segments: **14,338,901 RX and 429,929 TX events per variant**, replacing 179,133 ACC send slots. There were **zero added candidate rejections and no relay faults**. Eleven callbacks were outside original send-slot reconstruction. Existing packet rejections remain; this is a relative acceptance result, not zero total rejections. Native permission was never forced. The unsanitized-build limitation below still applies.

## Why the point forecast was insufficient

The first newest-drive command divergence is at relative 226.23 seconds, 21.39 mph. The baseline requests friction braking/inactive propulsion; the candidate tries valid coast. The consumed planner target is −0.044 m/s² while measured acceleration is +0.762 m/s². A short coast trial can be favored by a point forecast, yet its returned actuator-limited feedback changes subsequent integral evolution. Those consequences persist after the immediate trial and outside its admission speed range. See `first-coupled-divergence.json`.

The coupled replay made 41 model comparisons, all nominally supported; 31 favored coast by the declared point-error margin. This did **not** establish a stable controller. In a separate 54-snapshot command-level screening (approximate eligibility, not the authoritative coupled replay), 43 point comparisons favored coast, but **zero** showed an unambiguous advantage when comparing the reported acceleration uncertainty intervals conservatively. Interval overlap is not proof that coasting cannot help; it means these forecasts do not resolve the choice confidently.

## Remaining work

A successful next design must control the interaction between coast selection, effective actuator authority and integral recovery, and preserve strong-deceleration response over the entire subsequent sequence. Merely extending admission time or selecting the lower predicted acceleration is insufficient. Use the present first-divergence fixture and unchanged planner target as the regression before broad replay. No timeout extension or substitution of forecast torque for received torque is justified.

Following-vehicle operation needs fresh radar gap/relative-speed context in the replay before a new coast policy can address the owner's following-related pulsing. No additional road drive is needed to investigate these software regressions. Active Alpha evidence above approximately 74 mph is still missing; **75–85 mph is not validated**, and synthetic fallback tests are not road evidence.

## Provenance and reproduction

Parent `74eaa6a60d344f141d06da16f4dbe10d3de49c0e`; child `3a5fe9fe5a296d44b7f898b580c2d3afafe6bfd1`. Both paired trees remain clean. Steering constants remain exactly **1.20/0.97**. The research root had existing unrelated changes before this task and those were preserved.

Archived model SHA-256: `5a43b5ad8d09000637ecdfcd8960cf306c61f3b9ad9afcf51fca6c91913a00d0`. The prototype asserts this exact model before importing it. Model fit/calibration roles were not changed. Previously inspected drives are not blind validation.

Use the paired checkout's `.venv/bin/python`:

```sh
python -m pytest -o addopts='' -q --confcutdir=. test_controller.py
python replay.py
JOINT_VARIANT=model_coast python joint_replay.py
JOINT_VARIANT=model_coast JOINT_MANIFEST=older-inputs.json JOINT_PREFIX=older- python joint_replay.py
JOINT_CANDIDATE=model_coast python compare_joint.py
JOINT_CANDIDATE=model_coast python native_replay.py
JOINT_CANDIDATE=model_coast JOINT_PREFIX=older- python native_replay.py
```

Private recordings and traces are referenced by manifests and remain local. Native hooks test packet acceptance, not ECU response or physical smoothness. The ordinary source-contract run has 145 passing tests and 20 passing subtests; its one native-permission test is blocked by macOS refusing the UBSan dynamic runtime. Separate native replay uses a documented unsanitized build rather than claiming sanitizer validation. No ARM/device build, installation or road validation was performed.

## October 25 follow-up

The introduced regression was subsequently isolated to persistent admission fallback and conflicting coast/positive propulsion intent. A narrower prototype repairs that interaction without changing PID/integral code; the exact first-divergence and subsequent replay now pass. Its actual braking reduction remains too small to claim the original pulsing is solved. [Repair and evidence](../navigator-coast-feedback-repair-2026-10-25/REPORT.md).
