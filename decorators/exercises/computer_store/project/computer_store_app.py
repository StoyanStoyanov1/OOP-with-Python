from typing import List
from exams.exam_10_december_2022.project import Computer
from exams.exam_10_december_2022.project import DesktopComputer
from exams.exam_10_december_2022.project import Laptop


class ComputerStoreApp:

    VALID_COMPUTERS = {"Desktop Computer": DesktopComputer,
                       "Laptop": Laptop,
                       }

    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int) -> str:
        try:
            computer = self.VALID_COMPUTERS[type_computer](manufacturer, model)

        except KeyError:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        configuration = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)

        return configuration

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget and\
                    computer.processor == wanted_processor and \
                        computer.ram >= wanted_ram:

                self.profits += client_budget - computer.price
                self.warehouse.remove(computer)

                return f"{computer} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")
