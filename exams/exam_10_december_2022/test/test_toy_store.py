import unittest
from project.toy_store import ToyStore


class TestToyStore(unittest.TestCase):

    def test_correct_init(self):
        self.toy_store = ToyStore()
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_add_toy_if_shelf_not_in_toy_shelf_keys(self):
        self.toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("S", "Name")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_if_shelf_and_name_are_exists(self):
        self.toy_store = ToyStore()
        self.toy_store.add_toy("A", "Name")
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Name")
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_if_shelf_is_exist_but_value_is_not_none(self):
        self.toy_store = ToyStore()
        result = self.toy_store.add_toy("A", "Name")
        expected_result = "Toy:Name placed successfully!"
        self.assertEqual(result, expected_result)
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": "Name",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Other Name")
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_remove_toy_if_shelf_not_exist(self):
        self.toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("S", "Name")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_toy_that_shelf_does_not_exist(self):
        self.toy_store.add_toy("A", "Name")
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "Other Name")
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy(self):
        self.toy_store = ToyStore()
        self.toy_store.add_toy("A", "Name")
        result = self.toy_store.remove_toy("A", "Name")
        expected_result = f"Remove toy:Name successfully!"

        self.assertEqual(result, expected_result)
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })


if __name__ == "__main__":
    unittest.main()
