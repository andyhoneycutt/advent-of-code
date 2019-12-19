from itertools import permutations

from intcode import run, read_input, input_to_codes


def get_digits(i):
    return [int(x) for x in str(i)]


def get_signals():
    return list(permutations(range(5)))


def list_to_int(lst: list) -> int:
    return int(''.join(lst))


def get_thruster_signal(inst, phase):
    p = iter(phase)
    c = next(p), 0
    for i in range(5):
        thrust = run(list(inst), iter(c))
        try:
            c = next(p), thrust
        except StopIteration:
            pass
    return thrust


def get_max_thruster_signal(sequence):
    signals = get_signals()
    max_signal = 0
    for phase in signals:
        signal = get_thruster_signal(list(sequence), phase)
        max_signal = signal > max_signal and signal or max_signal
    return max_signal


def part_one(inst):
    print(get_max_thruster_signal(list(inst)))


def part_two():
    pass


if __name__ == '__main__':
    instructions = input_to_codes(read_input('input.txt'))
    part_one(instructions)
    part_two(instructions)
