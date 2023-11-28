from typing import List
from exams.exam_10_december_2022.project.delicacies.stolen import Stolen
from exams.exam_10_december_2022.project.delicacies.gingerbread import Gingerbread
from exams.exam_10_december_2022.project.booths.open_booth import OpenBooth
from exams.exam_10_december_2022.project.booths.private_booth import PrivateBooth


class ChristmasPastryShopApp:
    TYPE_OF_DELICACIES = {Stolen.TYPE: Stolen, Gingerbread.TYPE: Gingerbread}
    TYPE_OF_BOOTHS = {PrivateBooth.TYPE: PrivateBooth, OpenBooth.TYPE: OpenBooth}

    def __init__(self):
        self.booths: List = []
        self.delicacies: List = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self.find_delicacy_by_name(name, self.delicacies):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.TYPE_OF_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.TYPE_OF_DELICACIES[type_delicacy](name, price)

        self.delicacies.append(delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self.find_booth_number(booth_number, self.booths):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.TYPE_OF_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.TYPE_OF_BOOTHS[type_booth](booth_number, capacity)

        self.booths.append(booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        current_booth = self.find_booth_number(booth_number, self.booths)
        current_delicacy = self.find_delicacy_by_name(delicacy_name, self.delicacies)
        if not current_booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not current_delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        current_booth.delicacy_orders.append(current_delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        current_booth = self.find_booth_number(booth_number, self.booths)

        bill = current_booth.price_for_reservation + sum([order.price for order in current_booth.delicacy_orders])

        self.income += bill

        current_booth.delicacy_orders = []
        current_booth.price_for_reservation = 0
        current_booth.is_reserved = False
        return (f"Booth {booth_number}:\n"
                f"Bill: {bill:.2f}lv.")

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    @staticmethod
    def find_delicacy_by_name(name, delicacy_list):
        for product in delicacy_list:
            if name == product.name:
                return product

        return False

    @staticmethod
    def find_booth_number(number, booth_list):
        for product in booth_list:
            if number == product.booth_number:
                return product

        return False
