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
        return [self.steps[k.key] for k in self._before]

    @property
    def after(self):
        return [self.steps[k.key] for k in self._after]

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

    start = sorted([s for k, s in steps.items() if len(s.after) == 0],
                   key=lambda x: x.key)
    print(start[0])


if __name__ == '__main__':
    filename = os.path.join(functions.get_path(__file__), 'input.txt')
    data = functions.read_file(filename)
    main(data)
