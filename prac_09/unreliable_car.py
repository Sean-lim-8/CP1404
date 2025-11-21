"""
CP1404 Practical 9
Unreliable Car
"""

from prac_09.car import Car
from random import randint

class UnreliableCar(Car):
    """Represent an unreliable car"""

    def __init__(self, name, fuel, reliability):
            """Initialize an UnreliableCar instance"""
            super().__init__(name, fuel)
            self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on distance"""
        if randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0

