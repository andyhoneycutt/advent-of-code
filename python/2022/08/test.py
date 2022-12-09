import unittest

from main import part_one, part_two

INPUTS = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0],
]


class TestDay08(unittest.TestCase):

    def test_part_one(self):
        expected = 21
        actual = part_one(INPUTS)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 8
        actual = part_two(INPUTS)
        self.assertEqual(expected, actual)
