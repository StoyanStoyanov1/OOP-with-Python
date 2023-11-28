from oop.classes_and_objects.exercises.guild_system.project.player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if self.name == player.guild:
            return f"Player {player.name} is already in the guild."

        if player.guild != Player.DEFAULT_GUILD:
            return f"Player {player.name} is in another guild."

        self.players.append(player)

        player.guild = self.name

        return f"Welcome player {player.name} to the guild {player.guild}"
    def kick_player(self, player_name: str):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = Player.DEFAULT_GUILD

            return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = [f"Guild: {self.name}"]
        [result.append(player.player_info()) for player in self.players]

        return '\n'.join(result)



player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())



