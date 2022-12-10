import time


def noop(register_value, *_):
    return [register_value]


def addx(register_value, value):
    return [register_value, register_value + value]


CMDS = {
    'noop': noop,
    'addx': addx,
}


def part_one(inputs, signals):
    program = parse_input(inputs)
    register = [1]
    for cmd, val in program:
        register += CMDS[cmd](register[-1], val)

    output = sum([register[i - 1] * i for i in signals])
    return output


def part_two(inputs):
    screen = ""
    register = [1]
    program = parse_input(inputs)

    for cmd, val in program:
        register += CMDS[cmd](register[-1], val)

    for cycle, x in enumerate(register[:-1]):
        # is the 3 col cursor over the current X value (it can be -1, 0, or +1 from X)
        # abs value of x - col, e.g.
        # x = 3, col = 5, abs(3 - 5) = 2, so cursor is 2 spaces away: cannot draw
        # x = 5, col = 5, abs(5 - 5) = 0, so cursor is on the value: can draw
        # x = 8, col = 9, abs(8 - 9) = 1, so cursor is 1 space away: can draw
        col = cycle % 40
        if abs(x - col) <= 1:
            screen += "#"
        else:
            screen += "."
        if cycle % 40 == 39:
            screen += "\n"

    # remove new line at the end
    return screen[:-1].split("\n")


def parse_input(inputs):
    for line in inputs:
        # command is first four characters
        cmd = line[:4]
        # value is everything after
        val = int(line[4:]) if line[4:] else None
        yield cmd, val


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        inputs = [l.strip() for l in fp.readlines()]
        one = part_one(inputs=inputs, signals=[20, 60, 100, 140, 180, 220])
        two = part_two(inputs=inputs)
        print(one)
        print("\n".join(two))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
