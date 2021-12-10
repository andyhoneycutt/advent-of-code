import unittest
from main import part_one, part_two, parse_input

INPUT = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc',
]


class TestDay02(unittest.TestCase):
    def test_part_one(self):
        inputs = parse_input(INPUT)
        expected = 2
        actual = part_one(inputs)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        inputs = parse_input(INPUT)
        expected = 1
        actual = part_two(inputs)
        self.assertEqual(expected, actual)
