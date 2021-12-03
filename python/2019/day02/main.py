import helpers
from op import run


def part_one():
    program = [int(i) for i in helpers.read_all('input.txt').split(',')]
    program[1] = 12
    program[2] = 2
    instructions = helpers.get_instruction_set(program)
    result = run(instructions)
    print(result[0])


def part_two(answer=None):
    program = [int(i) for i in helpers.read_all('input.txt').split(',')]
    params = [(x, y) for x in range(99) for y in range(99)]
    for args in params:
        cp = program.copy()
        cp[1], cp[2] = args
        instructions = helpers.get_instruction_set(cp)
        result = run(instructions)
        if result[0] == answer:
            print(100 * args[0] + args[1])


if __name__ == '__main__':
    part_one()
    part_two(answer=19690720)
