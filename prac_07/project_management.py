import datetime

class Project:
    """Class to represent a project."""

    def __init__(self, name, start_date, priority, estimate, completion_percentage):
        """Initialize project attributes."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.estimate = float(estimate)
        self.completion_percentage = int(completion_percentage)

def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            name, start_date, priority, estimate, completion_percentage = line.strip().split('\t')
            project = Project(name, start_date, priority, estimate, completion_percentage)
            projects.append(project)
    return projects

# Test the load_projects function
projects = load_projects('projects.txt')
for project in projects:
    print(project.name, project.start_date, project.priority, project.estimate, project.completion_percentage)
