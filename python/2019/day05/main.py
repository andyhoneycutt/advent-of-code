from intcode import input_to_codes, run
from util import read_input


def part_one(inst):
    run(inst, 1)


def part_two(inst):
    run(inst, 5)


if __name__ == '__main__':
    instructions = input_to_codes(read_input('input.txt'))
    part_one(list(instructions))
    part_two(list(instructions))
