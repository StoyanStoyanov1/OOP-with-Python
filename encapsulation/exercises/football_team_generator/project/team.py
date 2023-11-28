from oop.class_and_static_methods.lab.hotel_rooms.project import Player


class Team:

    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []


    def add_player(self, player: Player):

        for team_player in self.__players:
            if team_player.name == player.name:
                return f"Player {player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        for player in self.__players:
            if player_name == player.name:
                self.__players.remove(player)
                return player

        return f"Player {player_name} not found"



