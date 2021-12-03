import time
from collections import Counter


def part_one(inputs):
    _gamma = []
    _epsilon = []
    groups = zip(*inputs)

    for g in groups:
        common, _ = Counter(g).most_common()[0]
        inverse = "0" if common == "1" else "1"
        _gamma.append(common)
        _epsilon.append(inverse)
    gamma = int(''.join(_gamma), 2)
    epsilon = int(''.join(_epsilon), 2)
    return gamma * epsilon


def _get_life(diags, bit=0, weight='1', less='0'):
    if len(diags) == 1:
        return diags[0]
    toggled = [i[bit] for i in diags]
    ones = toggled.count('1')
    zeroes = toggled.count('0')
    selected = weight if ones > zeroes else weight if ones == zeroes else less
    bits = [b for b in diags if b[bit] == selected]
    return _get_life(bits, bit=bit + 1, weight=weight, less=less)


def _get_o2(o2, bit=0):
    return _get_life(o2, bit=bit)


def _get_co2(co2, bit=0):
    return _get_life(co2, bit=bit, weight='0', less='1')


def part_two(inputs):
    o2 = int(''.join(_get_o2(inputs)), 2)
    co2 = int(''.join(_get_co2(inputs)), 2)
    return o2 * co2


def main():
    with open('input.txt', 'r') as fp:
        diagnostics = [l.strip() for l in fp]
        one = part_one(diagnostics)
        print(one)
        two = part_two(diagnostics)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
