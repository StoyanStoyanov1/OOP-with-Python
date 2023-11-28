from oop.inheritance.exercises.players_and_monsters.project import Lizard
from oop.inheritance.exercises.players_and_monsters.project import Mammal

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
