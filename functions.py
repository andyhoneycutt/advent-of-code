import os


def get_path(file):
    return os.path.dirname(os.path.realpath(file))


def str_to_num(s):
    op = s[0]
    val = int(s[1:])
    if op == '+':
        return val
    return val * -1


def ftoi(file):
    return [str_to_num(l.strip()) for l in read_file(file)]


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


def distance(s, t):
    return sum(0 if x == y else 1 for x, y in zip(s, t))


def get_similar_string(strings):
    for s in strings:
        for t in strings:
            if s == t:
                continue

            if distance(s, t) == 1:
                return ''.join(x for x, y in zip(s, t) if x == y)