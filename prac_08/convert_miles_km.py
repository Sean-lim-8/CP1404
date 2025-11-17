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

    def get_valid_miles(self):
        """Validates and returns a value from the text field"""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0

    def handle_convert(self):
        """converts miles into kilometres"""
        miles = self.get_valid_miles()
        km = miles * MILES_TO_KM
        self.root.ids.output_label.text = f"{km:.2f}"

    def handle_increment(self, change):
        """Increase or decrease the input value"""
        miles = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(miles)



MilesConverterApp().run()