from oop.inheritance.lab.multiple_ingeritance.project.employee import Employee
from oop.inheritance.lab.multiple_ingeritance.project.person import Person


class Teacher(Employee, Person):

    def teach(self):
        return "teaching..."
