from oop.class_and_static_methods.lab.hotel_rooms.project import Product


class Food(Product):

    def __init__(self, name, price, grams):
        super().__init__(name, price)
        self.__grams = grams

    @property
    def grams(self):
        return self.__grams