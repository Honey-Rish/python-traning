from abc import ABC, abstractmethod

# Abstract class
class Player(ABC):
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f"{self.name} - {self.country}"

    @abstractmethod
    def getpoints(self):
        pass



class Cricketer(Player):
    def __init__(self, name, country, runs, wickets):
        super().__init__(name, country)
        self.runs = runs
        self.wickets = wickets

    def __str__(self):
        return self.__str__() + f" - {self.runs} - {self.wickets}"

    def getpoints(self):
        return (self.runs // 100) + (self.wickets // 5)  # 100 runs-1 point, 5 wickets 1 point


class Footballer(Player):
    def __init__(self, name, country, goals, appearances):
        super().__init__(name, country)
        self.goals = goals
        self.appearances = appearances

    def getpoints(self):
        return (self.goals * 2) + self.appearances  # 1 goal 2 points, 1 appearance 1 point

    def __str__(self):
        return self.__str__() + f" - {self.goals} - {self.appearances}"


c = Cricketer("Dhoni", "India", 1000, 10)
print(c.getpoints())

f = Footballer("Messi", "Argentina", 10, 70)
print(f.getpoints())