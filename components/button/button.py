__all__ = ("IconButton",)

from os.path import dirname, join, basename
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior

from components.label import Icon

Builder.load_file(join(dirname(__file__), basename(__file__).split('.')[0] + '.kv'))


class IconButton(ButtonBehavior, Icon):
    pass
