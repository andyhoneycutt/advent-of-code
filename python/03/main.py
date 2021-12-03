import time


def part_one(inputs):
    return inputs


def part_two(inputs):
    return inputs


def main():
    with open('input.txt', 'r') as fp:
        values = []
        for line in fp.readlines():
            c, value = line.split(' ')
            values.append((c, int(value)))
        one = part_one(values)
        print(one)
        two = part_two(values)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
