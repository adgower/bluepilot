<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local steering admission repair — October27,2026

Status: final local candidate passes synthetic, latest21 and full658-segment replay gates. No integration, installation or physical-improvement claim. Paired source and owner1.20/.97 remain unchanged. No device access, CAN transmission, publication or settings writes.

## Final implementation

`prototype.py` subclasses exact installed `ObserverContinuity`, extending only nested `RollAwareMapping` leaves in35–55mph. The original mapping bounds(0.01rad/15%), calibration/target consistency, driver/signal/fault aborts and final range/slew behavior remain inherited. Unqualified extension evaluates the original mapping policy from its pre-step state; existing50–55mph mapping remains available. Withdrawal of an earned extension remains subject to inherited bounded release.

A dedicated admission observer copies the installed Observer's physical freshness, validity, independent timestamps, calibration and target checks. Its independent sample cadence accepts20–100ms scheduling intervals within the existing100ms motion freshness horizon. Physical source-age limits are unchanged; the original mapping's40–60ms cadence validity is also unchanged. Qualification uses a preceding approximately1s history(at least950ms and12 independent samples), rather than assuming21 perfectly scheduled samples.

Entry requires same-direction requests with maximum/minimum magnitude ratio<=1.15, coherent roll-aware wheel/body response ratios within0.15 in every retained sample, and ratios0.5–1.8. A reduction requires both ratios>1.08 throughout history; an increase requires both<0.92. These explicit engineering screening bounds are not fitted physical gain estimates.

Continuation deliberately differs from entry. Once qualified, gradual request evolution can retain qualification even when the entire historical request spread exceeds15%. Current evidence must remain coherent, with reduction release below1.03 or increase release above0.97. An adjacent request jump>15%, reversal, stale/invalid evidence or history incoherence clears qualification. Thus the same entry test is not reapplied every frame; bounded target hysteresis prevents repeated withdrawal/re-entry during gradual transitions. Existing mapping and final bounds still apply independently.

No intended behavior changes below35mph or at/above55mph. Full-history preservation is an explicit replay gate, not inferred from static scope.

## Why the history repair was needed

The original unconditional mapping extension had16 latest-drive eligible40–50mph reductions while observed body response was below80%, and two increases while it was above120%. Those slots were rising/transition-classified with wheel/body disagreement. They are observational screening associations, not demonstrated counterfactual regressions.

A first conservative admission gate also lost useful correction: the installed Observer's40–60ms sampling cadence repeatedly cleared on actual62–75ms controller intervals, despite fresh coherent body/wheel evidence. Each highlighted1s window had three cadence resets per fixture; retained admission history never exceeded7/8 samples. `admission-window-diagnostics.json`, `diagnostic_worker.py` and `admission-diagnostic.log` retain the exact diagnostic. The final elapsed-time observer fixes qualification starvation while preserving physical freshness and original mapping validity.

## Synthetic and focused evidence

`green-tests.log`:123 checks pass in15.09s. This includes original106 highway/midrange/full-controller checks, now using coherent positive-admission evidence where required, plus17 admission, abort, target-jump, exact fallback-history, scheduling-jitter and bilateral under-response checks. Midrange abort fixtures first assert a nonzero earned correction before applying each abort. The local helper preserves signed wheel excess; previous nonnegative fixtures are unchanged. Synthetic checks cannot measure vehicle stability or comfort.

Red evidence is retained: seven initial transition/premature-admission cases failed before implementation(`red-tests.log`), exact fallback-history parity failed before its repair(`red-fallback.log`), and a fresh75ms scheduling case failed before the elapsed-time repair(`red-jitter.log`).

The final latest21 replay passes `check_focused.py`: all18 exact prior adverse-screen timestamps match baseline; the current observed screen has zero reductions below80% and zero increases above120% in recorded atomic and separately labelled causal fixtures. There are407 changed angle slots, all reductions,39.50–51.28mph; maximum delta0.0065rad. No angle changes occur below35 or at/above55mph; default-off whole-stream equality holds and added native TX rejections are zero.

At10:15:59.9, median generated magnitude is98.0798% of baseline(-0.1035→-0.1010rad), maxdelta0.0025rad. At10:23:05.0, median remains100% with maxdelta0.003rad: only partial qualification. Its normalized preceding history includes wheel/body disagreement around0.17 and request spread approaching1.20, so entry excludes portions. Original mapping cadence validity and bounded release remain independent restrictions. These are generated commands against frozen observed response, not changed observed body response or proof of physical improvement.

## Completed full-corpus provenance and results

Both paired repositories are clean at parent`df788e02719c05595dab2f980e6fd9fb9e464006` and child`1d29e6e78abcbf5c6a80eb397d80b349c6cca960`; all37 original source/native-library hashes match(`verified-source-snapshot.json`). All658 raw segment hashes match original evidence manifests(`manifest-verification.json`). Raw recordings are referenced in place.

Final candidate SHA256:`110f831cf5c5fd3bf224cd4716be799869943ce63165badb1027d7afc22beede`. `run_full.py` completed32 historical routes/637 segments in1775.010s(29m35s), using three workers. The separately completed same-candidate21-segment focused replay is reused by verified hash, giving33 routes/658 segments total. This is not a claim that the focused route was rerun inside the1775s historic runtime. `full-runtime.json` records actual start/end epochs, duration and candidate hash.

Full replay processed3,814,069 controller updates and152,312,756 physical RX frames. Each of four recorded/causal reference/candidate variants generated2,476,839 TX frames. Of these,2,464,642 per variant were tested after native Ford configuration and all were accepted;12,197 generated frames per variant precede configuration and are excluded from the native pass claim. There are33 initialization invalid-safety ticks across33 routes. Controls permission was never forced.

`finalize.py` passes: zero added native rejections, exact default-off full-stream equality on every route, all55–85mph retained exposure and all other bands outside35–55mph unchanged, all reference-stream hashes equal the prior full658 baseline, unchanged clean paired source, and identical focused/full candidate hashes. `acceptance.json` and `summary.json` retain the complete receipts. The original baseline's native outcome and full TX-stream hashes are independently retained; no rejected-candidate replay is reused as final evidence.

| Changed angle slots |35–40mph|40–45mph|45–50mph|50–55mph|All other bands|
|---|---:|---:|---:|---:|---:|
|Recorded atomic|127|607|26|24|0|
|Past-only causal calibration fixture|164|650|305|81|0|

`command-audit.json` finds784 recorded magnitude reductions and1200 causal-fixture reductions, with zero magnitude increases in either full comparison. Maximum absolute wire-command delta is0.007rad. Recorded changes span35.965–51.282mph; causal changes35.965–52.357mph. These fixtures are separate comparisons, not additive independent road exposure. The latest adverse observed-response screen remains zero/zero in both.

This local candidate repairs the demonstrated command-screening associations while retaining useful first-window mapping. It does not establish that physical over-response is corrected, and the second symptom window remains only partly qualified. Historical generated controls are current-policy compatibility fixtures rather than historical installed-code reproduction. No counterfactual body response, vehicle comfort, road stability or installation readiness follows from native/replay success.

## Rejected attempts

`rejected-no-roll-wheel-partial.log`: stopped preliminary partial replay when wheel evidence omitted roll. No validation claim is drawn from it.

`rejected-fallback-scaling-*`: initial gate scaled an already slew-limited extension term, distorting original50–55mph fallback. Retained code and route artifacts are rejected; final fallback instead re-evaluates original policy from pre-step state.

`rejected-fixed-count-*`: exact fallback but21-sample cadence-starved admission. It changed only31 slots and corrected neither highlighted window. Its full latest route is retained solely as rejected diagnostic evidence.
