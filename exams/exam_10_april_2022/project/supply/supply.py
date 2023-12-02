from abc import ABC


class Supply(ABC):

    def __init__(self, name: str, energy: int):
        self.name: str = name
        self.energy: int = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be an empty string.")

        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        if value < 0:
            raise ValueError("Energy cannot be less than zero.")

        self.__energy = value

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
