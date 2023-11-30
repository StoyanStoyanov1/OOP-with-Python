from exams.exam_11_dezember_2021.project import Plantation
import unittest


class TestPlantation(unittest.TestCase):

    def setUp(self):
        self.plantation = Plantation(20)

    def test_init(self):
        self.assertEqual(self.plantation.size, 20)
        self.assertEqual(self.plantation.plants, {})
        self.assertEqual(self.plantation.workers, [])

    def test_props(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation = Plantation(-1)

        self.assertEqual(str(ve.exception), "Size must be positive number!")

    def test_hire_worker(self):
        result = self.plantation.hire_worker('test')
        expected_result = "test successfully hired."
        self.assertEqual(result, expected_result)
        self.assertEqual(self.plantation.workers, ['test'])

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker('test')
        self.assertEqual(str(ve.exception), "Worker already hired!")

    def test_len(self):
        self.plantation.plants = {"one": "one", "two": "two"}
        result = len(self.plantation)
        self.assertEqual(result, 6)
        self.assertEqual(self.plantation.plants, {"one": "one", "two": "two"})

    def test_planting(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("test", "test")
        self.assertEqual(str(ve.exception), "Worker with name test is not hired!")

        self.plantation.workers = ['test', 'one', 'three']
        self.plantation.plants = {"one": ['as', 'ads'], "two": ['one', 'three']}
        self.plantation.size = 2
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('test', 'test')
        self.assertEqual(str(ve.exception), "The plantation is full!")

        self.plantation.size = 20
        self.plantation.plants = {"one": ['one'], "two": ['two']}

        result = self.plantation.planting("one", 'two')
        expected_result = "one planted two."
        self.assertEqual(result, expected_result)
        self.assertEqual(self.plantation.plants, {"one": ['one', 'two'], "two": ['two']})

        result = self.plantation.planting('three', 'one')
        expected_result = "three planted it's first one."

        self.assertEqual(result, expected_result)
        self.assertEqual(self.plantation.plants, {"one": ['one', 'two'], "two": ['two'], "three": ["one"]})

    def test_str(self):
        self.plantation.workers = ['test', 'second_test']
        self.plantation.plants = {'one': ['one', 'two'], 'two': ['one', 'two']}
        result = str(self.plantation)
        expected_result = "Plantation size: 20\ntest, second_test\none planted: one, two\ntwo planted: one, two"
        self.assertEqual(result, expected_result)

    def test_repr(self):
        self.plantation.workers = ['test', 'second_test']
        result = repr(self.plantation)
        expected_result = "Size: 20\nWorkers: test, second_test"
        self.assertEqual(result, expected_result)
