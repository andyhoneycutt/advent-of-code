import unittest

from main import part_one, part_two

INPUTS = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


class TestDay07(unittest.TestCase):
    def test_part_one(self):
        expected = 95437
        actual = part_one(INPUTS)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 24933642
        actual = part_two(INPUTS)
        self.assertEqual(expected, actual)
