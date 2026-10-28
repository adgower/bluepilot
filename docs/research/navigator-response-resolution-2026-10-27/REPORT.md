<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Brake allocation and delayed steering response — October 27, 2026

**Specific software defects were corrected in isolated prototypes, but neither control blocker is resolved or selected for integration.** No Comma access, setting change, paired-source change, installation or CAN transmission occurred. The paired sources remain clean at `e05e42f43` / `5097b993`, with owner **1.20/0.97** unchanged.

## Brake allocation and integral response

The experiment introduced explicit command/authority transactions: cache the controller's own issued request, match returned command and owner/sequence/timing, use the packed numerical propulsion request, ignore within-quantum residuals, and commit an optional integral correction only once after acceptance. A consumer-side feasibility check can reject only that optional correction when newer grade information would cross the brake-entry boundary. It cannot raise native demand, suppress necessary braking, reset an allowance or grant pressure clearance. The independent measured-clearance and timeout rules remain intact.

The focused **21-segment replay** nonetheless rejects the candidate. Its first integral reduction occurs around +128.299 s. Earlier braking follows around +142.865 s. At +150.280 s, the candidate is braking and permits positive integration while the reference remains in release and freezes it. Candidate I then overtakes the reference; later strong braking becomes weaker even though optional tracking is off. The result is **85 extra brake callbacks, about 0.888 seconds of added braking and 212 weaker encoded strong-request rows**. Fewer brake-bit transitions are not credited as a treatment benefit.

The causal transaction and feasibility checks pass 17 tests; the first diagnostic has seven checks. These do not override the failed full-controller focused gate. No new full 316-segment candidate or native replay was run after that failure.

[Controller report](../navigator-allocation-response-resolution-2026-10-27/REPORT.md) · [Exact failure chain](../../navigator-reference/PRIVATE_ARTIFACTS.md)

We also tested whether short original transitions can identify dynamics, rather than assuming that missing settled coast windows make all modeling impossible. The assessment covers **175 original segments and 53,356 moving anchors**, with whole-session holdouts and separate retrospective robustness fits. Actual command histories add modest forecasting value beyond recent state. However, short-horizon command sensitivity changes sign across sessions, uncertainty bands under-cover the newest drive, and sustained Alpha quiet-coast counterfactuals are unsupported. Prediction is useful; causal directional authority is not validated.

[Dynamic identification](../navigator-allocation-response-resolution-2026-10-27/dynamic-identification/REPORT.md)

## Delayed steering feedback

The new prototype replaces repeated proportional adjustments with one outstanding correction transaction per raw-request episode: apply a bounded correction, wait for newer response evidence, maintain only under current valid conditions, then release monotonically and lock out that episode. It distinguishes entry from maintenance, handles fresh duplicates separately from new response evidence, and limits the optional correction by the existing selected curvature/deviation constraint. Original feedforward, owner factors and deviation limits are unchanged.

The frozen version passes **235 tests** and settles the five earlier quantization/delay counterexamples with material maintained corrections. A separate fixed-response fixture has 53 baseline-supported cases without added quality failures; 15 baseline-unstable/saturated cases remain unsupported. These are invented stress fixtures, not a validated Navigator plant. Earlier fixture failures and alternative normalization results remain retained.

Fresh **21-segment controller/native replay** produces 17 command reductions, zero increases and zero added native rejections. Seven reductions fall in independently qualified 40–45 mph steady samples. But its **three trials produce zero response associations and all abort**, so this brief activity is not a useful maintained treatment and does not qualify for another full 737-segment run.

The exact recordings expose a software bug: ordinary curvature-driven target motion of roughly 0.51–0.79 degrees was mistaken for calibration/basis drift, although unexplained basis changes were only about 0.03–0.18 degrees. A **separate revision** fixes that distinction, requires explicit angle receive/quality/value provenance, and refuses to acknowledge unknown moving-reference responses. Its 14 tests pass, including the three exact saved snapshots. That revision has **no raw/native/full replay**, and does not inherit the frozen version's 235-test or 21-segment receipts.

[Steering report](../navigator-steering-response-resolution-2026-10-27/REPORT.md) · [Separate contract revision](../navigator-steering-response-resolution-2026-10-27/moving-reference-contract/README.md)

## Can the original steering records supply the missing response envelope?

We recovered **535,962 original pinion-angle CAN frames from 100 segments**, including quality and host receive clocks, and fit original-command response models with whole-session holdouts. The label is the ECU's compensated pinion estimate, not independent wheel/tire truth. Known rejection neighborhoods are excluded; simulated reference packets are not used as observed actuator inputs.

Original command prefixes materially improve moving-target retrodiction. But the representative 0.6-second model has a **1.688-degree empirical error half-width**, versus a **0.900-degree median modeled effect** of a realizable trim of at most 5%. No tested held-out moving 35–50 mph null/corrected bands separate. This is evidence against using this particular model as a response provider, not proof that every possible model or all retained recordings are incapable of doing so.

Timing also remains limited: a receive frame's value matches each examined active carState publication within the search window, but **77.4% have multiple matching frames**. Neither repeated-value matching nor publication time identifies the exact consumed frame or internal ECU sampling time. No fitted gain, delay or dual-prefix provider is consumed by the controller.

[Original steering identification](steering-identification/REPORT.md) · [Known brake-signal scope](SIGNAL_OBSERVABILITY.md)

## Remaining prerequisites

- **Longitudinal:** validate response-horizon/directional authority through brake, pressure-release and propulsion transitions, retaining actual acceleration/speed error and later strong-braking gates. Another sticky freeze, integral reset or reopened allowance is not supported by this work.
- **Steering:** validate a moving-reference response envelope for both nominal and corrected command histories, with sufficiently narrow error, input-domain support and trustworthy receive/consumer timing. Unknown or overlapping responses must continue to wait and withdraw.

Existing original maneuver records may supply better excitation if provenance and timing can be established. If they cannot, controlled identification requires a separate validated and explicitly authorized plan; parked checks and offline replay cannot create that physical evidence. This task authorizes neither identification commands nor a road test.

[Independent review](REVIEW.md) · [Combined verification](PUBLIC_VERIFICATION.json) · [Work scope](PLAN.md)
