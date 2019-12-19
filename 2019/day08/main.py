import util

IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6


def get_layer(width, height):
    return [list(None for _ in range(width)) for _ in range(height)]


def load_image(pixels, width, height):
    p = iter(pixels)
    pixel = next(p)
    layers = []
    while pixel:
        layer = get_layer(width, height)
        for h in range(height):
            for w in range(width):
                layer[h][w] = pixel
                try:
                    pixel = next(p)
                except StopIteration:
                    pixel = None
        layers.append(layer)
    return layers


def get_layer_fewest_entry(layers, entry=0):
    counts = []
    for layer in layers:
        counts.append(sum([h.count(entry) for h in layer]))
    min_count = min(counts)
    for i, c in enumerate(counts):
        if c == min_count:
            return i


def part_one():
    pass


def part_two():
    pass


if __name__ == '__main__':
    image = load_image(
        [int(i) for i in util.read_input('input.txt')],
        IMAGE_WIDTH,
        IMAGE_HEIGHT,
    )
    part_one()
    part_two()
