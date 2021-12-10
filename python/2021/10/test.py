import unittest
from main import part_one, part_two

INPUT = True

class TestDay09(unittest.TestCase):
    def test_part_one(self):
        expected = True
        actual = part_one(INPUT)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = True
        actual = part_two(INPUT)
        self.assertEqual(expected, actual)
