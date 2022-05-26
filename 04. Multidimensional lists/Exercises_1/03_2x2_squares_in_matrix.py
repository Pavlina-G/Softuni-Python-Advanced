rows, columns = [int(x) for x in input().split(' ')]
matrix = [input().split(' ') for _ in range(rows)]
counter = 0

# for _ in range(rows):
#     matrix.append(input().split(' '))

for row in range(rows-1):
    for col in range(columns-1):
        sub_matrix = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row+1][col+1]]
        if len(set(sub_matrix)) == 1:
            counter += 1

print(counter)
