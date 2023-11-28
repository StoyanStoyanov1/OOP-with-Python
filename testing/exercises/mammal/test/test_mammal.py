from unittest import TestCase, main

from exams.exam_10_december_2022.project import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("some name", "some type", "some sound")

    def test_if_instance_is_correct(self):
        self.assertEqual("some name", self.mammal.name)
        self.assertEqual("some type", self.mammal.type)
        self.assertEqual("some sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_by_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("some name makes some sound", result)

    def test_by_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_by_get_info(self):
        result = self.mammal.info()
        self.assertEqual("some name is of type some type", result)


if __name__ == "__main__":
    main()
