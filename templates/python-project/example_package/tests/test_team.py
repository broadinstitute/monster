import unittest

from example_package.team import Team


class TeamTestCase(unittest.TestCase):
    def test_monster_is_cool(self):
        self.assertTrue(Team("monster").is_cool())

    def test_jade_is_uncool(self):
        self.assertFalse(Team("jade").is_cool())
