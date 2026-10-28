# Public reference export

This branch preserves the recorded workflow and research narrative while keeping private evidence separate. It is documentation and offline research support, not a deployment branch.

## Included

- Curated Markdown research, design and plan documents, guide, roadmap and feature inventory.
- Selected scalar outcomes from 73 historical verification receipts, clearly named `PUBLIC_VERIFICATION.json`.
- Selected offline decode/analysis and rejected-filter regression helpers. These contain no SSH/ECU/install/activation workflow. Rejected prototypes retain their rejected status.
- A generic curation tool, a public-reference validator, a CAN decode field schema and exact paired source/rebuild pins.
- `export-manifest.json`: original source-file hashes, exported-file hashes and transformation counts. A source hash is a provenance reference, not published raw data or a claim that redacted exports match original bytes.

## Private or intentionally excluded

[Private artifacts policy](PRIVATE_ARTIFACTS.md) lists what remains in the owner's separate storage. Historical supporting-artifact links point there rather than to absent raw data. Exact device addresses, user-home/cache paths, wall-clock times, vehicle identifiers and private chat references were redacted. Dates of studies and Git source revisions remain for history.

Generated local data/manifests/logs are ignored under `docs/research`; the validator rejects adding them outside the curated allowlist. Keep actual recordings and full parameter backups outside this repository. Do not load untrusted pickle/cached inputs into the offline helpers.

## Offline helpers

Set `OPENPILOT_ROOT` to a new checkout of the pinned parent, `BLUEPILOT_ROOT` to this reference checkout, and `NAVIGATOR_PRIVATE_CACHE` to an owner-controlled directory outside both repositories. Use the pinned source's compatible Python environment and dependencies. These variables do not connect to or modify a device.

The preserved study helpers expect the study-specific private acquisition/input manifests and caches described by their source reports. Those manifests must be rebuilt or restored privately; they are not supplied here. The scripts are selected reference implementations, not a promise that every historical replay runs on a clean machine without its private inputs. `protocol-fields.json` contains decode field names only, not a transmit utility.

Run the public documentation check without any vehicle or private data:

```sh
python3 scripts/navigator-reference/verify_reference.py
```

With a local parent source checkout, additionally check source pins:

```sh
python3 scripts/navigator-reference/verify_reference.py --openpilot-root /path/to/openpilot
```

`curate_reference.py` reproduces the initial redacted document/helper export from an owner's local evidence workspace into an isolated Git worktree; it never accesses the Comma. The public wrappers, rebuild manifest and export manifest are then reviewed/finalized before publication. Re-running curation overwrites the export and requires revalidation; do not treat it as an unattended sync.

Run the rejected-filter helper contracts from the study directory so the inherited BluePilot checkout does not shadow the pinned opendbc package:

```sh
cd docs/research/navigator-postclear-rebraking-2026-10-28
PYTHONPATH="$OPENPILOT_ROOT/opendbc_repo:$OPENPILOT_ROOT" "$OPENPILOT_ROOT/.venv/bin/python" -m unittest discover -s . -p 'test_*.py' -v
```

[Publication checks and limitations](PUBLICATION_NOTES.md).
