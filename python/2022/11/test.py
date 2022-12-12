import unittest

from main import part_one, part_two

INPUTS = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


class TestDay11(unittest.TestCase):

    def test_part_one(self):
        expected = 10605
        actual = part_one(INPUTS)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 2713310158
        actual = part_two(INPUTS)
        self.assertEqual(expected, actual)
