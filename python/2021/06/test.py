import unittest
from main import calc_fish, calc_fish_big


class TestDay06(unittest.TestCase):
    def test_day_one(self):
        initial = [3, 4, 3, 1, 2]
        expected = 5934
        actual = calc_fish(initial)
        self.assertEqual(expected, actual)

    def test_day_two(self):
        initial = [3, 4, 3, 1, 2]
        expected = 26984457539
        actual = calc_fish_big(initial, days=256)
        self.assertEqual(expected, actual)
