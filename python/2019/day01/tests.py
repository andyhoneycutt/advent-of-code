import unittest

from day01.main import fuel, fuel_two


class Tests(unittest.TestCase):
    def test_fuel(self):
        self.assertEqual(2, fuel(12))
        self.assertEqual(2, fuel(14))
        self.assertEqual(654, fuel(1969))
        self.assertEqual(33583, fuel(100756))

    def test_fuel_two(self):
        self.assertEqual(2, fuel_two(14))
        self.assertEqual(966, fuel_two(1969))
        self.assertEqual(50346, fuel_two(100756))
