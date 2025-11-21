"""
CP1404 Practical 9
Unreliable Car Test
"""

from prac_09.unreliable_car import UnreliableCar

def main():
    """Tests that Unreliable Car initialises correctly"""
    good_car = UnreliableCar("Good Car", 100,  90)
    weird_car = UnreliableCar("Weird Car", 100, 50)
    bad_car = UnreliableCar("Bad Car", 100, 30)


