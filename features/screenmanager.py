from importlib import import_module

from kivy import platform
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import DictProperty
from kivy.uix.screenmanager import ScreenManager


class AppScreenManager(ScreenManager):
    screens_config = DictProperty(
        {
            "home screen": {
                "presentation": ("features.home.presentation", "HomeScreen")
            },
            "new screen": {
                "presentation": ("features.new.presentation", "NewScreen")
            }
        }
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self._go_back)

    def on_current(self, instance, value):
        if not self.has_screen(value):
            screen_data = self.screens_config[value]
            presentation_module_path, presentation_class_name = screen_data["presentation"]
            presentation_module = import_module(presentation_module_path)
            presentation_class = getattr(presentation_module, presentation_class_name)
            presentation = presentation_class()
            presentation.app = App.get_running_app()
            self.add_widget(presentation)
        supra = super().on_current(instance, value)
        return supra

    def _go_back(self, _window, key, *_args):
        if key in [27, 1073742106]:
            if self.screens.index(self.current_screen) == 0 and platform == "android":
                from android import mActivity
                mActivity.moveTaskToBack(True)
                return True
            self.current = self.previous()
            return True

