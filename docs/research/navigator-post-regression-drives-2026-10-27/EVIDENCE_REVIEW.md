<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent evidence and methodology review

Read-only review of the longitudinal extraction/analysis and lateral analysis/normalization, with independent numerical calculations from the saved compact arrays. No device operations, runtime/source edits, or CAN transmission. Acquisition completeness and source receipts were not independently reacquired in this review.

## Findings

No critical numerical error was found in the independently checked adverse window or lateral steady-band/pressure context. The evidence does not justify declaring either physical complaint fixed across all speeds. Only candidate session 08 contributes moving evidence; newly acquired sessions 01–06 remain pre-update evidence. Empty candidate sessions contribute zero active exposure.

One important report wording correction was identified: the lateral report describes no gas/brake/steering pressure in the preceding 1s. The actual normalizer applies preceding-1s history only to steering pressure; brake and the additional gas guard are checked at the current aligned sample. Repair the wording to “no current gas or brake; no steering pressure in the preceding 1s,” unless the intended qualification is deliberately changed and rerun. This is a qualification-description mismatch, not evidence that the measured steady mismatch disappears.

## Independent recalculations

- Candidate longitudinal qualified active exposure: 974.620807788s, independently rebuilding past-only joins and validity/active/no-override/fault guards.
- Candidate 180.068223976–195.056639850s adverse window: 749 outgoing command rows, 99.7329773% qualified, 14 qualified full-brake changes, and 7.134804253s combined full-brake/precharge exposure. Independently counting raw window full/precharge/combined edges also yields 14 each. This confirms remaining command alternation at approximately 52–54mph; it does not convert edge counts into a passenger-comfort score.
- Candidate moving 5–40mph qualified exposure: 69.941765746s. Stops must not be presented as additional moving low-speed validation, even when included in the explicitly labeled 0–5mph band and below-40 totals.
- Candidate lateral 40–45mph steady meaningful-demand exposure: 25.25s; median body/request 1.1471935582; source-time signed body excess 0.212155329m/s².
- Candidate pressure event at relative 811.95s: independently recomputed preceding qualified context 2.8s, median body/request 1.2000067484, wheel/request 1.2257817110, signed body excess 0.152145099m/s². The association does not establish driver intent.
- Every session with meaningful lateral exposure has absolute requested acceleration at least 0.250095m/s² and wire-equivalent magnitude at least 0.274806m/s² across the inspected arrays. No near-zero denominator artifact was found in those reported meaningful-demand ratios.

## Interpretation boundaries

Longitudinal joins are backward-only with explicit 100ms limits and exact consumed epoch/sequence plus plan identity; edge denominators use qualified active exposure. Rapid reversals require continuous qualified history. Speed-band edge rates assign each edge to its current band; they are descriptive rates rather than matched-route treatment effects. Exported dense-window CSVs are decimated and omit qualification flags, so they cannot alone reconstruct exact full-resolution qualified edge counts; the private numerical arrays and input hashes provide that audit trail.

The lateral body baseline uses physical motion-source timestamps. Its report correctly discloses that this alone does not prove online arrival; the additional publication sensitivity handles arrival availability and preserves the 40–45mph steady median. These are distinct timing views and transient phase/lag remains relevant.

Requested, applied wire-equivalent, wheel-model and body-motion quantities remain distinct. The wire-equivalent is already larger than request in the inspected steady bands, while wheel/body equivalents are below wire-equivalent. This supports describing the observed ordering. It does not identify a unique mapping defect or establish that modifying that mapping would fix physical response: the wire field is a calibrated path-angle-derived equivalent, and wheel response remains model-derived.

The bounded-coast marker is feedback-state exposure, not direct physical coast duration. Absence of recorded controlsMismatch establishes absence in these saved logs, not a failure-free guarantee under unobserved conditions. Candidate speed coverage ends below 70mph; 70–85mph has no candidate validation.

## Resolution

The lateral qualification wording was corrected. Additional1s pedal-history exclusion removes0steady40–45/45–50samples and leaves medians unchanged. Qualified31.97ms delivery delay is explicitly separated from excluded stale startup sources. Final domain hashes were regenerated and verified.
