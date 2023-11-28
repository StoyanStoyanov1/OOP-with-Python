from unittest import TestCase, main

from exams.exam_10_december_2022.project import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Axe", 25, 2500, 120)
        self.other_hero = Hero("Spirit Breaker", 25, 2000, 250)

    def test_all_init(self):
        self.assertEqual("Axe", self.hero.username)
        self.assertEqual(25, self.hero.level)
        self.assertEqual(2500, self.hero.health)
        self.assertEqual(120, self.hero.damage)

    def test_battle_by_yourself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_health_is_0_or_lower(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.other_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_when_cannot_fight(self):
        self.other_hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.other_hero)

        self.assertEqual("You cannot fight Spirit Breaker. He needs to rest", str(ve.exception))

    def test_battle_when_both_heroes_have_0_or_lower_health(self):
        self.hero.damage = 300
        self.other_hero.damage = 300

        result = self.hero.battle(self.other_hero)
        self.assertEqual("Draw", result)

    def test_battle_when_hero_win(self):
        self.hero.damage = 300
        self.other_hero.damage = 2

        result = self.hero.battle(self.other_hero)
        self.assertEqual(26, self.hero.level)
        self.assertEqual(2455, self.hero.health)
        self.assertEqual(305, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_when_other_hero_win(self):
        self.hero.damage = 2
        self.other_hero.damage = 300

        result = self.hero.battle(self.other_hero)
        self.assertEqual(26, self.other_hero.level)
        self.assertEqual(1955, self.other_hero.health)
        self.assertEqual(305, self.other_hero.damage)
        self.assertEqual("You lose", result)

    def test_str_message(self):
        message = self.hero.__str__()
        expected_message = "Hero Axe: 25 lvl\nHealth: 2500\nDamage: 120\n"
        self.assertEqual(expected_message, message)


if __name__ == "__main__":
    main()
