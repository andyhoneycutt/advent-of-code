import time


class Submarine:
    commands: list = []
    depth: int = 0
    horizontal: int = 0

    def __init__(self, commands):
        self.commands = commands
        self._cmd = {
            'forward': self.forward,
            'down': self.down,
            'up': self.up,
        }

    def run(self):
        for cmd, val in self.commands:
            self._cmd[cmd](val)

    def up(self, val):
        self.depth -= val

    def down(self, val):
        self.depth += val

    def forward(self, val):
        self.horizontal += val


class SubPartTwo(Submarine):
    aim: int = 0

    def up(self, val):
        self.aim -= val

    def down(self, val):
        self.aim += val

    def forward(self, val):
        self.horizontal += val
        self.depth += self.aim * val


def part_one(inputs):
    submarine = Submarine(inputs)
    submarine.run()
    return submarine.horizontal * submarine.depth


def part_two(inputs):
    submarine = SubPartTwo(inputs)
    submarine.run()
    return submarine.horizontal * submarine.depth


if __name__ == '__main__':
    start = time.time()
    with open('input.txt', 'r') as fp:
        values = []
        for line in fp.readlines():
            c, value = line.split(' ')
            values.append((c, int(value)))
        one = part_one(values)
        print(one)
        two = part_two(values)
        print(two)
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
