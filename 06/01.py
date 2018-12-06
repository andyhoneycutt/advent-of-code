import os
import re

import functions


def mhd(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def main(data):
    start_x = min(d[0] for d in data)
    start_y = min(d[1] for d in data)
    size_x = max(d[0] for d in data) + 1
    size_y = max(d[1] for d in data) + 1
    grid = {}
    for x in range(start_x, size_x):
        for y in range(start_y, size_y):
            grid[(x, y)] = None

    _map = {}

    # get all distances for x, y to each specified point
    for point in grid:
        for d in data:
            dist = mhd(d, point)
            if not _map.get(point, None):
                _map[point] = []
            _map[point].append({'c': d, 'd': dist})

    for point in grid:
        # current x, y distance to each point
        c = _map[point]

        # what is grid x, y closest to?
        distances = sorted([p['d'] for p in c])
        if len(distances) > 1 and distances[0] == distances[1]:
            grid[point] = (-1, -1)
            continue
        lowest = [p['c'] for p in c if p['d'] == distances[0]][0]
        grid[point] = lowest

    infinites = set()
    for x in range(start_x, size_x):
        for y in range(start_y, size_y):
            c = grid[(x, y)]
            if any([x == start_x, y == start_y, x == size_x, y == size_y]):
                infinites.add(c)

    remap = {}
    for x in range(start_x, size_x):
        for y in range(start_y, size_y):
            c = grid[(x, y)]
            if c in infinites:
                continue
            if c == (-1, -1):
                continue
            if c not in remap:
                remap[c] = 0
            remap[c] += 1
    _max = 0
    for k, d in remap.items():
        if d > _max:
            _max = d

    safe_distances = []
    for point, coord_list in _map.items():
        if point not in infinites:
            s = sum([c['d'] for c in coord_list])
            if(s < 10000):
                safe_distances.append(s)

    return _max, len(safe_distances)


if __name__ == '__main__':
    test_data = ((1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9))
    test = main(test_data)
    assert test == (17, 69)

    test_data_two = (
        (0, 0), (0, 100), (1, 50), (80, 20), (80, 50), (80, 80), (100, 0),
        (100, 50), (100, 100)
    )
    test_two = main(test_data_two)
    assert test_two == (1876, 10197)

    filename = os.path.join(functions.get_path(__file__), 'input.txt')
    _data = [[int(i) for i in x] for x in
             [re.findall('\d+', l) for l in functions.read_file(filename)]]
    dataset = set()
    for _d in _data:
        dataset.add((_d[0], _d[1]))
    print(main(dataset))
