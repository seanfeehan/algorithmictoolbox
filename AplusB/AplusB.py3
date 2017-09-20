# Uses python3
# There are two ways of running this program:
# 1. Run
#     python3 APlusB.py
# then enter two numbers and press ctrl-d/ctrl-z
# 2. Save two numbers to a file -- say, dataset.txt.
# Then run
#     python3 APlusB.py < dataset.txt

import sys


class AplusB:
    def add_numbers(self, vala, valb):
        return vala + valb


def main():
    '''
    Adding main class
    :return:
    '''
    values = sys.stdin.read()
    tokens = values.split()
    a = int(tokens[0])
    b = int(tokens[1])

    print(AplusB().add_numbers(a, b))


if __name__ == '__main__':
    main()
