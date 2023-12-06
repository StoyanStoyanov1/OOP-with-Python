from abc import ABC, abstractmethod




class Astronaut(ABC):
    DECREASES_OXYGEN = 10

    def __init__(self, name: str, oxygen: int):
        self.name: str = name
        self.oxygen: int = oxygen
        self.backpack: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

        self.__name = value

    def breathe(self):
        self.oxygen -= self.DECREASES_OXYGEN

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

