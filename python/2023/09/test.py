import unittest

from main import part_one, part_two, parse


class TestDay(unittest.TestCase):
    def setUp(self):
        self.input = [
            "0 3 6 9 12 15",
            "1 3 6 10 15 21",
            "10 13 16 21 30 45",
        ]

    def test_part_one(self):
        expected = 114
        actual = part_one(self.input)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 2
        actual = part_two(self.input)
        self.assertEqual(expected, actual)
