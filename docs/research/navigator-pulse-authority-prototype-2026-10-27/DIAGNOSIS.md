<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Pulse prototype: first-divergence diagnosis

Read-only inspection of `joint-local_state.json`, `joint-pulse.json`, their referenced gzip callback traces and producer pickles, plus `comparison-local_state-pulse.json`. No policy changes or additional replay were run for this diagnosis. Results concern `pulse`, not the separately running `pulse2`. Independent recorded-feedback producer reproduction remains a prerequisite for trusting this as an exact installed-software regression.

## City fixture: broad phase freeze changes release before true coast is needed

The 25 mph fixture starts at mono 153762.445323964. At its first callback (153762.451246689), histories match: target 1.117221832, I .245879982, raw 1.363101840, gas equal raw and drive phase.

The first producer integral divergence **inside this fixture** is 153764.164899248, epoch 153679248100922 / sequence 8411. Both histories consume target .968337357, actual acceleration .549496353 and speed about 19.881 mph. Both see limited feedback, no brake, reason `no_release_pending`:

| History | Frozen? | I | raw |
|---|---:|---:|---:|
| local_state | false | .013762376 | .982099733 |
| pulse | true | .011668171 | .980005528 |

At callback 153764.168679505 both already report drive/at_target, but the earlier published feedback still constrains the producer. The broader phase predicate held one positive integral increment that the nominal numeric-delivery predicate permitted. This occurs before an in-fixture true-coast intervention is required; this candidate changes more than coast mode selection.

At **153771.407480393**, first fixture brake mismatch:

| History | target | I | raw | net | brake / phase |
|---|---:|---:|---:|---:|---|
| local_state | .072285600 | .096663501 | .168949097 | .031241722 | false / release |
| pulse | .072285600 | .085053309 | .157338902 | .019631527 | true / brake |

Both allocations report `budget_reference`. Lower accumulated I changes the subsequent nominal release decision; preserving the strong-current-target branch does not preserve later demand history. The complete fixture goes **17→27 brake changes**, **21.448→23.957 brake seconds**, and **14.588→10.854 valid-propulsion seconds**. These numbers do not support improved city comfort.

A protocol-validation gate alone cannot explain away the above chain if this feedback is protocol-valid. Do not treat a v2 protocol fix as evidence that this behavioral issue is corrected; inspect its completed comparison separately.

## Coast plus phase feedback can reinforce extra braking

An earlier route-local example makes the combined mechanism explicit. At mono153724.433302510 (~45.351s into smoothness-road-session-02), baseline is drive, raw .291639715, net −.015702464 and gas .291639715. Candidate selects `bounded_true_coast`, raw .290545404, net −.016796775, gas −5 and handoff qualify. This emits engineRamp/limited feedback even though no positive propulsion is delivered.

At153724.469756765, baseline integrates to I .039302162/raw .313266754; candidate is frozen at I .030223468/raw .304188043, continuing true coast. At153725.769434318, baseline has recovered to net +.087793206 and gas .258771300 with no brake. Candidate has I −.086446803/raw .153895885/net −.026935364; its area reaches .010157492 and it enters `budget_reference` with actual brake/precharge. Baseline I is +.028281755. The finite allowance is acting as designed on a demand history that the candidate itself changed.

Thus true coast → limited feedback → held positive integral → lower raw/net → exhausted signed-demand allowance → nominal braking is a concrete software chain. It is not evidence that unchanged recorded vehicle acceleration would physically persist under the candidate's different commands.

## Highway regression is the same history sensitivity, not a missing closed loop

For precharge-road-session-02, first producer difference occurs at135716.367081294 (sequence8904): baseline freeze false/I .440415031 versus pulse freeze true/I .440207712, same target1.423305273/actual1.381841421. Subsequent history diverges before the highway fixture.

At first highway fixture callback135868.723444384, baseline raw/gas .132984534, I .050658754 and drive; candidate raw .116054252, I .033728474, gas −5 and engineRamp/limited. At135868.864771539, baseline net +.000792996/brake false, candidate net −.016137282/brake true, both budget_reference. Full fixture changes **20→26 switches**, **9.914→10.489 brake seconds**, and **3.345→1.718 valid-propulsion seconds**.

The replay **does** close the software producer/consumer feedback loop: generated controller feedback is causally published back into LongControl, which recomputes I/raw and later consumer decisions. What remains frozen is the vehicle/ECU/lead/driver response. Missing physical closed loop limits performance claims, but it does not erase these observed software-history regressions.

## Why integration remains blocked

The completed 237-segment/14-route comparison reports1620 strong-target weaker encoded samples (1614 with brake bit), city/highway switching regressions, and candidate release-timeout faults. Its global extra-brake time (~456.878s) includes diagnostic or fault-altered routes and is not a clean eligible-road effect size. In the newest route, a candidate release-timeout at mono229915.670800896 is followed by inactive producer output; zero changes in later fixtures are therefore **lost activity**, not successful smoothing.

Even one apparently favorable new-highway window (12→5 changes) increases brake time4.159→10.586s and reduces valid-propulsion time9.356→3.237s. Counting switches alone hides materially different command exposure.

No native-safety, device or physical validation is inferred. Exact installed producer reproduction, clean eligible-route reporting, no new coordination faults, retained strong-braking protection and improvement across the protected city/highway windows remain required gates.
