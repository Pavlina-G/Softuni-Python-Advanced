size = int(input())
matrix = [[int(x) for x in input().split(' ')] for _ in range(size)]

# primary_diagonal = []

# for row in range(size):
#     primary_diagonal.append(matrix[row][row])
# print(sum(primary_diagonal))

primary_diagonal = sum(matrix[row][row] for row in range(size))
print(primary_diagonal)
