import time
from collections import defaultdict, Counter

VALUES = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

FIVE = 6
FOUR = 5
FULL = 4
THREE = 3
TWO = 2
ONE = 1
HIGH = 0


def parse(line):
    hand, bid = line.split(' ')
    bid = int(bid)
    hand = [VALUES.get(c) if c in VALUES else int(c) for c in hand]
    return hand, bid


def replace_jokers(hand):
    # find most common entry
    c = Counter([c for c in hand if c != VALUES['J']])
    most_common = c.most_common()
    # if there is a tie, pick the highest value
    try:
        replace = max([m[0] for m in most_common if m[1] == most_common[0][1]])
    except (IndexError, ValueError):
        # hand full of jokers, most_common is empty
        replace = VALUES['A']
    _hand = [replace if c == 11 else c for c in hand]
    return _hand


def score(hand, p2=False):
    h = set(hand)

    # handle jokers for part 2
    if p2 and 11 in hand:
        _hand = replace_jokers(hand)
        h = set(_hand)
        hand = _hand

    match len(h):
        case 1:
            return FIVE
        case 2:
            if any(hand.count(c) == 4 for c in h):
                return FOUR
            return FULL
        case 3:
            if any(hand.count(c) == 3 for c in h):
                return THREE
            return TWO
        case 4:
            return ONE
        case _:
            return HIGH


def rank(hands, p2=False):
    scored = defaultdict(list)

    # get a score for each hand, group by scores
    for hand, bid in hands:
        _hand = hand
        if p2:
            _hand = [1 if c == 11 else c for c in hand]
        cmp = [chr(97 + c) for c in _hand]
        scored[score(hand, p2=p2)].append((_hand, bid, cmp))

    # sort each scored group by cmp
    for sc, meta in scored.items():
        scored[sc] = sorted(meta, key=lambda x: x[2], reverse=True)

    # score according to rank
    order = [FIVE, FOUR, FULL, THREE, TWO, ONE, HIGH]
    hands_remaining = len(hands)
    for o in order:
        for hand, bid, cmp in scored[o]:
            winnings = bid * hands_remaining
            hands_remaining -= 1
            yield winnings


def part_one(inputs):
    parsed = [parse(line) for line in inputs]
    return sum(rank(parsed))


def part_two(inputs):
    parsed = [parse(line) for line in inputs]
    return sum(rank(parsed, p2=True))


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
