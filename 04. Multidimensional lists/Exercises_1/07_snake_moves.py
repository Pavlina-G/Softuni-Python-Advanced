rows, columns = [int(x) for x in input().split(' ')]
text = input()

idx = 0

for row in range(rows):
    elements = [None] * columns
    start, end, step = (0, columns, 1) if row % 2 == 0 else (columns - 1, -1, -1)
    for col in range(start, end, step):
        elements[col] = text[idx % len(text)]
        idx += 1
    print(''.join(elements))
