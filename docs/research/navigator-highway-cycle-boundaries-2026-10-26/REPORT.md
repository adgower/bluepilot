<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Highway pulsing boundary investigation — 2026-10-26

Local analysis of the integrated pair: parent 2ca969e45afee229d7ec5c03c8768e137410c8d1 / child bcd706d02fd6b8159b1eadcb6b2a56b504f69567. Neither paired source nor the Comma was changed.

## Finding

The remaining cycling is a mode-selection/control interaction, distinct from the below-6.7-mph integral guard. In the predeclared 15-second 62–64 mph regression, all 20 brake transitions have a positive consumed planner target (approximately +0.018 to +0.198 m/s²). Raw requests are positive too. The negative grade term plus changing integral shifts the compensated request repeatedly across admission/release boundaries. The precharge allocator is already budget-locked for 739/751 callbacks. Its fallback is the nominal policy, so it cannot sustain a coasting solution.

This explains the software command sequence, not the complete physical dynamics. Positive planner acceleration does not by itself mean braking is wrong on a descent: gravity, engine drag and delayed actuator response still matter. Holding brakes on longer or turning grade compensation off cannot be declared a fix from these observations.

## Cross-speed evidence

Full chronological trace analyzed: 8 previously inspected routes / 162 segments, 4,994.3 seconds of active, pedal-free, non-fault adjacent callbacks across the bands below. These are command transitions in frozen-response replay, not measured hydraulic brake cycles. Engagement boundaries, faulted samples, speed-band crossings and gaps >=100ms are excluded from transition counts.

| Speed | Active seconds | Brake transitions | Nonnegative planner target at transition | Positive raw request at transition |
|---|---:|---:|---:|---:|
| 0–20 mph | 1,043.4 | 157 | 125 | 109 |
| 20–40 mph | 1,269.9 | 235 | 147 | 172 |
| 40–60 mph | 1,628.6 | 390 | 278 | 333 |
| 60–70 mph | 1,025.5 | 328 | 244 | 290 |
| 70–86 mph | 27.0 | 0 | 0 | 0 |

Zero transitions in only 27 seconds above 70 mph is inadequate coverage, not evidence that 75–85 mph is resolved. Mixed routes and speed exposures do not support a causal rate comparison between bands.

## Lead context recovered from existing caches

Hash-verified cached radarState was joined backward in time at each transition (valid message, age <=150ms, actual leadOne present field). No future samples or missing-data-as-no-lead substitution. Of 1,110 transitions, 416 have a fresh lead, 320 fresh no-lead, and 374 lack sufficient context. The 374 cannot be classified safely. The planner hasLead boolean is retained separately and is not a substitute for fresh range/relative speed.

All 20 predeclared downhill transitions have a fresh lead. Recorded range spans 74.48–100.86m and relative velocity -1.3125 to +2.0625m/s. These values establish usable following context; they do not establish that withholding brakes would preserve the gap. Existing data is sufficient for the next local software experiment; a new drive is not required for that step.

## Next design constraint

Treat coast/engine/brake selection and producer integral recovery as one authority contract. A candidate must distinguish desired net acceleration from achievable coast acceleration; use received actuator/grade/lead context; and return truthful limited feedback. A switch reduction alone is insufficient: compare tracking, mode residence, clearance, subsequent integral history, strong-deceleration response and fault timing over the entire sequence. Do not extend the finite precharge budget, suppress weak brakes indefinitely, infer physical clearance from a forecast, or revive rejected point-forecast/post-ramp holds.

The archived point-forecast coast experiment already failed coupled replay, while broad integral freezing added faults. Consequently this task stops at the verified boundary diagnosis rather than adding another isolated threshold. No new runtime fix or physical comfort improvement is claimed.

## Reproduction and artifacts

Run `analyze.py` followed by `join_leads.py` using the paired checkout's Python. Inputs reference the completed integrated replay and SHA-verified private caches. `speed-summary.json`, `boundary-attribution.json`, `downhill-transitions.json`, `all-transitions.json`, and `lead-context.json` retain the analysis. All are local; source-rich raw data remains private. Preserve 1.20/0.97. No push, device connection, activation, setting change or CAN transmission occurred.

## Proposed next research design

The owner selected coast selection plus integral recovery while retaining the planner. [Proposed design](../../superpowers/specs/2026-10-26-coordinated-coast-integral-design.md) is drafted and independently reviewed with no unresolved planning questions. Stage A must establish causal coast authority and calibrated support before a runtime policy is attempted. Baseline/consumer-only/integral-only/coordinated ablations are required. Design approval and implementation remain pending; paired runtime and device unchanged.
