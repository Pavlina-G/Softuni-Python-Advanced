text = input()
parentheses_stack = []

for i in range(len(text)):
    if text[i] == '(':
        parentheses_stack.append(i)
    elif text[i] == ')':
        start_index = parentheses_stack.pop()
        print(text[start_index:i + 1])
