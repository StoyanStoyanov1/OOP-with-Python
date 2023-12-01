from exams.exam_11_dezember_2021.project import Team
import unittest


class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team = Team('test')

    def test_init(self):
        self.assertEqual(self.team.name, 'test')
        self.assertEqual(self.team.members, {})

    def test_props(self):
        with self.assertRaises(ValueError) as ve:
            Team('test123')
        self.assertEqual(str(ve.exception), "Team Name can contain only letters!")

    def test_add_member(self):
        result = self.team.add_member(test=2, other=3)
        expected_result = "Successfully added: test, other"
        self.assertEqual(result, expected_result)
        self.assertEqual(self.team.members, {'test': 2, 'other': 3})

    def test_remove_member(self):
        result = self.team.remove_member('test')
        expected_result = "Member with name test does not exist"
        self.assertEqual(result, expected_result)

        self.team.members = {'test': 3, 'other': 2}
        result = self.team.remove_member('test')
        expected_result = "Member test removed"
        self.assertEqual(result, expected_result)
        self.assertEqual(self.team.members, {'other': 2})

    def test_gt(self):
        other = Team('other')
        other.members = {'test': 1}
        result = self.team.__gt__(other)
        self.assertEqual(result, False)

        self.team.members = {'test': 2, 'other': 3}
        result = self.team.__gt__(other)
        self.assertEqual(result, True)

    def test_len(self):
        self.team.members = {'test': 2, 'other': 1}
        result = len(self.team)
        self.assertEqual(result, 2)

    def test_add(self):
        other = Team('other')
        other.members = {'test': 2, 'other': 3}
        self.team.members = {'set': 4}
        result = self.team.__add__(other)
        self.assertEqual(result.name, 'testother')
        self.assertEqual(result.members, {'test': 2, 'other': 3, 'set': 4})

    def test_str(self):
        self.team.members = {'test': 2, 'other': 3, 'apple': 3}
        result = str(self.team)
        expected_result = "Team name: test\nMember: apple - 3-years old\nMember: other - 3-years old\nMember: test - 2-years old"
        self.assertEqual(result, expected_result)
