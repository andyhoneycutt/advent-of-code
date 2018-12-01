import os

import functions

if __name__ == '__main__':
    filename = os.path.join(functions.get_path(__file__), 'input.txt')
    data = functions.ftoi(filename)
    answers = set()
    c = 0
    answer = None
    while not answer:
        for i in data:
            c += i
            if c in answers:
                answer = c
                break
            else:
                answers.add(c)
    print(answer)
