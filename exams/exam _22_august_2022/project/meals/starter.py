from project.meals.meal import Meal


class Starter(Meal):
    TYPE = "Starter"
    QUANTITY = 60

    def __init__(self, name: str, price: float, quantity: int = QUANTITY):
        super().__init__(name, price, quantity)

    def details(self) -> str:
        return f"Starter {self.name}: {self.price:.2f}lv/piece"