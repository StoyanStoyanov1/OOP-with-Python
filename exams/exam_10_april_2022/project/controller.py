from typing import List

from exams.exam_11_dezember_2021.project import Player
from exams.exam_11_dezember_2021.project import Supply


class Controller:

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    @staticmethod
    def _duel(first: Player, second: Player):

        second.stamina = max(0, second.stamina - first.stamina * 0.5)
        if second.stamina == 0:
            return first

        first.stamina = max(0, first.stamina - second.stamina * 0.5)
        if first.stamina == 0:
            return second

        return first if first.stamina > second.stamina else second

    def _find_player_by_name(self, name):
        for player in self.players:
            if player.name == name:
                return player

    def _find_supply_and_remove(self, given_type):

        for index in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[index]
            if type(supply).__name__ == given_type:
                self.supplies.pop(index)
                return supply

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player not in self.players:
                added_players.append(player.name)
                self.players.append(player)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self._find_player_by_name(player_name)

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."
        if sustenance_type in ['Food', 'Drink']:
            supply = self._find_supply_and_remove(sustenance_type)
            if not supply:
                raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

            player.stamina = min(100, player.stamina + supply.energy)

            return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self._find_player_by_name(first_player_name)
        second_player = self._find_player_by_name(second_player_name)

        if first_player.stamina == 0 or second_player.stamina == 0:
            if first_player.stamina == 0 and second_player.stamina == 0:
                return (f"Player {first_player.name} does not have enough stamina.\n"
                        f"Player {second_player.name} does not have enough stamina.")

            player = first_player.name if first_player.stamina == 0 else second_player.name

            return f"Player {player} does not have enough stamina."

        if first_player.stamina < second_player.stamina:
            winner = self._duel(first_player, second_player)
        else:
            winner = self._duel(second_player, first_player)

        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(0, player.stamina - player.age * 2)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        result.extend([str(player) for player in self.players])
        result.extend([supply.details() for supply in self.supplies])

        return "\n".join(result)
