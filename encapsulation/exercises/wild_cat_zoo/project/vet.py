from oop.class_and_static_methods.lab.hotel_rooms.project import Worker


class Vet(Worker):

    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)