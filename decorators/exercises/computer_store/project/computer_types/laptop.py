from exams.exam_10_december_2022.project import Computer


class Laptop(Computer):

    @property
    def available_processors(self):
        return {"AMD Ryzen 9 5950X": 900,
                "Intel Core i9-11900H": 1050,
                "Apple M1 Pro": 1200
                }

    @property
    def max_ram(self):
        return 64

    @property
    def type(self):
        return "laptop"

