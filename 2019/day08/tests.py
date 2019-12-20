from unittest import TestCase

from day08.main import load_image, get_layer_fewest_entry, \
    get_layer_count_entry, multiply_entries, merge_image


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

    def test_get_layer_count_entry(self):
        entry = 0
        expected = [0, 1]
        actual = [
            get_layer_count_entry(self.expected_image[0], entry),
            get_layer_count_entry(self.expected_image[1], entry),
        ]
        self.assertEqual(expected, actual)

    def test_get_layer_fewest_entry(self):
        expected = 0
        actual = get_layer_fewest_entry(self.expected_image, 0)
        self.assertEqual(expected, actual)

    def test_get_layer_multiply_entries(self):
        a = 4
        b = 5
        expected = 1
        actual = multiply_entries(self.expected_image[0], a, b)
        self.assertEqual(expected, actual)


class PartTwoTest(TestCase):
    def setUp(self) -> None:
        self.image = [
            [['0', '2'], ['2', '2']],
            [['1', '1'], ['2', '2']],
            [['2', '2'], ['1', '2']],
            [['0', '0'], ['0', '0']],
        ]

    def test_merge_image(self):
        expected = [
            ['0', '1'],
            ['1', '0'],
        ]
        layer = [['2', '2'], ['2', '2']]
        i_layers = iter(self.image)
        w = 2
        h = 2
        actual = merge_image(layer, i_layers, w, h)
        self.assertEqual(expected, actual)
