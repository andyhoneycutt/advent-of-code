def get_vector(a, b):
    return b[0] - a[0], b[1] - a[1]


def sign(x):
    if x == 0:
        return 0
    return 1 if x > 0 else -1
