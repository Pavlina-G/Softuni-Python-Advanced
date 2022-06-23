def find_queens(board):
    queens = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 'Q':
                queens.append((row, col))
    return queens


def is_valid(row, col, matrix):
    return row in range(len(matrix)) and col in range(len(matrix))


def get_next_position(row, col, board, directions, direction):
    check_row, check_col = row, col
    while True:

        next_row, next_col = directions[direction](check_row, check_col)

        if not is_valid(next_row, next_col, board):
            return
        else:
            if board[next_row][next_col] == 'Q':
                return
            elif board[next_row][next_col] == '.':
                check_row, check_col = next_row, next_col
                continue
            elif board[next_row][next_col] == 'K':
                return True


size = 8
board = [[x for x in input().split(' ')] for _ in range(size)]
queens_capture_positions = []
queens_positions = find_queens(board)
directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up_left': lambda r, c: (r - 1, c - 1),
    'up_right': lambda r, c: (r - 1, c + 1),
    'down_left': lambda r, c: (r + 1, c - 1),
    'down_right': lambda r, c: (r + 1, c + 1),
}

for queen in queens_positions:

    current_row, current_col = queen
    for direction in directions:
        condition = get_next_position(current_row, current_col, board, directions, direction)
        if condition is not None:
            queens_capture_positions.append([current_row, current_col])
            break

if queens_capture_positions:
    for position in queens_capture_positions:
        print(position)
else:
    print('The king is safe!')
