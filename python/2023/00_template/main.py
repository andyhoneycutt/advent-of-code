import time

def part_one(inputs):
    return 1


def part_two(inputs):
    return 1


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
