"""
CP1404 - Practical 6
Programming language
Estimate: 20 minutes
Actual:
"""

class ProgrammingLanguage:
    """Represent programming languages"""

    def __init__(self, name, typing, reflection, year):
        """Initialise programming language with information"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
