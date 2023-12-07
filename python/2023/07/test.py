import unittest

from main import part_one, part_two, parse, ONE, THREE, TWO, score, rank


class TestDay07(unittest.TestCase):
    def setUp(self):
        self.input = [
            "32T3K 765",
            "T55J5 684",
            "KK677 28",
            "KTJJT 220",
            "QQQJA 483",
        ]

    def test_score(self):
        parsed = [parse(line) for line in self.input]
        expected = [
            ONE,
            THREE,
            TWO,
            TWO,
            THREE,
        ]
        sc = [score(hand) for hand, _ in parsed]
        actual = [s[0] for s in sc]
        self.assertEqual(expected, actual)

    def test_rank(self):
        parsed = [parse(line) for line in self.input]
        expected = 6440
        actual = sum(rank(parsed))
        self.assertEqual(expected, actual)

    def test_part_one(self):
        expected = 6440
        actual = part_one(self.input)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 5905
        actual = part_two(self.input)
        self.assertEqual(expected, actual)
