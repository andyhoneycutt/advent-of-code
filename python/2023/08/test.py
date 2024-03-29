import unittest

from main import part_one, part_two, parse, link, Node


class TestDay(unittest.TestCase):
    def setUp(self):
        self.input = [
            "LLR",
            "",
            "AAA = (BBB, BBB)",
            "BBB = (AAA, ZZZ)",
            "ZZZ = (ZZZ, ZZZ)",
        ]
        self.input2 = [
            "LR",
            "",
            "11A = (11B, XXX)",
            "11B = (XXX, 11Z)",
            "11Z = (11B, XXX)",
            "22A = (22B, XXX)",
            "22B = (22C, 22C)",
            "22C = (22Z, 22Z)",
            "22Z = (22B, 22B)",
            "XXX = (XXX, XXX)",
        ]

    def test_parse(self):
        expected = (['L', 'L', 'R'], [('AAA', 'BBB', 'BBB'), ('BBB', 'AAA', 'ZZZ'), ('ZZZ', 'ZZZ', 'ZZZ')])
        actual = parse(self.input)
        self.assertEqual(expected, actual)

    def test_link(self):
        a = Node(name='AAA')
        b = Node(name='BBB')
        z = Node(name='ZZZ')
        a.left = a.right = b
        b.left = a
        b.right = z
        z.left = z.right = z
        actual = link(parse(self.input)[1])
        self.assertEqual(a, actual['AAA'])
        self.assertEqual(b, actual['BBB'])
        self.assertEqual(z, actual['ZZZ'])

    def test_part_one(self):
        expected = 6
        actual = part_one(self.input)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 6
        actual = part_two(self.input2)
        self.assertEqual(expected, actual)
