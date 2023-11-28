from exams.exam_10_december_2022.project import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):

    def setUp(self) -> None:
        self.second_hand_car = SecondHandCar("BMW", "Electric", 10_000, 30000.00)
        self.other = SecondHandCar("Audi", "Electric", 14000, 25000)

    def test_init(self):
        self.assertEqual("BMW", self.second_hand_car.model)
        self.assertEqual("Electric", self.second_hand_car.car_type)
        self.assertEqual(10_000, self.second_hand_car.mileage)
        self.assertEqual(30000.00, self.second_hand_car.price)
        self.assertEqual([], self.second_hand_car.repairs)

    def test_price_should_be_greater_than_1(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.price = 0.5

        expected_result = 'Price should be greater than 1.0!'
        self.assertEqual(expected_result, str(ve.exception))

    def test_if_mileage_is_not_greater_than_100(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.mileage = 35

        expected_result = 'Please, second-hand cars only! Mileage must be greater than 100!'
        self.assertEqual(expected_result, str(ve.exception))

    def test_set_promotional_price_if_new_price_is_greater_than_price(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.set_promotional_price(35000)

        expected_result = 'You are supposed to decrease the price!'
        self.assertEqual(expected_result, str(ve.exception))

    def test_set_promotional_when_new_price_is_lower_than_price(self):
        result = self.second_hand_car.set_promotional_price(10000)
        expected_result = 'The promotional price has been successfully set.'
        self.assertEqual(10000, self.second_hand_car.price)
        self.assertEqual(expected_result, result)


    def test_need_repair_if_repair_is_impossible(self):
        result = self.second_hand_car.need_repair(15001, "Car")
        expected_result = 'Repair is impossible!'

        self.assertEqual(expected_result, result)

    def test_need_repair(self):
        result = self.second_hand_car.need_repair(10000, "Car")
        expected_result = 'Price has been increased due to repair charges.'
        self.assertEqual(40000, self.second_hand_car.price)
        self.assertEqual(["Car"], self.second_hand_car.repairs)
        self.assertEqual(expected_result, result)

    def test_gt(self):
        self.second_hand_car.car_type = "El"
        result = self.second_hand_car.__gt__(self.other)
        expected_result = 'Cars cannot be compared. Type mismatch!'
        self.assertEqual(expected_result, result)

    def test_gt_if_the_type_is_the_same(self):
        bmw = self.second_hand_car.__gt__(self.other)
        self.second_hand_car.price = 15000
        audi = self.second_hand_car.__gt__(self.other)

        self.assertEqual(True, bmw)
        self.assertEqual(False, audi)

    def test_result(self):
        result = self.second_hand_car.__str__()
        expected_result = f"""Model BMW | Type Electric | Milage 10000km
Current price: 30000.00 | Number of Repairs: 0"""
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
