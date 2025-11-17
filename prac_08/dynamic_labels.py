"""
Cp1404 Practical 8
Dynamic labels
Estimate: 30 minutes
Actual:
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.seafood = ["fish", "crab", "lobster", "eel", "squid"]



DynamicLabelsApp().run()