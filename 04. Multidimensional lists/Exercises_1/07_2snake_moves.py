from collections import deque

rows, columns = [int(x) for x in input().split(' ')]
text = deque(input())

for row in range(rows):
    matrix = [] * columns
    for col in range(columns):
        current_char = text.popleft()
        if row % 2 == 0:
            matrix.append(current_char)
            text.append(current_char)
        else:
            matrix.append(current_char)
            text.append(current_char)
    if row % 2 == 0:
        print(''.join(matrix))
    else:
        print(''.join(reversed(matrix)))
