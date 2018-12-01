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
    with open(file, 'r') as f:
        return [str_to_num(l.strip()) for l in f.readlines()]
