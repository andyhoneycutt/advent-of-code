import time


def get_cals(elves):
    return [sum(int(x) for x in elf) for elf in elves]


def part_one(inputs):
    return max(inputs)


def part_two(inputs):
    return sum(sorted(inputs, reverse=True)[:3])


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        lines = fp.read()
        values = [x.split('\n') for x in lines.split('\n\n')]
        cals = get_cals(values)
        one = part_one(cals)
        two = part_two(cals)
        print(one)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
