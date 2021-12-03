def read_input(name):
    with open(name, 'r') as f:
        return f.readlines()


def read_all(name):
    with open(name, 'r') as f:
        return f.read()


def flatten(two_d):
    output = []
    for one_d in two_d:
        output += one_d
    return output


def get_instruction_set(data):
    if not data:
        return []
    # elif data[0] == 99:
    #     return [[99]] + get_instruction_set(data[1:])
    else:
        return [data[0:4]] + get_instruction_set(data[4:])
