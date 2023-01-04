import string
import time
from collections import deque

from grid import Grid, get_vector, sign

chars = [*string.ascii_lowercase]


def g_ord(c):
    _m = {
        'S': 'a',
        'E': 'z',
    }
    return chars.index(_m.get(c, c))


def breadth_first_search(grid, a, b):
    """Returns a list of all paths from start to end."""

    # Use deque for append and pop operations
    q = deque([[a]])

    # Keep track of visited nodes
    visited = {a}

    # Keep looping until there are nodes still to be checked
    while q:
        # Pop the first path from the queue
        path = q.popleft()

        # Get the last node from the path
        s = path[-1]

        # If we've reached the end, return the path
        if s == b:
            return path[1:]

        # Add all neighbors to the queue that we can climb and haven't been
        # visited
        ns = [
            n for n in grid.four_cardinal_neighbors(s)
            if n not in visited and grid[n] - grid[s] <= 1
        ]
        for n in ns:
            # Add the neighbor to the queue
            q.append(path + [n])
            # Mark the neighbor as visited
            visited.add(n)

    # Return empty path if no path is found
    return []


def part_one(inputs):
    _g = [list(line.strip()) for line in inputs.split("\n")]
    grid = Grid(_g)
    first = grid.find('S')
    last = grid.find('E')
    _g = [[g_ord(c) for c in line] for line in _g]
    grid = Grid(_g)
    path = breadth_first_search(grid, first, last)
    return len(path)


def part_two(inputs):
    _g = [list(line.strip()) for line in inputs.split("\n")]
    grid = Grid(_g)
    grid[grid.find('S')] = 'a'
    starts = grid.find_all('a')
    last = grid.find('E')
    _g = [[g_ord(c) for c in line] for line in _g]
    grid = Grid(_g)
    paths = []
    for a in starts:
        if path := breadth_first_search(grid, a, last):
            paths.append(path)
    best = min(paths, key=len)
    return len(best)


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        inputs = fp.read()
        one = part_one(inputs=f"{inputs}")
        two = part_two(inputs=f"{inputs}")
        print(one)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
