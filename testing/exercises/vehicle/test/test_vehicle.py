from unittest import TestCase, main

from exams.exam_10_december_2022.project import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(27.2, 25.6)

    def test_if_init_is_correct(self):
        self.assertEqual(27.2, self.vehicle.fuel)
        self.assertEqual(27.2, self.vehicle.capacity)
        self.assertEqual(25.6, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive(self):
        self.vehicle.drive(3)
        result = 27.2 - 1.25 * 3
        self.assertEqual(result, self.vehicle.fuel)

    def test_drive_by_not_enough_foul(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel(self):
        self.vehicle.refuel(0)
        self.assertEqual(27.2, self.vehicle.fuel)

    def test_refuel_by_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_if_message_is_correct(self):
        self.assertEqual("The vehicle has 25.6 horse power with 27.2 fuel left and 1.25 fuel consumption",
                         self.vehicle.__str__())


if __name__ == "__main__":
    main()
