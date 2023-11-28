from exams.exam_10_december_2022.project import BaseLoan


class MortgageLoan(BaseLoan):

    TYPE = "MortgageLoan"
    INTEREST_RATE = 3.5
    AMOUNT = 50000.0

    def __init__(self):
        super().__init__(interest_rate=self.INTEREST_RATE, amount=self.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.5
