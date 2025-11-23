"""
CP1404 Practical 9
Band
"""

class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def __str__(self):
        musician_strings = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_strings}) "

    def play(self):
        results = []
        for musician in self.musicians:
            results.append(musician.play())
        return "\n".join(results)

