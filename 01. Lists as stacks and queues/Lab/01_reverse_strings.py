# -- 1 --

text = list(input())

while text:
    print(text.pop(), end='')


# -- 2 --

text1 = list(input())
stack = []

for i in range(len(text1)):
    stack.append(text1.pop())

print(''.join(stack))
