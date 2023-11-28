class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, damage):
        self.health -= damage
        if not self.health > 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, amount):
        self.health += amount


hero = Hero("Alexander", 75)
print(hero.name, "Alexander")
print(hero.health, 75)
