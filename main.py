from kivy.app import App
from kivy.properties import StringProperty

from features.screenmanager import AppScreenManager


class KivyTutorialApp(App):
    kv_file = StringProperty("imports.kv")

    def build(self):
        sm = AppScreenManager()
        sm.current = "home screen"
        return sm


if __name__ == '__main__':
    KivyTutorialApp().run()
