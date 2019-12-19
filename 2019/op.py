import math

import helpers


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


FUNCTIONS = [
    None,
    add,
    multiply,
]


def op(i, i_set):
    if i[0] in [1, 2]:
        a = get_at(i_set, i[1])
        b = get_at(i_set, i[2])
        v = FUNCTIONS[i[0]](a, b)
        update_at(i_set, i[3], v)


def run(instructions):
    for instruction in instructions:
        op(instruction, instructions)
    return helpers.flatten(instructions)


def get_pos(idx):
    return math.floor(idx / 4), idx % 4


def get_at(i_set, idx):
    c, p = get_pos(idx)
    return i_set[c][p]


def update_at(i_set, idx, val):
    c, p = get_pos(idx)
    i_set[c][p] = val
