import time


def predict(ln):
    result = [ln]
    while set(result[-1]) != {0}:
        r = result[-1]
        result.append([r[i] - r[i - 1] for i in range(1, len(r))])
    result[-1].append(0)
    for i in range(len(result) - 1, 0, -1):
        r = result[i][-1] + result[i - 1][-1]
        result[i - 1].append(r)
    return result[0][-1]


def parse(lines, reverse=False):
    ints = [
        [int(x) for x in line.split()]
        for line in lines
    ]
    if reverse:
        return [list(reversed(x)) for x in ints]
    return ints


def part_one(inputs):
    inputs = parse(inputs)
    predictions = [predict(x) for x in inputs]
    return sum(predictions)


def part_two(inputs):
    inputs = parse(inputs, reverse=True)
    predictions = [predict(x) for x in inputs]
    return sum(predictions)


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        lines = [s.strip() for s in fp.readlines()]
        one = part_one(lines.copy())
        print(one)
        two = part_two(lines.copy())
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
