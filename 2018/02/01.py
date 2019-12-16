import os

import functions

if __name__ == '__main__':
    filename = os.path.join(functions.get_path(__file__), 'input.txt')
    twos = 0
    threes = 0
    data = functions.read_file(filename)
    for d in data:
        twos += functions.has_two(d)
        threes += functions.has_three(d)
    print(twos * threes)
