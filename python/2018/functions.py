import datetime
import os
import re


def get_filename(file):
    return os.path.join(get_path(file), 'input.txt')


def get_path(file):
    return os.path.dirname(os.path.realpath(file))


def read_input(filename):
    with open(filename) as f:
        return [int(c) for c in f.read().strip().split()]


def ftoi(file):
    return [int(l.strip()) for l in read_file(file)]


def read_file(file):
    with open(file, 'r') as f:
        return f.readlines()


def has_x(chars, x):
    s = set(chars)
    for c in s:
        if chars.count(c) == x:
            return 1
    return 0


def has_two(chars):
    return has_x(chars, 2)


def has_three(chars):
    return has_x(chars, 3)


# thanks codeguru42 for clever implementation
# https://github.com/codeguru42
def distance(s, t):
    return sum(0 if x == y else 1 for x, y in zip(s, t))


def get_similar_string(strings):
    for s in strings:
        for t in strings:
            if s == t:
                continue

            if distance(s, t) == 1:
                return ''.join(x for x, y in zip(s, t) if x == y)


def get_claims(lines):
    ret = []
    for l in lines:
        cid, left, top, width, height = parse_claim(l)
        claim = {
            'i': cid,
            'l': left,
            't': top,
            'w': width,
            'h': height,
            'x': left + width,
            'y': top + height,
        }
        ret.append(claim)
    return ret


def parse_claim(line):
    pattern = '#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
    return [int(g) for g in re.match(pattern, line).groups()]


def get_fabric(max_value, val):
    return [[val for _ in range(max_value)] for y in range(max_value)]


def max_of(obj_list, keys):
    return max([max([o[k] for o in obj_list]) for k in keys])


def get_shift_log(entry):
    pattern = '\[(.+)\] (.+)'
    matches = re.match(pattern, entry).groups()
    return datetime.datetime.strptime(matches[0], '%Y-%m-%d %H:%M'), matches[1]


def get_guard_id(shift):
    pattern = '\d+'
    return re.findall(pattern, shift)[0]


def get_guard_shifts(shifts_list):
    _log = [0 for _ in range(59)]
    log = {}
    shifts = iter(shifts_list)
    try:
        ptr = next(shifts)
        while True:
            guard = get_guard_id(ptr[1])
            if guard not in log:
                log[guard] = _log.copy()
            s = next(shifts)
            while '#' not in s[1]:
                w = next(shifts)
                for i in range(s[0].minute, w[0].minute):
                    log[guard][i] += 1
                s = next(shifts)
            ptr = s
    except StopIteration:
        pass
    return log


def remove_repelled(data):
    i = 0
    l = len(data)
    while i <= l:
        if i == l:
            break;
        a = ord(data[i])
        b = ord(data[i + 1])
        if max(a, b) - 32 == min(a, b):
            c, d = chr(a), chr(b)
            s = c + d
            t = d + c
            data = data.replace(s, '').replace(t, '')
            l = len(data) - 1
            i = max(0, i - 1)
        else:
            i += 1
    return data


def get_steps(data):
    return [(l[5], l[-12]) for l in [s.strip() for s in data]]
