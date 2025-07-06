__all__ = ("CoverImage", )

from kivy.clock import triggered
from kivy.properties import StringProperty
from components.behaviors.stencil import StencilBehavior
from kivy.uix.image import AsyncImage


class CoverImage(AsyncImage, StencilBehavior):
    fit_mode = StringProperty("cover")

    @triggered(1, True)
    def try_load_image(self, _):
        self.reload()
        self.try_load_image.cancel()

    def on_load(self, *args):
        self.try_load_image.cancel()

    def on_error(self, error):
        self.try_load_image()
