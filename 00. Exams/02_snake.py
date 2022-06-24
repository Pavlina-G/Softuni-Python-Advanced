def create_matrix(size):
    return [[x for x in list(input())] for _ in range(size)]


def not_valid(row, col, matrix):
    return row not in range(len(matrix)) or col not in range(len(matrix))


def find_position(matrix, symbol):
    result = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == symbol:
                result.append((row, col))
    return result


def move_to_burrow(lair, row, col):
    if (row, col) == lair[0]:
        (row, col) = lair[1]
    else:
        (row, col) = lair[0]
    return (row, col)


def print_end_game(winner, food, matrix):
    if not winner:
        print("Game over!")
    else:
        print("You won! You fed the snake.")
    print(f"Food eaten: {food}")
    for row in matrix:
        print(*row, sep='')


def play_snake(matrix):
    snake_position = find_position(matrix, 'S')
    snake_row, snake_col = snake_position[0]
    matrix[snake_row][snake_col] = '.'
    lair = find_position(matrix, 'B')
    food = 0

    directions = {
        "up": lambda r, c: (r - 1, c),
        "down": lambda r, c: (r + 1, c),
        "left": lambda r, c: (r, c - 1),
        "right": lambda r, c: (r, c + 1)
    }
    winner = False

    while True:
        command = input()
        next_row, next_col = directions[command](snake_row, snake_col)

        if not_valid(next_row, next_col, matrix):
            winner = False
            break
        if matrix[next_row][next_col] == "*":
            food += 1
            if food >= 10:
                matrix[next_row][next_col] = 'S'
                winner = True
                break
        elif matrix[next_row][next_col] == 'B':
            matrix[next_row][next_col] = '.'
            next_row, next_col = move_to_burrow(lair, next_row, next_col)
        snake_row, snake_col = next_row, next_col
        matrix[next_row][next_col] = '.'

        if matrix[next_row][next_col] == '-':
            matrix[next_row][next_col] = '.'
            continue

    print_end_game(winner, food, matrix)


size = int(input())
matrix = create_matrix(size)
play_snake(matrix)
