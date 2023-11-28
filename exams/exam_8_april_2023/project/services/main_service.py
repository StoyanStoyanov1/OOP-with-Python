from exams.exam_10_december_2022.project import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)

    def details(self):
        robots = " ".join([r.name for r in self.robots])
        return f"{self.name} Main Service:\nRobots: {robots if robots else 'none'}"
