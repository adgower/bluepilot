<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local controller regression repairs — October 27, 2026

The timeout/weaker-braking regressions and the flagged steering transitions were addressed in isolated local prototypes. Neither prototype is installed or integrated into the paired branches. Owner 1.20/0.97 and the Comma remain unchanged by this work.

## Longitudinal: introduced regressions cleared

The failed broad engine-ramp freeze was removed. Bounded true coast now has an explicit local revision-3 feedback contract and logical clearance ownership. It retains fresh measured-torque checks and three distinct clear readings after coast ends, without asserting a physical brake command, granting observer clearance, resetting I or changing the ordinary release-timeout rule. Existing signed debt, strong-braking bypass and peer fallback remain protected.

The full 237-segment / 14-route candidate replay clears the prior failures:

- 685,504 consumer callbacks; no changed fault history, lost activity, weaker strong braking, added full-brake exposure or new gas/torque conflict.
- All 1,311,408 recomputed producer steps retain identical raw acceleration, integral, freeze decisions, PID phase and rolling reduction against the retained current-source coupled reference.
- All 627 changed ACC packets only clear the precharge request bit. Other bits, raw demand and propulsion remain unchanged.
- Native saved-traffic replay: 685,398 replacement ACC slots, zero added TX rejections or relay faults; 32 focused, transport, budget and clearance tests pass.

The corpus retains one 12-segment diagnostic-only route with incomplete active-prefix inputs; 225 segments have complete active atomic input coverage. Baseline artifacts were reused after hashes and current imported source were verified, not mislabelled as a fresh baseline execution. Physical vehicle response and exact hidden consumer drain order remain unreconstructed.

**This resolves the prototype's introduced timeout/braking failures, not the physical highway-pulsing problem.** The named highway windows retain their full-brake counts and gas-withdrawal timing. Whether the short true-coast intervals improve actual brake torque and comfort remains unproved. The revision-3 transport is a local experiment, not a production migration.

[Longitudinal repair report and verification](../navigator-signed-coast-repair-2026-10-27/REPORT.md)

## Steering: qualify extensions, preserve original fallback

The unconditional midrange extension was replaced with direction-specific body/wheel evidence admission. Entry requires independent fresh coherent evidence over elapsed time, stable requested direction and hysteresis. The dedicated admission history tolerates scheduling jitter within the existing motion-freshness horizon; original mapping and actuator timing limits remain unchanged. Existing qualification can continue through gradual target changes while current evidence and release thresholds hold. Invalid or unqualified extension uses the exact original mapping, including its 50–55 mph behavior.

The focused newest-drive replay removes all 18 previously flagged transition changes and retains useful correction in the first oversteer window. The second highlighted window receives only partial qualification; the repair is not presented as a complete oversteer cure. Protected higher-speed/default-off comparisons and full historical validation are recorded in the steering report.

[Steering repair report](../navigator-midrange-admission-repair-2026-10-27/REPORT.md)

## Scope and remaining work

No SSH, device changes, ECU queries, CAN transmission, branch integration, publication, OS or firmware work occurred. Source stays clean at parent `df788e02719c05595dab2f980e6fd9fb9e464006` / child `1d29e6e78abcbf5c6a80eb397d80b349c6cca960`.

Production work still requires deliberately porting the local transport and steering changes into the paired sources, integration/build checks and appropriate hardware validation before activation. Physical coasting, shifting, ride comfort and highway stability are not established by these frozen-response replays. High-RPM protocol identification remains a separate open investigation.

Only task-generated temporary caches were deduplicated or compressed to recover Mac workspace room; their contents remain hash-verifiable and all original drive recordings are retained.

## Completed steering validation

The final candidate clears the full **33-route / 658-segment** saved corpus: 3,814,069 controller updates and 152,312,756 received frames. All original manifests, source hashes and paired heads are verified. The 637 historical segments were freshly run; the same-candidate focused 21-segment result is reused with verified input and candidate hashes. Both recorded-context and separately labelled causal-calibration-fixture comparisons add zero native safety rejections. There are 2,464,642 native-tested TX frames per comparison variant; 12,197 pre-Ford-configuration generated frames are excluded, with initialization ticks disclosed in the detailed report.

All reference stream hashes match the prior full-corpus baseline. Default-off streams are identical; every band below 35 mph and at/above 55 mph has zero changed angle frames. All 18 previous adverse-screen slots now equal baseline, and the newest-drive adverse screen is zero/zero. There are 784 recorded-context and 1,200 causal-fixture reductions, no increases, with maximum 0.007-rad path-command change. These fixture counts are separate comparisons, not additive independent road exposure.

An independent rerun passes **123 synthetic checks**, including target-history, timing-jitter, exact original fallback, driver/fault/target abort and protected-speed checks. Some correction is retained near 42 mph; the later approximately 50 mph example remains only partly qualified. This resolves the tested transition regressions without proving full physical oversteer correction.

The next stage is deliberate paired-source integration and its build/integration checks. No source integration, installation or moving-vehicle validation is implied by these local results.
