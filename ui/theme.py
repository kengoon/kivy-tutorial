from kivy.app import App
from kivy.clock import mainthread
from kivy.core.window import Window
from kivy.event import EventDispatcher
from kivy.properties import ColorProperty, OptionProperty, ObjectProperty


class ThemeManager(EventDispatcher):
    bg_color = ColorProperty()
    bg_color_light = ColorProperty("white")
    bg_color_dark = ColorProperty("#000000")
    card_color = ColorProperty()
    card_color_light = ColorProperty("#FFFFFF")
    card_color_dark = ColorProperty("#000000")
    primary_color = ColorProperty()
    primary_color_light = ColorProperty("#B7FF43")
    primary_color_dark = ColorProperty("#B7FF43")
    secondary_color = ColorProperty()
    secondary_color_light = ColorProperty()
    secondary_color_dark = ColorProperty()
    accent_color = ColorProperty()
    accent_color_light = ColorProperty([0, 0, 0, .05])
    accent_color_dark = ColorProperty([1, 1, 1, .08])
    shadow_color = ColorProperty()
    shadow_color_light = ColorProperty([0, 0, 0, .65])
    shadow_color_dark = ColorProperty([1, 1, 1, .65])
    text_color = ColorProperty()
    text_color_light = ColorProperty("#3F3F41")
    text_color_dark = ColorProperty("#FFFFFF")
    transparent_color = ColorProperty("#00000000")
    disabled_color = ColorProperty([.4, .4, .4, .7])
    theme_style = OptionProperty("Light", options=["Light", "Dark"])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_theme()

    def on_theme_style(self, *_):
        self.set_theme()

    def set_theme(self):
        if self.theme_style == "Light":
            self.bg_color = self.bg_color_light
            self.primary_color = self.primary_color_light
            self.secondary_color = self.secondary_color_light
            self.accent_color = self.accent_color_light
            self.text_color = self.text_color_light
            self.shadow_color = self.shadow_color_light
            self.card_color = self.card_color_light
        else:
            self.bg_color = self.bg_color_dark
            self.primary_color = self.primary_color_dark
            self.secondary_color = self.secondary_color_dark
            self.accent_color = self.accent_color_dark
            self.text_color = self.text_color_dark
            self.shadow_color = self.shadow_color_dark
            self.card_color = self.card_color_dark

        Window.clearcolor = self.bg_color
