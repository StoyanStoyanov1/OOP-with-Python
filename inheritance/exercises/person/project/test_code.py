from oop.inheritance.exercises.person.project.child import Child
from oop.inheritance.exercises.person.project.person import Person

person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)