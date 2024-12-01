import time

def dist(a, b):
    return abs(a - b)

def part_one(inputs):
    list_a = []
    list_b = []
    for line in inputs:
        a, b = line.split("   ")
        list_a.append(int(a))
        list_b.append(int(b))
    list_a = sorted(list_a)
    list_b = sorted(list_b)
    distances = [dist(a, b) for a, b in zip(list_a, list_b)]
    return sum(distances)


def part_two(inputs):
    list_a = []
    list_b = []
    for line in inputs:
        a, b = line.split("   ")
        list_a.append(int(a))
        list_b.append(int(b))
    counts = []
    for a in list_a:
        count = list_b.count(a)
        counts.append(count * a)
    return sum(counts)


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
