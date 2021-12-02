import time


def part_one():
    pass


def part_two():
    pass


if __name__ == '__main__':
    start = time.time()
    with open('input.txt', 'r') as fp:
        part_one()
        part_two()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
