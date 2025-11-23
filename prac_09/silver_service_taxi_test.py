"""
CP1404 Practical 9
Silver service taxi test
"""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a silver service Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """returns a string representation of the Taxi instance."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"


