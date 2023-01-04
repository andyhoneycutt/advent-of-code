import unittest

from main import part_one, part_two

INPUTS = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


class TestDay12(unittest.TestCase):

    def test_part_one(self):
        expected = 31
        actual = part_one(INPUTS)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 29
        actual = part_two(INPUTS)
        self.assertEqual(expected, actual)
