from intcode import read_input, input_to_codes, run


def part_one(inst):
    run(inst, 1)


def part_two(inst):
    run(inst, 5)


if __name__ == '__main__':
    instructions = input_to_codes(read_input('input.txt'))
    part_one(list(instructions))
    part_two(list(instructions))
