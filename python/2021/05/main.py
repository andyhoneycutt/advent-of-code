import math
import time

GRID_X = 1000
GRID_Y = 1000


def distance(a, b):
    x1, y1 = a
    x2, y2 = b
    _a = (x2 - x1) ** 2
    _b = (y2 - y1) ** 2
    return int(math.sqrt(_a + _b))


class Grid:
    coordinates = None
    points = {}

    def __init__(self, coords):
        self.coordinates = coords
        for _x in range(GRID_X + 1):
            for _y in range(GRID_Y + 1):
                self.points[(_x, _y)] = 0

    def draw_horizontal_line(self, a, b):
        x1, y1 = a
        x2, y2 = b
        assert y1 == y2, f"not horizontal: {a}, {b}"
        length = abs(x2 - x1)
        left = min([x1, x2])
        stop = length + left
        for x in range(left, stop + 1):
            self.points[x, y1] += 1

    def draw_vertical_line(self, a, b):
        x1, y1 = a
        x2, y2 = b
        assert x1 == x2, f"not vertical: {a}, {b}"
        length = abs(y2 - y1)
        top = min([y1, y2])
        stop = length + top
        for y in range(top, stop + 1):
            self.points[x1, y] += 1

    def draw_diagonal_line(self, a, b):
        x1, y1 = a
        x2, y2 = b
        assert x1 != x2 and y1 != y2, f"not diagonal: {a}, {b}"
        x_vel = 1 if x1 < x2 else -1
        y_vel = 1 if y1 < y2 else -1
        length = max(abs(x2 - x1), abs(y2 - y1))
        for point in range(length + 1):
            self.points[x1 + (x_vel * point), y1 + (y_vel * point)] += 1

    def draw_line(self, a, b):
        x1, y1 = a
        x2, y2 = b
        if y1 == y2:
            return self.draw_horizontal_line(a, b)
        if x1 == x2:
            return self.draw_vertical_line(a, b)
        else:
            return self.draw_diagonal_line(a, b)

    def fill(self):
        for a, b in self.coordinates:
            self.draw_line(a, b)


def read_coordinates(inputs):
    for inp in inputs:
        a, b = inp.split(" -> ")
        x1, y1 = [int(c) for c in a.split(',')]
        x2, y2 = [int(c) for c in b.split(',')]
        yield (x1, y1), (x2, y2)


def vert_or_horizontal(a, b):
    x1, y1 = a
    x2, y2 = b
    return x1 == x2 or y1 == y2


def part_one(coords):
    points = [coord for coord in coords if vert_or_horizontal(*coord)]
    grid = Grid(points)
    grid.fill()
    return sum([1 for _, p in grid.points.items() if p > 1])


def part_two(coords):
    points = [coord for coord in coords]
    grid = Grid(points)
    grid.fill()
    return sum([1 for _, p in grid.points.items() if p > 1])


def main():
    with open('input.txt', 'r') as fp:
        coordinates = list(read_coordinates(inputs=fp))
        one = part_one(coordinates)
        print(one)
        two = part_two(coordinates)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
