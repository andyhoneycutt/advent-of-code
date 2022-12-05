import re
import time
from collections import defaultdict


def init_matrix(input_str):
    """ every 1+3 character is a value in a box"""
    s_boxes, moves = input_str.split("\n\n")
    boxes = s_boxes.split("\n")[::-1]
    columns = int(boxes.pop(0).split()[-1])
    stacks = defaultdict(list)
    # fill in the boxes
    for box in boxes:
        for i in range(1, len(box), 4):
            val = box[i].strip()
            if val:
                stacks[f'{i // 4 + 1}'].append(val)

    moves = [l.split() for l in re.sub(r'move|from|to', '', moves).split("\n")]
    return stacks, moves


def run_moves(stacks, moves, as_whole=False):
    # process each move against the stacks
    # move N from A to B
    for move in moves:
        num_moves, from_stack, to_stack = move
        num_moves = int(num_moves)
        if as_whole:
            stacks[to_stack].extend(stacks[from_stack][-num_moves:])
            stacks[from_stack] = stacks[from_stack][:-num_moves]
            continue
        while num_moves:
            val = stacks[from_stack].pop()
            stacks[to_stack].append(val)
            num_moves -= 1
    return stacks


def part_one(inputs):
    stacks, moves = init_matrix(inputs)
    # process each move against the stacks
    # move N from A to B
    stacks = run_moves(stacks, moves)
    return ''.join([s[-1] for _, s in stacks.items()])


def part_two(inputs):
    stacks, moves = init_matrix(inputs)
    # process each move against the stacks
    # move N from A to B as a whole group
    stacks = run_moves(stacks, moves, as_whole=True)
    return ''.join([s[-1] for _, s in stacks.items()])


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        inputs = fp.read()
        one = part_one(inputs=inputs)
        two = part_two(inputs=inputs)
        print(one)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
