from abc import ABC, abstractmethod


class Meal(ABC):
    TYPE = "Meal"

    def __init__(self, name: str, price: float, quantity: int):
        self.name: str = name
        self.price: float = price
        self.quantity: int = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be an empty string!")

        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Invalid price!")

        self.__price = value

    @abstractmethod
    def details(self) -> str:
        pass
