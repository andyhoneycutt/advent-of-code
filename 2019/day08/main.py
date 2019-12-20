import util

IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6


def get_layer(width, height, initial=None):
    return [list(initial for _ in range(width)) for _ in range(height)]


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


def get_layer_count_entry(layer, entry):
    return sum([h.count(entry) for h in layer])


def get_layer_fewest_entry(layers, entry=0):
    counts = []
    for layer in layers:
        counts.append(get_layer_count_entry(layer, entry))
    min_count = min(counts)
    for i, c in enumerate(counts):
        if c == min_count:
            return i


def multiply_entries(layer, a, b):
    return get_layer_count_entry(layer, a) * get_layer_count_entry(layer, b)


@util.time_fn
def part_one(layers):
    index = get_layer_fewest_entry(layers, 0)
    result = multiply_entries(layers[index], 1, 2)
    print(result)
    return result


def merge_image(layer, i_layers, w, h):
    try:
        next_layer = next(i_layers)
    except StopIteration:
        return layer
    for r, l_w in enumerate(layer):
        for p, l_h in enumerate(l_w):
            if layer[r][p] == '2':
                layer[r][p] = next_layer[r][p]
    return merge_image(layer, i_layers, w, h)


def print_image(output):
    for r in output:
        for p in r:
            o = p == '1' and '[]' or '  '
            print(o, end='')
        print('\n', end='')


@util.time_fn
def part_two(layers):
    layer = get_layer(IMAGE_WIDTH, IMAGE_HEIGHT, initial='2')
    i_layers = iter(layers)
    output = merge_image(layer, i_layers, IMAGE_WIDTH, IMAGE_HEIGHT)
    print_image(output)
    return output


if __name__ == '__main__':
    image = load_image(
        [int(i) for i in util.read_input('input.txt')],
        IMAGE_WIDTH,
        IMAGE_HEIGHT,
    )
    part_one(image)

    # TODO: Determine why this doesn't work with integers
    image_two = load_image(
        util.read_input('input.txt'),
        IMAGE_WIDTH,
        IMAGE_HEIGHT,
    )
    part_two(image_two)
