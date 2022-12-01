import unittest

from main import part_one, part_two, get_cals

INPUT = [
    ['1000', '2000', '3000'],
    ['4000'],
    ['5000', '6000'],
    ['7000', '8000', '9000'],
    ['10000'],
]


class TestDay01(unittest.TestCase):
    def test_cals(self):
        expected = [6000, 4000, 11000, 24000, 10000]
        actual = get_cals(INPUT)
        self.assertEqual(expected, actual)

    def test_part_one(self):
        expected = 24000
        actual = part_one(get_cals(INPUT))
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 45000
        actual = part_two(get_cals(INPUT))
        self.assertEqual(expected, actual)
