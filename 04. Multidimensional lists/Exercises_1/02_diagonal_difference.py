size = int(input())
matrix = [[int(x) for x in input().split(' ')] for _ in range(size)]

primary_diagonal = []
secondary_diagonal = []

for row_index in range(size):
    primary_diagonal.append(matrix[row_index][row_index])
    secondary_diagonal.append(matrix[row_index][size - 1 - row_index])

difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(difference)
