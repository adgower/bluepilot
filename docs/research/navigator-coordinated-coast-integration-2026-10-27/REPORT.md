<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Coordinated coast/brake paired integration — October 27, 2026

**Integrated and committed locally; full Mac build and test checks pass.** No publication or Comma action.

- openpilot: `df788e02719c05595dab2f980e6fd9fb9e464006`
- opendbc: `1d29e6e78abcbf5c6a80eb397d80b349c6cca960`
- Both branches: `codex/navigator-tracking-release`; parent gitlink equals child HEAD and both checkouts are clean.

## Integration

Production `BoundedPrechargeAllocator` matches the reviewed final `coordinator3.py` class AST exactly after normalizing its name. There is no runtime research import or monkeypatch. The child owns the sampled weak-demand accounting and zero-debt/100ms measured-clear rearming. Existing signed braking/precharge feedback supplies integral continuity; no PID recovery debt, copied reference I, clearance exception, schema or new toggle was added.

Ported16pure-opendbc regression tests and one parent real-LongControl equivalence test. The child remains independent of parent imports. Two existing tests were retimed to interrupt the new100ms qualification instead of the superseded500ms dwell; debt and fresh-qualification assertions remain. Red/green evidence is retained.

Every other previously tracked file is hash-identical to the initial pair, including steering **1.20/0.97**, geometry, vehicle matching, consumer, safety, launch/settings code, OS manifests and parent runtime. The parent commit adds only its focused test and exact child pin. [Protected-file receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Build and test checks

- Minimal and full development Mac builds: pass.
- Parent suite: **1,087 passed**,87skipped,1expected failure,281passing subtests.
- Child suite: **4,702 passed**,1,690skipped,24,693passing subtests.
- Panda build, targeted Ruff and both whitespace checks: pass.
- Final focused port tests: **29passed**.
- Fresh whole-pair source review: no substantive finding; misleading test names corrected. [Review](REVIEW.md).

The initial sandboxed parent-suite run could not create its standard temporary home-prefix folders. The same suite reran successfully with approved filesystem access; no runtime path patch orHOME override was used. The failure receipt remains separate. The child suite uses the verified unsanitized Mac debug safety library; no UBSan claim.

## Production replay and native applicability

Fresh production-bound replay processes **216segments /13routes /625,238callbacks /1,203,463producer steps**. Every reconstructed ACC wire stream matches the accepted final prototype, and every producer raw/I/freeze/phase/recovery value is identical. The harness uses real installed classes and source-validity/urgency inputs; it does not inject the prototype class. Source and input hashes are bound before/after the run.

The retained12-segment route with five missing active prefix inputs remains diagnostic-only;204segments have complete active atomic-input coverage. Exact parity preserves the selected prototype's zero weaker strong-target request, added timeout/fault, extra full-brake sample, retained-pressure-gas and lost/gained-activity gates.

Native safety evidence is **reused by exact applicability**, not claimed as newly rerun for this port. Complete command streams, raw/joint manifest, safety headers and compiled binary match the selected final native replay:216segments /625,140ACC replacement slots,141retained TX rejections per side,zero added TX rejection/relay fault, no forced permission. [Applicability receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Benefit and limits

Complete-input full-brake changes remain **1,655→1,637**, and full-brake exposure **2,783.745→2,769.615seconds (-14.130)**. Combined brake/precharge timing and gas requests remain identical. The three new highway windows still have14/12/10changes; this is a modest bounded-precharge improvement, **not a demonstrated cure for highway pulsing**.

Sampled demand-area accounting is not an exact delivered-command integral or physical speed-loss bound. Actual motion, torque, RPM, gear and driver behavior are frozen in replay. Two preexisting reference timeout sequences remain unchanged. No further physical restart, braking, grade, fuel-economy or comfort improvement is established.

Local Mac/Panda build and saved replay evidence are separate from device ARM/model-startup, parked and road validation. The Comma has not been accessed, staged, installed, rebooted or changed. No settings, Alpha state, OS or firmware update, CAN transmission or push occurred.

[Commit receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Exact replay parity](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Build receipts](../../navigator-reference/PRIVATE_ARTIFACTS.md)

[Final committed-head verification](PUBLIC_VERIFICATION.json) · [Post-commit builds](../../navigator-reference/PRIVATE_ARTIFACTS.md)
