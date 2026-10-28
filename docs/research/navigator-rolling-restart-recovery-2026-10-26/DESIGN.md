<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Rolling-restart integral recovery — local research spike

User authorized a local prototype and full saved-drive replay including the city braking regression. No integration, device, CAN or installation work. Preserve paired parent2ca969e45 / childbcd706d0 and steering1.20/0.97.

## Baseline and choice

The only runtime difference from recorded installed parent5b301a944 / child884c9f491 is the earlier uninstalled broad below3m/s integral guard. That broad guard changes full-stop launches and later city braking. This experiment replaces it only inside an isolated replay import seam, using the exact installed integral function as reference. Do not add the new policy on top of the broad guard or credit broad-guard differences to it.

Prototype a narrow conditional anti-windup hold, not a planner/gas gain change, CAN-field rewrite or prediction-based brake clearance. Qualify only an active moving slowdown with no actual stop, then fresh owned limited engine-ramp feedback at0.3–3m/s and positive unmet demand. Full-stop launches are excluded until movement above4m/s re-establishes history. A low-speed brake episode must have been observed within3seconds. Missing/faulted/mismatched feedback or clocks clear eligibility.

During a qualified episode hold only positive integral growth; signed negative-error recovery and actual braking remain on the installed path. Once the ramp delivers authority or speed reaches3m/s, resume existing PID recovery, including its moving anti-windup. No integral reset, arbitrary back-calculation from gas−5, hidden shadow-baseline reseeding or repayment of withheld windup. Hold at most3seconds per low-speed approach; no rearming until speed>=4m/s or a reset/actual stop.

Other approaches considered: broad low-speed freeze already fails later-city exposure; direct I reset/backcalculation risks demand steps and treats a mode/ramp request as physical delivery; global output smoothing does not address accumulated I. The narrow rolling condition is the first spike choice, not a claimed field-ready solution.

## Declared checks

Focused high-RPM episodes must show lower stored integral/raw demand; RPM and actual response stay frozen, so no predicted shift/RPM/comfort claim. Normal full-stop launch should remain identical to installed reference until an independent eligible rolling approach. City17-change fixture must not increase brake exposure or replace chatter with sustained braking.

Full197-segment actual LongControl+CarController replay includes current source/installed integral baseline and candidate with causal returned feedback, raw hashes, actual owner/clock/pedal resets. Compare counts, gas under brake/precharge/retained pressure, stronger-deceleration command history, disabled-owner wire and fault histories. No weaker encoded strong-target braking or lost required brake bits accepted by inference from older tolerance approvals. Preserve earlier identified atomic-prefix/receive-order limitations. If candidate fails controller/city gates, retain rejected experiment and do not claim native/ARM/road validation.

## Bounded-depth revision after rejected first pass

The initial unbounded positive-growth hold preserved city17changes exactly but produced longer braking elsewhere and13 weaker encoded strong-target requests under the corrected all-strong-rows gate. Rejected.

Second predeclared trial limits actual foregone native PID integral growth to0.25m/s² per low-speed approach, in addition to the3second deadline. This is a research design choice, not a proved physical tolerance or a fitted threshold. A one-step copy of the current nativePID measures the exact positive growth that would occur without the rolling hold. It is not a parallel reference history, output substitute, borrowed vehicle response or I reseed. A whole update is held only if its measured cost fits the remaining budget; otherwise the approach is spent and signed native integration resumes. No threshold sweep to force the named fixtures to pass.

Validation fixes from independent review: check encoded braking on every common strong-target row regardless of producer raw ordering; explicitly reset inactive missing-input state; clear rolling qualification on active missing inputs and label any such route diagnostic-only; log active invalid-atomic counts. Keep pre-update CC phase because productioncontrolsd assigns it beforePIDupdate. All exact-source fingerprints are bound at replay start and rechecked at end.
