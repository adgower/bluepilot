<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Coast/integral regression repaired locally

October 25, 2026. The introduced controller regression is repaired in this research prototype. **The original highway pulsing is not solved.** No Comma access, installation, paired-source changes or CAN transmission occurred.

## Diagnosis and repair

The rejected prototype could remain locked after a coast trial and return the raw brake decision instead of the original bounded brake qualifier. That changed subsequent brake admission even when no new model trial was being attempted. The lock now suppresses only new experimental trials; the original qualifier remains authoritative during fallback. A deterministic regression fails on the old policy and passes on the repair.

Coast admission also allowed a positive PID propulsion request to be replaced with a negative engine-coasting request. Its actuator-limited feedback then affected integral recovery when the planner crossed into positive acceleration demand. The first command change occurred at relative 226.23 seconds/21.39 mph, but the first meaningful integral difference in the rejected version was about 72.5 seconds later, near 52 mph. Thus the prior report's broad attribution to coast feedback did not isolate the persistent admission-state problem.

The final policy requires the **planner target, PID request and compensated intent to agree on mild nonpositive demand**. It ends the experimental coast state as soon as the planner or PID requests propulsion. It also requires measured acceleration to be within +0.05 m/s² of the requested target before allowing a trial. In the saved first-divergence case, actual acceleration was +0.733 m/s² while the target was −0.044 m/s²: the repaired policy retains braking rather than trying coast.

A lock can rearm only after 0.5 seconds of fresh physical eligibility, clear actual/arbitrated torque, positive planner/request/compensated demand and measured tracking. Negative coast eligibility and positive recovery eligibility are separate; waiting or tiny sign crossings cannot reset the experimental debt budget.

**No PID gain, integral update, feedback schema or anti-windup function was changed.** An explicit coast-intent feedback marker was tested as an intermediate probe, then removed: the admission constraints alone produce the same full replay. `intent-metadata-probe.json` records the intermediate wire hash for the removal check. Keeping honest actuator-limit feedback is preferable to hiding a limit in order to obtain integral growth.

The original received-torque observer, three-sample clearance qualification, one-second release timeout, stop/restart handling, ownership checks and handoff still run. Forecast torque never substitutes for actual clearance. Models were not retrained.

## Regression evidence

- **46 local tests pass.** These include the saved first-divergence inputs, retired-lock baseline equivalence, positive-demand exit, positive-request exclusion, real recovery, cumulative tracking-debt exhaustion, missing/unsupported forecast fallback through synthetic 0–85 mph, and actual-controller retained-pressure/clearance tests.
- Actual LongControl and CarController replay covers **61 saved Alpha segments / 179,144 consumer callbacks** using chronological producer/consumer clocks, consumed plans, causal returned feedback and recorded physical inputs.
- The exact saved first-divergence sample now matches baseline braking and propulsion output.
- All **135,449 newest-drive producer outputs and integral computations** match recorded baseline within 1e−5. The full candidate-versus-current-baseline integral trajectory has **zero difference**.
- No added fault samples, weaker strong-deceleration command samples, inactive-output changes or increased rapid reversals in any five-mph comparison band. The older drives match their current-code baselines. These older current-code baselines differ from historical installations and are not presented as reproducing old installed software.
- The original newest-drive **47.71 mph release timeout remains** at the same time. The prototype's added 61.23 and 65.95 mph timeout episodes are absent. This repairs introduced failures, not all existing ControlsMismatch causes.

`verify_regression.py` asserts the actual saved sample, subsequent integral trajectory and broad no-regression checks. `regression-result.json` and `joint-comparison-model_coast_final.json` retain the results. Intermediate lock-only and phase-only summaries are retained as summaries; their reused trace slots are explicitly marked rather than presented as final evidence.

Native safety-hook replay also completes all 61 segments: **14,338,901 RX / 429,929 TX events per variant**, with 179,133 reconstructed ACC send slots, zero added candidate rejections and no relay faults. Existing original/baseline packet rejections are retained; this is not a claim of zero total rejections. Permission was never forced. The runner uses an unsanitized native debug build; sanitizer and ECU/hardware validation are not claimed. The final simplified prototype has an identical full newest-drive wire hash to the tested feedback-marker probe.

## Actual comfort benefit is still small

The final newest-drive replay makes five supported model comparisons and changes only 12 feedback callbacks. Brake-command time falls by about **0.249 seconds total**: approximately 0.081 seconds at 30–35 mph, 0.142 seconds at 60–65 mph and 0.026 seconds at 65–70 mph. Brake-transition and rapid-reversal counts are unchanged. No experimental trial is admitted on the two older drives.

This is enough to demonstrate removal of the introduced feedback/integral regression, **not** a meaningful reduction in the owner's highway pulsing. Do not install or describe this as the overall comfort fix. The remaining problem needs a planner/controller/actuator strategy that can handle requests conflicting with passive coast without arbitrarily overriding positive propulsion or hiding actuator feedback. Following-vehicle coast changes still need fresh gap and closing-speed context in the replay. Existing recordings remain useful; no new road test is required to continue that investigation.

## Validation limits

This is frozen-recorded-input software replay. Candidate commands cannot change historical measured acceleration, torque or driver response. Model support and packet acceptance do not establish ECU response, stopping distance, smoothness or physical readiness. Active Alpha coverage above approximately 74 mph remains missing; synthetic 75–85 mph fallback tests are not road validation. No ARM/device build or road test was performed.

## Source and reproduction

The paired integration remains parent `74eaa6a60d344f141d06da16f4dbe10d3de49c0e` / child `3a5fe9fe5a296d44b7f898b580c2d3afafe6bfd1`, with **1.20/0.97** preserved. Previous unrelated research-root changes were retained. Archived response-model SHA-256 remains `5a43b5ad8d09000637ecdfcd8960cf306c61f3b9ad9afcf51fca6c91913a00d0`.

Use the paired checkout's `.venv/bin/python` from this directory:

```sh
python -m pytest -o addopts='' -q --confcutdir=. test_controller.py
JOINT_VARIANT=model_coast_final python joint_replay.py
JOINT_VARIANT=model_coast_final JOINT_MANIFEST=older-inputs.json JOINT_PREFIX=older- python joint_replay.py
JOINT_CANDIDATE=model_coast_final python compare_joint.py
python verify_regression.py
JOINT_CANDIDATE=model_coast_final python native_replay.py
JOINT_CANDIDATE=model_coast_final JOINT_PREFIX=older- python native_replay.py
```

Private caches/recordings remain local and are referenced by the manifests. Raw joint-cache hashes are checked by replay; forecasts use causal current context and hypothetical command prefixes, not future recorded response.
