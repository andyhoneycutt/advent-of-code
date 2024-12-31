import re
import time

def to_ints(ln):
    # convert csv to ints
    return [int(x) for x in ln.replace("mul(", "").replace(")", "").split(',')]

def part_one(inputs):
    # only keep commas and numbers
    file_string = "".join(inputs)
    result = 0
    for match in re.finditer(r"mul\(\d+,\d+\)", file_string):
        a, b = to_ints(match.group())
        result += a * b
    return result


def part_two(inputs):
    file_string = "".join(inputs)
    enabled = True
    result = 0
    for match in re.finditer(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", file_string):
        if match.group() == "don't()":
            enabled = False
            continue
        if match.group() == "do()":
            enabled = True
            continue
        if enabled:
            a, b = to_ints(match.group())
            result += a * b
    return result


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
