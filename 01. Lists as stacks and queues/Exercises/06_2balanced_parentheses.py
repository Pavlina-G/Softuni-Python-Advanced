parentheses = input()
stack = []
balanced = True

for char in parentheses:
    if char in '({[':
        stack.append(char)
    elif not stack:
        balanced = False
        break
    else:
        current_char = stack.pop()
        if current_char == '(':
            if char != ")":
                balanced = False
                break
        if current_char == '{':
            if char != "}":
                balanced = False
                break
        if current_char == '[':
            if char != "]":
                balanced = False
                break

if not balanced:
    print('NO')
else:
    print('YES')

