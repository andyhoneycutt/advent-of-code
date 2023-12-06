import time

DEBUG = False

relationships = {
    "seeds": "seed-to-soil",
    "seed-to-soil": "soil-to-fertilizer",
    "soil-to-fertilizer": "fertilizer-to-water",
    "fertilizer-to-water": "water-to-light",
    "water-to-light": "light-to-temperature",
    "light-to-temperature": "temperature-to-humidity",
    "temperature-to-humidity": "humidity-to-location",
}


def read_almanac(lines: list[str]):
    ln = lines.pop(0)
    name = ln.split(":")[0].replace(" map", "")
    ranges = []
    while True:
        if "map" not in ln:
            ranges.append([int(x) for x in ln.split(":")[1].split()])
        try:
            line = lines.pop(0)
        except IndexError:
            break
        if line == "":
            break
        ranges.append([int(x) for x in line.split()])
    return Almanac(name, ranges)


class Almanac:
    name: str
    ranges: list

    def __init__(self, name: str, ranges: list):
        self.name = name
        self.ranges = ranges

    def __str__(self):
        return f"{self.name}: {self.ranges}"


def part_one(inputs):
    seeds = read_almanac(inputs)
    almanacs = []
    while inputs:
        almanac = read_almanac(inputs)
        almanacs.append(almanac)

    locations = []
    for seed in seeds.ranges[0]:
        if DEBUG:
            print(f"seed: {seed}")
        for almanac in almanacs:
            for dest, src, rng in almanac.ranges:
                if src <= seed <= src + rng:
                    diff = seed - src
                    if DEBUG:
                        print(f"{seed} -> {dest + diff}")
                    seed = dest + diff
                    break
        locations.append(seed)
    return min(locations)


def part_two(inputs):
    seeds = read_almanac(inputs)
    almanacs = []
    while inputs:
        almanac = read_almanac(inputs)
        almanacs.append(almanac)

    locations = []
    seed_ranges = iter(seeds.ranges[0])
    while True:
        try:
            strt = next(seed_ranges)
            length = next(seed_ranges)
        except StopIteration:
            break
        for almanac in almanacs:
            for dest, src, rng in almanac.ranges:
                if src <= length <= src + rng:
                    diff = length - src
                    length = dest + diff
                    break
        locations.append(strt)
    if DEBUG:
        print(locations)
    return min([l for l in locations if l > 0])


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        lines = [l.strip() for l in fp.readlines()]
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
