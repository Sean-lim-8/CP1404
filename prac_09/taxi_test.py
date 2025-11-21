"""
CP1404 Practical 9
taxi test
"""

from prac_09.taxi import Taxi

def main():
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)

