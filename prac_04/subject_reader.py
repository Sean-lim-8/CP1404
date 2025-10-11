"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(subject_data=data)

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

def display_subject_details(subject_data):
    """Displays the subject details"""

    for subject in subject_data:
        subject_code, name, number_of_students = subject
        print(f"{subject_code} is taught by {name} and has {number_of_students} students.")


main()