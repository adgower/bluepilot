from pathlib import Path
import subprocess

from openpilot.common.basedir import BASEDIR
from openpilot.common.bp_spinner import BPSpinner


class _FakeProcess:
  stdin = None

  def kill(self):
    pass

  def communicate(self, timeout):
    pass


def test_spinner_starts_from_nested_openpilot_ui_directory(monkeypatch):
  observed = {}

  def fake_popen(command, **kwargs):
    observed["command"] = command
    observed.update(kwargs)
    return _FakeProcess()

  monkeypatch.setattr(subprocess, "Popen", fake_popen)
  spinner = BPSpinner()
  try:
    assert observed["command"] == ["./bp_spinner.py"]
    assert observed["cwd"] == str(Path(BASEDIR) / "openpilot" / "system" / "ui")
  finally:
    spinner.close()


def test_spinner_start_failure_is_observable(monkeypatch, capsys):
  def fail_popen(*args, **kwargs):
    raise OSError("not executable")

  monkeypatch.setattr(subprocess, "Popen", fail_popen)
  spinner = BPSpinner()

  assert spinner.spinner_proc is None
  assert isinstance(spinner.start_error, OSError)
  assert "not executable" in capsys.readouterr().err
