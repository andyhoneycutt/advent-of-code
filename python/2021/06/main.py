import time


class Pond:
    fish = []

    def add(self, fish):
        self.fish.append(fish)

    def advance_day(self):
        for fish in self.fish:
            fish.advance()


class LanternFish:
    timer = 9
    pond = None

    def __init__(self, pond, timer=9):
        self.timer = timer
        self.pond = pond

    def advance(self):
        self.timer -= 1
        if self.timer == -1:
            self.pond.add(LanternFish(self.pond))
            self.timer = 6

    def __str__(self):
        return f"Fish timer is: {self.timer}"


def calc_fish(fish, days=80):
    pond = Pond()
    for f in fish:
        lantern_fish = LanternFish(pond, timer=f)
        pond.add(lantern_fish)

    for day in range(days):
        pond.advance_day()

    return len(pond.fish)


def calc_fish_big(fish, days=80):
    pond = {f: fish.count(f) for f in set(fish)}
    for day in range(days):
        new_pond = {}
        for val in range(1, 9):
            prev = val - 1
            new_pond[prev] = pond.get(val, 0)
        # Each day, a 0 becomes a 6 and adds a new 8 to the end of the list
        if 0 in pond:
            add_fish = pond[0]
            # The new lanternfish starts with an internal timer of 8
            new_pond[8] = add_fish
            # A lanternfish that creates a new fish resets its timer to 6
            new_pond[6] = new_pond.get(6, 0) + add_fish
        pond = new_pond
    counts = [v for k, v in pond.items()]
    return sum(counts)


def main():
    with open('input.txt', 'r') as fp:
        initial = [int(f) for f in fp.read().split(',')]
        one = calc_fish(initial)
        print(one)
        two = calc_fish_big(initial, days=256)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
