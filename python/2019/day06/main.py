def get_orbits(path):
    orbs = {}
    for p in path:
        a, b = p.split(')')
        if a not in orbs:
            orbs[a] = []
        orbs[a].append(b)
    return orbs


def get_len(origin, length, orbs):
    try:
        return sum(get_len(p, length + 1, orbs) for p in orbs[origin]) + length
    except KeyError:
        return length


def get_orbit_for(satellite: str, orbs: dict) -> str:
    for k, v in orbs.items():
        if satellite in v:
            return k


def get_path_for(satellite: str, orbs: dict) -> list:
    orbit = get_orbit_for(satellite, orbs)
    path = [orbit]
    while orbit:
        orbit = get_orbit_for(orbit, orbs)
        if orbit:
            path.append(orbit)
    return path


def len_until(lst, v):
    i = 0
    for c in lst:
        if c == v:
            return i
        i += 1


def get_transfers(origin, target, orbs):
    path_origin = get_path_for(origin, orbs)
    path_target = get_path_for(target, orbs)
    match = [v for v in path_origin if v in path_target]
    node = match[0]
    return len_until(path_origin, node) + len_until(path_target, node)


def part_one(orbs):
    orbs = get_orbits(orbs)
    print(get_len('COM', 0, orbs))


def part_two(orbs):
    orbs = get_orbits(orbs)
    print(get_transfers('YOU', 'SAN', orbs))


if __name__ == '__main__':
    orbits = []
    with open('input.txt', 'r') as fp:
        orbits = fp.read().split('\n')
    part_one(list(orbits))
    part_two(list(orbits))
