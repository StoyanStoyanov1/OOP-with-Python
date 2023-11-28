from oop.inheritance.exercises.players_and_monsters.project.wizard import Wizard


class DarkWizard(Wizard):

    def __str__(self):
        return f"{self.username} of type {DarkWizard.__name__} has level {self.level}"