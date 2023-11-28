from exams.exam_10_december_2022.project import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.tennis_player = TennisPlayer("Andrey", 30, 25.5)
        self.other_player = TennisPlayer("Stephan", 29, 24.5)

    def test_init(self):
        self.assertEqual("Andrey", self.tennis_player.name)
        self.assertEqual(30, self.tennis_player.age)
        self.assertEqual(25.5, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_name_if_len_ot_name_is_less_or_equal_than_2(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = "Ha"

        expected_result = "Name should be more than 2 symbols!"
        self.assertEqual(expected_result, str(ve.exception))

    def test_age_if_value_is_less_than_18(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 17

        expected_result = "Players must be at least 18 years of age!"
        self.assertEqual(expected_result, str(ve.exception))

    def test_add_new_win(self):
        self.tennis_player.add_new_win("Bulgaria")
        self.assertEqual(["Bulgaria"], self.tennis_player.wins)

    def test_add_new_win_if_win_is_in_list(self):
        self.tennis_player.wins = ["Bulgaria"]
        self.tennis_player.add_new_win("Bulgaria")
        result = self.tennis_player.add_new_win("Bulgaria")
        expected_result = f"Bulgaria has been already added to the list of wins!"
        self.assertEqual(expected_result, result)

    def test_lt_if_player_is_more_points_than_other_player(self):
        result = self.tennis_player.__lt__(self.other_player)
        expected_result = 'Andrey is a better player than Stephan'
        self.assertEqual(expected_result, result)

    def test_lt_if_player_is_less_points_than_other_player(self):
        self.tennis_player.points = 10
        result = self.tennis_player.__lt__(self.other_player)
        expected_result = 'Stephan is a top seeded player and he/she is better than Andrey'
        self.assertEqual(expected_result, result)

    def test_result(self):

        result = str(self.tennis_player)
        expected_result = "Tennis Player: Andrey\n" \
                          "Age: 30\n" \
                          "Points: 25.5\n" \
                          "Tournaments won: "

        self.assertEqual(expected_result, result)

    def test_result_if_wins(self):
        self.tennis_player.wins = ["Bulgaria", "Italy", "Germany"]

        result = str(self.tennis_player)
        expected_result = "Tennis Player: Andrey\n" \
                          "Age: 30\n" \
                          "Points: 25.5\n" \
                          "Tournaments won: Bulgaria, Italy, Germany"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
