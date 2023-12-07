import unittest

from main import part_one, part_two


class TestDay(unittest.TestCase):
    def setUp(self):
        self.input = [

        ]

    def test_part_one(self):
        expected = 1
        actual = part_one(self.input)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 1
        actual = part_two(self.input)
        self.assertEqual(expected, actual)
