from io import BytesIO
import json
from pathlib import Path
import signal
from types import SimpleNamespace

import pytest

from bluepilot.backend.network import utils as network_utils
from openpilot.common.params import Params


class StateParams:
  def __init__(self, state):
    self.state = state

  def get(self, key):
    assert key == "IsOffroad"
    if self.state == "error":
      raise OSError("params unavailable")
    if self.state == "missing":
      return None
    if self.state == "unknown":
      return b"unknown"
    return b"1" if self.state == "offroad" else b"0"

  def get_bool(self, key):
    if key == "EnableWebRoutesServer":
      return True
    raise OSError(f"unexpected bool key: {key}")


@pytest.mark.parametrize(
  ("state", "expected"),
  [("offroad", False), ("onroad", True), ("missing", True), ("unknown", True), ("error", True)],
)
def test_onroad_state_uses_is_offroad_and_fails_closed(monkeypatch, state, expected):
  monkeypatch.setattr(network_utils, "params", StateParams(state))
  assert network_utils.is_onroad() is expected


def portal_request(monkeypatch, params, method, path, payload=None):
  from bluepilot.backend import bp_portal

  monkeypatch.setattr(bp_portal, "params", params)
  handler = bp_portal.WebRoutesHandler.__new__(bp_portal.WebRoutesHandler)
  body = json.dumps(payload).encode() if payload is not None else b""
  handler.path = path
  handler.headers = {"Content-Length": str(len(body)), "Content-Type": "application/json"}
  handler.rfile = BytesIO(body)
  handler.client_address = ("127.0.0.1", 0)
  handler._enforce_rate_limit = lambda *args, **kwargs: True
  response = {}

  def send_json(data, status=200):
    response["status"] = status
    response["data"] = data

  handler.send_json_response = send_json
  getattr(handler, f"do_{method}")()
  return response["status"], response["data"]


@pytest.mark.parametrize("state", ["offroad", "onroad", "missing", "unknown", "error"])
def test_route_endpoints_block_every_protected_verb_when_not_known_offroad(monkeypatch, state):
  state_params = StateParams(state)
  monkeypatch.setattr(network_utils, "params", state_params)

  statuses = {
    "GET": portal_request(monkeypatch, state_params, "GET", "/api/routes")[0],
    "POST": portal_request(monkeypatch, state_params, "POST", "/api/preserve/not-a-route", {"preserve": True})[0],
    "DELETE": portal_request(monkeypatch, state_params, "DELETE", "/api/delete/not-a-route")[0],
  }

  if state == "offroad":
    assert statuses["GET"] != 403
    assert statuses["POST"] != 503
    assert statuses["DELETE"] != 503
  else:
    assert statuses == {"GET": 403, "POST": 503, "DELETE": 503}


@pytest.fixture
def disposable_portal_params(tmp_path, monkeypatch):
  from bluepilot.backend import bp_portal
  from bluepilot.backend.params import params_manager

  params = Params(str(tmp_path / "params"))
  params.put_bool("EnableWebRoutesServer", True, block=True)
  params.put_bool("IsOffroad", True, block=True)
  params.put_bool("BPUseCustomSounds", True, block=True)
  params.put_bool("AdbEnabled", True, block=True)
  params.put("FordAngleHighSpeedFactor", 1.25, block=True)

  params_manager._BLUEPILOT_PARAMS_CACHE = None
  params_manager._BLUEPILOT_PARAM_DEFINITIONS_CACHE = None
  params_manager._PARAM_TYPE_CACHE = None
  params_manager._PARAM_ATTRIBUTES_CACHE = None
  monkeypatch.setattr(network_utils, "params", params)
  monkeypatch.setattr(bp_portal, "params", params)
  return params


def test_portal_panels_and_categories_use_current_params_schema(monkeypatch, disposable_portal_params):
  status, panel_list = portal_request(monkeypatch, disposable_portal_params, "GET", "/api/panels")
  assert status == 200
  assert panel_list["panels"] == [{
    "id": "bp_settings_panel",
    "name": "BluePilot",
    "description": "BluePilot settings from the current parameter schema",
    "icon": "",
  }]

  status, panel_response = portal_request(monkeypatch, disposable_portal_params, "GET", "/api/panels/bp_settings_panel")
  assert status == 200
  controls = [control for group in panel_response["panel"]["groups"] for control in group["controls"]]
  param_names = {control.get("param") for control in controls}
  assert {"EnableWebRoutesServer", "BPUseCustomSounds", "FordAngleHighSpeedFactor"} <= param_names

  status, category_response = portal_request(monkeypatch, disposable_portal_params, "GET", "/api/params/categories")
  assert status == 200
  categories = category_response["categories"]
  assert set(categories) == {"BluePilot", "System"}
  assert "BPUseCustomSounds" in {item["key"] for item in categories["BluePilot"]["params"]}
  assert "AdbEnabled" in {item["key"] for item in categories["System"]["params"]}


def test_portal_backup_restore_round_trip_uses_declared_types(monkeypatch, disposable_portal_params):
  params = disposable_portal_params
  status, backup = portal_request(monkeypatch, params, "GET", "/api/params/backup")
  assert status == 200
  assert backup["params"]["AdbEnabled"] is True
  assert backup["params"]["BPUseCustomSounds"] is True

  params.put_bool("AdbEnabled", False, block=True)
  params.put_bool("BPUseCustomSounds", False, block=True)

  status, restored = portal_request(monkeypatch, params, "POST", "/api/params/restore", {"params": backup["params"]})
  assert status == 200
  assert {"AdbEnabled", "BPUseCustomSounds"} <= set(restored["restored"])
  assert params.get_bool("AdbEnabled") is True
  assert params.get_bool("BPUseCustomSounds") is True


def test_portal_device_info_reports_nested_checkout_versions(monkeypatch, disposable_portal_params):
  repo_root = Path(__file__).resolve().parents[3]
  status, info = portal_request(monkeypatch, disposable_portal_params, "GET", "/api/system/device-info")

  assert status == 200
  assert info["bp_version"] == (repo_root / "BPVERSION").read_text().strip()
  assert info["op_version"] in (repo_root / "openpilot/common/version.h").read_text()
  assert info["sp_version"] in (repo_root / "openpilot/sunnypilot/common/version.h").read_text()


def test_restart_ui_targets_actual_dotted_python_module(monkeypatch):
  from bluepilot.backend import bp_portal

  class Process:
    pid = 42
    info = {
      "pid": 42,
      "name": "python3",
      "cmdline": ["python3", "-m", "openpilot.selfdrive.ui.ui"],
    }

    def __init__(self):
      self.signals = []

    def send_signal(self, sent_signal):
      self.signals.append(sent_signal)

  process = Process()
  fake_psutil = SimpleNamespace(
    process_iter=lambda attrs: [process],
    NoSuchProcess=RuntimeError,
    AccessDenied=PermissionError,
  )
  monkeypatch.setattr(bp_portal, "psutil", fake_psutil)
  monkeypatch.setattr(bp_portal.subprocess, "run", lambda *args, **kwargs: SimpleNamespace(returncode=1, stderr=""))

  success, _ = bp_portal.restart_ui_process()

  assert success is True
  assert process.signals == [signal.SIGINT]


def test_restart_ui_fallback_uses_exact_dotted_module_match(monkeypatch):
  from bluepilot.backend import bp_portal

  observed = {}

  def fake_run(command, **kwargs):
    observed["command"] = command
    observed.update(kwargs)
    return SimpleNamespace(returncode=0, stderr="")

  monkeypatch.setattr(bp_portal, "psutil", None)
  monkeypatch.setattr(bp_portal.subprocess, "run", fake_run)

  success, _ = bp_portal.restart_ui_process()

  assert success is True
  assert observed["command"] == ["pkill", "-2", "-f", "openpilot.selfdrive.ui.ui"]
  assert observed["timeout"] == 3
