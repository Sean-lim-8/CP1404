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

        elif choice == "S":
            filename = input("Filename: ")
            save_projects(filename, projects)
            print(f"Projects saved to {filename}")


def load_projects(filename):
    """Load projects from a file"""
    projects = []
    try:
        with open(filename, 'r') as file:
            file.readline()
            for line in file:
                parts = line.strip().split()('\t')
                if len(parts) == 5:
                    name = parts[0]
                    start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
                    priority = int(parts[2])
                    cost = float(parts[3])
                    completion = int(parts[4])
                    projects.append(Project(name, start_date, priority, cost, completion))
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return projects

def save_projects(filename, projects):
    """Save projects to a file"""
    with open(filename, 'w') as in_file:
        in_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            in_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost}\t{project.completion}\n")
    print(f"Saved {len(projects)} projects to {filename}.")

main()