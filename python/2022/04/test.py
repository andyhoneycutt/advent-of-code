import unittest

from main import part_one, part_two

INPUT = [
    '2-4,6-8',
    '2-3,4-5',
    '5-7,7-9',
    '2-8,3-7',
    '6-6,4-6',
    '2-6,4-8',
]


class TestDay02(unittest.TestCase):
    def test_part_one(self):
        expected = 2
        actual = part_one(INPUT)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 4
        actual = part_two(INPUT)
        self.assertEqual(expected, actual)
