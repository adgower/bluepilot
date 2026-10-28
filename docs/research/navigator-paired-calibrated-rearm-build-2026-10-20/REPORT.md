<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Paired calibrated feedback, mid-speed correction and rearming integration

October20,2026. Integrated and committed locally on both `codex/navigator-tracking-release` branches:

- openpilot: `f750d756caf772c36c01a97be4c03501de8851db`
- opendbc: `de70d4f945b2bb1472e5207b92d2276137d8c5a1`

The parent pins the child; both checkouts are clean. Starting pair was `0171b897289be53fd62f330935c55825b86c3c3a` / `4167433e5c575f620a9dedf8144a0bc7cba14291`. **No push or installation.** Passive device access was limited to the separately documented new-drive download.

## Integration

The child adds `CalibratedMidUnwind`, retaining the installed `SustainedErrorUnwind` and older modules as independent references. The parent selects the new class through the existing Expedition/pinion/low-speed/tracking/roll/high-speed prerequisites. No new parameter, default or producer. The combined accepted policy includes consistent calibrated feedback, bounded25–30mph correction, once-faded60–70mph unwind feedback and resolution-aware one-second quiet rearming.

Owner **1.20/0.97**, geometry, native pinion/shadow/deviation/range/slew limits, parameter registry and producer/card/motion sources remain unchanged by hash. The420-row anonymous26mph rearming fixture contains only the fields consumed by its regression test; no raw route identifiers or GNSS.

## Checks

| Check | Result |
| --- | --- |
| Factory integration regression | Expected1failure/11passes before selector change; final12passes |
| Focused integrated tests |103passed |
| Full parent suite |1,018passed,343subtests;86skipped,1expected failure |
| Full opendbc suite |4,203passed,24,673subtests;1,690skipped |
| Configured minimal/development/Panda Mac builds |All pass; repeated at committed heads |
| Integrated transitions |714cases,228,480frames; range/slew/exposure and settling pass |
| Integrated active-abort checks |128cases pass; relative extra command tail<=0.10s |
| Actual factory vs frozen prototype |70,560returned-command updates identical, including boundaries, faults and noisy rearm histories |
| Class/helper AST equivalence |Exact after exported/private helper names and explicit default zip(strict=False); formatting/import/docstring normalization |
| Scoped Ruff/format/whitespace |Pass |
| Independent review |No material findings; independently103tests passed; fixture retained values verified |

The accepted46recording/766segment/4,432,831update-per-variant generated-controller replay is carried through verified source and actual-factory equivalence. That replay had **zero additional native rejects**, two shared inactive/not-allowed0x83 rejects, default-off whole-generated-stream parity and protected30–60mph/>=75mph parity. A fresh integrated766segment replay was **not** run here. New recordings downloaded in this task are observational evidence and were not added to that frozen acceptance corpus.

Initial test collection without paired PYTHONPATH and the sandbox-limited parent-suite attempt are excluded from passing results. Correct paired environment and temporary IPC/log permissions produced the successful full run. Source behavior stayed unchanged through formatting and fixture trimming.

These are configured **incremental Mac builds** and local tests, not clean-room builds, ARM/AGNOS boot, physical CAN delivery, closed-loop stability or road validation. The native child suite uses the preserved unsanitized Mac debug library; no UBSan claim. Source/test/build receipts are in[final verification](../../navigator-reference/PRIVATE_ARTIFACTS.md),[build results](../../navigator-reference/PRIVATE_ARTIFACTS.md),[committed build results](../../navigator-reference/PRIVATE_ARTIFACTS.md),[equivalence](../../navigator-reference/PRIVATE_ARTIFACTS.md) and[review](REVIEW.md).

## New drive review and next gate

[Two recordings/18segments reviewed](../navigator-post-rearm-build-drives-2026-10-20/REPORT.md) still use the earlier installed pair. They retain a24mph shortfall and65–70mph unwind excess, add almost no steady35–50mph evidence, no clean meaningful15mph demand and no>=75mph coverage. These drives cannot demonstrate benefit from the newly integrated code.

Local integration/build work is complete. Publication and activation require the separate authorized push, backup, device staging/build and parked acceptance sequence. No device settings or firmware changes were made; no physical improvement claimed.

Subsequent authorized publication/device activation is recorded in the[installation report](../navigator-calibrated-rearm-installation-2026-10-20/REPORT.md); the local-only statements above describe that completed build stage.
