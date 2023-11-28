from oop.class_and_static_methods.lab.hotel_rooms.project import Beverage


class ColdBeverage(Beverage):

    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)