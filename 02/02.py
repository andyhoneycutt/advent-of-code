import os

import functions

if __name__ == '__main__':
    filename = os.path.join(functions.get_path(__file__), 'input.txt')
    twos = 0
    threes = 0
    data = functions.read_file(filename)
    answer = functions.get_similar_string(data)
    print(answer)
