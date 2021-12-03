import math

import helpers


def fuel(mass):
    return math.floor(int(mass) / 3) - 2


def fuel_two(mass):
    f = math.floor(int(mass) / 3) - 2
    if f <= 0:
        return 0
    return f + fuel_two(f)


def day_one():
    print(sum(fuel(m) for m in helpers.read_input('input.txt')))


def day_two():
    print(sum(fuel_two(m) for m in helpers.read_input('input.txt')))


if __name__ == '__main__':
    day_one()
    day_two()
