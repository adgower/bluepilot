<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Offline health and disengagement review

All 34 acquired completed segments have clean initData: session01 has ten segments on old `5b301a944f40b6d3d4a490e2a2f30cbeab3a8d45`; session02 has five and session03 nineteen on `1dbbc01892616c4b1a5c7c841d132f724ea5132c`. Session01 and session02 have no longActive samples or engagements. Only session03 supplies new-code active-road evidence. This review does not establish that every older failure is repaired.

No recorded Navigator fault flag, controlsMismatch onroad event, or controlsMismatch alert occurs in any session. Session03 has 109,938 populated Navigator feedback samples. Its noninactive reasons include actual_brake, no_release_pending, wait_observed_clear, observed_clear, override_pending_release and installed_stop_creep; none is a fault transition. No release-timeout fault is present to diagnose in this drive.

Session03 has two enabled-to-disabled transitions, both associated with a recorded driver brake input. These input associations do not establish driver intent. Relative times below use session03 first monotonic timestamp 180751.464670928 seconds. Local clock labels use the median valid wall-minus-monotonic offset; its full spread is 4.86ms, so millisecond labels should not imply finer clock accuracy.

| Observation | First transition | Second transition |
|---|---:|---:|
| brakePressed rises | +558.003839s, 54.28mph | +1063.992339s, 25.74mph |
| carControl.enabled becomes false | +558.009827s | +1064.005170s |
| local time of disabled command | <private clock time> CDT | <private clock time> CDT |
| Panda controlsAllowed first false | +558.021815s | +1064.020212s |
| disable alert | pedalPressed/userDisable | pedalPressed/userDisable |

Gas input is false at both transitions. Steering input is present around both. Panda controlsAllowed was true just before each brake input and becomes false after the disabled command. These are not controlsMismatch events. Raw CAN rejection ordering requires joining the separate CAN report on absolute monotonic timestamps; these sampled fields alone do not identify the rejected message.

Panda safetyRxInvalid has zero positive increments and no resets in all three sessions. Positive safetyTxBlocked increments are 13, 15 and 14 respectively; these are differences of cumulative counters, not retained counter totals. Session03's increments are +6 at startup (+8.912697s), +1 each during two gas-override transitions (+71.619751s and +75.520611s), +2 at +558.021815s, +2 at +558.122806s, and +2 at +1064.020212s. The latter increments align with brake-associated disables, not an independently observed safety mismatch. No Panda heartbeatLost, nmiReset, hardfaultReset, safetyRxChecksInvalid, or nonempty faults row occurs in the extracted Panda stream.

All 260 session03 steerFaultTemporary rows occur while disabled: startup +2.716..5.373s and end +1108.240..1108.280s. All 58 CAN-invalid carState rows occur disabled at startup +2.716..3.404s. No invalid extracted control, carState, model-derived, radar or other retained stream message occurs while carControl.enabled is true. This does not classify the separate Chestnut supplyFault field, which is outside the retained health extraction.

Tracked streams have no gap over one second. Session03 maximum modelV2 interval is 73.0ms, carControl 33.7ms, carState 149.2ms, Panda 109.8ms and deviceState 515.4ms. These observations do not suggest a broad logging/model/control outage coincident with the two disables. Startup/end invalid messages are retained in the evidence, rather than erased from overall counts.

Session03 recorded CPU maximum 67.6 C, GPU 59.4 C, memory 58.4 C, PMIC 51.17 C; Panda supply range 10.758–13.398V over the full session. Free space reaches 9.934%, and memory use reaches 57%. Full-session voltage minima include startup and cannot alone diagnose a moving-drive supply problem. powerDrawW is uniformly zero in this schema and should not be interpreted as measured zero consumption.

Inspectable support: `health-analysis.json` gives exact monotonic/local takeover samples, engagement edges, counters and feedback reason counts; `fault-health-streams.json` gives every segment initData provenance, stream intervals, invalid counts and temperature/supply ranges. Private rows remain in the retained acquisition backup; no location or VIN is included here.

## Independent CAN join

`fault-can-join.json` independently joins each new blocked-TX increment to the latest nonfuture logged sendcan command and received-state observations. The raw lateral extraction starts 25.550115ms earlier than the health extraction; the join converts both to absolute monotonic time before comparing. Recorded rejection timestamps describe the rejection echo's arrival, not the instant the safety hook decided. Received messages sharing an event timestamp cannot be ordered within that event using these arrays.

At the two gas-associated single-count increments, the echoed rejection is address 390 (0x186), at raw-relative +71.607882s and +75.507499s. Latest preceding sendcan commands are 7.78ms and 6.23ms old, both enabled with brake/precharge requested; requested brake acceleration is -0.1100 and -1.0226m/s² respectively. Accelerator position is 2.5% in the same received event as each rejection. At the first rejection carState already reports gasPressed; at the second its latest preceding report is still false, illustrating the input/report timing boundary. Subsequent commands before the Panda counter observation are disabled with brake/precharge requests cleared. This supports a gas-input/command-boundary association, not a logged controlsMismatch or Navigator release fault.

At the two brake-associated disables, the echoed rejected messages include both active steering 982 (0x3d6, mode1) and longitudinal 390. Echoes arrive at health-relative +558.010839s and +1064.011894s. Latest preceding active sendcan batches are respectively 8.45ms and 10.98ms old. In both cases brakePressed is already true in the latest preceding carState, and latActive is already false in the latest preceding carControl. The last preceding Panda sample still says controlsAllowed=true but is 88.90ms/91.21ms old; the next Panda sample reports false and a +2 counter increment. Thus the logs do not establish that safety permission remained true at the rejection instant. The first brake disable also has two echoed 0x83 rejections on buses2/0 about21.40ms after the paired steering/longitudinal rejection, consistent with the following +2 counter increment. No field here supplies a per-message rejection reason.

These are narrow pedal/permission/queued-command boundary observations. They do not prove every rejection cause, do not imply a controlsMismatch event, and do not show that all older lateral or longitudinal faults are resolved. The one Chestnut supplyFault sample is raw-relative +0.175597s, at startup, with supplyVoltage10922mV and zero-initialized temperatures; it is not concurrent with either active-road disable.
