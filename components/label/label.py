__all__ = ("CustomLabel", "Icon")

from os.path import dirname, join, basename, abspath
from kivy.lang import Builder
from kivy.properties import ColorProperty, VariableListProperty, StringProperty, NumericProperty
from kivy.uix.label import Label

from components.behaviors import AdaptiveBehavior
from components import font_path

Builder.load_file(join(dirname(__file__), basename(__file__).split('.')[0] + '.kv'))


class CustomLabel(AdaptiveBehavior, Label):
    bg_color = ColorProperty([0, 0, 0, 0])
    radius = VariableListProperty(0)
    shadow_color = ColorProperty([0, 0, 0, 0])
    line_color = ColorProperty([0, 0, 0, 0])
    line_width = NumericProperty("1dp")


class Icon(CustomLabel):
    icon = StringProperty()
    font_name = StringProperty(join(font_path, "materialdesignicons-webfont.ttf"))
