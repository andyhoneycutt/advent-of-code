import time

SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

AUTO_SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

VALID = ('[]', '{}', '<>', '()')

def get_score(ln):
    for c in ln:
        try:
            return SCORES[c]
        except KeyError:
            pass
    return 0

def get_autocomplete_score(ln):
    score = 0
    for c in ln:
        score *= 5
        score += AUTO_SCORES[c]
    return score


def parse_input(ln):
    pairs = {a: b for a, b in VALID}
    expected = []
    for c in ln:
        if c in pairs:
            expected.append(c)
            continue
        if c != pairs[expected.pop()]:
            return c, None
    return None, reversed([pairs[c] for c in expected])


def part_one(inputs):
    parsed = [p for p, _ in [parse_input(ln) for ln in inputs]]
    score = sum([get_score(ln) for ln in parsed if ln])
    return score


def part_two(inputs):
    lines = [b for a, b in [parse_input(ln) for ln in inputs] if not a]
    scores = sorted([get_autocomplete_score(ln) for ln in lines])
    i = len(scores) // 2
    return scores[i]


def main():
    with open('input.txt', 'r') as fp:
        initial = [ln.strip() for ln in fp]
        one = part_one(initial)
        print(one)
        two = part_two(initial)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
