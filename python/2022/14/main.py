import time


def get_points_between(a, b):
    # get all points between a and b
    ax, ay = a
    bx, by = b
    if ax == bx:
        src_y = min(ay, by)
        dst_y = max(ay, by)
        return [(ax, y) for y in range(src_y, dst_y + 1)]
    src_x = min(ax, bx)
    dst_x = max(ax, bx)
    return [(x, ay) for x in range(src_x, dst_x + 1)]


def parse_input(inputs):
    lines = []
    min_xy = (0, 0)
    max_xy = (0, 0)
    for line in inputs.splitlines():
        points = line.split(' -> ')
        for i in range(len(points) - 1):
            x, y = tuple(map(int, points[i].split(',')))
            nx, ny = tuple(map(int, points[i + 1].split(',')))
            # update min_xy and max_xy
            # min_xy = (min(min_xy[0], x, nx), min(min_xy[1], y, ny))
            max_xy = (max(max_xy[0], x, nx), max(max_xy[1], y, ny))
            # get all points between last_point and current point
            between = get_points_between((x, y), (nx, ny))
            lines.append(between)
    return lines, min_xy, max_xy


def get_grid(lines, min_xy, max_xy):
    nx, ny = min_xy  # (min_xy[0] - 1, min_xy[1] - 1)
    mx, my = max_xy  # (max_xy[0] + 1, max_xy[1] + 1)
    grid = [['.' for _ in range(mx - nx + 1)] for _ in range(my + 1)]
    for line in lines:
        for point in line:
            x, y = point
            x = x - nx
            grid[y][x] = '#'
    return grid


def move(grid, sand):
    y, x = sand
    try:
        # check if sand can move down
        if grid[y + 1][x] == '.':
            return y + 1, x
        # check if sand can move diagonally down and to the left
        if grid[y + 1][x - 1] == '.':
            return y + 1, x - 1
        # check if sand can move diagonally down and to the right
        if grid[y + 1][x + 1] == '.':
            return y + 1, x + 1
    except IndexError:
        return None
    return sand


def move_sand(grid, print_grid, infinite=False):
    running = True
    last_moves = None
    while running:

        # sand falls from 500 x-pos
        sand = (0, 500)

        moves = []
        while True:
            before_move = sand
            sand = move(grid, sand)

            # tried to move out-of-bounds
            if sand is None:
                if not infinite:
                    running = False
                    break
                y = before_move[0]
                sand = grid[y][before_move[1]]

            if infinite:
                # tried to move out-of-bounds
                if sand == (0, 500):
                    grid[0][500] = 'o'
                    running = False
                    break

            # sand couldn't move, so it stays at rest
            if sand == before_move:
                grid[sand[0]][sand[1]] = 'o'
                break

            # sand moved
            moves.append(sand)
            last_moves = moves

    grains = sum([1 for row in grid for cell in row if cell == 'o'])

    if print_grid:
        for mv in last_moves:
            grid[mv[0]][mv[1]] = '~'
        for row in grid:
            print(row)
    return grains


def part_one(inputs, print_grid=False):
    lines, min_xy, max_xy = parse_input(inputs)
    grid = get_grid(lines, min_xy, max_xy)
    return move_sand(grid, print_grid)


def part_two(inputs, print_grid=False):
    lines, min_xy, max_xy = parse_input(inputs)
    max_xy = (max_xy[0] * 2, max_xy[1])
    grid = get_grid(lines, min_xy, max_xy)
    grid.append(['.' for _ in range(len(grid[0]))])
    grid.append(['#' for _ in range(len(grid[0]))])

    return move_sand(grid, print_grid, infinite=True)


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        inputs = fp.read()
        one = part_one(inputs=f"{inputs}")
        print(one)
        two = part_two(inputs=f"{inputs}")
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
