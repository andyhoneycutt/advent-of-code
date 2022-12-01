import unittest
from main import part_one, part_two, parse_input

INPUT = [
    '..##.......',
    '#...#...#..',
    '.#....#..#.',
    '..#.#...#.#',
    '.#...##..#.',
    '..#.##.....',
    '.#.#.#....#',
    '.#........#',
    '#.##...#...',
    '#...##....#',
    '.#..#...#.#',
]


class TestDay02(unittest.TestCase):
    def test_part_one(self):
        inputs = list(parse_input(INPUT))
        expected = 7
        actual = part_one(inputs)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        inputs = list(parse_input(INPUT))
        expected = 336
        actual = part_two(inputs)
        self.assertEqual(expected, actual)
