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


def _left(n: Node):
    return n.left


def _right(n: Node):
    return n.right


DIRS = {
    'L': _left,
    'R': _right,
}


def walk(root: str = 'AAA', last: str = 'ZZZ', path: list = None, nodes: dict = None, current: str = None,
         walked: list = None):
    if current is None:
        current = root
    if current == last:
        return walked
    for direction in path:
        current = DIRS[direction](nodes[current]).name
        walked.append(current)
    return walk(root, last, path, nodes, current, walked)


def part_one(inputs):
    path, nodes = parse(inputs)
    nodes = link(nodes)
    return len(walk('AAA', 'ZZZ', path, nodes, None, []))


def walk_two(last, path):
    i = 0
    pl = len(path)
    while not last.name.endswith('Z'):
        c = i % pl
        last = DIRS[path[c]](last)
        i += 1
    return i


def part_two(inputs):
    path, nodes = parse(inputs)
    nodes = link(nodes)
    last = [v for k, v in nodes.items() if k.endswith('A')]
    walked = [walk_two(n, path) for n in last]
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
