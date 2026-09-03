# BluePilot Portal Backend

The Portal provides local HTTP and WebSocket APIs for route browsing, video
streaming/export, parameter settings, and device health information.

> This checkout is the unpublished `codex/chestnut-personal-2` development
> integration rooted on SunnyPilot
> `e87dbbaba710bbfe7661d9ff064d46170cac9442`. Its host tests do not make the
> branch installable or drive-ready. The Sunny Chestnut model/provenance,
> device, and vehicle gates remain open.

## Runtime contract

The openpilot manager registers the process in
[`openpilot/system/manager/process_config.py`](../../openpilot/system/manager/process_config.py):

- process: `bp_portal`
- Python module: `bluepilot.backend.bp_portal`
- enable parameter: `EnableWebRoutesServer`
- route preprocessor: `bluepilot.backend.routes.preprocessor`, enabled only
  while the device is explicitly offroad

The repository uses SunnyPilot's nested platform layout. Core Params metadata
is read from `openpilot/common/params_keys.h`; BluePilot settings metadata is
read from the canonical `bluepilot/params/params.json` schema.

Portal route endpoints use the canonical `IsOffroad` parameter. A missing,
unknown, or failed road-state read is treated as onroad, so protected GET,
POST, and DELETE route operations fail closed. Parameter and device-status
endpoints retain their explicit onroad allowlist.

## Structure

```text
bluepilot/backend/
├── bp_portal.py          # HTTP endpoint dispatch and server entry point
├── config.py             # ports, paths, cache, and rate limits
├── core/                 # lifecycle, state, and process coordination
├── params/               # Params metadata, categories, backup, and restore
├── network/              # Wi-Fi and fail-closed road-state helpers
├── routes/               # scanning, metadata, and preprocessing
├── video/                # remux, stream, and export support
├── realtime/             # WebSocket broadcaster and log streaming
├── storage/              # route preservation
├── system/               # system metrics
└── handlers/             # focused endpoint helpers
```

## Development

Run the module from the repository root:

```bash
.venv/bin/python -m bluepilot.backend.bp_portal
```

Run the focused backend regressions without installing dependencies:

```bash
.venv/bin/python -m pytest -p no:cacheprovider -q \
  bluepilot/backend/tests/test_final_review_portal.py
```

The server defaults to HTTP port 8088 and WebSocket port 8089. Configuration
constants live in [`config.py`](config.py). Route mutation endpoints are for
offroad use only.

## Main APIs

- `GET /api/routes` — route inventory (offroad only)
- `GET /api/video/...` — route video (offroad only)
- `POST /api/preserve/...` — preservation state (offroad only)
- `DELETE /api/delete/...` — route deletion (offroad only)
- `GET /api/panels` and `GET /api/panels/bp_settings_panel` — current
  schema-backed Portal settings
- `GET /api/params/categories` — BluePilot/System parameter categories
- `GET /api/params/backup` and `POST /api/params/restore` — typed BACKUP
  parameter round trip
- `GET /api/system/device-info` — nested-checkout version information

Add endpoint tests alongside behavior changes. Use disposable Params roots and
safe mocks for process, filesystem, and device-only operations.
