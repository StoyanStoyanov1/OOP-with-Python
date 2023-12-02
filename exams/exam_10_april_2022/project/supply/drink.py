from exams.exam_11_dezember_2021.project import Supply


class Drink(Supply):

    def __init__(self, name: str, energy: int = 15):
        super().__init__(name, energy)
