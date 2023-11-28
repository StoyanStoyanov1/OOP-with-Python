from oop.class_and_static_methods.lab.hotel_rooms.project import Product


class Drink(Product):

    def __init__(self, name):
        super().__init__(name, 10)
