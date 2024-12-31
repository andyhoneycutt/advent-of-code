from main import part_one, part_two


def test_part_one():
    input_parts_one = [
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))",
    ]
    assert part_one(input_parts_one) == 161


def test_part_two():
    inputs = [
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    ]
    assert part_two(inputs) == 48
