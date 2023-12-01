from typing import List
from exams.exam_11_dezember_2021.project.car.muscle_car import MuscleCar
from exams.exam_11_dezember_2021.project.car.sports_car import SportsCar
from exams.exam_11_dezember_2021.project.driver import Driver
from exams.exam_11_dezember_2021.project.race import Race


class Controller:
    POSSIBLE_TYPES = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars: List = []
        self.drivers: List = []
        self.races: List = []

    def _find_model_car(self, model):
        for car in self.cars:
            if car.model == model:
                return car

    def _find_driver(self, name):
        for driver in self.drivers:
            if driver.name == name:
                return driver

    def _find_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in ["MuscleCar", "SportsCar"]:

            if self._find_model_car(model):
                raise Exception(f"Car {model} is already created!")

            new_car = Controller.POSSIBLE_TYPES[car_type](model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self._find_driver(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self._find_race(race_name):
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self._find_driver(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        found_type_cars = [car for car in self.cars if type(car).__name__ == car_type]

        for i in range(len(found_type_cars) - 1, -1, -1):
            car = found_type_cars[i]
            if not car.is_taken:
                if driver.car:
                    old_model = driver.car.model
                    driver.car.is_taken = False
                    driver.car = car
                    car.is_taken = True
                    return f"Driver {driver.name} changed his car from {old_model} to {car.model}."
                else:
                    driver.car = car
                    car.is_taken = True
                    return f"Driver {driver_name} chose the car {car.model}."

        raise Exception(f"Car {car_type} could not be found!")

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self._find_race(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        driver = self._find_driver(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        for race_driver in race.drivers:
            if race_driver == driver:
                return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self._find_race(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        top_3_drivers = list(sorted(race.drivers, key=lambda driver: -driver.car.speed_limit))[:3]
        result = []
        for driver in top_3_drivers:
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return "\n".join(result)
