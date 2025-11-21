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

