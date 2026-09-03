"""BluePilot detection. Safe to import on any fork — returns False when not BluePilot."""
from functools import cache
from pathlib import Path

from openpilot.common.basedir import BASEDIR

@cache
def is_bluepilot() -> bool:
  return (Path(BASEDIR) / "BPVERSION").is_file()
