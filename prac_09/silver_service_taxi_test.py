"""
CP1404 Practical 9
Silver service taxi test
"""

from silver_service_taxi import SilverServiceTaxi

def main():
    """Tests silver service taxi"""

    taxi = SilverServiceTaxi("Test taxi", 100, 2)
    print(taxi)
    taxi.drive(18)
    fare = taxi.get_fare()
    print(f"Fare for 18km trip: {fare:.2f}")
    assert fare == 48.78, f"Expected fare is $48.78, got ${fare:.2f}"
    print("Test passed")

main()



