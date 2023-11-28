from exams.exam_10_december_2022.project import ElbowPad
from exams.exam_10_december_2022.project import KneePad
from exams.exam_10_december_2022.project import IndoorTeam
from exams.exam_10_december_2022.project import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAM_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):

        if equipment_type not in self.VALID_EQUIPMENT_TYPES:
            raise ValueError("Invalid equipment type!")
        new_equipment = self.VALID_EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):

        if team_type not in self.VALID_TEAM_TYPES:
            raise ValueError("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        new_team = self.VALID_TEAM_TYPES[team_type](team_name, country, advantage)

        self.teams.append(new_team)

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = self.find_last_equipment_by_type(equipment_type)
        team = self.find_team_by_name(team_name)

        if equipment.price > team.budget:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self.find_team_by_name(team_name)

        if team is None:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        changed_eq_pcs = len([e.increase_price() for e in self.equipment if e.TYPE == equipment_type])

        return f"Successfully changed {changed_eq_pcs}pcs of equipment."

    def play(self, team_name1, team_name2):
        first_team = self.find_team_by_name(team_name1)
        second_team = self.find_team_by_name(team_name2)

        if not first_team.TYPE == second_team.TYPE:
            raise Exception("Game cannot start! Team types mismatch!")

        points_first_team = first_team.advantage + sum([e.protection for e in first_team.equipment])
        points_second_team = second_team.advantage + sum([e.protection for e in second_team.equipment])

        if points_first_team > points_second_team:
            first_team.win()
            return f"The winner is {first_team.name}."
        if points_first_team < points_second_team:
            second_team.win()
            return f"The winner is {second_team.name}."
        return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [f"""Tournament: {self.name}
Number of Teams: {len(self.teams)}
Teams:"""]
        [result.append(t.get_statistics()) for t in sorted_teams]
        return '\n'.join(result)

    def find_last_equipment_by_type(self, equipment_type):
        collection = [e for e in self.equipment if e.TYPE == equipment_type]
        return collection[-1] if collection else None

    def find_team_by_name(self, team_name):
        collection = [t for t in self.teams if t.name == team_name]
        return collection[0] if collection else None
