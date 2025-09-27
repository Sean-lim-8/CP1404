"""
CP1404/CP5632 - Practical
Program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    message = determine_score(score)
    print(message)


def determine_score(score):
    if score < 0 or score > 100:
        message = "Invalid score"
    elif score >= 90:
        message = "Excellent"
    elif score >= 50:
        message = "Passable"
    else:
        message = "Bad"
    return message


main()