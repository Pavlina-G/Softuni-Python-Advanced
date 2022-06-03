def operate(operator, *args):

    def sum_num(*args):
        return sum(args)

    def substract(x, *args):
        return x - sum(y for y in args)

    def multiply(*args):
        if 0 in args:
            return 0
        else:
            result = 1
            for num in args:
                result *= num
            return result

    def divide(x, *args):
        if x == 0:
            return 0
        else:
            result = x
            for num in args:
                result /= num
            return result


    if operator == '+':
        return sum_num(*args)
    elif operator == '-':
        return substract(*args)
    elif operator == '*':
        return multiply(*args)
    elif operator == '/':
        return divide(*args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 8, 2, 2))
print(operate("-", 5, 1, 1))