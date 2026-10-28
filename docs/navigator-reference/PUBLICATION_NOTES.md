# Publication checks — October 28, 2026

The public reference export contains redacted documents, selected offline helpers, curated verification summaries and rebuild metadata. The [export manifest](export-manifest.json) binds final published bytes and records original source hashes separately. Original private evidence is not part of the branch.

Checks performed before publication:

- Original source contents for 658 selected documents/helpers/receipts remained unchanged in the owner's source workspace.
- Public file hashes and local links were validated; selected Python helpers compile.
- Explicit privacy-pattern checks report no remaining matches in curated files. Four synthetic negative checks confirm that the detector rejects vehicle IDs, private hosts, private chat references and owner home paths. These checks supplement curation, not a guarantee that arbitrary future exports are safe without review.
- Exact parent/opendbc commits and selected source hashes match the rebuild manifest. Both source branch tips were verified on GitHub before publication.
- All 14 preserved filter/adapter unit tests pass against the pinned source. An initial run from the reference repository root selected the inherited BluePilot opendbc package; the documented study-directory/PYTHONPATH invocation resolves that environment-selection error.
- No private recordings, trace datasets, models, binaries, full parameter backups, live SSH/acquisition/activation scripts or credentials are staged. No vehicle/device access occurred in this publication task.

This is documentation/helper verification only. It does not add a full controller replay, native sanitizer run, ARM/model build, installation, road trial or a new tuning success. The preserved grade-filter prototype remains rejected. A rebuild snapshot does not certify smooth longitudinal behavior or resolve the high-RPM and steering questions.

Use [verify_reference.py](../../scripts/navigator-reference/verify_reference.py) from the repository root to repeat the public checks. Its optional source argument reads a local pinned checkout; it never contacts the Comma.
