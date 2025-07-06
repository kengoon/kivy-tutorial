from features.basescreen import BaseScreen
from os.path import dirname, join, basename
from kivy.lang import Builder

Builder.load_file(join(dirname(__file__), basename(__file__).split('.')[0] + '.kv'))


class MatchaScreen(BaseScreen):
    pass

