"""
CP1404 - Practical 6
Guitars
Estimate: 25 minutes
Actual:
"""

from guitar import Guitar

def main():
    """Program to manage guitar collection"""
    guitars = []

    print("My guitars!")

    name =  input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = input("Cost: ")

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")
