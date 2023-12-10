import time
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: str = ""
    prev: Optional["Node"] = None
    next: Optional["Node"] = None
    pos: tuple[int, int] = (0, 0)
    step: int = 0

    def __repr__(self):
        return f"Node({self.value}, {self.pos})"

    @property
    def north(self):
        y, x = self.pos
        return y - 1, x

    @property
    def south(self):
        y, x = self.pos
        return y + 1, x

    @property
    def east(self):
        y, x = self.pos
        return y, x + 1

    @property
    def west(self):
        y, x = self.pos
        return y, x - 1

    @property
    def distance(self):
        cur = self
        prev = 0
        # get count for prev until reaching node.value == "S"
        while cur.value != "S":
            cur = cur.prev
            prev += 1

        # get count for next until reaching node.value == "S"
        cur = self
        _next = 0
        while cur.value != "S":
            cur = cur.next
            _next += 1

        return min(prev, _next)


def parse(inputs):
    ys = []
    for line in inputs:
        xs = [c for c in line]
        ys.append(xs)
    return ys


def get_node_list(grid):
    nodes = {}
    start_pos = (0, 0)
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "S":
                start_pos = (y, x)
            node = Node(prev=None, next=None, pos=(y, x), value=col)
            nodes[(y, x)] = node

    cur = nodes[start_pos]

    def can_be_neighbor(a: "Node", b: "Node") -> bool:
        """
        west (x - 1): can have "-", "L", "F"
        east (x + 1): can have "-", "J", "7"
        north (y - 1): can have "|", "7", "F"
        south (y + 1): can have "|", "L", "J"
        """
        # get the direction of the neighbor
        ay, ax = a.pos
        by, bx = b.pos
        if ax == bx:
            # neighbor is north or south
            if ay > by:
                # neighbor is north
                return a.value in "S|LJ" and b.value in "S|7F"
            # neighbor is south
            return a.value in "S|7F" and b.value in "S|LJ"
        # neighbor is east or west
        if ax > bx:
            # neighbor is west
            return a.value in "S-J7" and b.value in "S-LF"
        # neighbor is east
        return a.value in "S-LF" and b.value in "S-J7"

    found = set()
    while True:
        found.add(cur.pos)
        dirs = [cur.north, cur.south, cur.east, cur.west]
        neighbors = [nodes[d] for d in dirs if
                     d in nodes and can_be_neighbor(cur, nodes[d]) and nodes[d].pos not in found]

        if len(neighbors) == 0:
            cur.next = nodes[start_pos]
            nodes[start_pos].prev = cur
            break

        cur.next = neighbors[0]
        cur.next.prev = cur
        cur = cur.next

    return {nodes[i].pos: nodes[i] for i in found}


def part_one(inputs, draw=False):
    lines = parse(inputs)
    nodes = get_node_list(lines)

    grid_y = len(lines)
    grid_x = len(lines[0])

    if draw:
        for y in range(grid_y):
            for x in range(grid_x):
                if (y, x) in nodes:
                    print("X", end="")
                    continue
                print(" ", end="")
            print()

    return max(node.distance for node in nodes.values())


def part_two(inputs):
    return 1


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        lines = [s.strip() for s in fp.readlines()]
        one = part_one(lines.copy(), draw=True)
        print(one)
        two = part_two(lines.copy())
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
