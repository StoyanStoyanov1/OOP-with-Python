from oop.class_and_static_methods.lab.hotel_rooms.project import Food


class Dessert(Food):

    def __init__(self, name, price, grams, calories):
        super().__init__(name, price, grams)
        self.__calories = calories

    @property
    def calories(self):
        return self.__calories
