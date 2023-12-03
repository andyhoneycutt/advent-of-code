import math
import re
import time

def get_symbols(schematic: list):
    symbols = set()
    for line in schematic:
        symbols.update(re.findall('[^0-9]', line.strip()))
    symbols.discard('.')
    return symbols

def get_symbol_locations(schematic: list, symbols=None):
    for y, line in enumerate(schematic):
        for x, char in enumerate(line):
            if char in symbols:
                yield x, y

def get_all_numbers(schematic_row: str, pos: int):
    """
    read all chars left and right until we hit a non-digit, return the new integer
    number can be left and right of pos up to 2 places, as they are no more than 3 digits
    """
    _left = pos
    _right = pos
    while schematic_row[_left - 1].isdigit():
        _left -= 1
        if _left == 0:
            break
    while schematic_row[_right + 1].isdigit():
        _right += 1
        if _right == len(schematic_row) - 1:
            break

    substr = schematic_row[_left:_right+1]
    number = int(substr)
    return number, _left, _right + 1


def get_numbers_adjacent_to_symbols(schematic: list, coordinates: iter):
    for x, y in coordinates:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                try:
                    char = schematic[y + dy][x + dx]
                    if char.isdigit():
                        # get the number
                        number, p1, p2 = get_all_numbers(schematic[y + dy], x + dx)
                        # replace characters from p1 to p2 with .
                        schematic[y + dy] = schematic[y + dy][:p1] + '.' * (p2 - p1) + schematic[y + dy][p2:]
                        yield number
                except IndexError:
                    continue

def part_one(inputs):
    symbols = get_symbols(inputs)
    locations = list(get_symbol_locations(inputs, symbols))
    return sum(get_numbers_adjacent_to_symbols(inputs, locations))


def part_two(inputs):
    symbols = {'*'}
    locations = list(get_symbol_locations(inputs, symbols))
    ratios = 0
    for location in locations:
        numbers = list(get_numbers_adjacent_to_symbols(inputs, [location]))
        if len(numbers) == 2:
            ratios += math.prod(numbers)
    return ratios


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        lines = fp.readlines()
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
