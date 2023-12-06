from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    DECREASES_OXYGEN = 5

    def __init__(self, name, oxygen=70):
        super().__init__(name, oxygen)