parentheses = input()

balanced = True
opening_brackets = []

for ch in parentheses:
    if ch in '({[':
        opening_brackets.append(ch)
    elif not opening_brackets:
        balanced = False
        break
    else:
        last_opening_bracket = opening_brackets.pop()
        if f'{last_opening_bracket}{ch}' not in '(){}[]':
            balanced = False
            break

if balanced:
    print('YES')
else:
    print('NO')