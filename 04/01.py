import os

import functions

if __name__ == '__main__':
    filename = os.path.join(functions.get_path(__file__), 'input.txt')
    data = sorted(functions.read_file(filename))
    shifts = [functions.get_shift_log(d) for d in data]
    guards = functions.get_guard_shifts(shifts)
    totals = [{'id': gid, 't': sum(t)} for gid, t in guards.items()]
    max_total = max([g['t'] for g in totals])
    _guard = next(guard for guard in totals if guard['t'] == max_total)
    log = guards[_guard['id']]
    minute = log.index(max(log))
    print(minute * int(_guard['id']))
