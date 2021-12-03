import itertools
import os

import functions


class Step:
    def __init__(self, key, steps=None):
        self.key = key
        self.steps = steps
        self._after = []
        self._before = []

    def add_after(self, w):
        self._after.append(w)

    def add_before(self, b):
        self._before.append(b)

    @property
    def before(self):
        return sorted([self.steps[k.key] for k in self._before],
                      key=lambda x: x.key)

    @property
    def after(self):
        return sorted([self.steps[k.key] for k in self._after],
                      key=lambda x: x.key)

    def __str__(self):
        return self.key

    def __repr__(self):
        return '<{}: ({}), ({})>'.format(
            self.key,
            ','.join(s.key for s in self._before),
            ','.join(s.key for s in self._after)
        )


def time(x):
    return ord(x) - ord('A') + 61


def main(step_data):
    steps = get_step_dictionary(step_data)

    current = sorted([s for k, s in steps.items() if len(s.after) == 0],
                     key=lambda x: x.key)
    route = []
    while len(route) < len(steps):
        current = [
            k for k in current
            if len([c for c in k.after if c in route]) == len(k.after)
        ]
        c = current.pop(0)
        route.append(c)
        possible = set(c.before) | {k for k in current}
        for k in current:
            possible |= set(k.before)
        possible = sorted(possible, key=lambda x: x.key)
        current = possible

    return ''.join(str(k) for k in route)


def main_two(step_data):
    timer = 0
    workers = [0 for _ in range(5)]
    steps = get_step_dictionary(step_data)

    current = sorted([s for k, s in steps.items() if len(s.after) == 0],
                     key=lambda x: x.key)
    route = []
    while current or any([w > 0 for w in workers]):
        current = [
            k for k in current
            if len([c for c in k.after if c in route]) == len(k.after)
        ]

        added = set()
        for i in range(5):
            v = max(0, workers[i] - 1)
            workers[i] = v
            if workers[i] == 0 and current:
                c = current.pop(0)
                workers[i] = time(c.key)
                route.append(c)
                added.add(c)

        possible = {k for k in current}
        for k in added:
            possible |= set(k.before)
        for k in current:
            possible |= set(k.before)
        possible = sorted(possible, key=lambda x: x.key)
        current = possible

        timer += 1
    return timer


def get_step_dictionary(step_data):
    steps = {}
    # setup and determine which step occurs before other steps
    for a, b in functions.get_steps(step_data):
        step = steps.get(a, Step(a, steps=steps))
        steps[a] = step
        if b not in steps:
            steps[b] = Step(b, steps=steps)
        step.add_before(steps[b])

    # set which steps come after other steps
    for key, step in steps.items():
        for b in step.before:
            b.add_after(step)

    return steps


if __name__ == '__main__':
    data = [
        'Step C must be finished before step A can begin.',
        'Step C must be finished before step F can begin.',
        'Step A must be finished before step B can begin.',
        'Step A must be finished before step D can begin.',
        'Step B must be finished before step E can begin.',
        'Step D must be finished before step E can begin.',
        'Step F must be finished before step E can begin.',
    ]
    test = main(data)
    assert test == 'CABDFE'

    filename = os.path.join(functions.get_path(__file__), 'input.txt')
    data = functions.read_file(filename)
    answer = main(data)
    assert answer not in ['BKCJMSDVFGHQRXFYZOAULPIEWT', ]
    print(answer)

    print(main_two(data))
