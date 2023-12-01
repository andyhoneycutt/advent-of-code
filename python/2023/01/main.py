import re
import time


def _get_all_numbers(line: str):
    numbers = re.findall(r'\d', line)
    digits = f'{numbers[0]}{numbers[-1]}'
    return int(digits)


def get_calibration(document):
    # get only the numbers from the document
    for line in document:
        yield _get_all_numbers(line)


def replace_numbers(document):
    _map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    for line in document:
        # find the first spelled-out number and replace it with the number
        # then yield the line
        buffer = ''
        for character in line:
            if character.isdigit():
                buffer = ''
                continue
            buffer += character
            for key in _map.keys():
                if key in buffer:
                    line = line.replace(key, str(_map[key]), 1)
                    buffer = ''
        yield line


def part_one(inputs):
    return sum(get_calibration(inputs))


def part_two(inputs):
    return sum(get_calibration(replace_numbers(inputs)))


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        lines = fp.readlines()
        one = part_one(lines)
        print(one)
        two = part_two(lines)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
