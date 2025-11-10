from datetime import datetime

class Project:
    """Represents a project"""
    def __init__(self, name, start_date, priority, cost, completion):
        """Initialise a project instance"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion = completion

