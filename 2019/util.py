import time


def read_input(filename):
    with open(filename, 'r') as fp:
        return fp.read()


def time_fn(fn):
    def _t(*args, **kwargs):
        t = time.time()
        result = fn(*args, **kwargs)
        e = time.time() - t
        print(f"{fn.__name__}: {e:2.6f}")
        return result

    return _t
