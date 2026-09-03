import importlib
from enum import IntEnum
import sys
from types import ModuleType, SimpleNamespace

import pytest


def _module(name, **attributes):
  module = ModuleType(name)
  for key, value in attributes.items():
    setattr(module, key, value)
  return module


def _install(monkeypatch, name, **attributes):
  module = _module(name, **attributes)
  monkeypatch.setitem(sys.modules, name, module)
  return module


def _fresh_import(monkeypatch, name):
  monkeypatch.delitem(sys.modules, name, raising=False)
  return importlib.import_module(name)


class Rectangle:
  def __init__(self, x=0, y=0, width=0, height=0):
    self.x = x
    self.y = y
    self.width = width
    self.height = height


class FakeWidget:
  def __init__(self, *args, **kwargs):
    self.rect = Rectangle()
    self.visible = True
    self.click_callback = None
    self.hide_count = 0
    self.show_count = 0

  def set_rect(self, rect):
    self.rect = rect

  def set_visible(self, visible):
    self.visible = visible() if callable(visible) else visible
    self.visibility_predicate = visible

  def set_click_callback(self, callback):
    self.click_callback = callback

  def hide_event(self):
    self.hide_count += 1

  def show_event(self):
    self.show_count += 1

  def render(self, rect):
    self.last_render_rect = rect


class FakeItems:
  def __init__(self, items=None):
    self._items = list(items or [])
    self.scroll_calls = []

  def add_widget(self, item):
    self._items.append(item)

  def add_widgets(self, items):
    self._items.extend(items)

  def set_reset_scroll_at_show(self, value):
    self.reset_scroll_at_show = value

  def set_scrolling_enabled(self, callback):
    self.scrolling_enabled = callback

  def scroll_to(self, x, smooth=False):
    self.scroll_calls.append((x, smooth))


class FakeScroller(FakeWidget):
  def __init__(self, *args, **kwargs):
    super().__init__()
    self._scroller = FakeItems()
    self._rect = Rectangle(0, 0, 480, 480)
    self.base_updates = 0

  def _update_state(self):
    self.base_updates += 1

  def _render(self, rect):
    self.last_render_rect = rect


class FakeButton(FakeWidget):
  def __init__(self, *args, **kwargs):
    super().__init__()
    self.args = args
    self._label = SimpleNamespace(set_font_weight=lambda weight: None)


class FakeGui:
  width = 480
  height = 480

  def __init__(self):
    self.pushed = []
    self.nav_ticks = []

  def sunnypilot_ui(self):
    return True

  def texture(self, path, width, height):
    return SimpleNamespace(path=path, width=width, height=height)

  def push_widget(self, widget):
    self.pushed.append(widget)

  def pop_widget(self):
    pass

  def pop_widgets_to(self, *args, **kwargs):
    callback = args[1] if len(args) > 1 else None
    if callback is not None:
      callback()

  def add_nav_stack_tick(self, callback):
    self.nav_ticks.append(callback)

  def widget_in_stack(self, widget):
    return False


def test_sunnypilot_mici_settings_constructs_always_offroad_and_bluepilot_seams(monkeypatch):
  gui = FakeGui()
  ui_state = SimpleNamespace(
    started=False,
    always_offroad=False,
    engaged=False,
    params=SimpleNamespace(put_bool=lambda key, value: None),
  )

  class BaseSettings(FakeWidget):
    def __init__(self):
      super().__init__()
      self._scroller = FakeItems([FakeButton(str(index)) for index in range(7)])

    def _update_state(self):
      self.updated = True

  class Confirmation(FakeWidget):
    def __init__(self, *args, confirm_callback=None, **kwargs):
      super().__init__()
      self.confirm_callback = confirm_callback

  _install(monkeypatch, "openpilot.selfdrive.ui.mici.layouts.settings.settings",
           SettingsLayout=BaseSettings, SettingsBigButton=FakeButton)
  _install(monkeypatch, "openpilot.selfdrive.ui.mici.layouts.settings.device", DeviceLayoutMici=FakeWidget)
  _install(monkeypatch, "openpilot.selfdrive.ui.mici.widgets.button", BigButton=FakeButton, BigCircleButton=FakeButton)
  _install(monkeypatch, "openpilot.selfdrive.ui.mici.widgets.dialog", BigConfirmationDialog=Confirmation, BigDialog=FakeWidget)
  _install(monkeypatch, "openpilot.selfdrive.ui.sunnypilot.mici.layouts.sunnylink", SunnylinkLayoutMici=FakeWidget)
  _install(monkeypatch, "openpilot.selfdrive.ui.sunnypilot.mici.layouts.models", ModelsLayoutMici=FakeWidget)
  _install(monkeypatch, "openpilot.selfdrive.ui.ui_state", ui_state=ui_state)
  _install(monkeypatch, "openpilot.system.ui.lib.application", gui_app=gui,
           FontWeight=SimpleNamespace(AUDIOWIDE="audiowide"))
  _install(monkeypatch, "openpilot.system.ui.lib.multilang", tr=lambda text: text)
  _install(monkeypatch, "openpilot.selfdrive.ui.bp.mici.widgets.button_bp", BigButtonBP=FakeButton)
  _install(monkeypatch, "openpilot.selfdrive.ui.bp.mici.layouts.settings.bluepilot", BluePilotLayoutMici=FakeWidget)

  module = _fresh_import(monkeypatch, "openpilot.selfdrive.ui.sunnypilot.mici.layouts.settings")
  layout = module.SettingsLayoutSP()

  assert module.BIG_ICON_SIZE == 110
  assert isinstance(layout._enable_offroad_btn_onroad, FakeButton)
  assert isinstance(layout._enable_offroad_btn_offroad, FakeButton)
  assert isinstance(layout._disable_offroad_btn, FakeButton)
  assert any(button.args and button.args[0] == "bluepilot" for button in layout._scroller._items)
  layout._handle_always_offroad(True)
  assert isinstance(gui.pushed[-1], Confirmation)


def test_bluepilot_mici_home_inherits_sunnypilot_home(monkeypatch):
  class StockHome(FakeWidget):
    pass

  class SunnyHome(StockHome):
    def _set_chestnut_visibility(self):
      self.chestnut_visibility_refreshed = True

  class Label:
    def __init__(self, *args, **kwargs):
      self.args = args

  _install(monkeypatch, "pyray", Color=lambda *args: tuple(args))
  _install(monkeypatch, "openpilot.system.ui.widgets.label", UnifiedLabel=Label)
  _install(monkeypatch, "openpilot.system.ui.lib.application",
           FontWeight=SimpleNamespace(AUDIOWIDE="audiowide"))
  _install(monkeypatch, "openpilot.selfdrive.ui.mici.layouts.home", MiciHomeLayout=StockHome)
  _install(monkeypatch, "openpilot.selfdrive.ui.sunnypilot.mici.layouts.home", MiciHomeLayoutSP=SunnyHome)

  module = _fresh_import(monkeypatch, "openpilot.selfdrive.ui.bp.mici.layouts.home")
  layout = module.BpMiciHomeLayout()

  assert isinstance(layout, SunnyHome)
  layout._set_chestnut_visibility()
  assert layout.chestnut_visibility_refreshed is True


def _install_main_layout_stubs(monkeypatch, *, mici):
  gui = FakeGui()
  ui_state = SimpleNamespace(
    started=False,
    ignition=False,
    is_body=False,
    sm={"carState": SimpleNamespace(standstill=True)},
    body_callbacks=[],
  )
  ui_state.add_on_body_changed_callbacks = ui_state.body_callbacks.append
  device = SimpleNamespace(timeout_callbacks=[])
  device.add_interactive_timeout_callback = device.timeout_callbacks.append

  class PubMaster:
    def __init__(self, services):
      self.services = services

    def send(self, service, message):
      pass

  _install(monkeypatch, "pyray", Rectangle=Rectangle, get_time=lambda: 0.0)
  messaging = _install(monkeypatch, "openpilot.cereal.messaging", PubMaster=PubMaster,
                       new_message=lambda service, valid=True: SimpleNamespace())
  cereal = _install(monkeypatch, "openpilot.cereal", messaging=messaging)
  cereal.__path__ = []
  import openpilot
  monkeypatch.setattr(openpilot, "cereal", cereal, raising=False)
  _install(monkeypatch, "openpilot.system.ui.lib.application", gui_app=gui)
  _install(monkeypatch, "openpilot.system.ui.widgets", Widget=FakeWidget)
  _install(monkeypatch, "openpilot.selfdrive.ui.ui_state", ui_state=ui_state, device=device)
  _install(monkeypatch, "openpilot.selfdrive.ui.body.layouts.onroad", BodyLayout=type("BodyLayout", (FakeWidget,), {}))

  if mici:
    class Home(FakeWidget):
      def set_callbacks(self, **callbacks):
        self.callbacks = callbacks

    class Alerts(FakeWidget):
      def __init__(self):
        super().__init__()
        self.update_count = 0

      def active_alerts(self):
        return 2

      def max_severity(self):
        return 4

      def _update_state(self):
        self.update_count += 1

    class Car(FakeWidget):
      def __init__(self, *args, **kwargs):
        super().__init__()

      def is_swiping_left(self):
        return False

    _install(monkeypatch, "openpilot.system.ui.widgets.scroller", Scroller=FakeScroller)
    _install(monkeypatch, "openpilot.selfdrive.ui.mici.layouts.home", MiciHomeLayout=Home)
    _install(monkeypatch, "openpilot.selfdrive.ui.bp.mici.layouts.home", BpMiciHomeLayout=Home)
    _install(monkeypatch, "openpilot.selfdrive.ui.sunnypilot.mici.layouts.home", MiciHomeLayoutSP=Home)
    _install(monkeypatch, "openpilot.selfdrive.ui.mici.layouts.settings.settings", SettingsLayout=FakeWidget)
    _install(monkeypatch, "openpilot.selfdrive.ui.sunnypilot.mici.layouts.settings", SettingsLayoutSP=FakeWidget)
    _install(monkeypatch, "openpilot.selfdrive.ui.mici.layouts.offroad_alerts", MiciOffroadAlerts=Alerts)
    _install(monkeypatch, "openpilot.selfdrive.ui.mici.onroad.augmented_road_view", AugmentedRoadView=Car)
    _install(monkeypatch, "openpilot.selfdrive.ui.bp.mici.onroad.augmented_road_view_bp",
             MiciAugmentedRoadViewBP=type("MiciAugmentedRoadViewBP", (Car,), {}))
    _install(monkeypatch, "openpilot.selfdrive.ui.mici.layouts.onboarding",
             OnboardingWindow=lambda *args: SimpleNamespace(completed=True))
  else:
    class SetupWidget:
      def set_open_settings_callback(self, callback):
        self.callback = callback

    class Home(FakeWidget):
      def __init__(self):
        super().__init__()
        self._setup_widget = SetupWidget()

      def set_settings_callback(self, callback):
        self.settings_callback = callback

      def set_model_settings_callback(self, callback):
        self.model_callback = callback

    class Settings(FakeWidget):
      def set_callbacks(self, **callbacks):
        self.callbacks = callbacks

      def set_current_panel(self, panel):
        self.panel = panel

    class Sidebar(FakeWidget):
      is_visible = True

      def set_callbacks(self, **callbacks):
        self.callbacks = callbacks

    class Car(FakeWidget):
      pass

    class PanelType:
      DEVICE = "device"
      FIREHOSE = "firehose"
      MODELS = "models"
      NETWORK = "network"
      TOGGLES = "toggles"

    _install(monkeypatch, "openpilot.selfdrive.ui.layouts.sidebar", Sidebar=Sidebar, SIDEBAR_WIDTH=300)
    _install(monkeypatch, "bluepilot.ui.widgets.sidebar", SidebarBP=Sidebar)
    _install(monkeypatch, "bluepilot.ui.lib.constants", BPConstants=SimpleNamespace(SIDEBAR_WIDTH=350))
    _install(monkeypatch, "openpilot.selfdrive.ui.layouts.home", HomeLayout=Home)
    _install(monkeypatch, "bluepilot.ui.layouts.home_bp", HomeLayoutBP=type("HomeLayoutBP", (Home,), {}))
    _install(monkeypatch, "openpilot.selfdrive.ui.sunnypilot.layouts.home", HomeLayoutSP=Home)
    _install(monkeypatch, "openpilot.selfdrive.ui.layouts.settings.settings",
             SettingsLayout=Settings, PanelType=PanelType)
    _install(monkeypatch, "openpilot.selfdrive.ui.layouts.settings", settings=SimpleNamespace(PanelType=PanelType))
    _install(monkeypatch, "openpilot.selfdrive.ui.sunnypilot.layouts.settings.settings", SettingsLayoutSP=Settings)
    _install(monkeypatch, "openpilot.selfdrive.ui.onroad.augmented_road_view", AugmentedRoadView=Car)
    _install(monkeypatch, "openpilot.selfdrive.ui.bp.onroad.augmented_road_view_bp",
             AugmentedRoadViewBP=type("AugmentedRoadViewBP", (Car,), {}))
    _install(monkeypatch, "openpilot.selfdrive.ui.layouts.onboarding",
             OnboardingWindow=lambda: SimpleNamespace(completed=True))
    _install(monkeypatch, "bluepilot.ui.widgets.debug",
             ControlsDebugPanel=type("ControlsDebugPanel", (FakeWidget,), {
               "is_panel_visible": False,
               "toggle_visibility": lambda self: None,
             }))

  return gui, ui_state, device


def test_mici_main_preserves_alert_refresh_and_body_routing(monkeypatch):
  _, ui_state, _ = _install_main_layout_stubs(monkeypatch, mici=True)
  module = _fresh_import(monkeypatch, "openpilot.selfdrive.ui.mici.layouts.main")
  layout = module.MiciMainLayout()

  assert type(layout._car_onroad_layout).__name__ == "MiciAugmentedRoadViewBP"
  assert type(layout._body_onroad_layout).__name__ == "BodyLayout"
  assert set(layout._home_layout.callbacks) >= {
    "on_settings", "on_alerts", "alert_count_callback", "max_severity_callback",
  }
  assert layout._on_body_changed in ui_state.body_callbacks

  layout._update_state()
  assert layout._alerts_layout.update_count == 1
  ui_state.is_body = True
  layout._on_body_changed()
  assert layout._onroad_layout is layout._body_onroad_layout
  assert layout._body_onroad_layout.visible is True
  assert layout._car_onroad_layout.visible is False


def test_large_main_routes_body_separately_from_bluepilot_car_layout(monkeypatch):
  _, ui_state, _ = _install_main_layout_stubs(monkeypatch, mici=False)
  module = _fresh_import(monkeypatch, "openpilot.selfdrive.ui.layouts.main")
  layout = module.MainLayout()

  assert type(layout._home_layout).__name__ == "HomeLayoutBP"
  assert type(layout._home_body_layout).__name__ == "BodyLayout"
  assert type(layout._layouts[module.MainState.ONROAD]).__name__ == "AugmentedRoadViewBP"
  assert layout._on_body_changed in ui_state.body_callbacks

  ui_state.is_body = True
  layout._on_body_changed()
  assert layout._layouts[module.MainState.HOME] is layout._home_body_layout
  assert layout._current_mode == module.MainState.HOME

  ui_state.is_body = False
  layout._on_body_changed()
  assert layout._layouts[module.MainState.HOME] is layout._home_layout


def test_mici_hud_runs_sunnypilot_model_source_and_bsm_chain(monkeypatch):
  class StockHud:
    def _update_state(self):
      self.events.append("stock_update")

    def _render(self, rect):
      self._torque_bar.render(rect)
      self.events.append("model_source")
      self._draw_steering_wheel(rect)

  class SunnyHud(StockHud):
    def _update_state(self):
      super()._update_state()
      self.events.append("bsm_update")

    def _render(self, rect):
      super()._render(rect)
      self.events.append("bsm_render")

    def _has_blind_spot_detected(self):
      return False

  class LateralMode(IntEnum):
    curvature = 0
    angle = 1

  class FakeParams:
    def get_bool(self, key):
      return False

    def get(self, key):
      return 0

  class WheelStyle(IntEnum):
    COMMA_4 = 0
    COMMA_3X = 1

  ui_state = SimpleNamespace(sm={}, status=0, is_metric=True)
  _install(monkeypatch, "pyray", Rectangle=Rectangle, Color=lambda *args: tuple(args))
  _install(monkeypatch, "openpilot.common.params", Params=FakeParams)
  _install(monkeypatch, "opendbc.sunnypilot.car.ford.lateral_curv_ext",
           PrimaryLateralControl=LateralMode)
  _install(monkeypatch, "opendbc.car.structs",
           ControllerStateBP=SimpleNamespace(LateralMode=LateralMode))
  _install(monkeypatch, "openpilot.selfdrive.ui.mici.onroad.hud_renderer",
           HudRenderer=StockHud, FONT_SIZES=SimpleNamespace(set_speed=1, max_speed=1),
           KM_TO_MILE=1.0, CRUISE_DISABLED_CHAR="-", SET_SPEED_PERSISTENCE=1)
  _install(monkeypatch, "openpilot.selfdrive.ui.sunnypilot.mici.onroad.hud_renderer", HudRendererSP=SunnyHud)
  _install(monkeypatch, "openpilot.system.ui.lib.multilang", tr=lambda text: text)
  _install(monkeypatch, "openpilot.selfdrive.ui.bp.mici.onroad.powerflow_gauge",
           MiciPowerflowGauge=FakeWidget)
  _install(monkeypatch, "openpilot.selfdrive.ui.ui_state", ui_state=ui_state,
           UIStatus=SimpleNamespace(DISENGAGED=0))
  _install(monkeypatch, "openpilot.selfdrive.ui.bp.lib.steering_wheel_style",
           ensure_steering_wheel_icon_style_initialized=lambda *args: WheelStyle.COMMA_4,
           get_steering_wheel_icon_style=lambda *args: WheelStyle.COMMA_4,
           SteeringWheelIconStyle=WheelStyle)
  _install(monkeypatch, "openpilot.selfdrive.ui.bp.lib.ui_debug_logger",
           bp_ui_log=SimpleNamespace(state=lambda *args: None))
  _install(monkeypatch, "openpilot.selfdrive.ui.bp.lib.theme_pack",
           get_active_pack=lambda *args, **kwargs: None)
  _install(monkeypatch, "openpilot.system.ui.lib.text_measure",
           measure_text_cached=lambda *args: SimpleNamespace(x=0, y=0))
  _install(monkeypatch, "openpilot.system.ui.lib.application", gui_app=FakeGui())
  _install(monkeypatch, "openpilot.bluepilot.ui.lib.bp_shaders",
           draw_shader_circle_gradient=lambda *args: None)
  _install(monkeypatch, "openpilot.selfdrive.ui.bp.mici.onroad.torque_bar_bp", TorqueBarBP=FakeWidget)

  module = _fresh_import(monkeypatch, "openpilot.selfdrive.ui.bp.mici.onroad.hud_renderer_bp")
  renderer = module.MiciHudRendererBP.__new__(module.MiciHudRendererBP)
  renderer.events = []
  renderer._bp_params = FakeParams()
  renderer._animate_wheel_param_counter = 0
  renderer._brakes_on = False
  renderer._torque_bar = SimpleNamespace(render=lambda rect: renderer.events.append("torque"))
  renderer.is_cruise_set = False
  renderer._draw_steering_wheel = lambda rect: renderer.events.append("bp_wheel")

  assert issubclass(module.MiciHudRendererBP, SunnyHud)
  renderer._update_state()
  renderer._render(Rectangle())
  assert renderer.events == [
    "stock_update", "bsm_update", "torque", "model_source", "bp_wheel", "bsm_render",
  ]
