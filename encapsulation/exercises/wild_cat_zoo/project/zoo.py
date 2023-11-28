from oop.class_and_static_methods.lab.hotel_rooms.project import Animal
from oop.class_and_static_methods.lab.hotel_rooms.project import Worker


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal,  price):
        if self.__budget < price:
            return "Not enough budget"

        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker:Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_money = 0
        for worker in self.workers:
            needed_money += worker.salary

        if needed_money > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= needed_money

        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed_money = 0

        for animal in self.animals:
            needed_money += animal.money_for_care

        if needed_money > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= needed_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += self.__build_animal_str(self.animals, "Lion")
        result += self.__build_animal_str(self.animals, "Tiger")
        result += self.__build_animal_str(self.animals, "Cheetah")

        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        result += self.__build_animal_str(self.workers, "Keeper")
        result += self.__build_animal_str(self.workers, "Caretaker")
        result += self.__build_animal_str(self.workers, "Vet")

        return result.strip()

    def __build_animal_str(self,entities, entity_type):
        counter = 0
        result = ""

        for obj in entities:
            if obj.__class__.__name__ == entity_type:
                counter += 1
                result += repr(obj) + "\n"

        return f"----- {counter} {entity_type}s:\n" + result


