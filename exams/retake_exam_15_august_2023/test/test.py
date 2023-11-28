from exams.exam_10_december_2022.project import Trip
from unittest import TestCase, main


class TestTrip(TestCase):

    def setUp(self) -> None:
        self.trip = Trip(300.0, 3, False)

    def test_init_if_is_correct(self):
        self.assertEqual(300.0, self.trip.budget)
        self.assertEqual(3, self.trip.travelers)
        self.assertEqual(False, self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_travelers_by_negative_number(self):
        with self.assertRaises(ValueError) as ve:
            Trip(70.3, -1, False)

        expected_result = "At least one traveler is required!"
        self.assertEqual(expected_result, str(ve.exception))

    def test_is_family(self):
        trip = Trip(50.2, 1, True)
        self.assertEqual(False, trip.is_family)

        trip = Trip(50.2, 2, True)
        self.assertEqual(True, trip.is_family)

        trip = Trip(50.2, 1, False)
        self.assertEqual(False, trip.is_family)

    def test_book_a_trip_if_destination_not_in_destination_prices(self):
        result = self.trip.book_a_trip("Germany")
        expected_result = "This destination is not in our offers, please choose a new one!"
        self.assertEqual(result, expected_result)

    def test_book_a_trip_if_destination_is_valid_but_not_enough_budget(self):
        self.trip.is_family = True
        result = self.trip.book_a_trip("Bulgaria")
        expected_result = "Your budget is not enough!"
        self.assertEqual(result, expected_result)

    def test_book_a_trip_if_destination_is_valid_and_is_family(self):
        self.trip.is_family = True
        self.trip.budget = 3000
        result = self.trip.book_a_trip("Bulgaria")
        expected_result = 'Successfully booked destination Bulgaria! Your budget left is 1650.00'
        self.assertEqual(1650.00, self.trip.budget)
        self.assertEqual(expected_result, result)
        self.assertEqual({'Bulgaria': 1350.0}, self.trip.booked_destinations_paid_amounts)

    def test_booking_status_if_not_booked_destinations_paid_amounts(self):
        result = self.trip.booking_status()
        expected_result = "No bookings yet. Budget: 300.00"
        self.assertEqual(result, expected_result)

    def test_booking_status_if_true_return_sorted_result(self):
        self.trip.booked_destinations_paid_amounts = {'Australia': 5700, 'Brazil': 6200}
        correct_result = self.trip.booking_status()
        result = []
        sorted_bookings = sorted(self.trip.booked_destinations_paid_amounts.items())
        for booked_destination, paid_amount in sorted_bookings:
            result.append(f"""Booked Destination: {booked_destination}
Paid Amount: {paid_amount:.2f}""")
        result.append(f"""Number of Travelers: {self.trip.travelers}
Budget Left: {self.trip.budget:.2f}""")
        expected_result = '\n'.join(result)

        self.assertEqual(correct_result, expected_result)


if __name__ == "__main__":
    main()
