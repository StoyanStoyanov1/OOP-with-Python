from unittest import TestCase, main

# from car_manager.car import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("some make", "some model", 10, 40)

    def test_if_init_is_correct(self):
        self.assertEqual("some make", self.car.make)
        self.assertEqual("some model", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(40, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_if_make_is_null_or_empty(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = 0

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_if_model_is_null_or_empty(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_if_consumption_is_zero_or_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_if_capacity_is_zero_or_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_if_fuel_amount_is_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_if_refuel_is_zero_or_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-2)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_if_refuel_is_correct(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_if_drive_it_not_enough(self):
        distance = 1000

        with self.assertRaises(Exception) as ex:
            self.car.drive(distance)

        self.assertTrue(distance > self.car.fuel_amount)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_if_drive_is_correct(self):
        self.car.fuel_amount = 40
        self.car.drive(100)
        self.assertEqual(30, self.car.fuel_amount)


if __name__ == "__main__":
    main()
