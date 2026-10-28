<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local Alpha cycling experiment

Question: can one coherent brake/release policy reduce the recorded near-zero switching without delaying genuine deceleration, losing grade hold, or reintroducing small-positive restart deadlock?

Scope: throwaway report-local controller copy and tests. No paired branch/source/device/setting changes; preserve steering1.20/0.97. No road readiness claim.

1. Extract full-rate recorded carControl/carState and actual ACC slots from all23Alpha segments. Reconstruct installed baseline; quantify byte agreement before trusting counterfactual comparisons. Keep recorded-input replay distinct from closed-loop vehicle simulation.
2. Compare approaches: wider release-only hysteresis (may prolong braking/deadlock), filtered pitch (may delay true grade response), coherent coast band/brake admission (may miss grade/deceleration). Prefer evidence-led bounded policy; no blanket brake delay or gain increase.
3. Write failing contracts for chatter reduction, immediate genuine braking, existing-brake grade holds, stopping, small-positive restart, invalid inputs/time, scope isolation. Prototype only the smallest justified change.
4. Replay full drive and prior historical Alpha segment; compare native RX/TX, stopping/override behavior and unchanged non-ACC output. Run existing longitudinal/parent restart tests plus transitions/grades. Document remaining blockers and physical limits.
