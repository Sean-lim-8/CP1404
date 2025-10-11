"""
CP1404 - Practical 4
Program to generate quick pick numbers
"""
import random

NUMBER_PER_PICK = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

def main():
    """Asks the user how many quick pick numbers to generate"""
    number_of_picks = validate_user_input("How many quick picks?: ")
    for i in range(number_of_picks):
        quick_picks = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_picks))


def generate_quick_pick():
    """Generates and sorts quick pick numbers in ascending order"""
    quick_picks = []
    for i in range(NUMBER_PER_PICK):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while number in quick_picks:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_picks.append(number)
    quick_picks.sort()
    return quick_picks


def validate_user_input(prompt):
    """Validates the user's input"""
    while True:
        try:
            number_of_picks = int(input(prompt))
            if number_of_picks <= 0:
                print("Invalid number.")
            else:
                return number_of_picks
        except ValueError:
            print("Please enter an integer."    )

main()