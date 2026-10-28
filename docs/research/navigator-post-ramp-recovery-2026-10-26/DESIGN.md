<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Post-ramp recovery and full-replay investigation

Authorized local research prototype only. No paired integration, source pin change, device access or CAN. Keep1.20/0.97 and installed-reference function884c9f491; current paired2ca969e45/bcd706d0 untouched.

Hypothesis: the previous rolling hold leaves integral history displaced; different brake/release phases subsequently ratchet it above reference and cause the61mph frozen-response timeout. A finite skipped-growth budget does not manage recovery. Original highway pulsing remains a separate unresolved mode/grade/planner problem.

Use explicit accounting of actual native integral increments withheld by the existing0.25m/s²/3s rolling guard. Debt is independent of moving qualification; it is not erased when speed reaches4m/s. Do not start another hold while an earlier approach's debt remains. Native PID resets can discharge debt because they reset actual integral too; source gaps/qualification resets cannot silently do so.

Recover only with fresh same-owner valid unlimited drive feedback, no brake/precharge/reference brake, gas>=0, activevalidstate/no pedals, positive model target and positive current request, speed3–12m/s. No recovery on stop/FCW/force-deceleration.

Proposed recovery rate0.1m/s³ (0.001 per100Hz update), a research choice not fitted to the failure. When native integral decreases under negative error, reduce that decrement by at most its magnitude (I cannot rise across that update). When positive error exceeds0.05 and native integral grows with actual software authority, allow at most one native positive increment of additional growth, also rate/headroom bounded. No extra step on zero error or unknown growth. A partial clipping residual may recover using at most the current unclipped native integral capacity (ki * i_dt * error), still bounded by available headroom. No recorded-baseline I copy or vehicle-response substitution.

Both types of recovery are explicit changes to integration during positive-demand drive. Negative-target/actual braking stays native. Unknown response is not synthesized; pressure release/timeout and firmware limits remain authoritative. Debt accounting must conserve held=repaid+reset+native_absorbed+pending, and pending debt upon leaving12m/s is reported as a gate, not hidden.

Run focused RED/GREEN and actual productionPID tests; full197segment controller replay with the namedcity17-change regression, normalstop and highRPM starts, all strong-target encoded braking independent of raw order, no new releasefault/lostactivity and full native RX/TX compatibility. Keep12segment/fiveactiveprefix-gap route diagnostic;185segments have no activeatomicgap. No physical RPM/comfort claim from frozen response.

## Integration corrections before authoritative rerun

ProductionLongCtrlState is a numeric constant, not an enum whose str() returnspid. Actual-wrapper integration tests exposed inactive recovery; corrected with explicit comparison toLongCtrlState.pid. The first full run is retained only as inactive-recovery debugging evidence. New integration tests cover debt conservation, authority recovery, PIDreset, epoch, urgent demand, clipping and pending-approach gating. Added an elapsedtime cap0.1*dt as well as0.001/update so fast callbacks cannot exceed the recovery slope. Final replay uses a distinct privatecache and exact sourcebindings.

## Clipping-aware revision after flat recovery rejection

The corrected flat account removed the old 61 mph fault but introduced a 20.59 mph timeout and 409 weaker encoded strong-target braking rows (maximum 0.1053 m/s²). It is rejected. Merely counting omitted increments overstates debt when native clipping would have prevented growth.

The new bookkeeping advances a comparison integral, initialized from current actual I plus outstanding debt, through the exact installed freeze function and native PID under the same current inputs and actual returned software feedback. This is an explicit auxiliary integral state; it is not a parallel vehicle simulation or saved-baseline replay override. Native clipping/freeze can absorb pending debt. Positive native growth crossing the comparison integral is trimmed only within that positive step. Negative crossings are measured, not reseeded away. Account conservation includes native absorption. Final full-replay gates still require no additional timeout, lost activity, weaker encoded strong braking, or unsafe request with retained brake pressure.

Reference reconciliation is gated by valid CAN, no pedals or urgent/stop demand, fresh valid fault-free feedback of the same epoch and causal sequence, valid callback timing, and either active rolling-hold context or the 3–12 m/s recovery window. It cannot trim output under stale feedback or outside that scope. Negative-target integration is not guaranteed byte-identical after changed integral history; every encoded strong-braking row remains independently gated by replay. Native absorption is signed revaluation, not an irreversible physical credit.
