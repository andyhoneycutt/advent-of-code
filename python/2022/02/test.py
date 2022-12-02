import unittest

from main import part_one, part_two, score

INPUT = [
    ('A', 'Y'),
    ('B', 'X'),
    ('C', 'Z'),
]


class TestDay02(unittest.TestCase):
    def test_score(self):
        expected = 15
        actual = score(INPUT)
        self.assertEqual(expected, actual)

    def test_part_one(self):
        expected = 15
        actual = part_one(INPUT)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 12
        actual = part_two(INPUT)
        self.assertEqual(expected, actual)
