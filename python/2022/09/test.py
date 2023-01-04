import unittest

from main import part_one, part_two

INPUTS1 = [
    ('R', 4),
    ('U', 4),
    ('L', 3),
    ('D', 1),
    ('R', 4),
    ('D', 1),
    ('L', 5),
    ('R', 2),
]

INPUTS2 = [
    ('R', 5),
    ('U', 8),
    ('L', 8),
    ('D', 3),
    ('R', 17),
    ('D', 10),
    ('L', 25),
    ('U', 20),
]

class TestDay09(unittest.TestCase):
    def test_part_one(self):
        expected = 13
        actual = part_one(INPUTS1)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 36
        actual = part_two(INPUTS2)
        self.assertEqual(expected, actual)
