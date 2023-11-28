from exams.exam_10_december_2022.project import FormulaTeam


class RedBullTeam(FormulaTeam):

    def sponsors(self):
        return {"Oracle": {1: 1_500_000,
                           2: 800_000},
                "Honda": {8: 20_000,
                          10: 10_000}}

    @property
    def expenses_for_one_race(self):
        return 250_000


