from kivy.app import App
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.factory import Factory
from features.screenmanager import AppScreenManager


class KivyTutorialApp(App):
    kv_file = StringProperty("imports.kv")

    def build(self):
        sm = AppScreenManager()
        sm.current = "matcha skeleton screen"
        return sm

    def on_start(self):
        Window.add_widget(Factory.BottomNavigation())


if __name__ == '__main__':
    KivyTutorialApp().run()
