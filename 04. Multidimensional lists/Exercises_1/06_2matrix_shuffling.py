def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, columns = [int(x) for x in input().split(' ')]
matrix = []

for _ in range(rows):
    matrix.append(input().split())

while True:
    line = input()
    if line == 'END':
        break

    command_elements = line.split()

    if len(command_elements) != 5 or command_elements[0] != 'swap':
        print('Invalid input!')
        continue

    row1, col1, row2, col2 = [int(x) for x in command_elements[1:]]

    if is_outside(row1, col1, rows, columns) or is_outside(row2, col2, rows, columns):
        print('Invalid input!')
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        print(*row, sep=' ')
