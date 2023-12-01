import unittest

from main import part_one, part_two, get_calibration, replace_numbers

INPUT = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]

INPUT_PART_TWO = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

class TestDay01(unittest.TestCase):
    def test_calibration(self):
        expected = [12, 38, 15, 77]
        actual = list(get_calibration(INPUT))
        self.assertEqual(expected, actual)

    def test_part_one(self):
        expected = 142
        actual = part_one(INPUT)
        self.assertEqual(expected, actual)

    def test_yields_numbers(self):
        expected = ['219', '8wo3', 'abc123xyz', 'x2ne34', '49872', 'z1ight234', '7pqrst6teen']
        actual = list(replace_numbers(INPUT_PART_TWO))
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 281
        actual = part_two(INPUT_PART_TWO)
        self.assertEqual(expected, actual)
