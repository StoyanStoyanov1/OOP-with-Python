from exams.exam_10_december_2022.project import BaseTeam


class OutdoorTeam(BaseTeam):
    TYPE = "OutdoorTeam"
    increases_advantage = 115
    BUDGET = 1000.0

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self.BUDGET)

    def win(self):
        self.advantage += self.increases_advantage
        self.wins += 1