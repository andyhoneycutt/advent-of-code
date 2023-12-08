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
        expected = 1
        actual = part_two(self.input)
        self.assertEqual(expected, actual)
