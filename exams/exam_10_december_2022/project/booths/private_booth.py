from exams.exam_10_december_2022.project.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_PER_PERSON = 3.50
    TYPE = "Private Booth"

    def reserve(self, number_of_people: int):
        self.price_for_reservation += number_of_people * self.PRICE_PER_PERSON
        self.is_reserved = True
