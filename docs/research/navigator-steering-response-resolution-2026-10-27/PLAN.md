<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Steering Response Transaction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans inline; existing independent reviewer reviews design and results. No new subagents or commits.

**Goal:** Falsify or validate a bounded one-outstanding-correction lifecycle without changing installed source or vehicle state.
**Architecture:** Pure response transaction with stamped evidence/generated-packet observation. Local strategy/replay adapters leave installed feedforward/history intact and apply a separately bounded correction. No within-episode adaptive ratchet.
**Tech Stack:** Python, existing installed opendbc/controller/native safety library, pytest, compressed saved-corpus artifacts.
**Spec:** DESIGN.md in this directory; main/reviewer approved with listed clarifications.

## Global Constraints

- Only this new research directory; e05e42f43/5097b993 and1.20/.97unchanged; no network/device/CAN/commit/integration.
- Existing entry/quality/calibration/freshness/atomic-target guards and combined cap/final slew; held correction has fresh continuation checks distinct from earned entry.
- Generated-frame association is not ECUack or causal body-response proof; scalar envelopes not a validated vehicle model.

## Review Focus

- Old response cannot acknowledge a newer correction: strictly newer physical stamps and exact generated identity.
- Invalid/reengagement cannot clear lockout for unchanged target.
- Tracking improvement cannot withdraw earned maintenance; credible underresponse/driver/quality must release.
- FF moves while correction is fixed; target/calibration drift cannot masquerade as correction response.
- Acknowledgment/timeout never authorizes ratchet; expiry and maintained useful action separately counted.

## Task1: Pure transaction lifecycle

Files: `response.py`, `test_response.py`.
Interface: `CorrectionResponse.update(Evidence)->Decision`; `observe_generated(CommandObservation)`; explicit QUALIFY/APPLY/WAIT_RESPONSE/MAINTAIN/RELEASE/LOCKOUT.
- [ ] Write stamped transaction/regression tests, including old/cross-generation response, maintained tracking, invalid-reset lockout and zero-residue exits; watch expected red.
- [ ] Implement one action per target episode, immutable admitted amplitude, response association, exposure lease and monotonic release.
- [ ] Pass pure lifecycle tests with action/rejection/expiry counters.

## Task2: Installed strategy and stress adapter

Files: `prototype.py`, `helpers.py`, `envelopes.py`, `test_strategy.py`.
- [ ] Write regression for exact B1/B2 quantization/delay failures using real strategy interface, plus protected speed/cap/parameter/abort tests.
- [ ] Implement installed-history-preserving post-correction wrapper and explicit generated-packet observation seam.
- [ ] Predeclare broader training/held-out stress grid and seeds, varying target/noise/delay; require maintained material action as well as no same-episode repeated transactions. Run all tests before route selection.

## Task3: Focused raw controller/native proof

Files: `route_worker.py`, `focus_audit.py`, source/input snapshots.
- [ ] Freeze strategy/module/adapter hashes after review; use exact installed reference and compare full packet slots/nonsteering bytes/native outcomes.
- [ ] Run21source-matched segments;±10s planned event excluded from tracking-action screen; retain all native execution. Count trial/response-associated-maintained/expired/unsupported actions separately.
- [ ] Only select if both dynamic and raw material-action/native guards pass. Otherwise retain negative artifacts and concrete blocker; do not force a threshold pass.

## Task4: Full selected-candidate replay and report

- [ ] Only after Task3passes, run737unique hashed segments under frozen candidate/current native safety; explicitly bind any reused references/default-off scope.
- [ ] Verify paired source and all start hashes unchanged; summarize local/native/stress limits separately, preserve failures and artifact hashes. No vehicle improvement or readiness claim from frozen response.
