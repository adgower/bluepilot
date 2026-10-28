<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local brake-admission / release prototype

Authorized exploratory prototype only. Paired parent9590ea8fd/childd2e8d040 stay unchanged and clean. No SSH, push, commit, device writes or CAN I/O. Preserve1.20/.97 and existing native limits.

## Diagnosis

New41.45mph fault is real release_timeout_disengage with52fresh non-clear torque samples over1.020s, not a pose fault. Exact last brake onset is one net-acceleration sample around-0.00118m/s² with planner demand+0.302m/s². Immediate sign-based hysteresis admission latches actual brake/precharge for~140ms, then waits for physical/received clearance. A brief crossing can therefore produce a long release obligation.

## Alternatives / chosen spike

- Longer timeout alone: not justified by clear torque observed only after disengagement; does not remove needless pulse or measured-clearance obligation. Rejected.
- Global pitch smoothing/reference changes: touches actual grade following and urgent braking beyond the identified one-sample crossing. Rejected for this narrow spike.
- Chosen: qualify only a new, tiny, pitch-compensated braking edge while raw planner intent remains positive, coasting without propulsion during qualification. Stronger/negative-planner/existing braking remains immediate/unchanged. Keep measured clearance and1s fault deadline. Add protective detection of unexpected reported torque, stale/invalid/reversed feedback before enabling propulsion; never make a changed-command/old-response replay succeed by dropping its release obligation.

Exploratory bounds: net acceleration(-0.05,0)m/s², raw intent>+0.02m/s², active coordinated Navigator PID>=3m/s, previous brake false, fresh valid zero/<=4Nm torque and already qualified clearance. Qualify40ms continuous mild-negative demand, or admit sooner when unserved negative-command exposure reaches0.002m/s. Small positive crossings credit exposure rather than resetting it. Any stronger/raw-nonpositive braking, unknown clearance/feedback, invalid pitch/context, stop/creep or owner change bypasses/reset qualification. Clock gap>40ms aborts pending qualification into baseline braking;100ms clock/pose guards remain unchanged. Delivery is discrete:40focused cases verify actual admission latency<=80ms with healthy<=40ms callbacks and withheld negative-command exposure<0.002m/s in the tested sustained cases. This is a command bound, not physical speed/trajectory proof.

Prototype lives in report-local modules and an explicitly transformed in-memory copy of the existing child controller. Test failing production behavior first, then candidate. Never patch installed or paired production source during this spike.

## Proof and limits

Actual controller output, command-phase/native safety checks, frozen observed-feedback replay, model/response stress, default-off/stop/non-ACC exact parity and full historical corpus. Separate original-command observer, changed-command/old-response counterfactual and generic modeled response. Recorded torque after suppressed commands cannot establish actual physical candidate response. A retained observed-feedback fault is expected if measured torque does not clear; zero faults is not permission to weaken the guard.
