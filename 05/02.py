import os
import string

import functions

if __name__ == '__main__':
    filename = os.path.join(functions.get_path(__file__), 'input.txt')
    polymers = []
    with open(filename, 'r') as f:
        data = f.read()
        for c in string.ascii_lowercase:
            d = c.upper()
            polymer = functions.remove_repelled(data.replace(c, '').replace(d, ''))
            polymers.append(len(polymer))
    print(min(polymers))
