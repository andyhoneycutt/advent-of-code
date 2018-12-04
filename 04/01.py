import os

import functions

if __name__ == '__main__':
    filename = os.path.join(functions.get_path(__file__), 'input.txt')
    data = functions.read_file(filename)
    shifts = sorted([functions.get_shift_log(d) for d in data], key=lambda x: x[0])
    guards = functions.get_guard_shifts(shifts)
    times = {}
    print(guards)
