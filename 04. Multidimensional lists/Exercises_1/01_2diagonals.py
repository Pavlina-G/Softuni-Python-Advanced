size = int(input())

primary_diagonal = []
secondary_diagonal = []

for row_index in range(size):
    matrix_row = [int(x) for x in input().split(', ')]
    primary_diagonal.append(matrix_row[row_index])
    secondary_diagonal.append(matrix_row[size - 1 - row_index])

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")
