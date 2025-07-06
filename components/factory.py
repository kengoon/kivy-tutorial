from kivy.factory import Factory


def register_factory():
    r = Factory.register
    r("CustomLabel", module="components.label")
    r("Icon", module="components.label")
    r("IconButton", module="components.button")
    r("BottomNavigationBar", module="components.bar")
    r("NavigationItem", module="components.bar")
    r("CoverImage", module="components.image")
