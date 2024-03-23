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

    # Other methods for the Project class
