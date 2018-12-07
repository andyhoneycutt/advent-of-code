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

    def __repr__(self):
        return self.key + '; ' + \
               ','.join(s.key for s in self._before) + '; ' + \
               ','.join(s.key for s in self._after)


def main(step_data):
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

    current = sorted([s for k, s in steps.items() if len(s.after) == 0],
                   key=lambda x: x.key)[0]

    route = [current, ]
    while current.before:
        n = current.before[0]
        route.append(n)
        current = n

    print(''.join(k.key for k in route))


if __name__ == '__main__':
    filename = os.path.join(functions.get_path(__file__), 'input.txt')
    data = functions.read_file(filename)
    main(data)
