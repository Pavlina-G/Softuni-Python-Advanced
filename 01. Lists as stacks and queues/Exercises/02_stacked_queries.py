n = int(input())
stack =[]

for i in range(n):
    command = input()

    if '1' in command:
        _, number = map(int, command.split(' '))
        stack.append(number)
    elif command == '2' and stack:
        stack.pop()
    elif command == '3' and stack:
        print(max(stack))
    elif command == '4' and stack:
        print(min(stack))

# print(', '.join(map(str,(stack[::-1]))))

while stack:
    element = stack.pop()
    if stack:
        print(element, end=', ')
    else:
        print(element)