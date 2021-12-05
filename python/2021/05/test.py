import io
import unittest

from main import read_coordinates, vert_or_horizontal

inputs = io.StringIO(
    "0,9 -> 5,9\n"
    "8,0 -> 0,8\n"
    "9,4 -> 3,4\n"
    "2,2 -> 2,1\n"
    "7,0 -> 7,4\n"
    "6,4 -> 2,0\n"
    "0,9 -> 2,9\n"
    "3,4 -> 1,4\n"
    "0,0 -> 8,8\n"
    "5,5 -> 8,2\n"
)


class TestMethods(unittest.TestCase):
    def test_reads_input(self):
        expected = [
            ((0, 9), (5, 9)),
            ((8, 0), (0, 8)),
            ((9, 4), (3, 4)),
            ((2, 2), (2, 1)),
            ((7, 0), (7, 4)),
            ((6, 4), (2, 0)),
            ((0, 9), (2, 9)),
            ((3, 4), (1, 4)),
            ((0, 0), (8, 8)),
            ((5, 5), (8, 2))
        ]
        self.assertEqual(expected, list(read_coordinates(inputs)))

    def test_vert_or_horizontal(self):
        expected = [
            True,
            False,
            True,
            True,
            True,
            False,
            True,
            True,
            False,
            False,
        ]
        actual = [vert_or_horizontal(a, b) for a, b in read_coordinates(inputs)]
        self.assertEqual(expected, actual)

