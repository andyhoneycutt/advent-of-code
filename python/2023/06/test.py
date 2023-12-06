import unittest

from main import part_one, part_two


class TestDay06(unittest.TestCase):
    def setUp(self):
        self.input = [
            "Time:      7  15   30",
            "Distance:  9  40  200",
        ]

    def test_part_one(self):
        expected = 288
        actual = part_one(self.input)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 71503
        actual = part_two(self.input)
        self.assertEqual(expected, actual)
