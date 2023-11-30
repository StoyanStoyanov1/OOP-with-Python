from exams.retake_exam_18_april_2022.project.movie_specification.movie import Movie
from exams.retake_exam_18_april_2022.project.user import User


class Fantasy(Movie):
    DEFAULT_AGE_RESTRICTION = 6

    def __init__(self, title: str, year: int, owner: User, age_restriction=DEFAULT_AGE_RESTRICTION):
        super().__init__(title, year, owner, age_restriction)
