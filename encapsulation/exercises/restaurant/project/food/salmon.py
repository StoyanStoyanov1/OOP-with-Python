from oop.class_and_static_methods.lab.hotel_rooms.project import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self, name, price):
        super().__init__(name, price, Salmon.GRAMS)
