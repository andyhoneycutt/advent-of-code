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


def run(codes, user_input):
    i = 0
    diagnostic = []
    if not hasattr(user_input, '__next__'):
        user_input = iter([user_input])
    while codes[i] != 99:
        _, mode2, mode1, opcode = parse_op(codes[i])
        d = codes[i + 3]

        # add
        if opcode == 1:
            a = get_value(mode1, codes[i + 1], codes)
            b = get_value(mode2, codes[i + 2], codes)
            codes[d] = a + b
            i += 4
        # multiply
        elif opcode == 2:
            a = get_value(mode1, codes[i + 1], codes)
            b = get_value(mode2, codes[i + 2], codes)
            codes[d] = a * b
            i += 4
        # provide input
        elif opcode == 3:
            try:
                codes[codes[i + 1]] = next(user_input)
            except StopIteration:
                return diagnostic and int(''.join(diagnostic)) or 0
            i += 2
        # output value
        elif opcode == 4:
            diagnostic.append(str(get_value(mode1, codes[i + 1], codes)))
            i += 2
        # jump if true
        elif opcode == 5:
            a = get_value(mode1, codes[i + 1], codes)
            b = get_value(mode2, codes[i + 2], codes)
            i = a and b or i + 3
        # jump if false
        elif opcode == 6:
            a = get_value(mode1, codes[i + 1], codes)
            b = get_value(mode2, codes[i + 2], codes)
            i = not a and b or i + 3
        # less than
        elif opcode == 7:
            a = get_value(mode1, codes[i + 1], codes)
            b = get_value(mode2, codes[i + 2], codes)
            codes[d] = a < b and 1 or 0
            i += 4
        # equal
        elif opcode == 8:
            a = get_value(mode1, codes[i + 1], codes)
            b = get_value(mode2, codes[i + 2], codes)
            codes[d] = a == b and 1 or 0
            i += 4

    val = int(''.join(diagnostic))
    print(val)
    return val
