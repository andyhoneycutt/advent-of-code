import re
import time

def part_one(inputs):
    valid = []
    for match in inputs:
        i, j, c, password = match
        if i <= password.count(c) <= j:
            valid.append(password)
    return len(valid)

def part_two(inputs):
    valid = []
    for match in inputs:
        i, j, c, password = match
        a, b = password[i-1], password[j-1]
        if (a == c or b == c) and a != b:
            valid.append(password)
    return len(valid)


def parse_input(fp):
    pattern = re.compile(r'(\d+)-(\d+) ([a-z]): (\w+)')
    for ln in fp:
        a, b, c, d = pattern.findall(ln)[0]
        yield int(a), int(b), c, d


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
