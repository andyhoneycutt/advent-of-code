import unittest

from main import part_one, part_two

INPUTS = [
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7, 19),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5, 23),
    ('nppdvjthqldpwncqszvftbrmjlhg', 6, 23),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10, 29),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11, 26),
]


class TestDay06(unittest.TestCase):
    def test_part_one(self):
        for inp, exp, _ in INPUTS:
            actual = part_one(inp)
            self.assertEqual(exp, actual)

    def test_part_two(self):
        for inp, _, exp in INPUTS:
            actual = part_two(inp)
            self.assertEqual(exp, actual)
