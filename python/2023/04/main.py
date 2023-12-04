import math
import time


def parse_card(line):
    label, rest = line.strip().split(':')
    label = int(label.split(' ')[-1])
    winners, numbers = rest.split('|')
    winners = set([int(x.strip()) for x in winners.strip().split(' ') if x])
    numbers = [int(x.strip()) for x in numbers.strip().split(' ') if x]
    matches = winners.intersection(numbers)
    return label, winners, numbers, matches


def score_card(matches: set):
    """
    winning card is worth 1 for the first match and doubled for each
    subsequent match
    """
    count = len(matches)
    if count == 1:
        return count
    return math.floor(math.pow(2, count - 1))


def part_one(inputs):
    cards = [parse_card(line) for line in inputs]
    scores = [score_card(card[3]) for card in cards]
    return sum(scores)


def part_two(inputs):
    total_cards = len(inputs)
    cards = [(c[0], len(c[3])) for c in [parse_card(line) for line in inputs]]
    stack = cards.copy()
    while len(stack) > 0:
        idx, c = stack.pop()
        total_cards += c
        stack += cards[idx:idx + c]

    return total_cards


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        lines = fp.readlines()
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
