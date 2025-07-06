from kivy.app import App
from kivy.core.text import LabelBase
from kivy.loader import Loader
from kivy.properties import StringProperty, NumericProperty
from kivy import platform
from components.bar.bar import win_bnb
from features.screenmanager import AppScreenManager
from ui.theme import ThemeManager
from components.factory import register_factory

LabelBase.register(
    "Roboto",
    'assets/fonts/Poppins-Regular.ttf',
    'assets/fonts/Poppins-Italic.ttf',
    'assets/fonts/Poppins-Bold.ttf',
    'assets/fonts/Poppins-BoldItalic.ttf'
)
Loader.error_image = "assets/images/transparent.png"
Loader.loading_image = "assets/images/transparent.png"
register_factory()

if platform == "android":
    """
    This block is executed only when the application is running on an Android platform.

    1. It imports the set_edge_to_edge function from the kvdroid.tools.display module.
    2. The set_edge_to_edge() function is called to configure the application's edge-to-edge display layout. 
       This layout setup allows the application content to extend to the full screen, 
       including areas under system bars (status bar and navigation bar), in compliance with Android UI guidelines.
    """
    from kvdroid.tools.display import set_edge_to_edge

    set_edge_to_edge()


class KivyTutorialApp(App):
    kv_file = StringProperty("imports.kv")
    if platform == "android":
        from kvdroid.tools.display import get_statusbar_height, get_navbar_height
        statusbar_height = NumericProperty(get_statusbar_height())
        navbar_height = NumericProperty(get_navbar_height())
    else:
        statusbar_height = NumericProperty(0)
        navbar_height = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Dark"
        if platform == "android":
            from kvdroid.tools import change_statusbar_color, navbar_color
            change_statusbar_color(
                [0, 0, 0, 0],
                "black" if self.theme_cls.theme_style == "Light" else "white"
            )
            navbar_color(
                [0, 0, 0, 0],
                "white" if self.theme_cls.theme_style == "Light" else "black"
            )
            self.theme_cls.bind(
                bg_color=lambda _, value: (
                    change_statusbar_color(
                        [0, 0, 0, 0],
                        "black" if self.theme_cls.theme_style == "Light" else "white"
                    ),
                    navbar_color(
                        [0, 0, 0, 0],
                        "white" if self.theme_cls.theme_style == "Light" else "black"
                    )
                )
            )

    def build(self):
        sm = AppScreenManager()
        sm.current = "matcha screen"
        return sm

    def on_start(self):
        win_bnb.create_bnb(
            tabs=[
                {
                    "icon": "home",
                    "active": True
                },
                {
                    "icon": "map",
                },
                {
                    "icon": "heart",
                },
                {
                    "icon": "gamepad",
                }
            ],
        )
        win_bnb.push()


if __name__ == '__main__':
    KivyTutorialApp().run()
