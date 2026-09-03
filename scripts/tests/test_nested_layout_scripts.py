from pathlib import Path
import os
import subprocess


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_device_scripts_use_nested_openpilot_paths():
  health = (REPO_ROOT / "scripts/device_health_check.sh").read_text()
  repair = (REPO_ROOT / "scripts/fix_device_issues.sh").read_text()
  cleanup = (REPO_ROOT / "release/clean_repo.sh").read_text()

  assert "/data/openpilot/openpilot/sunnypilot/common/version.h" in health
  assert "/data/openpilot/openpilot/sunnypilot/common/version.h" in repair
  for expected in (
    "openpilot/cereal/gen",
    "openpilot/selfdrive/controls/lib/longitudinal_mpc_lib/*.json",
    "openpilot/selfdrive/controls/lib/lateral_mpc_lib/*.json",
    "openpilot/tools/plotjuggler/bin",
    "openpilot/selfdrive/assets/translations_assets.qrc",
  ):
    assert expected in cleanup


def test_boot_logo_uses_nested_assets_and_remounts_read_only_on_failure(tmp_path):
  script = REPO_ROOT / "scripts/boot_logo.sh"
  openpilot_root = tmp_path / "checkout"
  boot_image = tmp_path / "bg.jpg"
  call_log = tmp_path / "sudo.log"
  boot_image.write_bytes(b"stock")

  command = f"""
    source {script!s}
    sudo() {{
      printf '%s\\n' "$*" >> "$CALL_LOG"
      if [ "$1" = mount ]; then return 0; fi
      command "$@"
    }}
    HEADLESS_MODE=true
    QUIET_MODE=true
    set +e
    update_boot_image
    status=$?
    set -e
    test "$status" -ne 0
    test "$(grep -c 'remount,rw /' "$CALL_LOG")" -eq 1
    test "$(grep -c 'remount,ro /' "$CALL_LOG")" -eq 1
  """
  env = {
    **os.environ,
    "BP_OPENPILOT_ROOT": str(openpilot_root),
    "BP_BOOT_IMG": str(boot_image),
    "CALL_LOG": str(call_log),
  }

  result = subprocess.run(["bash", "-c", command], env=env, capture_output=True, text=True, timeout=10)

  assert result.returncode == 0, result.stdout + result.stderr
  script_text = script.read_text()
  assert '"$OPENPILOT_ROOT/openpilot/selfdrive/assets/img_bluepilot_boot' in script_text
  assert '"$OPENPILOT_ROOT/openpilot/sunnypilot/selfdrive/assets/images/spinner_sunnypilot.png"' in script_text


def test_boot_logo_exit_trap_covers_exit_immediately_after_rw_mount(tmp_path):
  script = REPO_ROOT / "scripts/boot_logo.sh"
  call_log = tmp_path / "sudo.log"
  command = f"""
    source {script!s}
    sudo() {{
      printf '%s\n' "$*" >> "$CALL_LOG"
      if [[ "$*" == *remount,rw* ]]; then exit 9; fi
      return 0
    }}
    trap cleanup_root_mount EXIT
    mount_partition_rw /
  """
  result = subprocess.run(
    ["bash", "-c", command],
    env={**os.environ, "CALL_LOG": str(call_log)},
    capture_output=True,
    text=True,
    timeout=10,
  )

  assert result.returncode == 9
  calls = call_log.read_text().splitlines()
  assert calls == ["mount -o remount,rw /", "mount -o remount,ro /"]
