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


def part_one(inputs):
    submarine = Submarine(inputs)
    submarine.run()
    return submarine.horizontal * submarine.depth


def part_two():
    pass


if __name__ == '__main__':
    start = time.time()
    with open('input.txt', 'r') as fp:
        values = []
        for line in fp.readlines():
            cmd, val = line.split(' ')
            values.append((cmd, int(val)))
        one = part_one(values)
        print(one)
        part_two()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
