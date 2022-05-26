import sys
from io import StringIO

test_input1 = '''3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
'''

test_input2 = '''3, 3
1 2 3
4 5 6
7 8 9
'''

sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def get_column_sums(matrix):
    column_sums = [0] * columns

    for row_index in range(rows):
        for col_index in range(columns):
            column_sums[col_index] += matrix[row_index][col_index]

    return column_sums


rows, columns = [int(x) for x in input().split(', ')]

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(' ')])


[print(x) for x in get_column_sums(matrix)]