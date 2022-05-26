# ----------- 1 solution -----------:

# rows = int(input())
# flattened_matrix = []

# for row in range(rows):
#     flattened_matrix.extend([int(x) for x in input().split(', ')])


# ----------- 2 solution -----------:

rows = int(input())
matrix = [] # [[1, 2, 3], [4, 5, 6]]
# matrix = [map(int, input().split(', ')) for _ in range(rows)]
for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

flattened_matrix = [num for sublist in matrix for num in sublist] # [1, 2, 3, 4, 5, 6]
print(flattened_matrix)


# comprehension / for loop
# flattened_matrix = [ #(3)num #(1)for sublist in matrix #(2)for num in sublist ]

#(1) for sublist in matrix:
#(2)    for num in sublist:
#(3)        flattened_matrix.append(num)
# print(flattened_matrix)


# ----------- 3 solution -----------:

# rows = int(input())
# matrix = []
# for row in range(rows):
#     matrix.append([int(x) for x in input().split(', ')])
#
# flattened_matrix = []
# for row_index in range(rows):
#     for col_index in range(len(matrix[row])):
#         flattened_matrix.append(matrix[row_index][col_index])
# print(flattened_matrix)