__all__ = ("BottomNavigationBar", "NavigationItem", "win_bnb")

from os.path import join, dirname, basename

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import BooleanProperty, ColorProperty, ListProperty, VariableListProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window as win
from kivy.animation import Animation
from components.behaviors import AdaptiveBehavior
from components.button import IconButton

Builder.load_file(join(dirname(__file__), basename(__file__).split('.')[0] + '.kv'))


class NavigationItem(IconButton):
    active = BooleanProperty(True)
    icon_color_normal = ColorProperty(None, allownone=True)
    icon_color_active = ColorProperty(None, allownone=True)
    indicator_color = ColorProperty(None, allownone=True)


class BottomNavigationBar(AdaptiveBehavior, BoxLayout):
    tabs = ListProperty()
    radius = VariableListProperty(None, allownone=True)
    bg_color = ColorProperty(None, allownone=True)
    indicator_color = ColorProperty(None, allownone=True)
    variant_icon_enabled = BooleanProperty(True)
    icon_color_normal = ColorProperty(None, allownone=True)
    icon_color_active = ColorProperty(None, allownone=True)
    line_color = ColorProperty(None, allownone=True)
    line_width = NumericProperty("1dp")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        tab: dict
        for tab in self.tabs:
            btn = NavigationItem(
                active=tab.get('active', False),
                indicator_color=self.indicator_color,
                icon_color_normal=self.icon_color_normal,
                icon_color_active=self.icon_color_active,
                on_release=tab.get('on_release', lambda _: None),
            )
            if self.variant_icon_enabled:
                btn.icon = tab["icon" if tab.get("active") else "variant_icon"]
            else:
                btn.icon = tab["icon"]
            btn.bind(on_release=self._set_active_item)
            self.bind(
                indicator_color=btn.setter("indicator_color"),
                icon_color_normal=btn.setter("icon_color_normal"),
                icon_color_active=btn.setter("icon_color_active"),
            )
            self.add_widget(btn)

    def _set_active_item(self, item):
        for widget, tab in zip(self.children[::-1], self.tabs):
            if widget is item:
                widget.active = True
                if self.variant_icon_enabled:
                    widget.icon = tab["icon"]
            else:
                widget.active = False
                if self.variant_icon_enabled:
                    widget.icon = tab["variant_icon"]


class base_bar:
    bar = None
    state = "pop"
    bind_win_size_to_bar_pos = None
    _pop_listeners = []
    _push_listeners = []
    _push_height = 0
    _y = 0

    @classmethod
    def push(cls):
        cls.state = "push"
        for func in cls._push_listeners:
            func()

    @classmethod
    def pop(cls):
        cls.state = "pop"
        for func in cls._pop_listeners:
            func()

    @classmethod
    def remove_bar(cls):
        cls.pop()
        win.remove_widget(cls.bar)
        cls.bar = None
        cls.bar_win_size_to_bar_pos = None
        cls._pop_listeners = []
        cls._push_listeners = []

    @classmethod
    def _bind_win_size(cls):
        if cls.bar:
            win.bind(size=cls.bind_win_size_to_bar_pos)

    @classmethod
    def _unbind_win_size(cls):
        win.unbind(size=cls.bind_win_size_to_bar_pos)

    @classmethod
    def register_listener(cls, **kwargs):
        if (func := kwargs.get("pop")) and callable(func):
            cls._pop_listeners.append(func)
        if (func := kwargs.get("push")) and callable(func):
            cls._push_listeners.append(func)


class win_bnb(base_bar):
    _y = dp(20)

    @classmethod
    def create_bnb(
            cls,
            bg_color=None,
            indicator_color=None,
            variant_icon_enabled=False,
            tabs=None,
            icon_color_normal=None,
            icon_color_active=None,
            radius=None
    ):
        if cls.bar:
            return
        if tabs is None:
            tabs = []
        cls.bar = BottomNavigationBar(
            tabs=tabs,
            variant_icon_enabled=variant_icon_enabled,
            indicator_color=indicator_color,
            radius=radius,
            bg_color=bg_color,
            icon_color_normal=icon_color_normal,
            icon_color_active=icon_color_active,
        )
        cls.bar.pos = ((win.size[0] / 2) - (cls.bar.width / 2), -cls.bar.height - cls._y)
        cls.bind_win_size_to_bar_pos = lambda *_: (
            setattr(
                cls.bar,
                "pos",
                (
                    (win.size[0] / 2) - (cls.bar.width / 2),
                    cls._y if cls.state == "push" else -cls.bar.height - cls._y,
                )
            )
        )
        cls.bar.bind(size=cls.bind_win_size_to_bar_pos)
        cls._bind_win_size()
        win.add_widget(cls.bar)

    @classmethod
    def push(cls):
        Animation(y=cls._y, d=.2).start(cls.bar)
        super().push()

    @classmethod
    def pop(cls):
        Animation(y=-cls.bar.height - cls._y, d=.2).start(cls.bar)
        super().pop()


if __name__ == "__main__":
    from kivy.app import App
    from ui.theme import ThemeManager

    class TestApp(App):
        theme_cls = ThemeManager()

        def on_start(self):
            self.theme_cls.theme_style = "Dark"
            win_bnb.create_bnb(
                # variant_icon_enabled=True,
                tabs=[
                    {
                        "icon": "home",
                        "variant_icon": "home-outline",
                        "active": True,
                        "on_release": print
                    },
                    {
                        "icon": "map",
                        "variant_icon": "map-outline",
                    },
                    {
                        "icon": "heart",
                        "variant_icon": "heart-outline",
                    }
                ]
            )
            win_bnb.push()

    TestApp().run()