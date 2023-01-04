import time

from grid import sign

directions = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
    'UL': (-1, 1),
    'UR': (1, 1),
    'DL': (-1, -1),
    'DR': (1, -1),
}

def is_touching(a, b):
    tx, ty = a
    return b in [(tx + dx, ty + dy) for dx, dy in directions.values()]


def can_move(head, tail):
    return abs(head[0] - tail[0]) + abs(head[1] - tail[1]) > 1


def get_pos(head, tail):
    return (
        tail[0] + sign(head[0] - tail[0]),
        tail[1] + sign(head[1] - tail[1]),
    )


def part_one(inputs):
    # Initialize variables for head and tail positions
    head_pos = (0, 0)
    tail_pos = (0, 0)
    positions = {tail_pos, }

    # Iterate through the series of motions
    for direction, steps in inputs:
        # Update head position
        dx, dy = directions[direction]
        for step in range(steps):
            px, py = head_pos
            head_pos = (px + dx, py + dy)

            # if touching, don't move tail:
            if is_touching(tail_pos, head_pos):
                continue

            # if the head is at least 2 steps away from the tail, move the tail
            if can_move(head_pos, tail_pos):
                tail_pos = get_pos(head_pos, tail_pos)
                positions.add(tail_pos)

    return len(positions)


def part_two(inputs):
    # Initialize variables for head and tail positions
    head_pos = (0, 0)
    t_len = 9
    knots = [(0, 0)] * t_len
    positions = {head_pos, }

    # Iterate through the series of motions
    for direction, steps in inputs:
        # Update head position
        dx, dy = directions[direction]
        for step in range(steps):
            px, py = head_pos
            head_pos = (px + dx, py + dy)

            # if touching, don't move tail, 0th knot is closest to head
            for i in range(t_len):
                forward_knot = head_pos if i == 0 else knots[i - 1]

                if is_touching(knots[i], forward_knot):
                    continue

                # if the next knot is at least 2 steps away from the tail, move the tail
                if can_move(forward_knot, knots[i]):
                    knot = get_pos(forward_knot, knots[i])
                    knots[i] = knot
                    if i == t_len - 1:
                        positions.add(knot)

    return len(positions)


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        inputs = [(a, int(b)) for a, b in [line.split() for line in fp.readlines()]]
        one = part_one(inputs=inputs)
        two = part_two(inputs=inputs)
        print(one)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
