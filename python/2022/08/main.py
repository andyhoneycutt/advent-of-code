import time
from functools import reduce
from operator import mul

from grid import Grid


def part_one(inputs):
    grid = Grid(inputs)
    visible = get_visible(grid)
    return len(visible)


def get_visible(grid):
    visible = set()

    fns = (
        grid.neighbors_left,
        grid.neighbors_right,
        grid.neighbors_top,
        grid.neighbors_bottom,
    )

    for y in range(grid.height):
        for x in range(grid.width):
            pt = grid.points[(y, x)]
            for fn in fns:
                try:
                    neighbors = fn((y, x))
                    m = max(neighbors)
                    if pt > m and pt != 0:
                        visible.add((y, x))
                        break
                except ValueError:
                    """ Has no neighbors on this edge, so is visible """
                    visible.add((y, x))
                    break
    return visible


def part_two(inputs):
    grid = Grid(inputs)
    high_score = 0
    for y in range(grid.height):
        for x in range(grid.width):
            pt = grid.points[(y, x)]
            fns = (
                grid.neighbors_left,
                grid.neighbors_right,
                grid.neighbors_top,
                grid.neighbors_bottom,
            )
            score = []
            for fn in fns:
                ns = fn((y, x))
                s = 0
                for n in ns:
                    s += 1
                    if pt <= n:
                        break
                score.append(s)
            current_score = reduce(mul, score, 1)
            high_score = max(high_score, current_score)
    return high_score


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        inputs = [list(map(int, list(line.strip()))) for line in fp.readlines()]
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
