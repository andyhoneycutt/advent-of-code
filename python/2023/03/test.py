import re
import unittest

from main import part_one, part_two, get_symbol_locations, get_numbers_adjacent_to_symbols, get_symbols


SYMBOLS = {'*', '#', '$', '+'}
class TestDay03(unittest.TestCase):
    def setUp(self):
        self.input = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]

    def test_get_symbols(self):
        actual = get_symbols(self.input)
        self.assertEqual(SYMBOLS, actual)

    def test_coords(self):
        expected = [(3, 1), (6, 3), (3, 4), (5, 5), (3, 8), (5, 8)]
        actual = list(get_symbol_locations(self.input, symbols=SYMBOLS))
        self.assertEqual(expected, actual)

    def test_adjacent_numbers(self):
        expected = [467, 35, 633, 617, 592, 664, 598, 755]
        locations = list(get_symbol_locations(self.input, symbols=SYMBOLS))
        actual = list(get_numbers_adjacent_to_symbols(self.input, locations))
        self.assertEqual(expected, actual)
    def test_part_one(self):
        expected = 4361
        actual = part_one(self.input)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 467835
        actual = part_two(self.input)
        self.assertEqual(expected, actual)
