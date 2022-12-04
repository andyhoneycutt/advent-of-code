import time


def ranges_overlap(pairs):
    """ return ranges with any overlap """
    return [
        (a, b) for a, b in pairs
        if a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]
    ]


def ranges_fully_overlapped(pairs):
    """ return ranges that fully overlap """
    return [
        (a, b) for a, b in pairs
        if (
            (a[0] <= b[0] <= a[1] and b[1] <= a[1]) or
            (b[0] <= a[0] <= b[1] and a[1] <= b[1])
        )
    ]

def input_to_int_tuples(inputs):
    """ convert the inputs into a list of tuples of ints """
    def to_ints(s):
        return [int(i) for i in s.split('-')]
    return [tuple(map(to_ints, l.split(','))) for l in inputs]

def part_one(inputs):
    """ find pairs that fully overlap """
    pairs = input_to_int_tuples(inputs)
    fully = ranges_fully_overlapped(pairs)
    return len(fully)


def part_two(inputs):
    """ find any pairs with any overlap """
    pairs = input_to_int_tuples(inputs)
    overlap = ranges_overlap(pairs)
    return len(overlap)


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        values = [l.strip() for l in fp]
        one = part_one(values)
        two = part_two(values)
        print(one)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
