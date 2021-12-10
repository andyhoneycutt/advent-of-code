import unittest
from main import part_one, part_two

INPUT = [
    '2199943210',
    '3987894921',
    '9856789892',
    '8767896789',
    '9899965678',
]

class TestDay09(unittest.TestCase):
    def test_part_one(self):
        expected = 15
        actual = part_one(INPUT)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 1134
        actual = part_two(INPUT)
        self.assertEqual(expected, actual)
