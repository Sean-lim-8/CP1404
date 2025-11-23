"""
CP1404 Practical 9
Silver service taxi test
"""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """represent silver service taxi with a higher fare"""

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a silver service Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """calculates the fare including flagfall"""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """returns a string representation of the Taxi instance."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"




