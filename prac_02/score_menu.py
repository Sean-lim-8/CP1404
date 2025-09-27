"""
CP1404 - Practical 2
Program to display a menu to get a score and print results and stars depending on the score.
"""
from score import determine_score

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    print(MENU)
    choice = input("Please choose an option: ").upper()
    score = determine_score(MENU)

def print_results(score):
    results = determine_score(score)
    print(f"Results:{results}")

def print_stars(score):
    print(int(score) * "*")

