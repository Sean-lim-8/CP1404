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

    print(good_car)
    for i in range(5):
        distance_driven = good_car.drive(20)
        print(f"Attempt {i+1}: Drove {distance_driven} km")
    print(good_car)

    print(weird_car)
    for i in range(5):
        distance_driven = weird_car.drive(20)
        print(f"Attempt {i + 1}: Drove {distance_driven} km")
    print(weird_car)

    print(bad_car)
    for i in range(5):
        distance_driven = bad_car.drive(20)
        print(f"Attempt {i + 1}: Drove {distance_driven} km")
    print(bad_car)

main()