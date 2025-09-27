"""
CP1404 - Practical 2
Program to display a menu to get a score and print results and stars depending on the score.
"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

def get_valid_score():
    """validates user's score"""
    score = float(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Please enter a valid score between 0 and 100")
        score = float(input("Enter your score: "))
    return score


def main():
    score = 0
    print(MENU)
    choice = input("Choose an option: ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_results(score)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")

        print(MENU)
        choice = input("Choose an option: ").upper()

    print("Farewell")

def determine_score(score):
    """Determines user's score"""
    if score < 0 or score > 100:
        message = "Invalid score"
    elif score >= 90:
        message = "Excellent"
    elif score >= 50:
        message = "Passable"
    else:
        message = "Bad"
    return message

def print_results(score):
    """Prints results in a message"""
    results = determine_score(score)
    print(f"Results:{results}")

def print_stars(score):
    """Prints stars according to the score"""
    print(int(score) * "*")

main()