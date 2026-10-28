<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Newly returned drives — October 28, 2026

**New drive evidence confirms continued longitudinal cycling, a likely match to the owner’s one high-RPM report, and a low-speed steering shortfall. No software or settings were changed.**

Downloaded 29 previously unarchived completed segments / 266,844,797 compressed bytes across 3 recording groups. Each file’s byte count and SHA256 match before/after acquisition. Original logs are retained in the private CommaBackups archive, whose contents were verified. No raw route identities or GNSS are published here.

All three groups record installed parent e05e42f43d2907a4f02915a924cfd95a46197e79 with clean startup provenance. Live paired child is 5097b993965b2b65ea3fcca7e3769cfa9403d49c. Alpha and longitudinal coordination are ON. Source/settings/protected files and service state match before/after the read-only retrieval; owner 1.20/0.97 remain preserved. The rejected grade-filter prototype was never installed. Older analyzer artifacts use cohort label `candidate` to mean this installed source, not that rejected local experiment.

## Recorded health and exposure

| Group | Local time | Segments | Maximum carState speed | Lateral active | Longitudinal active |
|---|---|---:|---:|---:|---:|
| returned-session-01 | <private clock time>–<private clock time> | 16 | 67.6 mph | 461.8 s | 455.0 s |
| returned-session-02 | <private clock time>–<private clock time> | 3 | 27.0 mph | 98.3 s | 87.9 s |
| returned-session-03 | <private clock time>–<private clock time> | 10 | 61.0 mph | 336.2 s | 315.7 s |

Zero recorded controlsMismatch alert episodes and zero longitudinal coordination fault episodes in these recordings. Recorded model frame-drop maximum is 0%. This is bounded saved-log health evidence, not a guarantee of future engagement. The Comma reported 90% disk usage / 8.9 GB available at retrieval; no cleanup/deletion was performed.

## Longitudinal pulsing remains

| Group | Qualified assisted/no-override exposure | Full-brake bit changes | Reversals under 0.6 s |
|---|---:|---:|---:|
| returned-session-01 | 397.1 s | 94 | 29 |
| returned-session-02 | 81.9 s | 16 | 3 |
| returned-session-03 | 300.0 s | 54 | 13 |

The counts are original outgoing CAN bit selections with matched producer/plan/feedback and no driver override, not a count of independent physical braking events. They confirm the software cycling remains under the unchanged install. Different route, grade and lead exposure prevents declaring improvement or worsening from whole-drive rates.

| Selected 15-second regression | Approximate local start | Speed range | Brake-bit changes |
|---|---|---:|---:|
| returned-session-01, highway | <private clock time> | 61.2–62.2 mph | 17 |
| returned-session-01, city | <private clock time> | 23.8–26.0 mph | 11 |
| returned-session-03, highway | <private clock time> | 56.6–59.2 mph | 5 |
| returned-session-03, city | <private clock time> | 23.6–33.9 mph | 9 |

Coasting labels are corrected in this new analysis: 400.31 s with brake/precharge requests clear is mostly valid engine requests, not inactive coast. Only 15.25 s also has the inactive propulsion sentinel; 6.87 s additionally has fresh reported actual/arbitrated brake torque <=4 Nm and brake/precharge status clear. These are descriptive command/received-signal states, not independently measured free-coast authority. The inherited analyzer’s `true_coast_s` label previously meant only absence of brake/precharge; prior frozen artifacts are left intact. New inactive-propulsion run fields are named explicitly, and command runs do not imply measured pressure clearance.

## High RPM and launches

The owner reports one high-RPM incident. One likely matching recorded episode is retained separately; the owner has not confirmed its exact time.

- <private clock time>, returned-session-01: decoded RPM peaks at 4362, remains above 3,200 for 4.26 s, and speed spans 16.6–23.8 mph. Alpha is active with no driver gas/brake; actual gear reports 1, target gear reports 1→2. Propulsion request spans 0.24–1.22 m/s²; no brake/precharge is commanded during the interval.

RPM QF remains 0, labeled Faulty by the current DBC, across the observed active samples. Thus the numerical RPM is unqualified; the owner report and recorded gear/command sequence strengthen this as a review target without resolving signal quality or proving why the shift was delayed. No transmission fault or new protocol fix is inferred.

Five stopped-to-moving launch observations were retained. Four remain qualified for a full 15-second observation and cross 6.7 mph in 2.24–3.03 s after first observed movement, and 10 mph in 3.06–4.48 s. One is censored after 1.4 s by invalid/override/ownership context and is not counted as a successful restart. These timings start after movement begins; they do not measure traffic-light or lead reaction delay, establish smoothness, or prove absence of a brief acceleration hesitation.

## Lateral review

All five-mph bands are retained in [speed-range evidence](../../navigator-reference/PRIVATE_ARTIFACTS.md), [lateral bands](../../navigator-reference/PRIVATE_ARTIFACTS.md) and the full longitudinal metrics. There is no new 70–85 mph exposure; these trips cannot establish stability there.

| Candidate review episode | Approximate local time | Evidence |
|---|---|---|
| Low-speed rising demand, 14.6–17.3 mph | <private clock time>–<private clock time> | 3.25 s; median body/request 53%, wheel-model/request 51%; driver steering input follows around <private clock time> |
| Steering input near 52 mph | <private clock time> | 2.8 s of clean pre-input data; median body/request about 117%; no nearby pedal/signal. Driver intent unknown. |
| Steering input near 53 mph | <private clock time> | Median clean pre-input body/request about 115%; brief unwind excess precedes it. Driver intent unknown. |

The low-speed shortfall has both body-yaw and wheel-model support. Its transmitted curvature-equivalent is already above the planner reference; this does not prove more global gain is appropriate. Ford’s angle/path mapping and the selected limits require separate diagnosis. The low-speed event is a specific regression candidate, not proof every sample in that band achieves only half the requested steering.

At 50–65 mph, pooled meaningful-demand samples show modest positive median tracking excess, with brief larger body-yaw excess during unwind. Body uncertainty is substantial; no window passes the existing stronger uncertainty-qualified coherent-excess screen. The 27 grouped driver-pressure/disengagement events are candidate takeovers for review, not 27 confirmed steering failures. Several coincide with pedals/signals or lack clean automatic context. No lane crossing or hazard avoidance is inferred without context/video.

## Outcome

These recordings add new city/highway cycling regressions, another owner-reported high-RPM case with a likely recorded match, and a low-speed steering shortfall. They do not evaluate the rejected local grade filter and do not prove a tuning improvement. No new tune, integration, installation, OS/firmware action, CAN transmission or settings change occurred.

[Acquisition verification](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Health scan](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Longitudinal metrics](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Lateral episodes](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Launch/RPM evidence](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Human context](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Final verification](PUBLIC_VERIFICATION.json)
