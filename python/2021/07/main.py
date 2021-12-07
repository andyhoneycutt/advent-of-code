import time


def part_one(inputs):
    a = min(inputs)
    b = max(inputs)
    # crabs will be closest to a point within the points range that crabs
    # start out at
    distances = []
    for position in range(a, b):
        # generate a distance to each position for each crab
        distances.append(sum([abs(i - position) for i in inputs]))
    return min(distances)


def fuel_cost(loc, pos):
    # return triangle number of the distance from crab position to arbitrary
    # position
    # https://en.wikipedia.org/wiki/Triangular_number
    distance = abs(loc - pos)
    return distance * (distance + 1) // 2


def part_two(inputs):
    a = min(inputs)
    b = max(inputs)
    fuel_costs = []
    for position in range(a, b):
        # generate the fuel cost for each potential position for each crab
        fuel_costs.append(sum([fuel_cost(i, position) for i in inputs]))
    return min(fuel_costs)


def main():
    with open('input.txt', 'r') as fp:
        initial = list(map(int, fp.read().split(',')))
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
