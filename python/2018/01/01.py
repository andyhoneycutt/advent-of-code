import os

import functions


if __name__ == '__main__':
    filename = os.path.join(functions.get_path(__file__), 'input.txt')
    data = functions.ftoi(filename)
    answer = sum(data)
    print(answer)
