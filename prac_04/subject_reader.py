"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)

def load_data():
    """Read data from file and formats it into subject, name, number of students"""
    subject_data = []

    with open(FILENAME, "r") as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(",")
            parts[2] = int(parts[2])
            subject_data.append(parts)
    return subject_data



main()