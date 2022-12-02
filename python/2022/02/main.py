import time

HANDS = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

WINS = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

LOSES = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}

SCORES = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}


def score(inputs):
    s = sum([6 if WINS[a] == b else 3 if HANDS[a] == b else 0 for a, b in inputs])
    s += sum([SCORES[b] for _, b in inputs])
    return s


def part_one(inputs):
    return score(inputs)


def part_two(inputs):
    move = {
        # draw
        'Y': lambda x: HANDS[x],
        # lose
        'X': lambda x: LOSES[x],
        # win
        'Z': lambda x: WINS[x],
    }
    modified = [(a, move[b](a)) for a, b in inputs]
    return score(modified)


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        values = [l.split() for l in fp.readlines()]
        one = part_one(values)
        two = part_two(values)
        print(one)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
