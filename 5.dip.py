"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""


from abc import ABC, abstractclassmethod

class Report(ABC):

    def __init__(self, char) -> None:
        self.char = char

    @abstractclassmethod
    def report(self):
        pass

class Player:

    def __init__(self, name, reporter: Report):
        self.__reporter = reporter
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name

class StatsReporter(Report):

    def __init__(self, char: Player) -> None:
        super().__init__(char)

    def report(self):
        print(f'Name:{self.char.name()}')
        print(f'HP:{self.char.hp()}')