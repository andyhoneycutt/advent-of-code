def read_input(filename):
    with open(filename, 'r') as fp:
        return fp.read()


def input_to_codes(string):
    return [int(i) for i in string.split(',')]


def parse_op(c):
    parsed = f"{c:05d}"
    opcode = int(parsed[-2:])
    modes = [int(i) for i in parsed[0:3]]
    return modes + [opcode]


def get_value(mode, inp, memory):
    if mode == 0:
        return memory[inp]
    return inp


def run(codes):
    i = 0
    while codes[i] != 99:
        mode3, mode2, mode1, opcode = parse_op(codes[i])
        a = get_value(mode1, codes[i+1], codes)
        b = get_value(mode2, codes[i+2], codes)
        d = get_value(mode3, codes[i+3], codes)

        # add
        if opcode == 1:
            codes[d] = a + b
            i += 4
        # multiply
        elif opcode == 2:
            d = codes[i+3]
            codes[d] = a * b
            i += 4
        # provide input
        elif opcode == 3:
            inp = 1
            codes[a] = inp
            i += 2
        # output value
        elif opcode == 4:
            a = codes[i+1]
            i += 2
            print(get_value(mode1, a, codes), end='')


def part_one(inst):
    run(inst)


if __name__ == '__main__':
    instructions = [int(i) for i in read_input('input.txt').split(',')]
    part_one(instructions)
