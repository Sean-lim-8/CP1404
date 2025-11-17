"""
Cp1404 Practical 8
Dynamic labels
Estimate: 30 minutes
Actual: 20 minutes
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.seafood = ["fish", "crab", "lobster", "eel", "squid"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Creates labels for names in the list"""
        for name in self.seafood:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)

DynamicLabelsApp().run()