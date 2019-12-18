def get_orbits(path):
    orbs = {}
    for p in path:
        a, b = p.split(')')
        if a not in orbs:
            orbs[a] = []
        orbs[a].append(b)
    return orbs


def get_len(planet, length, orbs):
    try:
        return sum(get_len(p, length + 1, orbs) for p in orbs[planet]) + length
    except KeyError:
        return length


def part_one(orbs):
    orbs = get_orbits(orbs)
    print(get_len('COM', 0, orbs))


if __name__ == '__main__':
    orbits = []
    with open('input.txt', 'r') as fp:
        orbits = fp.read().split('\n')
    part_one(list(orbits))
