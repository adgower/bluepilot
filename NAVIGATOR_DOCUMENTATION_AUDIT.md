<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator documentation audit — October 28, 2026

The durable record is extensive, but the roadmap and feature inventory had become long chronological journals without a single tuning/workflow manual. This consolidation adds [the main guide](NAVIGATOR_TUNING_GUIDE.md) and [the complete document catalog](docs/research/NAVIGATOR_RESEARCH_INDEX.md), with entry links from README, roadmap and feature inventory.

## Coverage provided

| Topic | Primary durable record |
|---|---|
| Goals, priorities, progress and blocked work | [Roadmap](NAVIGATOR_ROADMAP.md) |
| Runtime/child/safety/UI feature history and commits | [Feature inventory](docs/research/navigator-branch-feature-list.md) |
| Practical tuning loop, evidence gates, lessons and rejected approaches | [Tuning/development guide](NAVIGATOR_TUNING_GUIDE.md) |
| Historical settings, geometry, forced identity and migration reasoning | [October 14 settings snapshot](docs/research/navigator-migration-settings-2026-10-14.md), interpreted with later dated receipts |
| Acquisition, hash checks, driver context, exact installed pair and newest drives | [October 28 drive review](docs/research/navigator-returned-drive-review-2026-10-28/REPORT.md) |
| Grade/integral attribution and rejected prototype | [October 28 post-clear study](docs/research/navigator-postclear-rebraking-2026-10-28/REPORT.md) |
| Controlled longitudinal tests and clearance observations | [Maneuver recovery](docs/research/navigator-evidence-recovery-2026-10-27/REPORT.md), [release validation](docs/research/navigator-maneuver-release-validation-2026-10-28/REPORT.md) |
| Lateral calibration, roll, speed bands, transitions, unwind and uncertainty | Guide plus dated studies indexed in the catalog |
| OS/model/Chestnut staging, activation, recovery and parked checks | Dated operational studies in the catalog; stage/activation receipts are distinct from road proof |
| MADS, Auto Start/Stop, parking assist, upstream recognition and fork ideas | Guide’s research links and dated roadmap/catalog entries |
| Full file inventory and content hashes at consolidation | [Coverage manifest](docs/navigator-reference/PRIVATE_ARTIFACTS.md) |

The catalog enumerates all Markdown currently present in `docs/research` and `docs/superpowers`, including nested reports/designs/plans and rejected work. It links the containing studies whose associated JSON receipts, source/input manifests, logs, tests and scripts carry the numerical details. It does not execute or certify those scripts. Markdown count is verified by the generator and recorded in the coverage manifest; later refreshes can legitimately change it.

## Important limits

- This is **not a verbatim archive of every chat message**. An unrecorded conversation or experiment is not made recoverable merely by indexing files. Human observations remain distinct from assistant hypotheses and automated event matches.
- The historical settings inventory explicitly lacks an original full pre-customization baseline. It cannot identify every setting ever changed. A fresh private full backup is still part of a migration, with selected nonsecret differences documented separately.
- Older “current,” Alpha-OFF, AGNOS 19.7 and branch-stage labels are dated historical snapshots. They are retained without rewriting frozen evidence. The main guide points to the latest verified source/settings and identifies historical conflicts.
- Accepted, installed, parked-checked and road-improved are different statuses. A verification receipt can pass while declaring the candidate rejected. Local/replay/native/build results are not physical comfort, braking, fuel-use or high-speed validation.
- Private recordings, identity mappings, full parameter backups and caches are not part of a public Git repository. Receipts record provenance; reproduction on another computer also requires the authorized private inputs and compatible runtime.
- The original consolidation was local. This separate `docs/navigator-reference` export is curated for GitHub, with private supporting artifacts omitted and source/published hashes distinguished.
- Public fork/PR/upstream claims in older research were checked at their stated date. This consolidation does not refresh external GitHub state.
- Longitudinal pulsing, RPM quality/shift behavior, sparse higher-speed evidence and validated causal response models remain engineering gaps, not solved documentation items.

## Verification and maintenance

The catalog generator checks document counts and all generated local links, and writes a dated path/hash inventory. The consolidation also validates local links in this audit and the guide, checks that all four entrypoints link back to the guide, and verifies the latest drive-review/rejected-prototype artifact hashes remain unchanged. These are documentation checks, not a fresh controller replay, build, device audit or physical test.

For each later iteration: retain the dated report and exact artifacts, mark the actual decision/status, update the roadmap and feature inventory, update the guide only when a reusable lesson/current baseline changes, and regenerate the catalog. Do not relabel historical passing evidence as proof for newer code or overwrite rejected variants to make the journal look clean.

## Public-export amendment

This copy is a sanitized reference document. The original consolidation checks described above are historical checks of the local source workspace, not byte-integrity proof for these transformed exports. Use `scripts/navigator-reference/verify_reference.py` and the export manifest for current published-file/link checks. Private backing data and many original operational scripts/receipts are intentionally excluded.
