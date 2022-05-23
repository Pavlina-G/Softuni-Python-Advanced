from collections import deque
from math import floor


def operations(element, nums):
    while len(nums) > 1:
        first = nums.popleft()
        second = nums.popleft()
        result = 0

        if element == '+':
            result = first + second
        elif element == '-':
            result = first - second
        elif element == '*':
            result = first * second
        else:
            result = int(float(first / second))

        nums.appendleft(result)

    return nums


def expression_evaluator():
    elements = input().split(' ')
    numbers = deque()

    for el in elements:
        if el in '+-*/':
            operations(el, numbers)
        else:
            numbers.append(int(el))

    print(numbers.popleft())

expression_evaluator()
