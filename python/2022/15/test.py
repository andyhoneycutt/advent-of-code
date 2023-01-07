import unittest

from main import part_one, part_two, parse_input

INPUTS = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


class TestDay15(unittest.TestCase):

    def setUp(self) -> None:
        self.sensors, self.beacons = parse_input(INPUTS)

    def test_parse_input(self):
        sensors = {
            (0, 11, 3),
            (2, 0, 10),
            (2, 18, 7),
            (8, 7, 9),
            (9, 16, 1),
            (10, 20, 4),
            (12, 14, 4),
            (13, 2, 3),
            (14, 3, 1),
            (14, 17, 5),
            (16, 7, 5),
            (17, 20, 6),
            (20, 1, 7),
            (20, 14, 8)
        }
        beacons = {(2, 10), (21, 22), (10, 16), (15, 3), (25, 17), (-2, 15)}
        self.assertEqual(sensors, self.sensors)
        self.assertEqual(beacons, self.beacons)

    def test_part_one(self):
        expected = 26
        actual = part_one(INPUTS)
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 93
        actual = part_two(INPUTS)
        self.assertEqual(expected, actual)
