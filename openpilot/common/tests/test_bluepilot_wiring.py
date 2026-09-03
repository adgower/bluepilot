from openpilot.cereal.services import SERVICE_LIST
from openpilot.common.bluepilot import is_bluepilot
from openpilot.system.manager.process_config import managed_processes


def test_bluepilot_checkout_is_detected_and_manager_wiring_is_enabled():
  assert is_bluepilot() is True
  assert managed_processes["soundd"].module == "openpilot.selfdrive.ui.bp.soundd_bp"
  assert managed_processes["bp_portal"].module == "bluepilot.backend.bp_portal"
  assert managed_processes["bp_route_preprocessor"].module == "bluepilot.backend.routes.preprocessor"


def test_bluepilot_message_services_are_registered():
  assert "controllerStateBP" in SERVICE_LIST
  assert "carStateBP" in SERVICE_LIST


def test_bluepilot_card_cruise_and_desire_extensions_are_selected():
  from openpilot.selfdrive.car import card, cruise
  from openpilot.selfdrive.controls.lib import desire_helper

  assert card.publish_controller_state_bp.__module__ == "openpilot.bluepilot.selfdrive.car.bp_card_publisher"
  assert card.publish_car_state_bp.__module__ == "openpilot.bluepilot.selfdrive.car.bp_card_publisher"
  assert desire_helper.BPBlinkerPause.__module__ == "openpilot.bluepilot.selfdrive.controls.bp_desire_helper"
  assert cruise.is_bluepilot() is True
