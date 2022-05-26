rows, columns = [int(x) for x in input().split(' ')]
matrix = [[int(x) for x in input().split(' ')] for _ in range(rows)]

max_sum = -999999999999

for row in range(rows-2):
    for col in range(columns-2):
        sub_matrix = [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2], matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2], matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        current_sum = sum(sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sub_matrix = sub_matrix.copy()

print(f"Sum = {max_sum}")
[print(max_sub_matrix[row], max_sub_matrix[row+1], max_sub_matrix[row+2]) for row in range(0, len(max_sub_matrix)-2, 3)]