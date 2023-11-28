from oop.inheritance.exercises.players_and_monsters.project.hero import Hero


class Elf(Hero):

    def __str__(self):
        return f"{self.username} of type {Elf.__name__} has level {self.level}"
