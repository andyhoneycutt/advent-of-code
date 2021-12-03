def get_move(last, length, marble):
    if length == 0:
        return 0

    if marble % 23 == 0:
        move = last - 7 % length
        if move < 0:
            move = length - move
        return move

    if marble > 0:
        return last + 2 % length


def get_score(game):
    players = [0 for _ in range(game[0])]
    marbles = game[1]
    moves = []
    last_move = 0
    for i in range(marbles):
        player = i % len(players)
        move = get_move(last_move, len(moves), i)
        print(i, move, len(moves) - 1, last_move)
        if i > 0 and i % 23 == 0:
            moves.pop(move)
            players[player] += i + moves[move]
        else:
            moves.insert(move, i)
        last_move = move
    return max(players)


if __name__ == '__main__':
    data = [
        (10, 1618, 8317),
        (13, 7999, 146373),
        (17, 1104, 2764),
        (21, 6111, 54718),
        (30, 6807, 37305),
    ]

    for d in data:
        player, score = get_score(d)
        assert score == d[2]

    print(get_score((441, 71032)))
