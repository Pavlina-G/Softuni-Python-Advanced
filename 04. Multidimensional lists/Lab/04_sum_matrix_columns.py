rows, columns = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(' ')] for row in range(rows)]

column_sum = 0
# result = []

for col_index in range(columns):
    column_sum = 0
    for row_index in range(rows):
        column_sum += matrix[row_index][col_index]
    print(column_sum)
    # result.append(column_sum)

# [print(x) for x in result]
