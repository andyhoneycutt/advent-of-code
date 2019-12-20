from itertools import groupby


def get_pw_array(pw):
    return [int(i) for i in str(pw)]


def has_only_two_adjacent_same_digits(pw):
    groups = [len(list(g)) for _, g in groupby(str(pw))]
    return 2 in groups


def has_two_adjacent_same_digits(pw):
    e = len(pw) - 1
    for i, n in enumerate(pw):
        if i != e and n == pw[i+1]:
            return True
    return False


def never_decreases(pw):
    e = len(pw) - 1
    for i, n in enumerate(pw):
        if i != e and n > pw[i+1]:
            return False
    return True


def password(pass_int):
    pw = get_pw_array(pass_int)
    try:
        assert len(pw) == 6, f"{pass_int} is not 6 digits"
        assert has_two_adjacent_same_digits(pw), f"{pass_int} no adjacent same"
        assert never_decreases(pw), f"{pass_int} decreases"
    except AssertionError:
        return False
    return True


def password_extra(pass_int):
    pw = get_pw_array(pass_int)
    try:
        assert len(pw) == 6, f"{pass_int} is not 6 digits"
        assert has_only_two_adjacent_same_digits(pass_int), \
            f"{pass_int} fail adjacent"
        assert never_decreases(pw), f"{pass_int} decreases"
    except AssertionError:
        return False
    return True


def part_one(options):
    passwords = [p for p in options if password(p)]
    return len(passwords)


def part_two(options):
    passwords = [p for p in options if password_extra(p)]
    return len(passwords)


if __name__ == '__main__':
    possible = range(206938, 679128)
    print(part_one(possible))
    print(part_two(possible))
