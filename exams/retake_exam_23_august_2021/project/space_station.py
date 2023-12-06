from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.uncompleted_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        astronaut = self.create_astronaut(astronaut_type, name)
        if astronaut:
            self.astronaut_repository.add(astronaut)
            return f"Successfully added {astronaut_type}: {name}."
        else:
            raise Exception("Astronaut type is not valid!")

    def create_astronaut(self, astronaut_type: str, name: str):
        astronaut_classes = {
            "Biologist": Biologist,
            "Geodesist": Geodesist,
            "Meteorologist": Meteorologist
        }
        astronaut_class = astronaut_classes.get(astronaut_type)
        if astronaut_class:
            return astronaut_class(name)
        return None

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(", ")
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut:
            self.astronaut_repository.remove(astronaut)
            return f"Astronaut {name} was retired!"
        else:
            raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        suitable_astronauts = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]
        suitable_astronauts.sort(key=lambda a: a.oxygen, reverse=True)
        suitable_astronauts = suitable_astronauts[:5]

        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        for counter, astronaut in enumerate(suitable_astronauts):
            while astronaut.oxygen > 0 and planet.items:
                astronaut.breathe()
                item = planet.items.pop()
                astronaut.backpack.append(item)

            if not planet.items:
                self.successful_missions += 1
                return f"Planet: {planet_name} was explored. {counter + 1} astronauts participated in collecting items."

        self.uncompleted_missions += 1
        return "Mission is not completed."

    def report(self):
        report_lines = [
            f"{self.successful_missions} successful missions!",
            f"{self.uncompleted_missions} missions were not completed!",
            "Astronauts' info:"
        ]
        for astronaut in self.astronaut_repository.astronauts:
            backpack_items = ', '.join(astronaut.backpack) if astronaut.backpack else "none"
            report_lines.append(f"Name: {astronaut.name}\nOxygen: {astronaut.oxygen}\nBackpack items: {backpack_items}")
        return "\n".join(report_lines)
