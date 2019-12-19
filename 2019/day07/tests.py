from unittest import TestCase

from day07.main import get_max_thruster_signal, get_thruster_signal


class PartOneTests(TestCase):
    def setUp(self) -> None:
        self.a = [
            3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0,
        ]
        self.b = [
            3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23,
            23, 1, 24, 23, 23, 4, 23, 99, 0, 0,
        ]
        self.c = [
            3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0,
            33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99,
            0, 0, 0,
        ]

    def test_get_thruster_signal(self):
        self.assertEqual(43210, get_thruster_signal(self.a, [4, 3, 2, 1, 0]))
        self.assertEqual(54321, get_thruster_signal(self.b, [0, 1, 2, 3, 4]))
        self.assertEqual(65210, get_thruster_signal(self.c, [1, 0, 4, 3, 2]))

    def test_get_max_thruster_signal(self):
        r = range(5)
        self.assertEqual(43210, get_max_thruster_signal(self.a, r))
        self.assertEqual(54321, get_max_thruster_signal(self.b, r))
        self.assertEqual(65210, get_max_thruster_signal(self.c, r))


class PartTwoTest(TestCase):
    def setUp(self) -> None:
        self.a = [
            3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
            27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5
        ]
        self.b = [
            3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55,
            1005, 55, 26, 1001, 54, -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008,
            54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53, 1001, 56, -1, 56,
            1005, 56, 6, 99, 0, 0, 0, 0, 10
        ]

    def test_get_thruster_signal(self):
        self.assertEqual(
            139629729, get_thruster_signal(
                self.a, [9, 8, 7, 6, 5], feedback=True
            )
        )
        self.assertEqual(
            18216, get_thruster_signal(
                self.b, [9, 7, 8, 5, 6], feedback=True
            ),
        )

    pass
