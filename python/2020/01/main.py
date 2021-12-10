import time

def get_2020s(inputs):
    for c in inputs:
        for d in inputs:
            if c + d == 2020:
                return c, d

def get_2020s_3(inputs):
    for a in inputs:
        for b in inputs:
            for c in inputs:
                if a + b + c == 2020:
                    return a, b, c

def part_one(inputs):
    a, b = get_2020s(inputs)
    return a * b

def part_two(inputs):
    a, b, c = get_2020s_3(inputs)
    return a * b * c


def main():
    with open('input.txt', 'r') as fp:
        initial = [int(ln) for ln in fp]
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
