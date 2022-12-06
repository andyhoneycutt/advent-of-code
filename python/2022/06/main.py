import time


def first_unique_n(value, n):
    for i, c in enumerate(value):
        if len(set(value[i:i + n])) == n:
            return i + n


def part_one(inputs):
    return first_unique_n(inputs, 4)


def part_two(inputs):
    return first_unique_n(inputs, 14)


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        inputs = fp.read()
        one = part_one(inputs=inputs)
        two = part_two(inputs=inputs)
        print(one)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
