from typing import List

from exams.exam_11_dezember_2021.project.driver import Driver


class Race:

    def __init__(self, name: str):
        self.name: str = name
        self.drivers: List[Driver] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Name cannot be an empty string!")

        self.__name = value