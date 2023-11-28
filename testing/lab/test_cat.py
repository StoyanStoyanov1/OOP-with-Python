class Cat:
    def __init__(self, name):

        self.name = name

        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):

        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):

        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main


class TestCat(TestCase):

    def setUp(self):
        self.cat = Cat("Jerry")

    def test_if_caft_is_initialized_successfully(self):
        self.assertEqual("Jerry", self.cat.name)
        self.assertEqual(False, self.cat.fed)
        self.assertEqual(False, self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_if_cat_size_is_increased_after_eating(self):
        self.cat.eat()
        self.assertEqual(True, self.cat.fed)
        self.assertEqual(True, self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_if_fed_is_true(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_sleeping(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertEqual(False, self.cat.sleepy)

    def test_if_is_hungry(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))


if __name__ == "__main__":
    main()
