import time


def split_rucksack(value):
    """ split string evenly in half"""
    return value[:len(value) // 2], value[len(value) // 2:]


def in_both(a, b):
    """ return the item in both list a and list b"""
    c, d = set(a), set(b)
    return list(c & d)[0]


def ascii_score(character):
    chars = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return chars.index(character)


def part_one(inputs):
    rucksacks = [split_rucksack(l) for l in inputs]
    common = [in_both(*rucksack) for rucksack in rucksacks]
    return sum([ascii_score(c) for c in common])


def part_two(inputs):
    """ find the common letters between three rucksacks """
    score = 0
    for i in range(0, len(inputs), 3):
        a, b, c = inputs[i:i + 3]
        l = list(set(a) & set(b) & set(c))[0]
        score += ascii_score(l)
    return score


def main():1
    with open('input.txt', 'r', encoding="utf-8") as fp:
        values = [l.strip() for l in fp]
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
