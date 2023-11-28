from oop.class_and_static_methods.lab.hotel_rooms.project import Animal


class Tiger(Animal):

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, 45)