from exams.exam_10_december_2022.project import Robot
from unittest import TestCase


class TestRobot(TestCase):

    def setUp(self) -> None:
        self.robot = Robot("005", "Education", 100, 100000.00)
        self.other_robot = Robot("007", "Military", 50, 10000)

    def test_init(self):
        self.assertEqual("005", self.robot.robot_id)
        self.assertEqual("Education", self.robot.category)
        self.assertEqual(100, self.robot.available_capacity)
        self.assertEqual(100000.00, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_if_not_one_of_allowed_categories(self):

        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Robot"

        expected_result = "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'"
        self.assertEqual(expected_result, str(ve.exception))

    def test_price_if_price_is_negative(self):

        with self.assertRaises(ValueError) as ve:
            self.robot.price = -100

        expected_result = "Price cannot be negative!"
        self.assertEqual(expected_result, str(ve.exception))

    def test_upgrade_if_hardware_component_is_in_hardware_upgrades(self):
        self.robot.hardware_upgrades = ["New Upgrade"]
        result = self.robot.upgrade("New Upgrade", 10000.0)
        expected_result = "Robot 005 was not upgraded."
        self.assertEqual(expected_result, result)

    def test_upgrade(self):
        result = self.robot.upgrade("New Upgrade", 10000.0)
        self.assertEqual(["New Upgrade"], self.robot.hardware_upgrades)
        self.assertEqual(115000.0, self.robot.price)
        expected_result = "Robot 005 was upgraded with New Upgrade."
        self.assertEqual(expected_result, result)

    def test_update_if_cannot_update(self):
        self.robot.software_updates = [3.5]
        result = self.robot.update(2.5, 20)
        expected_result = "Robot 005 was not updated."
        self.assertEqual(expected_result, result)

        second_result = self.robot.update(3.6, 102)
        self.assertEqual(expected_result, second_result)

    def test_update(self):
        result = self.robot.update(5.1, 50)
        self.assertEqual([5.1], self.robot.software_updates)
        self.assertEqual(50, self.robot.available_capacity)
        expected_result = "Robot 005 was updated to version 5.1."
        self.assertEqual(expected_result, result)

    def test_gt(self):
        first_result = self.robot.__gt__(self.other_robot)
        first_expected_result = 'Robot with ID 005 is more expensive than Robot with ID 007.'
        self.assertEqual(first_expected_result, first_result)

        self.robot.price = 10000
        second_result = self.robot.__gt__(self.other_robot)
        second_expected_result = 'Robot with ID 005 costs equal to Robot with ID 007.'
        self.assertEqual(second_expected_result, second_result)

        self.robot.price = 5000
        third_result = self.robot.__gt__(self.other_robot)
        third_expected_result = 'Robot with ID 005 is cheaper than Robot with ID 007.'
        self.assertEqual(third_expected_result, third_result)
