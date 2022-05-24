from collections import deque

text = deque(input().split())

main_colors = {'red', 'yellow', 'blue'}
secondary_colors = {'orange', 'purple', 'green'}

formed_colors = []

while text:
    first = text.popleft()
    last = text.pop() if text else ''

    current_color = first + last

    if current_color in main_colors or current_color in secondary_colors:
        formed_colors.append(current_color)
        continue

    current_color = last + first

    if current_color in main_colors or current_color in secondary_colors:
        formed_colors.append(current_color)
        continue

    first_substr = first[:-1]
    second_substr = last[:-1]

    if first_substr:
        text.insert(len(text) // 2, first_substr)
    if second_substr:
        text.insert(len(text) // 2, second_substr)

result = []

secondary_colors_dict = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

for color in formed_colors:
    if color in main_colors:
        result.append(color)
        continue

    formed = True

    for forming_color in secondary_colors_dict[color]:
        if forming_color not in formed_colors:
            formed = False
            break
    if formed:
        result.append(color)

print(result)
