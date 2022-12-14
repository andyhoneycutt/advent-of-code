from itertools import permutations

from intcode import run, input_to_codes
from util import read_input


def get_digits(i):
    return [int(x) for x in str(i)]


def get_signals(signal_range: range):
    return list(permutations(signal_range))


def list_to_int(lst: list) -> int:
    return int(''.join(lst))


def get_thruster_signal(inst, phase, copy_sequence=True):
    p = iter(phase)
    c = next(p), 0
    thrust = 0
    for i in range(5):
        seq = copy_sequence and list(inst) or inst
        thrust = run(seq, iter(c))
        try:
            c = next(p), thrust
        except StopIteration:
            pass
    return thrust


def get_thruster_signal_feedback(inst, phase):
    amps = [list(inst) for _ in range(5)]
    thrust = 0
    for amp in amps:
        thrust = get_thruster_signal(amp, phase, copy_sequence=False)
    for amp in amps:
        thrust = run(amp, thrust)
    return thrust


def get_max_thruster_signal(sequence: list, signal_range: range) -> int:
    signals = get_signals(signal_range)
    max_signal = 0
    for phase in signals:
        signal = get_thruster_signal(list(sequence), phase)
        max_signal = signal > max_signal and signal or max_signal
    return max_signal


def run_signal_to_halt(sequence: list, signal_range: range) -> int:
    signals = get_signals(signal_range)
    max_signal = 0
    for phase in signals:
        signal = get_thruster_signal_feedback(sequence, phase)
        max_signal = signal > max_signal and signal or max_signal
    return max_signal


def part_one(inst):
    print(get_max_thruster_signal(list(inst), signal_range=range(5)))


def part_two(inst):
    print(run_signal_to_halt(list(inst), signal_range=range(5, 10)))


if __name__ == '__main__':
    instructions = input_to_codes(read_input('input.txt'))
    part_one(instructions)
    part_two(instructions)
