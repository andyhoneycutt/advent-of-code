import os

import functions

if __name__ == '__main__':
    filename = os.path.join(functions.get_path(__file__), 'input.txt')
    data = functions.read_file(filename)
    claims = functions.get_claims(data)
    _max = functions.max_of(claims, ['x', 'y'])
    fabric = functions.get_fabric(_max, [])
    for c in claims:
        xa, xb = c['l'], c['x']
        ya, yb = c['t'], c['y']
        for x in range(xa, xb):
            for y in range(ya, yb):
                fabric[x][y].append(c['i'])
    cids = [c['i'] for c in claims]
    for x in range(_max):
        for y in range(_max):
            if len(fabric[x][y]) > 1:
                for cid in fabric[x][y]:
                    try:
                        cids.remove(cid)
                    except:
                        pass
    print(cids)
