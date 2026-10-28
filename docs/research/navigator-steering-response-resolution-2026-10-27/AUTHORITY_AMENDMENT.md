<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Amendment: optional correction authority under selected deviation constraint

For main/reviewer approval before code. Preserve the current frozen transaction, original68fixture failures, paired diagnostics and independent fixed-plant evaluation.

The atomic angle and original planner curvature remain validated producer provenance and the transaction's target/episode identity. They do not supersede the installed controller's actual selected curvature after its measured-pinion deviation constraint. A generated packet may be native-legal while an optional correction is aimed against that selected feasibility reference. The new correction must have explicit directional authority; it cannot treat the full.01rad/15%budget as available when the original constraint already binds in the same direction.

## Exact projection

In this35–50mphscope(v>9m/s), obtain the same installed fixed-pinion measured curvature`m` and unchanged `CarControllerParams.CURVATURE_ERROR=0.002/m`. The native selected-curvature interval is`[L=m−CE,U=m+CE]`. Obtain the actual selected shadow curvature`s` from the exact installed baseline result, rather than recomputing or changing the planner request. If`s`is outside that current interval or its nominal path direction disagrees with the actual baseline output, optional authority is zero.

The closest curvature to zero in that interval is`z=clip(0,L,U)`. The optional action always reduces the magnitude of baseline path angle. Let`F(k)=k*v*installed_raw_curvature_factor(v,k)`using the original pure Ford feedforward conversion and unchanged owner1.20/.97; this is a known code-space conversion, not an identified physical plant gain. The directional path-angle headroom is

`H=max(0, sign(baseline_path)*(F(s)−F(z)))`.

Thus if the original positive curvature is at its binding lower bound, or negative curvature at its binding upper bound,`s=z`and optional reduction authority is exactly zero. Near the bound, authority is continuously limited by the remaining selected-curvature headroom, rather than an empirical eligibility/deadband threshold. No CE/native limit changes.

Translate the frontier through the already-selected baseline output: the existing mapping/policy/rate contribution is`baseline_path−F(s)`, and is retained identically for the frontier. Only added correction is projected. Its available magnitude is the minimum ofH, the existing conservative combined budget after inherited mapping/selected-policy contributions, and the existing≤5%new/scope allowance. Baseline feedforward, roll mapping, selected shadow intent and original histories remain unchanged. The projection is not a statement that all existing baseline offsets are physically correct; it prevents this optional action from further opposing the selected constraint.

## Lifecycle and reference semantics

Original raw requested curvature—not measurement-dependent selected curvature—defines episode/lockout identity. Unclipping as a result of the controller's own response cannot rearm a locked-out transaction. Original producer atomic angle remains the feedback objective; no derived selected-curvature angle is silently called an atomic producer target. Logs carry raw plannerκ/raw atomic angle, selectedκ/derived feasible-angle diagnostic, native interval/headroom and each budget separately.

If authority shrinks during APPLY/WAIT/MAINTAIN, the transaction's admitted limit can only decrease. It cannot regrow when measured headroom returns. If it reaches zero, added intent withdraws and the same raw-target episode locks out. No fresh action is permitted just because its own response unbinds the constraint. Native final output-rate handling may retain a bounded restoration residual; record it separately from new authority, and do not claim instantaneous frontier equality under an incompatible abrupt baseline jump.

The zero-authority regime is explicitly unsupported for this optional tracking action, not treated as improved tracking. Count it separately from response-associated maintenance, expired trials and ordinary guard aborts. Nonzero unconstrained action is a required positive control. This is an authority/feasibility projection, not a gain cut, plant-confidence invention or a way to erase the previous dynamic failures.

## Test before implementation, then verification

1. Red signed binding-boundary cases and the exact case54configuration show current optional action across a superseding selected boundary. Require zero new authority when binding, finite directional margin when interior, and unchanged installed baseline/shadow.
2. Positive control: old unclipped gain1.10and supported gain1.15fixtures must still deliver material one-transaction maintenance and zero tail cycling. A default-off/all-inactive result cannot pass.
3. Dynamic authority loss/recovery cannot ratchet or rearm the same raw target; FF/roll/parameter/driver/speed exits retain native emitted-rate checks and exact zero residue.
4. Rerun original historical fixtures honestly, and independently fixed command→angle paired closed loops. Keep baseline instability/saturation unsupported, not reclassified as stability. Confirm frozen-source focused21/native only if these amended gates clear; full737selection remains conditional.
