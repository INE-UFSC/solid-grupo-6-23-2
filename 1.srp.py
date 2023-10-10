"""
Single Responsibility Principle

Uma classe deve ter somente uma responsabilidade
ou
Uma classe deve ter somente um motivo para mudar
"""

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

class DataSave:
    def __init__(self, animal: Animal) -> None:
        self.__animal = animal

    def save(self):
        pass