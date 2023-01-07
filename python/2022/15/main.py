import re
import time


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def parse_input(inputs):
    pat = re.compile(r"(-?\d+)")
    coords = [list(map(int, pat.findall(line))) for line in inputs.splitlines()]
    sensors = set()
    beacons = set()
    for group in coords:
        ax, ay, bx, by = group
        sensors.add((ax, ay, manhattan_distance((ax, ay), (bx, by))))
        beacons.add((bx, by))
    return sensors, beacons


def outside_sensor_range(coord, sensors, beacons):
    if coord in beacons:
        return False
    for x, y, d in sensors:
        if manhattan_distance((x, y), coord) <= d:
            return False
    return True


def part_one(inputs, target=10):
    sensors, beacons = parse_input(inputs)
    c = 0
    min_x = min(x - d for x, y, d in sensors)
    max_x = max(x + d for x, y, d in sensors)

    # sensor distance lookup table
    s_xy = {(x, y): d for x, y, d in sensors}

    # get straight-line distance from sensor to target row
    distances = [(x, y, manhattan_distance((x, y), (x, target))) for x, y, d in sensors]
    # sensors in possible range
    s_in_range = [(x, y, s_xy[(x, y)]) for x, y, d in distances if d <= s_xy[(x, y)]]

    for x in range(min_x, max_x):
        if not outside_sensor_range((x, target), s_in_range, beacons):
            c += 1
    return c - 1


def part_two(inputs):
    return inputs


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        inputs = fp.read()
        one = part_one(inputs=f"{inputs}", target=2000000)
        print(one)
        # two = part_two(inputs=f"{inputs}")
        # print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
