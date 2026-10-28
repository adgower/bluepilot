<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Lincoln Navigator: minimal upstream contribution plan

October 19, 2026. Planning and research only; no device access, firmware queries, CAN transmission, branch switch, push, or public PR performed.

## Recommendation

Aim for **automatic identification of the owner's exact 2023 Lincoln Navigator, with the existing upstream Ford control implementation and stock ACC**, provided compatibility checks support that claim. Prefer a distinct Navigator platform entry within the Ford implementation when its geometry or behavior differs. Do not turn this into a proposal to merge the personal steering fork.

Start with the reported standard-wheelbase Reserve 4×4 configuration, confirming the actual vehicle and assistance package before documenting support. Navigator L, other years, different assistance packages, Alpha Long improvements, Angle strategy, pinion feedback, owner gains, MADS, Chestnut work and UI changes are separate scope.

This is a realistic upstream opportunity, not a promise of acceptance. Recognition in opendbc, operational vehicle support, comma's final validation, and inclusion in an openpilot release are separate milestones. An opendbc merge does not immediately update every installed openpilot branch.

## Research coverage and source quality

Reviewed the linked Codex chat's recent work and its retained roadmap/research reports; indexed the visible ChatGPT `openpilot` project's chat list; read relevant recent turns from **Find Navigator Mass**, **Compare Ford Safety Modes**, **Openpilot AutoSpeed Settings**, **Alpha Long Highway Issues**, **Explain Codex Request**, **Faithful Controller Porting**, and **Openpilot PR Difference Explained**. This is a targeted synthesis, not a claim to have read every historical turn or every chat. Prior assistant explanations are leads; original source, captures, and owner observations take precedence.

The local [evidence audit](navigator-upstream-local-evidence-2026-10-19.md) records file-level provenance and limitations. The existing [roadmap](../../NAVIGATOR_ROADMAP.md) remains the broader personal-fork roadmap. CodeGraph tools were not exposed, so no graph verification is claimed.

Current public opendbc master observed in the browser: `48c7f06c6f27c41e7169242acb03ef9775658deb`, dated October 17. Refresh before implementation. Its Ford `CarSpecs` has wheelbase and steering ratio, without the old mass field. Do not transplant historical mass-bearing snippets or change Expedition globally to fit Navigator.

## What we have, and what is missing

| Item | Evidence already available | Smallest useful next step |
|---|---|---|
| Vehicle identity | Owner's earlier message explicitly describes 2023 SWB Reserve 4×4; local reports agree | Confirm market, year, body length, drivetrain, assistance options and harness using the owner's build information; retain VIN privately |
| Firmware | Saved camera, EPS, ABS, radar and engine identifiers; EPS and radar overlap the original Expedition port | Extract exact raw `carFw` bytes, addresses/subaddresses, bus/request details and acquisition provenance from existing artifacts; do not recreate padding from prose |
| Automatic detection | Historical launch forces `FORD_EXPEDITION_MK4`; cache says `fingerprintSource=fixed` | Run the current upstream matcher offline on the original firmware set, then on the proposed Navigator entry; record exact/fuzzy/no-match/ambiguous results |
| Dimensions | Tape-measured wheelbase 3.1115 m; historical ratio 19.6 is secondary/community sourced | Confirm wheelbase and choose a defensible ratio using primary specs or relevant measured evidence; inherited defaults need explicit justification, not blind copying |
| Driving data | Extensive personal-fork recordings, replays, paired builds and parked checks | Pick a small complete, reviewable raw route set with source revisions and firmware; first check whether saved data already covers the needed observations |
| Stock lateral compatibility | Personal implementation has custom feedback and paired safety; raw-yaw/model discrepancy is documented | Replay stock upstream parsing/controller/safety against raw Navigator data, identify actual failures, then establish normal supervised stock-path behavior separately |
| Stock ACC | Owner reports OEM ACC was smooth; Alpha Long caused shaking | Validate stock ACC interaction/cancel/override for the proposed stock path; disclose Alpha Long limitation and discuss how to represent unsupported modes |
| Public review package | No isolated upstream submission branch prepared in this task | Build from fresh upstream only after the identity and compatibility decision; carry only the minimal model changes |

Cached display IDs, **not paste-ready firmware entries**: camera `RJ6T-14H102-BAH`, EPS `NL14-14D003-AE`, ABS `PL14-2D053-AB`, radar `ML3T-14D049-AL`, engine `PL7A-14C204-DE`. Padding and original ECU metadata matter. Saved cache contents are historical observations, not new ECU responses.

No initial need to buy FORScan hardware, obtain steering firmware disassembly, collect hundreds more segments, or complete the custom controller's tuning program. Those become relevant only if a concrete compatibility question cannot be answered from existing data and normal port validation.

## Precedents that actually fit

| Merged PR | What it demonstrates | What to copy |
|---|---|---|
| [Expedition Mk4 #2368](https://github.com/commaai/opendbc/pull/2368), June 6, 2025 | 20 additions, four files; firmware, platform/specs, route registration and torque data; reused the Ford implementation | Tiny model-specific diff, actual validation routes, existing infrastructure |
| [2021 F-150 firmware #3183](https://github.com/commaai/opendbc/pull/3183), March 27, 2026 | Four additions in one file; validation route included | Fingerprint-only change stays fingerprint-only when the model already exists |
| [2018 Lexus LS 500 #3010](https://github.com/commaai/opendbc/pull/3010), January 5, 2026 | First car port, 27 additions/four files; exact year and incompatible package excluded; stock/openpilot routes and parameter sources; merged by Adeeb | Honest configuration boundary, useful sources, reviewable implementation. Adeeb's [comment](https://github.com/commaai/opendbc/pull/3010#issuecomment-3711573815): “Very clean PR, thanks!” |

These are selected relevant examples, not an exhaustive ranking of every merged PR. Their historical line counts are examples, not a line budget or permission to omit today's checks.

Current [Ford values](https://github.com/commaai/opendbc/blob/master/opendbc/car/ford/values.py) already document **Lincoln Aviator inside the Explorer platform**. That answers the brand-sharing question directly: a Lincoln name does not require a new brand implementation. Lexus models likewise live under Toyota. A shared implementation and a distinct model/platform identity can coexist.

For Navigator, use this decision order:

1. If current upstream already has the exact model by implementation time, submit only genuinely missing firmware/docs.
2. If behavior and geometry can legitimately be shared, ask whether a docs alias is appropriate. An alias alone may display the Lincoln name in docs while runtime identity remains Expedition; that may not meet the owner's goal.
3. If dimensions or required behavior differ, favor a distinct Navigator platform using the existing Ford configuration/controller/DBC/safety machinery.
4. If firmware cannot distinguish two platforms needing different behavior, solve or explicitly block the ambiguity. Do not stuff Navigator replies into Expedition merely to make matching succeed, relax matching broadly, or invent CAN fingerprints as a shortcut.

## Work sequence and acceptance gates

### 1. Assemble one private evidence sheet from existing material

- [ ] Record exact vehicle configuration, harness, original route references and relevant source revisions.
- [ ] Recover original `CarParams`/`carFw` and raw route artifacts; retain exact firmware bytes and private vehicle association.
- [ ] Record what is forced, cached, stock, or modified for each selected route. A file hash and source revision are enough; do not create another general evidence framework.
- [ ] Separate direct owner observations from old assistant hypotheses. In particular, Alpha Long shaking is an owner report; its root cause is not proved by the chat explanation.

**Done when:** a reviewer can trace firmware and representative CAN data to this actual configuration, and we know what existing data can be reused.

### 2. Test identification and stock compatibility offline

- [ ] Use freshly verified upstream `fw_versions.py` and Ford query/matching configuration to evaluate the real firmware set without forcing a fingerprint. Preserve the pre-change result.
- [ ] Inspect collision candidates across supported Ford platforms, including shared EPS/radar replies. A model name is not disambiguation evidence.
- [ ] Add a temporary minimal Navigator entry locally to evaluate post-change matching; check exact and relevant fuzzy matching and unsupported variants. Use existing fingerprint tests; add a focused regression only for a real uncovered case.
- [ ] Run existing model replay on the selected raw routes against stock parsing/controller/safety. Check CAN validity, parsed pedals/cruise/steering/faults, safety-state agreement and generated-command acceptance. Replay of a fork recording cannot prove the stock commands would drive the car well.
- [ ] Check camera-bus packet lengths for `0x3d6` and `0x186` against the current [Ford interface's SecOC rejection](https://github.com/commaai/opendbc/blob/master/opendbc/car/ford/interface.py). Current code requires eight-byte messages there; a CAN-FD platform label alone does not establish compatibility.
- [ ] Assess the documented yaw/model discrepancy against the actual current upstream path. Do not assume a custom-feedback issue automatically breaks stock, or that stock is validated because the custom path passes.

**Decision:** if the standard Ford path passes credible compatibility screening, proceed with the small model port. If it needs controller or safety changes, stop calling it a fingerprint-only port. Bring the exact failure and a bounded reproducer to maintainers; propose a separate fix or discuss a non-actuating identification entry. A dashcam-only entry is not equivalent to working vehicle support and requires explicit scope agreement.

### 3. Ask one concrete scope question in the community

Once the evidence sheet and offline result exist, post in the Ford/car-porting discussion channel actually used by the community. Check channel rules; this research did not inspect Discord history or establish a specific channel's tagging convention.

Suggested first message, replacing brackets with actual results:

> I'm preparing a small opendbc port for my 2023 Lincoln Navigator [confirmed body/drivetrain/package]. It currently runs a fork with forced Expedition identification. I want to add native Navigator identification using the existing Ford implementation, retaining stock ACC, without bringing in my custom steering changes. I have the original firmware responses and [route/replay result]; [remaining limitation]. Would a separate Navigator platform be the right shape, and is there any additional evidence you'd want before I open the PR?

Do not say the firmware, replay or stock driving passed before it actually has. Share route identifiers only after deliberately choosing what to make available.

Start in the relevant public thread rather than sending an unsolicited DM. If Adeeb is participating, answers the question, or is the relevant reviewer, one targeted mention with the concrete question is reasonable. Ford contributors/reviewers from the relevant PRs may be better first contacts. Avoid repeated pings, multiple parallel requests, appeals to effort spent, or arguments about whether someone likes AI. Respond to the technical constraint, thank the reviewer, and revise the same branch. A terse response is not evidence of personal dislike.

### 4. Gather only the missing vehicle proof

The current [porting checklist](https://github.com/commaai/opendbc/blob/master/docs/CAR_PORTING_CHECKLIST.md) is the acceptance reference; many shared-platform checks can reuse existing implementation, but we must show why they apply. It explicitly allows explaining checks that cannot be performed. Do not substitute a new enormous testing project.

- [ ] Repeated natural identification on separate cold starts without forced selection or cache masking the result. Two or three independent starts are a practical initial target, not an upstream-prescribed count.
- [ ] Verify stock-path vehicle state, cruise buttons, set speed/units, brake/gas, cancel and driver steering override, faults and power lifecycle. Prefer existing captures where adequate; stationary checks cover only stationary behavior.
- [ ] A representative route using the exact proposed implementation, stock safety and stock ACC, with ordinary turns/speeds and normal override/cancel observations. Use the applicable checklist to identify any additional mode/condition coverage; no arbitrary mileage target.
- [ ] Explicitly report Alpha Long as unvalidated/problematic. Confirm with maintainers whether it must be disabled for this platform or can be documented under the existing Alpha policy; do not silently expose it and advertise full support.
- [ ] Confirm no new dashboard faults or persistent DTCs associated with normal identification/use. Additional diagnostics or device changes require an explicit parked collection/backup plan when we reach that step.

Device installation is a separate later action: preserve the working paired source, settings/calibration and firmware, establish rollback, then use a deliberately selected matched test build. Do not reset learning, remove owner tuning, switch the live installation, or flash a Panda just to execute this research plan. No deliberate lane-edge, high-speed fault reproduction, emergency-braking target tests or unusual public-road maneuvers are needed; validate failure/AEB interactions through existing bench/replay methods.

### 5. Prepare a clean submission branch

Use the existing GitHub fork if it is still `adgower/opendbc`; a new fork is unnecessary for every contribution. Create a separate clean managed worktree or checkout from freshly fetched **commaai/opendbc master**. Do not use the stale top-level fork checkout or cherry-pick the experimental integration wholesale. Current upstream targets `master`, despite the common shorthand “main repo.”

Suggested branch: `codex/lincoln-navigator-2023`.

Expected diff, conditional on current upstream conventions:

| File | Intended change |
|---|---|
| `opendbc/car/ford/values.py` | Navigator platform/docs, verified geometry, correct inherited CAN-FD configuration |
| `opendbc/car/ford/fingerprints.py` | Observed firmware bytes under the correct identity |
| `opendbc/car/tests/routes.py` | Existing route registration for the verified configuration |
| `opendbc/car/torque_data/substitute.toml` or `override.toml` | Only the entry actually required by current platform tests/conventions; confirm applicability, do not copy historical torque numbers blindly |
| Existing Ford fingerprint tests | Only if a distinct matching/collision case is not already covered |

No new controller, safety mode, general matcher, configuration framework, dependency, mass migration, research dump or unrelated cleanup by default. If a real correctness issue requires another file, justify it rather than meeting an artificial four-file limit. New enum/platform names should follow repository convention; the provisional label does not pre-decide a model-generation/year range.

- [ ] Inspect the exact upstream base SHA and working tree before editing.
- [ ] Demonstrate the original no-match/incorrect-match in existing infrastructure, then the corrected result.
- [ ] Run applicable fingerprint, model/route and Ford safety tests; run the current `./test.sh`, which upstream documents as its combined checks. Record exact commands/revisions and skips or environmental failures.
- [ ] Check related Ford platforms for matching regressions; inspect the complete diff for accidental research/device identifiers or secrets.
- [ ] Commit a small coherent change under the owner's configured author identity, then push only this branch to the owner's fork when the candidate is ready. Confirm remote branch SHA equals tested local HEAD.

### 6. Owner opens the upstream PR manually

1. Open the owner's fork on GitHub and select the submission branch.
2. Choose **Contribute → Open pull request**, or use Compare across forks.
3. Verify base repository `commaai/opendbc`, base branch `master`, head repository the owner's fork, and compare branch `codex/lincoln-navigator-2023`.
4. Inspect **Files changed**. It must contain only the intended model change, not the personal fork's history/features.
5. Use a factual title such as **Ford: add 2023 Lincoln Navigator**. Follow the live PR template, including Validation/Route fields.
6. Open as draft if evidence or checks remain. Mark ready only after the described behavior is verified and current-head checks pass. Fork CI success does not replace upstream CI.
7. Reply briefly to review, make requested changes on the same branch, rerun affected checks, and push. GitHub updates the PR automatically; do not open a new PR for each revision. Avoid rewriting a reviewed branch unless requested or needed and coordinated.
8. After merge, verify the merged commit and when the openpilot branch/release you intend to install actually incorporates it. Keep the known-working installation until that path is checked.

Provisional body — fill only after verification:

> Adds native identification for the 2023 Lincoln Navigator [verified configuration] using the existing Ford CAN-FD implementation.
>
> Adds observed firmware versions, [verified parameter differences], and a test route. [Exact control-mode boundary and known limitation, including Alpha Long disposition.] No changes to the shared Ford controller or safety limits. [Use that last sentence only if true.]
>
> Validation: [route/device reference chosen for sharing], [unforced startup observations], [exact tests and result].

## Keeping the contribution credible and small

The [contribution guide](https://github.com/commaai/openpilot/blob/master/docs/CONTRIBUTING.md), linked from opendbc, prioritizes project value versus review cost, a singular goal, relevant changed lines, verification and passing CI. It discourages 500+ line PRs and asks for before/after plots when tuning is changed. This is a reason to avoid bundling tuning into identification, not a reason to hide limitations or omit meaningful tests.

[Ponytail](https://github.com/DietrichGebert/ponytail) is relevant as a reuse/minimal-scope philosophy, not as a vehicle-support implementation or evidence standard. Its own README preserves validation rather than recommending untested brevity. No plugin installation is needed.

Keep the large internal research privately available and cite only the facts a reviewer needs. Use existing fixtures and tests; do not manufacture dozens of synthetic tests to inflate a validation count. Personally read every changed line and be able to explain it. Disclose AI assistance honestly when asked or required; do not use polished generated prose to imply work or understanding that does not exist. A handful of reproducible checks against actual vehicle evidence is more persuasive than a huge unrelated test total.

Public examples of Adeeb's AI-related feedback are recorded in the [evidence audit addendum](navigator-upstream-local-evidence-2026-10-19.md). He rejected [#38250](https://github.com/commaai/openpilot/pull/38250#issuecomment-4871218169) and [#38255](https://github.com/commaai/openpilot/pull/38255#issuecomment-4871232700) as indistinguishable from an LLM, without explaining the decisive feature. He also merged [#38467](https://github.com/commaai/openpilot/pull/38467), which disclosed Claude assistance and verified a concrete documentation issue. These are evidence of specific review decisions, not a reliable psychological profile or a ban on tests.

## Immediate next deliverable

Produce **one private firmware/route compatibility sheet and an offline natural-matching result**, then decide whether the existing Ford path can support this model with a tiny platform entry. This resolves the critical uncertainty without changing the Comma. Only after that should we prepare the submission branch and fill in a final PR body.
