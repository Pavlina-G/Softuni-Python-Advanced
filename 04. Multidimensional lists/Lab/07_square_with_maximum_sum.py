rows, columns = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(', ')] for row in range(rows)]

max_sum = -99999999999
max_sum_matrix = []
for row_index in range(rows-1):
    for col_index in range(columns-1):
        sub_matrix = [matrix[row_index][col_index], matrix[row_index][col_index+1],
                      matrix[row_index+1][col_index], matrix[row_index+1][col_index+1]]

        current_sum = sum(sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_matrix = sub_matrix.copy()

for row in range(0, len(max_sum_matrix)-1, 2):
    print(max_sum_matrix[row], max_sum_matrix[row+1])

print(max_sum)


