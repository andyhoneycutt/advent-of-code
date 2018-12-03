import os
import re


def get_path(file):
    return os.path.dirname(os.path.realpath(file))


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


def get_fabric(max, val):
    return [[val for _ in range(max)] for y in range(max)]


def max_of(obj_list, keys):
    return max([max([o[k] for o in obj_list]) for k in keys])
