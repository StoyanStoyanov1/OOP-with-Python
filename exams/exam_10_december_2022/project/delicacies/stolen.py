from exams.exam_10_december_2022.project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    PORTION = 250
    TYPE = "Stolen"

    def __init__(self, name: str, price: float):
        super().__init__(name, self.PORTION, price)

