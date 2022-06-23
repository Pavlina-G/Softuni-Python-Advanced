def place_bombs(counter, matrix):
    for bomb in range(counter):
        bomb_row, bomb_col = eval(input())
        matrix[bomb_row][bomb_col] = "*"


def find_free_places(matrix):
    result = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] != '*':
                result.append((row, col))
    return result


def is_valid(row, col, matrix):
    return row in range(len(matrix)) and col in range(len(matrix))


def check_around(free_row, free_col, matrix, deltas):
    current_row, current_col = free_row, free_col
    num = 0

    for delta in deltas:
        row, col = delta[0], delta[1]
        next_row = current_row + row
        next_col = current_col + col

        if not is_valid(next_row, next_col, matrix):
            continue
        if matrix[next_row][next_col] == "*":
            num += 1
        else:
            continue
    return num


def place_numbers(matrix):
    free_places = find_free_places(matrix)
    for place in free_places:
        free_row, free_col = place
        matrix[free_row][free_col] = check_around(free_row, free_col, matrix, deltas)


size = int(input())
bombs_count = int(input())
matrix = [[None] * size for _ in range(size)]
place_bombs(bombs_count, matrix)
deltas = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
]
place_numbers(matrix)

for row in matrix:
    print(*row, sep=' ')
