class Player:

    DEFAULT_GUILD = "Unaffiliated"

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = Player.DEFAULT_GUILD

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"

        self.skills = {skill_name: mana_cost}
        return  f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        current_info = [f"Name: {self.name}", f"Guild: {self.guild}", f"HP: {self.hp}", f"MP: {self.mp}"]
        [current_info.append(f"==={name} - {mana}\n") for name, mana in self.skills.items()]

        return '\n'.join(current_info)



