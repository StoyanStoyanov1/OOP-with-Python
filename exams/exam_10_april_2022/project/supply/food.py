from exams.exam_11_dezember_2021.project import Supply


class Food(Supply):

    def __init__(self, name: str, energy: int = 25):
        super().__init__(name, energy)
