import math
import time


class Game:
    def __init__(self, config, _id, rounds):
        self.id = _id
        self.config = config
        self.rounds = rounds or []

    @staticmethod
    def parse(line):
        game, rounds = line.split(':')
        _id = int(game.split(' ')[1])
        rounds = rounds.split(';')
        results = []
        for _round in rounds:
            result = {
                'red': 0,
                'green': 0,
                'blue': 0,
            }
            rolls = _round.strip().split(',')
            for roll in rolls:
                count, color = roll.strip().split(' ')
                result[color] += int(count)
            results.append(result)
        return {
            '_id': _id,
            'rounds': results,
        }

    @property
    def is_valid(self):
        for _round in self.rounds:
            if not (_round['red'] <= self.config['red'] and
                    _round['green'] <= self.config['green'] and
                    _round['blue'] <= self.config['blue']):
                return False
        return True

    def minimum_set(self):
        return {
            'red': max([_round['red'] for _round in self.rounds]),
            'green': max([_round['green'] for _round in self.rounds]),
            'blue': max([_round['blue'] for _round in self.rounds]),
        }

    def power(self):
        return math.prod(self.minimum_set().values())

    def __str__(self):
        return f'Game {self.id}'

    def __repr__(self):
        return self.__str__()


def parse_games(inputs, config):
    for line in inputs:
        yield Game(config=config, **Game.parse(line))


def part_one(inputs):
    config = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    games = parse_games(inputs, config)
    return sum([game.id for game in games if game.is_valid])


def part_two(inputs):
    config = {}
    games = parse_games(inputs, config)
    return sum([game.power() for game in games])


def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        lines = fp.readlines()
        one = part_one(lines)
        print(one)
        two = part_two(lines)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
