import time
import typing
from functools import cmp_to_key

from grid import sign


def parse_input(inputs):
    pairs = inputs.split("\n\n")
    for pair in pairs:
        a, b = pair.split("\n")
        yield eval(a), eval(b)


def compare(a: typing.Union[int, list], b: typing.Union[int, list]) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return sign(b - a)

    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]

    for i in range(len(a)):
        try:
            x = compare(a[i], b[i])
            if x != 0:
                return x
        except IndexError:
            return -1

    v = sign(len(b) - len(a))
    return v


def part_one(inputs):
    pairs = parse_input(inputs)
    correct = [compare(a, b) for a, b in pairs]
    indexes = [i for i, x in enumerate(correct, start=1) if x == 1]
    return sum(indexes)


def part_two(inputs):
    pairs = [[[2]], [[6]]]
    for a, b in parse_input(inputs):
        pairs.append(a)
        pairs.append(b)
    ordered = sorted(pairs, key=cmp_to_key(compare), reverse=True)
    a = ordered.index([[2]]) + 1
    b = ordered.index([[6]]) + 1
    return a * b


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
