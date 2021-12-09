import unittest
from main import part_one, part_two


class TestDay07(unittest.TestCase):
    def test_part_one(self):
        initial = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        expected = 37
        actual = part_one(initial)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        initial = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        expected = 168
        actual = part_two(initial)
        self.assertEqual(expected, actual)
