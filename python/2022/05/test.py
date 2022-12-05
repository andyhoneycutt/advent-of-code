import unittest

from main import part_one, part_two, init_matrix

INPUT = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


class TestDay05(unittest.TestCase):
    def test_init_matrix(self):
        stack = {'1': ['Z', 'N'], '2': ['M', 'C', 'D'], '3': ['P']}
        expected = (
            stack,
            [['1', '2', '1'], ['3', '1', '3'], ['2', '2', '1'], ['1', '1', '2']],
        )
        actual = init_matrix(INPUT)
        self.assertEqual(expected, actual)
    def test_part_one(self):
        expected = 'CMZ'
        actual = part_one(INPUT)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 'MCD'
        actual = part_two(INPUT)
        self.assertEqual(expected, actual)
