import io
import re
import time
from typing import List

import pandas as pd

TEST_INPUT = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


def score_card(answer, card, scored_positions):
    total = 0
    for i, row in enumerate(scored_positions):
        for j, col in enumerate(row):
            if not col:
                total += int(card[i][j])
    return int(answer) * total


def part_one(inputs: List, answers):
    cards = [[[0 for i in range(5)] for j in range(5)] for _ in range(len(inputs))]
    for answer in answers:
        for idx, card in enumerate(inputs):
            for i, row in enumerate(card):
                try:
                    match = row.index(answer)
                    cards[idx][i][match] = 1
                    cdf = pd.DataFrame(cards[idx])
                    for j, rs in enumerate(cards[idx]):
                        if sum(rs) == 5:
                            return score_card(answer, card, cards[idx])
                        if sum(list(cdf[cdf.columns[j]])) == 5:
                            return score_card(answer, card, cards[idx])
                except ValueError:
                    pass


def part_two(inputs: List, answers):
    cards = [[[0 for i in range(5)] for j in range(5)] for _ in range(len(inputs))]
    wins = []
    last = []
    for answer in answers:
        for idx, card in enumerate(inputs):
            if idx in wins:
                continue
            for i, row in enumerate(card):
                try:
                    match = row.index(answer)
                    cards[idx][i][match] = 1
                    cdf = pd.DataFrame(cards[idx])
                    for j, rs in enumerate(cards[idx]):
                        if sum(rs) == 5 or sum(list(cdf[cdf.columns[j]])) == 5:
                            last.append(score_card(answer, card, cards[idx]))
                            wins.append(idx)
                            continue
                except ValueError:
                    pass
    return last[-1]


def read_cards(data):
    cards = []
    card = []
    lines = list([d for d in data if d.strip()])
    for line in lines:
        row = re.split('\s+', line.lstrip(' ').rstrip("\n"))
        card.append(row)
        if len(card) == 5:
            cards.append(card)
            card = []
    return cards


def test():
    inp = io.StringIO(TEST_INPUT)
    draws = inp.readline().rstrip().split(',')
    test_input = read_cards(inp)
    score_one = part_one(test_input, answers=draws)
    assert score_one == 4512, f"{score_one} != 4512"


def test2():
    inp = io.StringIO(TEST_INPUT)
    draws = inp.readline().rstrip().split(',')
    test_input = read_cards(inp)
    score_two = part_two(test_input, answers=draws)
    assert score_two == 1924, f"{score_two} != 1924"


def main():
    with open('input.txt', 'r') as fp:
        draws = fp.readline().rstrip().split(',')
        card_inputs = read_cards(fp)
        one = part_one(card_inputs, answers=draws)
        print(one)
        two = part_two(card_inputs, answers=draws)
        print(two)


if __name__ == '__main__':
    test()
    test2()
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
