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

    choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()

    while choice != 'q':
        if choice == 'c':
            current_taxi =  choose_taxi(taxis)
        elif choice == 'd':
            bill += drive_taxi(current_taxi)
        else:
            print("invalid choice")

        print(f"Bill to date: ${bill:.2f}")
        choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)



def display_taxis(taxis):
    """Display all taxis"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Allows the user to choose a taxi"""
    print("Taxis available: ")
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        if taxi_choice < 0 or taxi_choice >= len(taxis):
            print("invalid taxi choice")
            return None
        return taxis[taxi_choice]
    except ValueError:
        print("invalid taxi choice")
        return None


def drive_taxi(current_taxi):
    """Drive the taxi and return the fare"""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0.0

    try:
        distance = int(input("Drive how far? "))
        current_taxi.start_fare()
        current_taxi.drive(distance)
        fare = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
        return fare
    except ValueError:
        print("Invalid distance")
        return 0.0

main()