def find_count(row, col, board):
    possible_moves = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1],
    ]
    result = 0
    for move_row, move_col in possible_moves:
        if move_row in range(len(board)) and move_col in range(len(board)) and board[move_row][move_col] == 'K':
            result += 1
    return result


n = int(input())
board = []

for row in range(n):
    board.append(list(input()))

removed_knights = 0

while True:
    knight_row = 0
    knight_col = 0
    max_count = 0

    for row in range(n):
        for col in range(n):
            if board[row][col] == '0':
                continue

            count = find_count(row, col, board)
            if count > max_count:
                max_count = count
                knight_row = row
                knight_col = col

    if max_count == 0:
        break
    board[knight_row][knight_col] = '0'
    removed_knights += 1

print(removed_knights)
