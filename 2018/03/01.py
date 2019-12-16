import os

import functions

if __name__ == '__main__':
    filename = os.path.join(functions.get_path(__file__), 'input.txt')
    data = functions.read_file(filename)
    claims = functions.get_claims(data)
    _max = functions.max_of(claims, ['x', 'y'])
    fabric = functions.get_fabric(_max, 0)
    for c in claims:
        for x in range(c['l'], c['x']):
            for y in range(c['t'], c['y']):
                fabric[x][y] += 1
    sqin = 0
    for x in range(_max):
        for y in range(_max):
            if fabric[x][y] > 1:
                sqin += 1
    print(sqin)
