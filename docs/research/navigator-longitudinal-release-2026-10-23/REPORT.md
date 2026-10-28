<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Qualified brake release and restart — local correction

October23,2026, America/Chicago. **Reproduced software restart/release blocker resolved locally. Scoped tests and replay pass; ready for paired integration/build and subsequent bench/device acceptance, not installation or road clearance yet.** Current paired branches and Comma unchanged; owner1.20/0.97 retained. No device access, settings change, firmware change, publication or active ECU query.

## Cause and correction

The current Ford interface caps positive requested acceleration at0.2m/s² near cruise speed. The original brake latch needs pitch-compensated acceleration strictly above0.3to release. A positive0.2request can therefore remain latched indefinitely. Current openpilot LongControl transitions stopping→pid; there is no starting-state transition in this path. Tests exercise that real state machine rather than relying on the legacy enum alone.

The new local gate allows earlier release only when active pid/legacy starting control has sustained raw positive intent and processed brake acceleration plus pitch both above0.02m/s² for60ms. The original valid release path is retained. Negative net braking demand relatches immediately. Stop/off states, invalid pitch/demand, backward/repeated timestamps or gaps cannot clear a previously latched brake. Near-zero±0.01noise does not qualify release. The0.02positive margin and60msqualifier are explicit exploratory engineering choices, not fitted OEM/hydraulic calibration. Positive net demands inside the margin remain conservatively latched by design.

Propulsion remains withdrawn while braking/stopping or data is invalid, and resumes through the prior bounded handoff. The main exploratory0.5m/s³ positive-request limit /20msbrake-clear qualifier remains unchanged; other rates/qualifiers are swept. Brake acceleration, its existing limit/creep/pitch/rate processing for valid inputs, stopping flag, predicted acceleration, target speed, steering and native safety code remain unchanged. Only justified brake/precharge bits and propulsion can differ. Other platforms and stock mode bypass the correction.

Invalid target acceleration now holds the last **processed** finite brake acceleration while active, bypassing repeat creep/rate processing, and neutralizes acceleration on disengagement. Missing/NaN/infinite orientation is checked before target-platform trigonometry. Independent review found and reproduced a repeated-creep fallback bug; the correction and persistent-low-speed-invalid regression resolve it.

## Verification

| Check | Result |
| --- | --- |
| Focused helper/controller/real LongControl integration tests |33passed; includes noise and persistent-invalid regression |
| Existing Ford controller and native safety suites with candidate bound before collection |854passed,79skipped,12,063subtests passed |
| Qualified release randomized/burst transitions |100,000updates passed, including4,001qualified early releases |
| Propulsion handoff randomized transitions |90,000updates passed across nine settings |
| Frozen-input differential |12variants ×2,984ACC outputs; all accepted by scoped native TX hooks |
| Actual-send-slot RX-driven replay |239,195RX frames per variant, zero RX rejections;2,983ACC send slots;2,982accepted/one shared rejection, zero added candidate rejections |
| Exported candidate package |Nine controller test groups passed through production-style package imports; Ruff checks pass; formatting of new helpers verified AST-equivalent |
| Patch application preflight |`git apply --check` passes against the pinned child; patch not applied |
| Independent review |One P2 fallback finding fixed and33tests independently rerun; no remaining concrete findings in scoped follow-up |

In the final synthetic-clock main configuration, **61brake-bit frames and733propulsion frames differ** from baseline;768ACC frames differ in at least one permitted field (sets overlap). All3,889non-ACC outputs remain identical for the reconstructed input fields. Brake+valid-propulsion frames fall751→0. There are43positive-request reductions while baseline brake is clear. Valid-wire positive slew peaks0.5m/s³ in this sample; sentinel transitions are not physical acceleration changes. Counts in the actual-send-slot replay differ because that replay uses recorded slots and actual elapsed time;770candidate packets differ there. Do not combine the two clock models into one exact-wire claim.

### RX-driven permission edge

Native permission is never forced in `replay_rx.py`. It processes recorded bus0–3RX, timer and one-second safety ticks, stable timestamp ordering and actual recorded ACC send times. All TX slots have valid native RX configuration. At+48.859173s, the original recorded ACC packet, reconstructed baseline, earlier handoff and new candidate are all rejected: driver brake is pressed, native permission false, but recorded longActive still true. This preserves the expected safety cancellation boundary; it is not a candidate-only rejection and is not bypassed. No relay fault occurs.

This replay sorts934out-of-order adjacent logged event pairs by timestamp, reconstructs50Hz controller phase and seeds initial accel/latch. Inputs are past-only and at most100msold. It exercises only longitudinal TX with real RX—not a full lateral/forwarding/heartbeat/vehicle simulation or exact original application cycle. The existing Ford suite separately covers its own native contracts. Mac hooks are debug/unsanitized. No ARM build or device test is claimed.

### Reproduced request timing

With fixed synthetic state at standstill after braking:

- Flat raw+0.2: brake bits clear after0.06s; first positive propulsion request0.10s; reaches+0.2by0.48s. Original stays latched.
- Pitch contribution−0.3/raw+0.4, net+0.1: clear0.06s, positive0.10s, reaches+0.4by0.88s. Original stays latched.
- Pitch contribution−0.3/raw+0.2, net−0.1: remains braking, as required; no forced release.

These are **emitted command timings**, not vehicle launch time, hydraulic release, rollback measurements or guaranteed acceleration. The0.5positive rise limit can take about4s to reach a hypothetical2m/s² request; real vehicle response and urgency tradeoffs remain part of physical validation. No final on-road calibration selected.

## Deliverables and next gates

[Design](DESIGN.md), [review](REVIEW.md), [focused tests](../../navigator-reference/PRIVATE_ARTIFACTS.md), [Ford suite](../../navigator-reference/PRIVATE_ARTIFACTS.md), [frozen-input results](../../navigator-reference/PRIVATE_ARTIFACTS.md), [RX-driven results](../../navigator-reference/PRIVATE_ARTIFACTS.md), [release timing](../../navigator-reference/PRIVATE_ARTIFACTS.md), [randomized release results](../../navigator-reference/PRIVATE_ARTIFACTS.md), [export verification](../../navigator-reference/PRIVATE_ARTIFACTS.md).

[Candidate patch](../../navigator-reference/PRIVATE_ARTIFACTS.md) and `stage/opendbc/car/ford/` contain the concrete local integration candidate. The export preserves tested helper ASTs while using production-style imports and explicit main prototype constants. No patch was applied to the live local paired checkouts.

Next gates: integrate into the paired branches, add normal in-tree tests, complete retained build/context regressions on that exact integrated pair, then separate backup/ARM build/parked hardware acceptance before a supervised low-speed evaluation. Production freshness/lifecycle behavior needs integration review; this helper does not independently know orientation sensor age beyond its packet/timestamp inputs. Existing safety limits and cancellation behavior must remain unchanged. Physical brake release, hill rollback, comfort, repeated stop/go, shaking outcome and fuel consumption are unverified. Do not claim OEM-equivalent or better longitudinal behavior from these local checks.

Keep Alpha off on the current Comma. The prior [future testing/OEM comparison plan](../navigator-longitudinal-handoff-2026-10-23/TEST_DRIVE_PLAN.md) remains applicable, but its original software restart-blocker status is superseded by this local correction. No80–85mphreproduction is requested.
