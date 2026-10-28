<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local steering correction response transaction

Proposed for review before implementation. Local research only; exact installed source e05e42f43/5097b993, native library, owner1.20/.97 and Comma remain untouched. This design replaces B1/B2's continuously recomputed proportional trim with an explicit outstanding correction transaction. It does not identify the Navigator plant or estimate a universal gain.

## Alternatives and selected scope

Repeated Ptrim plus larger amplitude deadbands fails the observed quantization/delay question. A Smith predictor or adaptive plant controller would require delay/gain/model uncertainty that the saved observations do not identify. The proposed conservative alternative permits **one bounded correction transaction per independently evolving target episode**. It waits for fresh post-command response, never ratchets while response is outstanding, and never reopens a completed/rejected transaction because its own error falls or rebounds. This sacrifices continuous convergence/adaptation to make the feedback lifecycle explicit and falsifiable.

Entry and continuation differ. Entry retains the installed approximately1s earned coherent wheel/body reduction admission and stable request. An acknowledged correction can remain earned when tracking approaches target; it must not be withdrawn just because the entry over-response threshold is no longer met. Every continuation still requires current independent fresh state/motion, valid calibrated atomic target, ECUquality, same direction and noncontradicting current wheel/body evidence. No cached good sample revives invalid input.

## Module and interface

A pure `CorrectionResponse` module accepts current stamped evidence and emits a desired bounded reduction fraction plus state/reason. A local adapter connects it to the installed admission/mapping seam. The installed feedforward and original strategy histories advance every frame. A staged controller adapter reports the **actual generated/decoded steering packet** and time to the module; a generated packet is not an ECU receipt/acknowledgment.

Evidence includes current independent state/control/motion stamps, calibration generation, requested curvature and atomic angle, compensated ECUangle and quality, body yaw/reported standard deviation, original admission, current inherited mapping budget, and current driver/target/speed guards. It does not invent parameter covariance or use newer/future vehicleParameters as an exact producer snapshot.

## Lifecycle

1. `QUALIFY`: exact installed entry and freshness/calibration/quality gates. No added correction. A stable external target episode has an anchor requested curvature/direction; the existing15% target-change/reversal rule defines when that episode is no longer the same request. Requalification alone after changed response is not a new episode.
2. `APPLY`: choose a single correction amplitude from current/past independently sampled wheel-angle error, existing0.5degdeadband,≤5%new and combined≤.01rad/15%budget. The action slews in; its amplitude is frozen for that transaction rather than reevaluated from a quantized derivative. Current feedforward remains live. A predicted target crossing may veto/withdraw but cannot create a larger action or count as stable amplitude evidence.
3. `WAIT_RESPONSE`: begins only once a fresh generated steering slot shows the new correction quantum. Record its generated time, source high-water stamps and actual/target/error anchors. No larger or second correction is allowed. Only physical state/motion samples newer than that generation can supply response evidence. Angle movement consistent with reduced over-response must exceed nominal quantization plus observed target movement; this is an association/consistency check, not a causal plant-gain proof.
4. `MAINTAIN`: a fresh consistent response permits holding the acknowledged bounded correction while the target is tracked. No automatic increase and no repeated Pupdate follow acknowledgment. Current independent freshness/quality/target consistency and body direction/coherence continue every frame. Losing initial `body/wheel>1.08`entry excess is not an exit. A credible body shortfall (directional error+2×reported yaw uncertainty<0), wheel under-target beyond the inherited deadband, invalidity, driver action, target/scope departure or source-generation change starts withdrawal. Good tracking itself is not a release trigger.
5. `RELEASE`: monotonic correction-only withdrawal with the existing mapping/final native slew. No renewed trim during withdrawal. Driver/inactive/fault provenance aborts use inherited hard-abort/final native handling. Zero requested correction must reach exact zero; no quantized residue or debt remains.
6. `LOCKOUT`: once released/rejected/timed out, remain at exact baseline for that same external target episode. Error rebound caused by restoring baseline cannot rearm the loop. A new independently changed curvature/direction episode, followed by fresh full admission, may arm a new transaction. A reset/disengagement cannot replay old outstanding evidence.

## Unsupported response and timing

Acknowledgment is event-driven; elapsed time never substitutes for measured response or settling. Without an observed fresh consistent response, no new correction is admitted. A bounded maximum **observation lease** is a research exposure policy, not an assumed actuator delay or required dwell. Proposed default2s, explicitly parameterized and swept independently (0.5/1/2/4s). Lease expiration withdraws and locks out; it never declares settling or allows another attempt. Held-out delays beyond the lease must therefore fail closed. This choice is for review; no current-source physical2sdelay claim is made.

A false/ambiguous response association cannot authorize a larger second action because this prototype permits no within-episode ratchet. Persistent current quality and contradictory response exits still apply. A future multi-update controller needs an identified response/settling contract and independent target uncertainty; it is outside this bounded design.

## Maintained correction and mapping

The adapter separates original admission from the response module's earned maintained state. It must not misuse the original entry gate as continuation or silently enable new roll mapping. The existing roll term follows its original admission. Only the new transaction's fraction may remain while its current continuation checks pass. Combined signed correction, caps, range, scope fade and final slew remain enforced. Feedforward requests are never held; only the correction transaction is held. No integral/error accumulation/new budget account is introduced.

## Required regressions before route replay

- Exact frozen B1gain1.10quantized cases and B2gain1.15/delay0.5s/tau0.1s three-wire-LSB counterexample, retaining old failures.
- Unknown/no response, delayed response beyond lease, out-of-order/duplicate physical samples, post-generation acknowledgment identity, ambiguous/wrong-direction response, source-generation resets.
- Maintained correction does not withdraw merely because angle/body tracking reaches target; strong body/wheel shortfall still withdraws; baseline rebound cannot rearm the same episode.
- APPLY/WAIT/MAINTAIN/RELEASE/LOCKOUT driver/quality/fault/atomic-target/reversal/speed exits, exact zero residue, default-off and protected-speed behavior.
- Fresh feedforward moves while correction is fixed; cumulative real target evolution forms a new episode only by the explicit external rule.
- Broader predeclared scalar stress grid: both directions, gain1.02–1.4, delays0–3s, time constants0.05–2s,0.1degECU/.0005radwire quantization, bounded noise, changing targets/roll/parameters, abrupt delay changes. Scalar models are invented stress envelopes, not a validated vehicle simulation.

Pass conditions include no self-sustained repeated correction entry/release in a constant-target episode, finite monotonic withdrawal/exact zero on exits, no added quality/native regressions, and nonzero bounded action where response/entry support it. Merely becoming inactive everywhere is not treatment success. The timeout/fail-closed results are separately counted from useful maintained actions.

Only after source-bound dynamic/unit gates pass: fresh focused21actual controller/native replay versus exact installed reference, exact nonsteering packet/slot comparison, planned811.95±10s excluded from benefit counts. Frozen measured body/angle response cannot establish physical improvement. Only if focused material command action and quality/native gates pass: fresh candidate full737corpus/native replay with explicit reference/default-off/diagnostic reuse scopes and preserved hashes. No integration, installation, network or CAN transmission follows.

## Review clarifications accepted

- A response uses physical state/motion source stamps strictly newer than the final generated correction slot, not event-arrival time alone. The packet anchor binds exact generated baseline/candidate decoded values, target/angle/error, calibration values/generation and source high-water stamps. Generated publication remains distinct from ECUreceipt.
- Repeated20Hz calibration publication timestamps alone do not change generation. Actual calibration-generation invalidation, material parameter/roll-driven target drift or atomic-target inconsistency invalidates response association. Lockout/episode anchor survives transient invalidity, calibration resets and reengagement with unchanged target. A planner-derived evolving target is not guaranteed exogenous in a real closed loop; the episode rule prevents this prototype from proving vehicle stability.
- The one transaction has a finite planned ramp; its final generated quantum anchors WAIT. No observation during the ramp is credited as response to its completed amplitude. Acknowledgment does not authorize a larger action or prove settling.
- Implementation seam proposal: a local strategy wrapper advances exact installed strategy unchanged, then applies only the new response correction. Its conservative available budget subtracts the maximum existing mapping contribution across installed leaves and existing selected-policy reduction from the inherited.01rad/15%envelope; it adds nothing if existing correction already spends that envelope. Original roll admission is never overridden for maintenance. A separate output-history field enforces final native slew without overwriting installed strategy history. This avoids reconstructing the sixteen mapping leaves again.
- The staged replay adapter reports exact reference/candidate generated packets after encoding. This research-only observation interface must not be represented as an existing production ECUacknowledgment transport. Source/slot identities are explicit receipts.
