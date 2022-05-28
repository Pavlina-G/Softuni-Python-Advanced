def is_valid(matrix, row, col):
    return row in range(len(matrix)) and 0 <= col < len(matrix)


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command = input()
    if command == 'END':
        # for row in matrix:
        [print(' '.join(str(x) for x in row)) for row in matrix]
        break

    data = command.split()

    action, row, col, value = data[0], int(data[1]), int(data[2]), int(data[3])

    if action == 'Add' and is_valid(matrix, row, col):
        matrix[row][col] += value
    elif action == 'Subtract' and is_valid(matrix, row, col):
        matrix[row][col] -= value
    else:
        print("Invalid coordinates")
