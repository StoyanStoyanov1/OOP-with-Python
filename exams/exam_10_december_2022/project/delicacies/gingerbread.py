from exams.exam_10_december_2022.project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    PORTION = 200
    TYPE = "Gingerbread"

    def __init__(self, name: str, price: float):
        super().__init__(name, self.PORTION, price)

