<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent paired integration review — 2026-10-27

Reviewed pending parent/child runtime diffs and new clock, signed-coast, clearance and midrange tests. Parent baseline df788e02719c05595dab2f980e6fd9fb9e464006; child baseline 1d29e6e78abcbf5c6a80eb397d80b349c6cca960. No runtime or test files edited by reviewer.

## Findings

No actionable runtime defect identified in the reviewed changes. This is a focused local review, not approval for installation or road use.

The control cycle drains secondary pose inputs before sampling its common clock; publish uses the frozen subscription with drain=False. The primary subscriber is updated earlier in Controls.update, so both producer inputs precede the clock. Source timestamps remain unchanged. Primary pose invalidity remains conjunctive, and true future timestamps remain rejected. Replay supplies the original carState clock rather than advancing to pose time. Existing callers retain default drain=True compatibility.

Signed coast emits truthful brake/precharge=False, inactive gas, reference_brake=True and bounded age/budget metadata. V3 signed integral treatment is limited to validated coast metadata; V1 precharge compatibility and ordinary ramp fallback remain explicit. CoastClearance arms a logical pending obligation without a fake brake command, preserves clock/torque/owner checks, and requires fresh distinct release samples after coast exit. The controller obtains the lease bounds from the allocator rather than incoming wire claims.

Midrange factory selection remains behind all existing tracking/roll/high preferences and required vehicle flags. The explicit sixteen mapping owners retain their specialized baseline objects. Mapping outside admission re-evaluates the original policy from the pre-step history; boundary and fallback tests cover this seam.

## Verification

With cwd at the parent integration checkout and PYTHONPATH=opendbc_repo:msgq_repo:rednose_repo:tinygrad_repo:teleoprtc_repo:., using .venv/bin/python -m pytest -c /dev/null -p no:cacheprovider -o addopts='' -q:

- Clock cycle, high-speed context, longitudinal coordination, precharge transport, signed coast, coast clearance and midrange admission: 61 passed, including actual Controls.state_control + publish in subprocess.
- Existing longitudinal pose suite: 25 passed, one existing capnp repeated-write warning.

An earlier incomplete PYTHONPATH failed to import msgq in the subprocess; the correctly configured run passed. No full build, native safety suite, device execution, CAN transmission or road validation was performed by this reviewer.

## Remaining coverage / claim limits

No missing critical test identified for the focused changes. Useful additional regression coverage: run the actual producer cycle fixture with stale secondary source, genuinely future secondary source, and invalid primary pose, rather than limiting those cases to helper and existing consumer tests. Replay currently has a helper clock-preservation test rather than an actual producer-cycle replay test. These are coverage improvements, not demonstrated defects.

Local replay/fixture evidence establishes ordering and contract behavior only. It does not establish physical brake clearance, steering comfort, actual vehicle calibration, or absence of other controlsMismatch causes. Full builds and broader suites are owned by the integrating agent and are not implied by this report.

## Coverage follow-up

After review, actual producer-cycle regressions were expanded to include stale and genuinely future secondary sources, invalid primary pose, unhealthy sources and replay-clock preservation. All 13 clock tests passed. The production runtime is unchanged from the reviewed implementation. Full suite results are recorded separately.
