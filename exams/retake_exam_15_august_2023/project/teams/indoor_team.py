from exams.exam_10_december_2022.project import BaseTeam


class IndoorTeam(BaseTeam):
    TYPE = "IndoorTeam"
    increases_advantage = 145
    BUDGET = 500.0

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self.BUDGET)

    def win(self):
        self.advantage += self.increases_advantage
        self.wins += 1

