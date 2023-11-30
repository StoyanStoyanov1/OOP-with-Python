from abc import ABC

from exams.retake_exam_18_april_2022.project.user import User


class Movie(ABC):
    DEFAULT_AGE_RESTRICTION = 0

    def __init__(self, title: str, year: int, owner: User, age_restriction: int):
        self.title: str = title
        self.year: int = year
        self.owner: object = owner
        self.age_restriction: int = age_restriction
        self.likes: int = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if value == "":
            raise ValueError("The title cannot be empty string!")

        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")

        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if type(value).__name__ != "User":
            raise ValueError("The owner must be an object of type User!")

        self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.DEFAULT_AGE_RESTRICTION:
            raise ValueError(
                f"{type(self).__name__} movies must be restricted for audience under {self.DEFAULT_AGE_RESTRICTION} years!")

        self.__age_restriction = value

    def details(self):
        return (f"{type(self).__name__} - Title:{self.title}, "
                f"Year:{self.year}, "
                f"Age restriction:{self.age_restriction}, "
                f"Likes:{self.likes}, "
                f"Owned by:{self.owner.username}")
