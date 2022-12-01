import time

def calc_trees(inputs, deltax, deltay):
    h = len(inputs)
    w = len(inputs[0])
    for y in range(deltay, h):
        x = y * deltax % w
        yield inputs[y][x]

def part_one(inputs):
    trees = sum(calc_trees(inputs, 3, 1))
    return trees

def part_two(inputs):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = [sum(tree) for tree in [calc_trees(inputs, *s) for s in slopes]]
    prod = 1
    for tree in trees:
        prod *= tree
    return prod


def parse_input(fp):
    for ln in fp:
        yield [1 if c == '#' else 0 for c in ln.strip()]


def main():
    with open('input.txt', 'r') as fp:
        inputs = list(parse_input(fp))
        one = part_one(inputs)
        print(one)
        two = part_two(inputs)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
