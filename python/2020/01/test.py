import unittest
from main import part_one, part_two

INPUT = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]

class TestDay01(unittest.TestCase):
    def test_part_one(self):
        expected = 514579
        actual = part_one(INPUT)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 241861950
        actual = part_two(INPUT)
        self.assertEqual(expected, actual)