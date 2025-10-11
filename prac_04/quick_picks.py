"""
CP1404 - Practical 4
Program to generate quick pick numbers
"""
import random

def main():
    """Asks the user how many quick pick numbers to generate"""
    number_of_picks = int(input("How many quick picks?: "))


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
            print("Please enter an integer.")

