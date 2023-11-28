from unittest import TestCase, main
from oop.testing.lab.list.extended_list import IntegerList


class TestGunitSquad(TestCase):

    def setUp(self):
        self.list = IntegerList(2, 4, 3.8, True, (), "python")

    def test_successful_initial(self):
        self.assertEqual([2, 4], self.list._IntegerList__data)

    def test_successful_get_data(self):
        self.assertEqual([2, 4], self.list.get_data())

    def test_unsuccessful_add_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.list.add("new element")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_successful_add_to_list(self):
        self.list.add(35)
        self.assertEqual([2, 4, 35], self.list.get_data())
        self.assertEqual([2, 4, 35], self.list._IntegerList__data)

    def test_unsuccessful_remove_index_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.list.remove_index(10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_successful_remove_index_from_list(self):
        result = self.list.remove_index(0)
        self.assertEqual(2, result)
        self.assertEqual([4], self.list._IntegerList__data)

    def test_unsuccessful_get_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.list.get(5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_successful_get_item_from_list_by_index(self):
        result = self.list.get(0)

        self.assertEqual(2, result)
        self.assertEqual(2, self.list._IntegerList__data[0])

    def test_unsuccessful_insert_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.list.insert(5, 2)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_unsuccessful_insert_with_wrong_element_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.list.insert(0, "wow")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_successful_insert_element_in_list(self):
        self.list.insert(0, 7)

        self.assertEqual([7, 2, 4], self.list._IntegerList__data)

    def test_successful_get_biggest_element_in_list(self):
        result = self.list.get_biggest()
        self.assertEqual(4, result)

    def test_successful_get_index_element_in_list(self):
        result = self.list.get_index(2)
        self.assertEqual(0, result)


if __name__ == "__main__":
    main()
