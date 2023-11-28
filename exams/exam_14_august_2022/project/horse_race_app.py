from project.horse_race import HorseRace
from project.horse_specification.horse import Horse
from project.jockey import Jockey
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class HorseRaceApp:
    VALID_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: list[Horse] = []
        self.jockeys: list[Jockey] = []
        self.horse_races: list[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if self.find_by_name(horse_name, self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type in self.VALID_TYPES:
            new_horse = self.VALID_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)

            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.find_by_name(jockey_name, self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jokey = Jockey(jockey_name, age)
        self.jockeys.append(new_jokey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self._find_type_horse_race(race_type):
            raise Exception(f"Race {race_type} has been already created!")

        new_horse_race = HorseRace(race_type)
        self.horse_races.append(new_horse_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.find_by_name(jockey_name, self.jockeys)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        type_horses = [horse for horse in self.horses if type(horse).__name__ == horse_type and not horse.is_taken]

        if not type_horses:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        horse = type_horses[-1]

        horse.is_taken = True
        jockey.horse = horse

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = self._find_type_horse_race(race_type)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.find_by_name(jockey_name, self.jockeys)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)

        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = self._find_type_horse_race(race_type)

        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = None

        for jockey in horse_race.jockeys:
            if not winner:
                winner = jockey
            elif jockey.horse.speed > winner.horse.speed:
                winner = jockey

        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

    @staticmethod
    def find_by_name(name, current_list):
        for current_object in current_list:
            if current_object.name == name:
                return current_object

    def _find_type_horse_race(self, search_type):
        for horse_race in self.horse_races:
            if horse_race.race_type == search_type:
                return horse_race
