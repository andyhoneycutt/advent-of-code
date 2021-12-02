import time


def part_one(pings):
    total = 0
    for i, value in enumerate(pings):
        try:
            if pings[i+1] > value:
                total += 1
        except IndexError:
            pass
    return total


def part_two(pings):
    c = len(pings) - 3
    sets = [pings[i:i+3] for i, _ in enumerate(pings) if i <= c]
    sums = [sum(p) for p in sets]
    return part_one(sums)


if __name__ == '__main__':
    start = time.time()
    with open('input.txt', 'r') as fp:
        values = [int(ln) for ln in fp.readlines()]
        one = part_one(values)
        two = part_two(values)
        print(one)
        print(two)
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
