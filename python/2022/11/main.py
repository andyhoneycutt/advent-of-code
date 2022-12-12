import math
import time
import typing


class Monkey:
    items: typing.List[int] = []
    operation: typing.Tuple
    test_divisor: int = 1
    test_pass: int = 0
    test_fail: int = 0
    inspected: int = 0

    def __init__(self, items, operation, test_divisor, test_pass, test_fail):
        self.items = items
        self.operation = operation
        self.test_divisor = test_divisor
        self.test_pass = test_pass
        self.test_fail = test_fail

    @property
    def op(self):
        _ops = {
            '*': lambda x, y: x * y,
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '/': lambda x, y: x / y,
        }

        def _fn(item) -> bool:
            o = _ops[self.operation[1]]
            s = [item if subj == 'old' else int(subj) for subj in (self.operation[0], self.operation[2])]
            return o(*s)

        return _fn

    def act(self, monkeys, relief=True, lcm=None):
        _op = self.op
        for item in self.items:
            worry = _op(item)
            throw = self.test_fail
            if relief:
                worry = worry // 3
            else:
                worry = worry % lcm
            if worry % self.test_divisor == 0:
                throw = self.test_pass
            monkeys[throw].items.append(worry)
            self.inspected += 1
        self.items = []


def parse_input(inputs):
    m_input = inputs.split("\n\n")
    monkeys = []

    for m in m_input:
        lines = [l.strip() for l in m.split("\n")]
        items = [int(i) for i in lines[1].split(':')[-1].strip().split(',')]
        operation = lines[2].split('=')[-1].strip().split(' ')
        test_divisor = int(lines[3].split(' ')[-1].strip())
        test_pass = int(lines[4].split(' ')[-1].strip())
        test_fail = int(lines[5].split(' ')[-1].strip())
        monkeys.append(
            Monkey(items, operation, test_divisor, test_pass, test_fail)
        )
    return monkeys


def part_one(inputs):
    monkeys = parse_input(inputs)
    for turn in range(20):
        for i, monkey in enumerate(monkeys):
            monkey.act(monkeys)
    inspections = sorted([m.inspected for m in monkeys], reverse=True)
    [a, b, *_] = inspections
    return a * b


def part_two(inputs):
    monkeys = parse_input(inputs)
    # find the lowest common multiple of the test divisors
    # we use this as our stress relief by modulo against it
    lcm = math.lcm(*[m.test_divisor for m in monkeys])
    for turn in range(10000):
        for i, monkey in enumerate(monkeys):
            monkey.act(monkeys, relief=False, lcm=lcm)
    inspections = sorted([m.inspected for m in monkeys], reverse=True)
    [a, b, *_] = inspections
    return a * b


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        inputs = fp.read()
        one = part_one(inputs=f"{inputs}")
        two = part_two(inputs=f"{inputs}")
        print(one)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
