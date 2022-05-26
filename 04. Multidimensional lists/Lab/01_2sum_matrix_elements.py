rows, columns = [int(x) for x in input().split(', ')]
matrix = []
total_sum = 0

for row_index in range(rows):
    matrix.append([int(x) for x in input().split(', ')])
    for col_index in range(columns):
        total_sum += matrix[row_index][col_index]

print(total_sum)
print(matrix)