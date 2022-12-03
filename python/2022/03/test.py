import unittest

from main import part_one, part_two, split_rucksack, in_both, ascii_score

INPUT = [
    'vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw',
]


class TestDay02(unittest.TestCase):
    def setUp(self) -> None:
        self.rucksacks = [split_rucksack(l) for l in INPUT]
        self.common = [
            in_both(*self.rucksacks[i]) for i in range(len(self.rucksacks))
        ]


    def test_in_both(self):
        expected = ['p', 'L', 'P', 'v', 't', 's']
        self.assertEqual(expected, self.common)

    def test_priorities(self):
        chars = ['p', 'L', 'P', 'v', 't', 's']
        expected = [16, 38, 42, 22, 20, 19]
        actual = [ascii_score(c) for c in chars]
        self.assertEqual(expected, actual)
    def test_part_one(self):
        expected = 157
        actual = part_one(INPUT)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 70
        actual = part_two(INPUT)
        self.assertEqual(expected, actual)
