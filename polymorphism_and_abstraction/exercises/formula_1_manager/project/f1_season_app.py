from exams.exam_10_december_2022.project import MercedesTeam
from exams.exam_10_december_2022.project import RedBullTeam


class F1SeasonApp:

    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name, budget):
        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)

        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)

        else:
            raise ValueError("Invalid team name!")

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.mercedes_team or not self.red_bull_team:
            raise Exception("Not all teams have registered for the season.")

        red_bull_revenue = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_revenue = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)

        ahead_team = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"
        return f"Red Bull: {red_bull_revenue}. Mercedes: {mercedes_revenue}. {ahead_team} is ahead at the {race_name} race."
