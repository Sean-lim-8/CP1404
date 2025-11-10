"""
CP1404 Practical 7
Project Management
Estimate: 1 hour
Actual:
"""

from datetime import datetime
from project import Project

FILENAME = "projects.txt"

MENU = """
(L)oad projects
(S)ave projects
(D)isplay projects
(F)ilter projects by date
(A)dd new project
(U)pdate project
(Q)uit
"""

def main():
    """Main function"""
    print("Welcome to Phytonic Project Management")
    projects = load_projects(FILENAME)
    print(f"{len(projects)} projects from {FILENAME}.")

    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").strip().upper()

        if choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}.")


def load_projects(filename):
    """Load projects from a file"""
    projects = []
    try:
        with open(filename, 'r') as file:
            file.readline()
            for line in file:
                parts = line.strip().split()('\t')
                if len(parts) == 5:
                    start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
                    priority = int(parts[2])
                    cost_estimate = float(parts[3])
                    completion_percentage = int(parts[4])
                    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return projects