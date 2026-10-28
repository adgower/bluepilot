<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Joint planner/integral/actuator local prototype

October24,2026. User-authorized investigation and local prototype only. Preserve paired source, steering1.20/0.97, device installation/settings and physical clearance/fault handling. No device contact, active queries, CAN transmission or installation.

1. Establish consumed planner feedforward, post-update integral and CarControl pairing from saved producer publication ordering; validate against the exact installed LongControl/PID code before counterfactuals.
2. Separate planner changes, integral changes, brake/release gating and measured torque/acceleration response for all available speed ranges. Keep stale/missing events and replay fidelity visible.
3. Build an actual LongControl + actual CarController software replay using recorded planner/state/pose/RX and returned software feedback. Initial gains/state exact baseline; vehicle response remains frozen. Minimize problematic episodes into fast deterministic fixtures.
4. Prototype a targeted actuator-aware integral correction only if evidence supports it. Test model-only versus integral-only hypotheses independently. Do not raise cruise past model/radar limits or hide a release timeout.
5. Replay all supported saved Alpha sessions, focused transitions/stop/restart/strong braking/override cases and native safety hooks. Report residual signature, regressions, limits and missing75–85mph Alpha evidence. No claim of physical comfort from frozen response.
