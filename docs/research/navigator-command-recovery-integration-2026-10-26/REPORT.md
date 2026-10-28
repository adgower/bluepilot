<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Command recovery paired integration — October 26, 2026

Integrated and committed locally on both `codex/navigator-tracking-release` branches. No push, Comma access, settings change, ARM build or activation.

- Openpilot: `1dbbc01892616c4b1a5c7c841d132f724ea5132c`
- opendbc: `beb10c25770471534261606072c131db5eefa117`
- Parent gitlink equals child HEAD; both checkouts clean. Steering **1.20/0.97**, geometry, controller consumer and safety sources remain byte-identical to the pre-port baseline.

## Port

Child owns RollingGuard/CommandRecovery preparation, signed local-constraint freeze and bounded output reduction. Parent retains native PID/state mechanics and supplies live source-validity and FCW/driver-monitoring/soft-disabling urgency. Removed the earlier uninstalled broad below-3m/s integral guard; the accepted qualified policy supersedes it. No runtime monkeypatch, replay oracle, I repayment/reseed, schema, new toggle or clearance/deadline change.

## Checks

- Minimal and full development Mac builds: pass.
- Parent: **1,086 passed**, 87 skipped, 1 expected failure, 281 passing subtests.
- Child: **4,686 passed**, 1,690 skipped, 24,693 passing subtests.
- Panda build, targeted Ruff and both whitespace checks: pass.
- Whole-pair review: no substantive finding; obsolete unused helper corrected. Fixtures now use real plan/driver-monitoring message fields and serialized qualified-recovery behavior. Initial failures are retained; no runtime checks were relaxed.
- **197 segments / 12 routes / 570,269 callbacks / 1,104,297 producer updates**: exact selected-prototype equality, zero producer or wire differences. Source bindings and raw joint-cache hashes verified.

One retained 12-segment route has five active prefix gaps and is diagnostic-only; 185 segments have no active atomic-input gap. Exact parity preserves the accepted candidate's zero added release-timeout/lost-activity/weaker strong-target request/new retained-pressure-gas gates. The saved 20.6/61mph regression episodes remain braking without added fault.

Native safety applicability is **reused**, not rerun for this port: identical complete command streams, same raw manifest, unchanged native binary and safety header hashes. Selected replay covers all197segments,570,178replacement ACC slots,134retained TX rejections each, zero added rejections/relay faults, no forced permission. See native-applicability.json. Child suite uses that verified Mac debug binary; no sanitizer/hardware claim.

## Limits

Highway pulsing remains unresolved: named20/22/12-change windows unchanged. City route remains byte-identical (17changes/21.533s), normal stopped launch unchanged; rolling requested peaks ~2.0→1.75 do not prove physical RPM/shift improvement. Aggregate braking exposure is **+4.349s**; stronger/longer braking is a material tradeoff, not demonstrated comfort. Two preexisting reference release-timeouts remain. Post-recovery integral history is not globally equal to reference or globally bounded by these replays.

Local build/parity evidence is separate from ARM/model-startup, parked and road response. The prototype script requires its recorded original paired base to reproduce; integrated harness uses final production code without the prototype seam. Earlier rejected account/transient-only artifacts remain separate.
