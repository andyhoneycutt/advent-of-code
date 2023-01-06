import unittest

from main import part_one, part_two, parse_input, compare

INPUTS = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


class TestDay13(unittest.TestCase):

    def setUp(self) -> None:
        self.input = list(parse_input(INPUTS))

    def test_parse_input(self):
        expected = [
            ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]),
            ([[1], [2, 3, 4]], [[1], 4]),
            ([9], [[8, 7, 6]]),
            ([[4, 4], 4, 4], [[4, 4], 4, 4, 4]),
            ([7, 7, 7, 7], [7, 7, 7]),
            ([], [3]),
            ([[[]]], [[]]),
            ([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9])
        ]
        self.assertEqual(expected, self.input)

    def test_compare_pair(self):
        expected = [1, 1, -1, 1, -1, 1, -1, -1]
        actual = [compare(a, b) for a, b in self.input]
        self.assertEqual(expected, actual)

    def test_part_one(self):
        expected = 13
        actual = part_one(INPUTS)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 140
        actual = part_two(INPUTS)
        self.assertEqual(expected, actual)
