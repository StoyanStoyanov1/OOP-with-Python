from exams.exam_10_december_2022.project import BaseEquipment


class ElbowPad(BaseEquipment):
    TYPE = "ElbowPad"
    PROTECTION = 90
    PRICE = 25.0
    INCREASES_PRICE_PERCENT = 1.1

    def __init__(self):
        super().__init__(protection=self.PROTECTION, price=self.PRICE)

    def increase_price(self):
        self.price *= self.INCREASES_PRICE_PERCENT


