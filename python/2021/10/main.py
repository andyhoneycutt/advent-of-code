import time

def part_one(inputs):
    return inputs


def part_two(inputs):
    return inputs

def main():
    with open('input.txt', 'r') as fp:
        initial = [ln.strip() for ln in fp]
        one = part_one(initial)
        print(one)
        two = part_two(initial)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
