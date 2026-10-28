<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Timing fix integration and new Controls Mismatch evidence

October 23, 2026. **Integrated locally; full build checks passed. Nothing pushed or installed.**

## Exact paired branches

Both branches remain `codex/navigator-tracking-release` in the existing dedicated paired checkout.

- Parent: `9590ea8fdeee58b75f0b97bab7762584ee686d39` (`fix(ford): refresh coordination pose at publication`).
- Child: unchanged `d2e8d0404143da0f2685c2ff4932b9b9f702951f`; exact parent gitlink verified.
- Both trees clean. The three tested code/test hashes match the reviewed timing prototype exactly. One validation note is included in the parent commit.
- Owner **1.20/0.97**, lateral refinements, vehicle geometry, child safety, default-off and stop/creep behavior remain unchanged.

The producer uses a nonblocking dedicated pose subscriber, chooses the newest publication for each topic across both caches, and constructs calibrated orientation/source timestamp/validity together. It preserves original sensor/request timestamps, the 100 ms guard, health/reversal checks, main invalidity, reference withdrawal and owner metadata.

## Fresh full checks

All five local phases passed: minimal Mac build, full Mac build, full parent tests, full child/native tests and standalone Panda build.

| Check | Result |
|---|---|
| Parent | 1,029 passed; 87 skipped; one expected failure; 281 passing subtests |
| Child/native | 4,485 passed; 1,690 skipped; 24,693 passing subtests; MISRA subchecks passed |
| Focused contracts | 44 passed locally and in independent review |
| Static | Changed files pass Ruff and `git diff --check` |
| Prior full safety regression | All 1,048 segments / 73 routes passed; exact replay source hashes reverified before commit; zero added rejection, protected-scope change or phase/counter mismatch |
| Fresh new-drive native replay | All 18 segments: 4,137,568 RX / 123,254 TX per variant, 17 shared recorded rejections, zero added rejection or relay fault |

The historical 1,048-segment replay was completed during the prototype task and retained by exact content verification, rather than re-executed for this unchanged code. Its 402 shared rejections and reconstruction/exclusion limitations remain documented in the [prototype report](../navigator-coordination-timing-prototype-2026-10-23/REPORT.md). It protects retained lateral/native behavior; targeted producer/IPC tests cover the new poll. No separate type checker, UBSan, ARM build or device/road validation is claimed.

## The new fault is different

Read-only SSH acquisition downloaded and hash-verified **18 completed new segments / two sessions**, with no open segments deferred. Device remains on `fe08ede1a` / `d2e8d040`, AGNOS 20.1, with the same settings and protected file hashes. All raw identities and full recordings remain private locally.

The first session contains no coordination fault. The second records one fault at approximately **<private clock time> CDT, 41.45 mph**, reason **`release_timeout_disengage`**.

This is not the previous stale-pose fault:

- The consumed request has valid pose data aged **77.699623 ms** and request age **3.379751 ms**.
- A roughly 0.14-second brake/precharge pulse precedes the release wait. Commanded brake/precharge bits then return to zero.
- The actual replayed release wait lasts **1,020.47 ms** at the first deadline-checking update. During it, **52 distinct fresh received torque samples remain 136–388 Nm**, with no qualifying ≤4 Nm clearance samples.
- At the fault, the latest received torque is **156 Nm**, only **2.25 ms** old. Neither pedal is pressed and CAN is valid. This is not missing/stale feedback or a manual pedal override.
- Propulsion stays inhibited (`-5` inactive command), then the existing release guard requests disengagement. It does not grant propulsion just because the deadline elapsed.
- Both the installed baseline and the timing-fix candidate reproduce the **same fault on the same consumed sequence (26505)**. The timing patch deliberately does not suppress it.

The received torque first falls to ≤4 Nm about **337 ms after the fault**. Disengagement changes ownership/commands, so this does not prove that simply lengthening the timeout would clear the brake safely under continued control. ECU-reported torque is also not independent physical pressure/drag ground truth.

The saved command timeline includes multiple preceding brake pulses. Pitch/grade-dependent brake admission and the vehicle's release/feedback response are now the next investigation targets. The evidence proves why the software guard fired; it does not yet identify a safe replacement release policy or establish that the reported torque is solely caused by our last pulse.

## Remaining blocker

The timing fix removes the previously recorded stale-pose fault in the earlier 33-segment replay (one baseline fault → zero), but **does not resolve this new brake-release fault**. The new 18-segment replay has one baseline release fault and one candidate release fault, with no newly added faults or native rejections. All 21,176 inactive/stop/creep packets remain exact.

Before another Alpha evaluation, investigate the short brake-pulse origin, torque arbitration/clearance semantics and release response against these exact saved episodes. Do not treat a timeout increase or forced clearance as a demonstrated fix. Hardware scheduling, staging and activation remain separate authorized work; no installation is performed here.

## Evidence

- [Build commands and exits](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Exact integration pair](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Hash-verified acquisition](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [New-drive native replay](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Release diagnosis](../../navigator-reference/PRIVATE_ARTIFACTS.md), [source summary](../../navigator-reference/PRIVATE_ARTIFACTS.md), [command groups](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- Full raw-feedback timeline and stateful baseline/candidate trace are retained alongside these files.
