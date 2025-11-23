"""
CP1404 Practical 9
Taxi Simulator
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    """run the taxi simulator program"""
    current_taxi = None
    bill = 0

    taxis = [Taxi("prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")

