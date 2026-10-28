<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Accepted local design: bounded precharge entry, nominal release

## Scope

A constrained BP-derived allocator, not the full BP follow/coasting extension. Keep the current pitch map, nominal brake/release decisions, planner and PID gains. No earlier coast/release decision, no downhill-disable toggle, no lead gas cap/no-lead braking override. All changes are private research overlays. No paired-source/device mutation.

## Budget and commitment

Maintain a nominal brake-decision history separate from selected wire bits. Current nominal admission and release still run. A higher BP threshold cannot prevent the original negative-demand budget from being charged.

Accumulate signed negative demand area (original experimental 0.01 m/s decision-area limit) and an absolute 300 ms decision deadline from the first negative demand or proposed precharge, whichever occurs first. Positive micro-crossings may repay area but never restart the episode deadline. The budget is a software decision guard, not a measured physical speed-error guarantee.

A weak nominal brake entry may be represented as precharge-only while budget remains. Strong requests and exhausted/invalid contexts use nominal actual braking immediately. Once actual braking is committed, never downgrade to precharge during that nominal brake episode. Withdraw both requests only when the nominal policy withdraws its request.

Owner disable resets the episode. Pedal override cannot rearm it. Rearming needs a continuous half-second of positive, nominally unbraked eligible control, with the existing observer already clear and a fresh valid received torque sample at most 4 Nm. Override/invalid-context/time interruptions reset this recovery dwell.

The 300 ms check runs at consumer callbacks; the command can persist until the next delivery. Report observed stage duration and delivery quantization rather than promise a 300 ms physical bound. Invalid delivery intervals over 40 ms select nominal behavior at the next callback.

## Clearance and output

Brake OR precharge is brake actuation for the release observer and gas handoff. Precharge is not a release attempt. Its finite budget prevents it from becoming an unlimited separate phase.

Only after both bits are withdrawn does the unchanged observer qualify release: fresh valid received torque, at most 4 Nm, three distinct samples spanning 40 ms, original stalled/progressing one/two-second rules. No forecast-based clearance or timeout enlargement.

Actual feedback brake bit stays truthful. Precharge-only reports brake false, precharge true, and limited propulsion; gas remains inactive. Fault and original observer reasons remain visible. No synthetic physical feedback.

## Integral recovery

Precharge-only is a short signed brake-control stage, not a phase of trying to deliver positive propulsion. Interpret fresh, owner/sequence-matched, budgeted precharge metadata as that stage: retain normal signed PID integration just as in nominal actual braking. Do not rewrite the brake bit to achieve this.

On actual release and gas-ramp phases immediately use the existing antiwindup/handoff behavior. No additional post-ramp hold, global one-sided braking freeze, recorded-integral reseeding or shadow hardware feedback. The full replay must preserve nominal I, acceleration and gas histories; a lower switching score obtained by holding braking is a failure.

## IPC needed for later paired integration

The research harness transports metadata alongside real returned feedback at the original publication times. It does not change the capnp schema or installed software. A later integration must explicitly version and encode equivalent fields: selected precharge request, nominal brake demand, allocator phase, episode age and remaining budget, using existing epoch/sequence/producer clocks for freshness. The actual consumed planner target used for the strong-demand guard must also be transmitted coherently; `CS.prototype_plan` is only the offline seam. Missing/mismatched metadata must select nominal behavior.

Do not install this overlay as a production replacement. Paired IPC implementation, normal build/ARM validation and device staging are separate future work.
