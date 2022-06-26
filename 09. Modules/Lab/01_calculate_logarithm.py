from math import log, e as euler_num


def logarithm(n, base):
    result = 0
    if base == 'natural':
        result = log(n, euler_num)
        # result = log(n)
    else:
        result = log(n, int(base))
    return f'{result:.2f}'


num = int(input())
base = input()
print(logarithm(num, base))
