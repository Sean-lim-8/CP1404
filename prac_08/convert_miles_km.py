"""
CP1404 Practical 8
Convert miles to kilometres
Estimate: 30 minutes
Actual:
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    def build(self):
        self.title = "Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root


MilesConverterApp().run()