"""
CP1404 - Practical 6
Guitar
Estimate: 30 minutes
Actual:
"""

class Guitar:
    """Represent guitar"""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a string representation of guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Returns the age of the guitar in years"""
        return 2022 - self.year

    def is_vintage(self):
        """Determines if the guitar is vintage or not"""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Returns true if chosen guitar is older than the other guitar"""
        return self.year < other.year


