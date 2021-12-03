import helpers

OPS = {
    'D': -1, 'L': -1,
    'U': 1, 'R': 1,
}


def get_path(w: str) -> list:
    moves = w.split(',')
    path = []
    c = (0, 0)
    step = 0
    for m in moves:
        direction, length = m[0], int(m[1:])
        op = OPS[direction]
        x, y = c
        for i in range(length):
            step += 1
            if direction in ['U', 'D']:
                y += op
            else:
                x += op
            path.append((x, y, step))
        c = (x, y)
    return path


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def distance(a, b):
    wire_a = set((x, y) for x, y, _ in get_path(a))
    wire_b = set((x, y) for x, y, _ in get_path(b))
    intersections = wire_a & wire_b
    distances = []
    for intersect in intersections:
        x, y = intersect
        distances.append(manhattan(0, 0, x, y))
    distances.sort()
    return distances[0]


def get_isect_with(isect, isects):
    x, y, s = isect
    for target in isects:
        x1, y1, s1 = target
        if x == x1 and y == y1 and s != s1:
            return target


def steps(a, b):
    wire_a = set(get_path(a))
    wire_b = set(get_path(b))
    points_a = set([(x, y) for x, y, _ in wire_a])
    points_b = set([(x, y) for x, y, _ in wire_b])
    intersections = [p for p in wire_a if (p[0], p[1]) in points_b] + \
                    [p for p in wire_b if (p[0], p[1]) in points_a]
    min_step = 0
    for intersect in intersections:
        x, y, s = intersect
        x1, y1, s1 = get_isect_with(intersect, intersections)
        new_step = s + s1
        if min_step == 0 or new_step < min_step:
            min_step = new_step
    return min_step


def part_one():
    wire1, wire2 = helpers.read_input('input.txt')
    result = distance(wire1, wire2)
    print(result)


def part_two():
    wire1, wire2 = helpers.read_input('input.txt')
    result = steps(wire1, wire2)
    print(result)


if __name__ == '__main__':
    part_one()
    part_two()

