from unittest import TestCase

from day08.main import load_image, get_layer_fewest_entry


class PartOneTests(TestCase):
    def setUp(self) -> None:
        self.image = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
        self.expected_image = [
            [
                [1, 2, 3],
                [4, 5, 6],
            ],
            [
                [7, 8, 9],
                [0, 1, 2],
            ]
        ]

    def test_load_image(self):
        self.assertEqual(self.expected_image, load_image(self.image, 3, 2))

    def test_get_layer_fewest_entry(self):
        expected = 0
        actual = get_layer_fewest_entry(self.expected_image, 0)
        self.assertEqual(expected, actual)


class PartTwoTest(TestCase):
    def setUp(self) -> None:
        pass
