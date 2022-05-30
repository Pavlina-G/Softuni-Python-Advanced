def is_valid(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


n = int(input())
matrix = []

for _ in range(n):
    matrix.append(input().split())

bunny_row = 0
bunny_col = 0

for row in range(n):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 'B':
            bunny_row, bunny_col = row, col

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
}

max_eggs = float('-inf')  # or max-eggs = -9999999999999999
best_direction = ''
best_path = []

for direction in directions:
    row, col = directions[direction](bunny_row, bunny_col)
    current_eggs = 0
    current_path = []

    while is_valid(row, col, matrix) and matrix[row][col] != 'X':
        current_eggs += int(matrix[row][col])
        current_path.append([row, col])
        row, col = directions[direction](row, col)

    if current_eggs > max_eggs and current_path:
        max_eggs = current_eggs
        best_direction = direction
        best_path = current_path

print(best_direction)
print(*best_path, sep='\n')
print(max_eggs)
