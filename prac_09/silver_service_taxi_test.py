"""
CP1404 Practical 9
Silver service taxi test
"""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness):
        """Initialise a silver service Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness
