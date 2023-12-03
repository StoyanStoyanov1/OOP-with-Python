from project.truck_driver import TruckDriver
from unittest import TestCase


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.truck_driver = TruckDriver("Stenly", 12.40)

    def test_init(self):
        self.assertEqual("Stenly", self.truck_driver.name)
        self.assertEqual(12.40, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_earned_money_by_a_negative_number(self):
        with self.assertRaises(ValueError) as ve:
            self.truck_driver.earned_money = -1

        expected_result = "Stenly went bankrupt."
        self.assertEqual(expected_result, str(ve.exception))

    def test_add_cargo_offer(self):
        result = self.truck_driver.add_cargo_offer("Hamburg", 1000)
        expected_result = "Cargo for 1000 to Hamburg was added as an offer."

        self.assertEqual({"Hamburg": 1000}, self.truck_driver.available_cargos)
        self.assertEqual(expected_result, result)

    def test_add_cargo_offer_if_offer_is_already_added(self):
        self.truck_driver.available_cargos = {"Sofia": 800}
        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("Sofia", 800)

        expected_result = "Cargo offer is already added."
        self.assertEqual(expected_result, str(ex.exception))

    def test_drive_best_cargo_offer(self):
        self.truck_driver.available_cargos = {"Hamburg": 1000, "Sofia": 800}
        result = self.truck_driver.drive_best_cargo_offer()
        expected_result = "Stenly is driving 1000 to Hamburg."

        self.assertEqual(12275.0, self.truck_driver.earned_money)
        self.assertEqual(1000, self.truck_driver.miles)
        self.assertEqual(expected_result, result)

    def test_drive_best_cargo_offer_by_no_offers_available(self):
        result = self.truck_driver.drive_best_cargo_offer()
        expected_result = "There are no offers available."

        self.assertEqual(expected_result, result)

    def test_check_for_activities(self):
        self.truck_driver.earned_money = 100000.0
        self.truck_driver.check_for_activities(4000)

        self.assertEqual(98500.0, self.truck_driver.earned_money)

    def test_eat(self):
        self.truck_driver.earned_money = 1000.0
        self.truck_driver.eat(1000)
        self.assertEqual(980.0, self.truck_driver.earned_money)

    def test_sleep(self):
        self.truck_driver.earned_money = 1000.0
        self.truck_driver.sleep(1000)
        self.assertEqual(955.0, self.truck_driver.earned_money)

    def test_pump_gas(self):
        self.truck_driver.earned_money = 1000.0
        self.truck_driver.pump_gas(1500)
        self.assertEqual(500.0, self.truck_driver.earned_money)

    def test_repair_truck(self):
        self.truck_driver.earned_money = 10000.0
        self.truck_driver.repair_truck(20000)
        self.assertEqual(2500.0, self.truck_driver.earned_money)

    def test_repr(self):
        self.truck_driver.miles = 1000
        expected_result = "Stenly has 1000 miles behind his back."
        self.assertEqual(expected_result, str(self.truck_driver))
