from main import part_one, part_two


def test_part_one():
    input_parts_one = [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3",
    ]
    assert part_one(input_parts_one) == 11


def test_part_two():
    inputs = [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3",
    ]
    assert part_two(inputs) == 31
