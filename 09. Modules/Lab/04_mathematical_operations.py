from math_operations import operation

info = input().split(' ')

num1 = float(info[0])
sign = info[1]
num2 = int(info[2])
print(f'{operation(sign, num1, num2):.2f}')
