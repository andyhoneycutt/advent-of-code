from unittest import TestCase

from day06.main import get_orbits, get_len, get_transfers


class PartOneTests(TestCase):
    def test_sample(self):
        sample = [
            'COM)B',
            'B)C',
            'C)D',
            'D)E',
            'E)F',
            'B)G',
            'G)H',
            'D)I',
            'E)J',
            'J)K',
            'K)L',
        ]
        orbits = get_orbits(sample)
        self.assertEqual(42, get_len('COM', 0, orbits))


class PartTwoTest(TestCase):
    def test_sample(self):
        sample = [
            'COM)B',
            'B)C',
            'C)D',
            'D)E',
            'E)F',
            'B)G',
            'G)H',
            'D)I',
            'E)J',
            'J)K',
            'K)L',
            'K)YOU',
            'I)SAN',
        ]
        orbits = get_orbits(sample)
        self.assertEqual(4, get_transfers('YOU', 'SAN', orbits))
