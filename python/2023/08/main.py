import time
from dataclasses import dataclass
from math import lcm
from typing import Optional


@dataclass
class Node:
    name: str
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.name == other.name and self.left.name == other.left.name and self.right.name == other.right.name

    def __repr__(self):
        return self.name


def parse(inputs):
    path = [c for c in inputs.pop(0)]
    inputs.pop(0)
    nodes = []
    for l in inputs:
        node, rest = l.split(' = ')
        left, right = rest.split(',')
        nodes.append((node, left.strip().strip('('), right.strip().strip(')')))
    return path, nodes


def link(nodes):
    linked = {}
    for node in nodes:
        name, left, right = node
        linked[name] = Node(name=name)

    for node in nodes:
        name, left, right = node
        linked[name].left = linked[left]
        linked[name].right = linked[right]

    return linked


DIRS = {
    'L': lambda n: n.left,
    'R': lambda n: n.right,
}


def walk(last, path):
    i = 0
    pl = len(path)
    while not last.name.endswith('Z'):
        c = i % pl
        last = DIRS[path[c]](last)
        i += 1
    return i


def part_one(inputs):
    path, nodes = parse(inputs)
    nodes = link(nodes)
    return walk(nodes['AAA'], path)


def part_two(inputs):
    path, nodes = parse(inputs)
    nodes = link(nodes)
    last = [v for k, v in nodes.items() if k.endswith('A')]
    walked = [walk(n, path) for n in last]
    return lcm(*walked)


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        lines = [s.strip() for s in fp.readlines()]
        one = part_one(lines.copy())
        print(one)
        two = part_two(lines.copy())
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
