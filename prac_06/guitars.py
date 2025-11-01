"""
CP1404 - Practical 6
Guitars
Estimate: 25 minutes
Actual: 35 minutes
"""

from guitar import Guitar

def main():
    """Program to manage guitar collection"""
    guitars = []

    print("My guitars!")

    name =  input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16055.40))
    guitars.append(Guitar("Another Guitar", 2013, 1512.9))

    print("These are my guitars:")

    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost:>10,.2f}{vintage_string}")

main()
