from unittest import TestCase

from day08.main import load_image


class PartOneTests(TestCase):
    def setUp(self) -> None:
        self.image = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]

    def test_load_image(self):
        expected = [
            [
                [1, 2, 3],
                [4, 5, 6],
            ],
            [
                [7, 8, 9],
                [0, 1, 2],
            ]
        ]
        self.assertEqual(expected, load_image(self.image, 3, 2))


class PartTwoTest(TestCase):
    def setUp(self) -> None:
        pass
