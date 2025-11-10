"""
CP1404 - Practical 7
MyGuitar
Estimate: 30 minutes
Actual:
"""

from guitar import Guitar

def main():
    """Main function to read, display, and sort guitars"""
    print("My guitars:")
    guitars = read_guitars("guitars.csv")

    guitars.sort()
    display_guitars(guitars)


def read_guitars(filename):
    """Read guitars from a csv file and changes it into a list of objects"""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                name = parts[0]
                year = int(parts[1])
                cost = float(parts[2])
                guitar = Guitar(name, year, cost)
                guitars.append(guitar)
    return guitars

def display_guitars(guitars):
    """Displays a list of guitars"""
    for guitar in guitars:
        print(guitar)

main()



