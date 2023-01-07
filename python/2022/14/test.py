import unittest

from main import part_one, part_two, parse_input, get_grid

INPUTS = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


class TestDay14(unittest.TestCase):

    def setUp(self) -> None:
        self.input, self.min_xy, self.max_xy = parse_input(INPUTS)
        self.grid = get_grid(self.input, self.min_xy, self.max_xy)

    def test_parse_input(self):
        expected = [
            [(498, 4), (498, 5), (498, 6)],
            [(496, 6), (497, 6), (498, 6)],
            [(502, 4), (503, 4)],
            [(502, 4), (502, 5), (502, 6), (502, 7), (502, 8), (502, 9)],
            [
                (494, 9), (495, 9), (496, 9), (497, 9), (498, 9), (499, 9),
                (500, 9), (501, 9), (502, 9)
            ],
        ]
        self.assertEqual(expected, self.input)

    def test_get_grid(self):
        grid = get_grid(self.input, (494, 0), self.max_xy)
        expected = [
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '#', '.', '.', '.', '#', '#'],
            ['.', '.', '.', '.', '#', '.', '.', '.', '#', '.'],
            ['.', '.', '#', '#', '#', '.', '.', '.', '#', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '.'],
        ]
        self.assertEqual(expected, grid)

    def test_part_one(self):
        expected = 24
        actual = part_one(INPUTS)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 93
        actual = part_two(INPUTS)
        self.assertEqual(expected, actual)
