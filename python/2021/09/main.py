import time

NS = ((1, 0), (-1, 0), (0, -1), (0, 1))


def get_neighbors(grid, y, x):
    eof = len(grid)
    eol = len(grid[0])
    return [
        grid[y + _y][x + _x]
        for _y, _x in NS
        if 0 <= y + _y < eof and 0 <= x + _x < eol
    ]



def part_one(inputs):
    eof = len(inputs)
    eol = len(inputs[0])
    risk_levels = []
    for row in range(eof):
        for col in range(eol):
            neighbors = get_neighbors(inputs, row, col)
            if all([n > inputs[row][col] for n in neighbors]):
                risk_levels.append(int(inputs[row][col]) + 1)
    return sum(risk_levels)


def part_two(inputs):
    eof = len(inputs)
    eol = len(inputs[0])
    basins = []
    visited = set()
    for row in range(eof):
        for col in range(eol):
            if inputs[row][col] == '9':
                continue
            basin = [(row, col)]
            for y, x in basin:
                for _y, _x in NS:
                    nx = x + _x
                    ny = y + _y
                    p = (ny, nx)
                    if 0 <= ny < eof and 0 <= nx < eol \
                            and inputs[ny][nx] < '9' \
                            and p not in visited | set(basin):
                        basin.append(p)
                        visited.add(p)
            basins.append(basin)
    _b = [len(b) for b in basins]
    _b.sort()
    return _b[-1] * _b[-2] * _b[-3]


def main():
    with open('input.txt', 'r') as fp:
        initial = [ln.strip() for ln in fp]
        one = part_one(initial)
        print(one)
        two = part_two(initial)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
