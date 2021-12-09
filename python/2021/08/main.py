import time

A = 1
B = 2
C = 4
D = 8
E = 16
F = 32
G = 64

DECODER = {
    0: [1, 1, 1, 0, 1, 1, 1],
    1: [0, 0, 1, 0, 0, 1, 0],
    2: [1, 0, 1, 1, 1, 0, 1],
    3: [1, 0, 1, 1, 0, 1, 1],
    4: [0, 1, 1, 1, 0, 1, 0],
    5: [1, 1, 0, 1, 0, 1, 1],
    6: [1, 1, 0, 1, 1, 1, 1],
    7: [1, 0, 1, 0, 0, 1, 0],
    8: [1, 1, 1, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 0, 1, 1],
    #   8, 6, 8, 7, 4, 9, 7
}

BINARY_DECODER = {
    0: A | B | C | E | F | G,
    1: C | F,
    2: A | C | D | E | G,
    3: A | C | D | F | G,
    4: B | C | D | F,
    5: A | B | D | F | G,
    6: A | B | D | E | F | G,
    7: A | C | F,
    8: A | B | C | D | E | F | G,
    9: A | B | C | D | F | G,
}

UNIQUE_LENGTHS = [2, 3, 4, 7]


def part_one(inputs):
    c = 0
    for a, b in inputs:
        c += sum([1 for x in b if len(x) in UNIQUE_LENGTHS])
    return c


def b_to_i(binary):
    for k, v in BINARY_DECODER.items():
        if binary == v:
            return k


def get_bits(segments, bases):
    salad = ''.join(segments)
    bin_counts = {c: salad.count(c) for c in 'abcdefg'}

    # known registers
    _8 = set(bases[8])
    _7 = set(bases[7])
    _4 = set(bases[4])
    _1 = set(bases[1])

    # b is used 6 times
    b = set([k for k, v in bin_counts.items() if v == 6])
    # e is used 4 times
    e = set([k for k, v in bin_counts.items() if v == 4])
    # f is used 9 times
    f = set([k for k, v in bin_counts.items() if v == 9])
    a = _7 - _1
    c = _7 - (a | f)
    d = _4 - (b | c | f)
    g = _8 - (a | b | c | d | e | f)
    return a, b, c, d, e, f, g


def get_binary(segment, bin_map):
    return sum([bin_map[o] for o in segment])


def part_two(inputs):
    total = 0
    debug = []
    for segments, outputs in inputs:
        s = sorted(set([x for x in segments if len(x) in UNIQUE_LENGTHS]), key=len)
        bases = {1: s[0], 7: s[1], 4: s[2], 8: s[3]}
        a, b, c, d, e, f, g = get_bits(segments, bases)
        _bin_map = {
            ''.join(k): bn
            for k, bn in zip([a, b, c, d, e, f, g], [A, B, C, D, E, F, G])
        }
        number = [str(b_to_i(get_binary(o, _bin_map))) for o in outputs]
        n = int(''.join(number))
        debug.append(n)
        total += n
    return total, debug


def main():
    with open('input.txt', 'r') as fp:
        initial = [
            (a.strip().split(), b.strip().split(' '))
            for a, b in [ln.split('|') for ln in fp]
        ]
        one = part_one(initial)
        print(one)
        two, _ = part_two(initial)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
