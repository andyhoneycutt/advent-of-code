import os

import functions

if __name__ == '__main__':
    filename = os.path.join(functions.get_path(__file__), 'input.txt')
    with open(filename, 'r') as f:
        data = f.read()
        output = functions.remove_repelled(data)
        print(len(output))