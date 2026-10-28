<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Throwaway local allocation experiment

Question: can distinct coast/precharge/brake outputs reduce weak brake/propulsion switching while retaining the installed urgent-braking and release/restart behavior?

The user authorized this spike and saved-drive replay. No integration, publication, device contact or activation. Keep 1.20/0.97 and paired sources untouched.

Approaches considered: copying BluePilot wholesale changes lead/planner behavior and unresolved pitch assumptions; changing pitch calibration alone obscures allocation behavior. This spike instead adds a narrow allocation layer after a shadow copy of the installed brake/release decisions. Original brake acceleration, creep, rate limits and all non-ACC packets remain unchanged. No fixed pitch correction.

Output states are inactive, drive, brake-free slowing/coast, precharge and brake. Brake forces propulsion inactive through the existing Handoff. Precharge can coexist with valid propulsion, as observed in OEM commands. Coast is a command category, not a guarantee of zero engine torque or fuel cut.

Only a NEW, weak, pitch-adjusted brake entry (-0.12 < net < 0 m/s²), with positive planner intent >0.02 m/s², PID phase, valid pitch and speed >=3m/s can become precharge first. Existing actual braking, negative planner demand, strong net braking, stopping/restart/low speed, invalid data and timing gaps use installed brake decisions. Qualification is bounded by 120ms and signed net-demand debt 0.006m/s (retained across short crossings). Precharge is not counted as harmless: it may create physical brake torque and its cycling is measured separately.

Preserve independent shadow baseline brake/release state so allocation cannot erase the baseline brake history. Preserve actual allocator braking while that shadow remains latched. Do not repeatedly reset exposure when net briefly crosses zero.

Verification: test-first urgency/budget/timing/override contracts; actual Alpha send-slot controller replay with split-bit packing; saved OEM state/packing replay and separately labeled OEM-demand-surrogate diagnostic; native ACC hook replay with real recorded RX/timers. Frozen inputs cannot predict physical response, following distance, comfort or fuel economy. OEM runs do not contain Alpha planner requests, so surrogate replay is not closed-loop comparison. No road readiness claim.
