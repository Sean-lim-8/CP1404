"""
CP1404 Practical 7
Project Management
Estimate: 1 hour
Actual:
"""

from datetime import datetime
from project import Project
from operator import attrgetter

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

        elif choice == "D":
            display_projects(projects)

        elif choice == "F":
            filter_projects(projects)

        elif choice == "A":
            add_projects(projects)





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


def display_projects(projects):
    """Display projects grouped by completion status"""
    incomplete_projects = [p for p in projects if not p.is_complete()]
    completed_projects = [p for p in projects if p.is_complete()]
    incomplete_projects.sort()
    completed_projects.sort()

    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects: ")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects(projects):
    """Filter projects by date"""
    date = input("Show projects that start after date (dd/mm/yy): ")
    try:
        filter_date = datetime.strptime(date, "%d/%m/%Y").date()
        filtered_projects  = [p for p in projects if p.start_date >= filter_date]
        filtered_projects.sort(key=attrgetter('start_date'))

        for projects in filtered_projects:
            print(projects)
    except ValueError:
        print("Invalid date.")


def add_projects(projects):
    """Add a new project"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate : $"))
    completion = int(input("Percent complete: "))

    start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
    new_project = Project(name, start_date, priority, cost, completion)
    projects.append(new_project)

    




main()