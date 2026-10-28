<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local 6.7 mph restart-continuity prototype — October 24, 2026

The prototype removes the demonstrated speed-boundary propulsion reset in saved-input replay while retaining measured-clearance and fault protections. This is a report-local experiment: paired production source, owner 1.20/0.97, settings and the Comma were not changed. Nothing was committed, pushed or installed.

## Behavior

The installed observer resets its moving clearance obligation below 3 m/s. The prototype separately retains consecutive, fresh clear-torque observations during uninterrupted owner-enabled, active PID, brake-free operation. A continuous crossing from below 3 m/s to the moving band can use that already-measured qualification.

Qualification requires at least three distinct samples spanning at least 40 ms, every accepted torque in 0–4 Nm, current feedback no older than 100 ms, sample gaps no greater than 50 ms and callback gaps no greater than 100 ms. Duplicate samples cannot create qualification. Braking, non-clear/invalid feedback, reversals, time gaps, phase changes, overrides and owner resets discard the carry evidence. The original observer executes afterward, retaining its current-feedback checks, clock/reversal faults and one-second release deadline. A latched fault is not cleared by an owner-enabled override or a speed crossing.

The propulsion handoff rise rate is unchanged. Avoiding the artificial withdrawal lets its existing valid request continue; it does not raise the requested acceleration, alter gains or allow propulsion without measured clearance. The candidate is a subclass/factory in this directory, not a modification to the paired modules.

## Results

- Original installed-source speed-only diagnostic is RED; the prototype version is GREEN. A steady positive request and repeated fresh zero torque no longer drop to the inactive sentinel solely because speed crosses 6.7 mph.
- **75 focused and retained contracts passed**, including insufficient/repeated/stale/future/reversed samples, real braking, gaps, clock reversal, phase changes, override/reset, small speed hunting, controller-context faults, default-off parity, urgent negative-demand wire parity and preservation of latched release faults.
- Full child regression with the candidate substituted only in the test process: **4,516 passed, 1,690 skipped, 24,693 subtests**. Existing Mac debug hooks were used; no UBSan/ARM claim.
- Saved-input controller replay covers **136,308 callbacks** from the two moving drives. It changes 1,261 propulsion-request slots and 44 reason labels. Brake and fault fields are unchanged. There are **10 measured-clearance carries**, including all nine selected launch examples and one additional qualified crossing.
- Observed differences are confined to **6.71–14.09 mph**. No changes occur below 3 m/s, while inactive, in non-PID phases or at higher recorded speeds. This is parity on these recorded inputs, not a guarantee of unchanged future physical trajectories.
- Every valid candidate propulsion request stays within the recorded request and existing bounds; its upward change remains limited to the existing 0.5 m/s³. Carry events have fresh clear received torque and enabled/active PID operation, without a brake command or fault.
- Both existing release-timeout episodes at about 34 and 46 mph remain at the same controller timestamps. This prototype does not resolve them or the highway brake-command cycling.

[Private/local visualization omitted](../../navigator-reference/PRIVATE_ARTIFACTS.md)

The graph's vehicle speed and feedback are the old recorded inputs. Only the command comparison is counterfactual; it does not predict improved acceleration, comfort or fuel consumption after installation.

## Native RX/TX comparison

The two moving drives provide **47 segments**, **10,914,382 RX** and **328,981 replayed TX per variant**. Baseline and candidate share 16 rejections: 12 button frames, two steering frames and two ACC frames. **Zero added candidate rejections**, relay faults or forced-controls permission. Original producer pose snapshots and owner lifetime are retained; no post-fault ownership extension.

Only ACC output is regenerated for each controller variant; non-ACC output is the original recorded data. There are **27,853 exact excluded inactive/stop/creep packets**, unchanged brake slots and unchanged fault counts. This is the new-recording native comparison, not a fresh complete historical replay, production build or physical validation. The executed harness is retained separately; its inherited header was corrected afterward with exact executable-core AST equivalence verified.

## Scope and limits

The baseline diagnostic reconstruction checks brake/gas/fault/reason at recorded consumer times using latest-published state and decoded torque. It disables lateral activity, substitutes vEgoRaw and uses fixed flag/frame setup. Native replay separately uses raw recorded state/RX and copies non-ACC TX. Neither is an exact physical or closed-loop vehicle model. Earlier source matching and current source hashes bind the baseline; the candidate module/factory are frozen in `frozen-prototype.json`.

No new parent suite, full historical corpus, full build, ARM build, vehicle staging or parked acceptance was performed in this prototype task. Moving-speed physical behavior remains unproven. The two residual release timeouts and brake/coast pulsing remain blockers to declaring Alpha comparable to OEM ACC.

Independent review found no implementation blocker; its suggested override/fault-retention case was added and passed. Both paired checkouts remain clean at parent `064e086d2` / child `50719b1e`, with protected source hashes identical to the road-review baseline. No device contact occurred.

Artifacts: `validation-receipt.json`, `contracts.xml`, `child-tests.xml`, `comparison.json`, `new-candidate-native-safety.json`, `REVIEW.md`, `source-snapshot.json` and the GREEN/RED reproduction logs. The next requested integration must port and validate actual paired files; this report-local class should not be treated as installed code.
