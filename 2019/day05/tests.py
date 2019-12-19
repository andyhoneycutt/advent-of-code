from unittest import TestCase

from intcode import run


class PartOneTests(TestCase):
    def setUp(self) -> None:
        pass

    def test_position_mode(self):
        codes = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        self.assertEqual(run(codes, 1), 1)
        self.assertEqual(run(codes, 0), 0)

    def test_immediate_mode(self):
        codes = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        self.assertEqual(run(codes, 1), 1)
        self.assertEqual(run(codes, 0), 0)

    def test_large_instruction(self):
        instruction = [
            3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20,
            31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1,
            46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46,
            98, 99
        ]
        self.assertEqual(run(instruction, 7), 999)
        self.assertEqual(run(instruction, 8), 1000)
        self.assertEqual(run(instruction, 9), 1001)
