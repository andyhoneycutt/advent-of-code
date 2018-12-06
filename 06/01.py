import os
import re
import sys

import functions


# 4146 too high
# 4116 too high
# others give 3890

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
    for x in range(start_x, size_x):
        for y in range(start_y, size_y):
            for d in data:
                dist = mhd(d, (x, y))
                if not _map.get((x, y), None):
                    _map[(x, y)] = []
                _map[(x, y)].append({'c': d, 'd': dist})

    for x in range(start_x, size_x):
        for y in range(start_y, size_y):
            if any([x == start_x, y == start_y, x == size_x, y == size_y]):
                grid[(x, y)] = (-1, -1)
                continue

            low = sys.maxsize
            lowest = (-1, -1)

            # current x, y distance to each point
            c = _map[(x, y)]

            # what is grid x, y closest to?
            for point in c:
                coord = point['c']
                dist = point['d']
                if dist < low:
                    low = dist
                    lowest = coord

            grid[(x, y)] = lowest

    remap = {}
    for x in range(start_x, size_x):
        for y in range(start_y, size_y):
            c = grid[(x, y)]
            if c == (-1, -1):
                continue
            if c not in remap:
                remap[c] = 0
            remap[c] += 1
    print(remap)
    _max = 0
    for k, d in remap.items():
        if d > _max:
            _max = d
    return _max


if __name__ == '__main__':
    test_data = ((1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9))
    test = main(test_data)
    assert test == 17

    filename = os.path.join(functions.get_path(__file__), 'input.txt')
    _data = [[int(i) for i in x] for x in [re.findall('\d+', l) for l in functions.read_file(filename)]]
    dataset = set()
    for _d in _data:
        dataset.add((_d[0], _d[1]))
    print(main(dataset))
