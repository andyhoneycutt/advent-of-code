import os

import functions

if __name__ == '__main__':
    filename = os.path.join(functions.get_path(__file__), 'input.txt')
    data = sorted(functions.read_file(filename))
    shifts = [functions.get_shift_log(d) for d in data]
    guards = functions.get_guard_shifts(shifts)
    minutes = [(0, 0) for _ in range(59)]
    for gid, times in guards.items():
        for m, t in enumerate(minutes):
            if times[m] > t[1]:
                minutes[m] = (gid, times[m], m)
    max_time = max(t[1] for t in minutes)
    guard = next(m for m in minutes if m[1] == max_time)
    print(int(guard[0]) * guard[2])
