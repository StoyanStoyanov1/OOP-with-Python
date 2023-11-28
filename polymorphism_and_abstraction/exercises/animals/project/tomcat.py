from exams.exam_10_december_2022.project import Cat


class Tomcat(Cat):

    def __init__(self, name, age):
        super().__init__(name, age, gender="Male")

    def make_sound(self):
        return "Hiss"
