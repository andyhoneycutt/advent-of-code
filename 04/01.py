import os

import functions

if __name__ == '__main__':
    filename = os.path.join(functions.get_path(__file__), 'input.txt')
    data = functions.read_file(filename)
    shifts = sorted([functions.get_shift_log(d) for d in data], key=lambda x: x[0])
    guards = functions.get_guard_shifts(shifts)
    biggest = 0
    guard = 0
    minute = 0
    for gid, _t in guards.items():
        guard_total = 0
        times = iter(_t)
        for start in times:
            end = next(times)
            total = (end - start).seconds / 60
            guard_total += total
            if guard_total > biggest:
                guard = gid
                biggest = guard_total
                minute = end.minute

    print(minute * int(guard), guard, biggest)
