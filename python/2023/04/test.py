import unittest

from main import part_one, part_two, parse_card, score_card


class TestDay04(unittest.TestCase):
    def setUp(self):
        self.input = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]

    def test_parse_card(self):
        card = self.input[0]
        expected = (
            1,
            {41, 48, 83, 86, 17},
            [83, 86, 6, 31, 17, 9, 48, 53],
            {48, 83, 17, 86},
        )
        actual = parse_card(card)
        self.assertEqual(expected, actual)

    def test_score_card(self):
        matches = {48, 83, 17, 86}
        expected = 8
        actual = score_card(matches)
        self.assertEqual(expected, actual)

    def test_part_one(self):
        expected = 13
        actual = part_one(self.input)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 30
        actual = part_two(self.input)
        self.assertEqual(expected, actual)
