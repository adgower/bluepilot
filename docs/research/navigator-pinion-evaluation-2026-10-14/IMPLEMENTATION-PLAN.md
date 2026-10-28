<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local pinion implementation and full recorded safety replay

Approved scope: local implementation of the evaluated startup-only fixed-geometry option, preserving exact live 1.20/0.97 tuning; no Comma writes, restarts, firmware flashing, or parameter changes.

Isolated clones: ${PRIVATE_CACHE} and its opendbc_repo, rooted at installed f35e6e5 / eb70bef4. Source workspaces remain unchanged except task research artifacts.

1. Establish minimal local test environment; run targeted existing Ford controller/safety tests as baseline.
2. Preserve the exact live steering patch in opendbc and test its 1.20/0.97 constants.
3. Add failing tests for default-off and Expedition-only pinion configuration, fixed model/paired safety, invalid/stale inputs, and initialization from cached opposite-mode CP.
4. Implement the option in opendbc: pure configuration before controller construction, flag-gated fixed model, matching receive checks in safety. Keep gain/rate/limit/override behavior unchanged.
5. Add openpilot persistent BOOL and restart-required toggle; card reads it once and passes the option before CI construction. Verify wiring and syntax using appropriate local checks.
6. Extract complete required raw CAN/control streams from saved drives, at original sampling rates, without active vehicle access. Replay the actual local controller and native safety RX/TX hooks in chronological order, comparing baseline/default-off/enabled. Document resets, gaps, and any unmodeled integration behavior. No bypassing live protections.
7. Run regression and fail-closed probes, review the full local diff independently, fix material findings with tests, and document exact limits. Save local commits and a parent gitlink when justified by passed checks; do not push or deploy.

Acceptance: default-off baseline behavior preserved; 1.20/0.97 retained; controller/native geometry agree; invalid pinion denies active output; no unrelated platform or high-speed tuning change; replay results auditable and any rejected frames explained rather than hidden.
