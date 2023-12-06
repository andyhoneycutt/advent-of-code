import math
import re
import time


def parse(lines):
    times = [int(t) for t in re.findall(r'\d+', lines[0])]
    distances = [int(t) for t in re.findall(r'\d+', lines[1])]
    return times, distances


def hold_button(dist, tm):
    """
    holding the button down for 0 to dist seconds
    boat will travel n per millisecond for up to tm milliseconds
    boat needs to travel full dist in tm seconds
    """
    for n in range(tm):
        if n * (tm - n) > dist:
            yield n


def part_one(inputs):
    times, distances = parse(inputs)
    hold_times = []
    for tm, dist in zip(times, distances):
        _holds = list(hold_button(dist, tm))
        print(_holds, tm, dist)
        hold_times.append(len(_holds))
    return math.prod(hold_times)


def part_two(inputs):
    times, distances = parse(inputs)
    tm = int(''.join([str(t) for t in times]))
    dist = int(''.join([str(t) for t in distances]))
    _holds = list(hold_button(dist, tm))
    return len(_holds)


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        lines = [s.strip() for s in fp.readlines()]
        one = part_one(lines)
        print(one)
        two = part_two(lines)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
