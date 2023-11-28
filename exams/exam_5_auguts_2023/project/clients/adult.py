from exams.exam_10_december_2022.project import BaseClient


class Adult(BaseClient):
    TYPE = "Adult"
    INITIAL_INTEREST = 4.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=self.INITIAL_INTEREST)

    def increase_clients_interest(self):
        self.interest += 2
