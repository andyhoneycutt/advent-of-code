import time

def is_bad(nodes: list):
    # is all increasing or all decreasing?
    if nodes != sorted(nodes) and nodes != sorted(nodes, reverse=True):
        return 1

    for i in range(len(nodes) - 1):
        if nodes[i] == nodes[i + 1]:
            return 1
        if abs(nodes[i] - nodes[i + 1]) > 3:
            return 1

    return 0

def tolerate_bad(nodes: list):
    if not is_bad(nodes):
        return 0
    # try removing one node
    for i in range(len(nodes)):
        _nodes = nodes.copy()
        _nodes.pop(i)
        if not is_bad(_nodes):
            return 0
    return 1


def part_one(inputs):
    reports = []
    for ln in inputs:
        reports.append([int(x) for x in ln.split(" ")])
    safe_nodes = [n for n in reports if not is_bad(n)]
    return len(safe_nodes)


def part_two(inputs):
    reports = []
    for ln in inputs:
        reports.append([int(x) for x in ln.split(" ")])
    safe_nodes = [n for n in reports if not tolerate_bad(n)]
    return len(safe_nodes)

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
