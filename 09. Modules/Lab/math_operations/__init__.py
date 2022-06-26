from collections import deque

def operation(sign, *args):
    if sign == '/':
        numbers = deque(args)
        first_num = numbers.popleft()
        for num in numbers:
            if num != 0:
                first_num /= num
            else:
                return 'None'
        return first_num

    elif sign == '*':
        result = 1
        for num in args:
            result *= num
        return result

    elif sign == '-':
        numbers = deque(args)
        start_num = numbers.popleft()
        for num in numbers:
            start_num -= num
        return start_num

    elif sign == '+':
        return sum(args)

    elif sign == '^':
        numbers = deque(args)
        start_num = numbers.popleft()
        for num in numbers:
            start_num **= num
        return start_num
