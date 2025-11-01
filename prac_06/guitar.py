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

