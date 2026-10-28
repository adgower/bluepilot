<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local highway coast/brake investigation and prototype

User authorized offline diagnosis, a prototype and full replay; no branch integration or device action. Preserve installed pair 1dbbc0189/beb10c25, lateral 1.20/0.97, real brake-clearance feedback and urgent/strong braking.

1. Extract exact atomic planner/state/PID and received torque from all 19 segments of the new moving drive. Replay current installed controller at recorded producer/consumer clocks, logging actual refreshed consumer pitch, net allocation demand, integral, release state and allocator state.
2. Locate first brake transitions in the three reported windows. Test one causal hypothesis against the current implementation; do not infer a grade trigger from producer pitch alone.
3. Prototype separately under this research directory. Evaluate fewer brake transitions against braking exposure, negative-demand area, strong braking, ownership, invalid inputs and physical-clearance constraints. Rejected variants remain identified as rejected.
4. Replay the complete existing 197-segment/12-route corpus plus the new 19-segment drive, then native safety replay with original RX, timers and non-ACC TX. Incomplete active-input routes remain diagnostic-only. Do not use baseline output as a candidate runtime oracle.
5. Document improvements, regressions and remaining blockers. Replay cannot predict changed vehicle response, RPM, following safety or subjective comfort.

Approaches: planner filtering risks hiding real lead demand; wholesale grade-disable contradicts known reference calibration; trace-first allocation/integral coordination targets the observed brake switching without changing planner intent. The latter is the authorized throwaway local prototype scope. Keeping or installing it requires a subsequent decision.
