from exams.exam_10_december_2022.project import mapper_month


class DVD:

    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        _, month, year = date.split('.')
        month = mapper_month[int(month)]
        return cls(name, id, int(year), month, age_restriction)

    def __repr__(self):
        rented = "rented" if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {rented}"


