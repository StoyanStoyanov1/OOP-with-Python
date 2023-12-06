from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    DECREASES_OXYGEN = 15

    def __init__(self, name, oxygen=90):
        super().__init__(name, oxygen)
