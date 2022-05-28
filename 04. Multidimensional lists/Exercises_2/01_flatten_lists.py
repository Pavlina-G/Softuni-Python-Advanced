list_nums = input().split('|')
list_nums.reverse()
matrix = []

for row in list_nums:
    matrix.append(row.split())

[print(num, end=' ') for sublist in matrix for num in sublist]

# for sublist in matrix:
#     for num in sublist:
#         print(num, end=' ')
