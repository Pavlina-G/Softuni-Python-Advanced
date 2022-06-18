from string import ascii_lowercase, digits


def create_square(size):
    matrix = []
    for row in range(size):
        matrix.append(input().split(' '))
    return matrix


def draw_a_chessboard(size):
    chessboard = []

    columns = ascii_lowercase[:8]
    rows = digits[1:9]
    for row in rows[::-1]:
        col_rows = []
        for col in columns:
            col_rows.append(f'{col}{row}')
        chessboard.append(col_rows)
    return chessboard


def get_pawns_positions(square):
    for row in range(len(square)):
        for col in range(len(square)):
            if square[row][col] == 'w':
                w_pawn_row = row
                w_pawn_col = col
            elif square[row][col] == 'b':
                b_pawn_row = row
                b_pawn_col = col
    return w_pawn_row, w_pawn_col, b_pawn_row, b_pawn_col


def get_next_position(player, row, col, square):
    if player == 'w':
        return row - 1, col
    elif player == 'b':
        return row + 1, col


def captured(player, row, col, square):

    if player == 'w' and square[row-1][col-1] == 'b' and col-1 in range(8):
        return True
    elif player == 'w' and col+1 in range(8) and square[row-1][col+1] == 'b':
        return True
    elif player == 'b' and square[row+1][col-1] == 'w' and col-1 in range(8):
        return True
    elif player == 'b' and col+1 in range(8) and square[row+1][col+1] == 'w':
        return True
    return False


def get_capture_position(player, row, col, square):
    if player == 'w':
        if square[row-1][col-1] == 'b':
            return row-1,col-1
        elif square[row-1][col+1] == 'b':
            return row-1,col+1
    elif player == 'b':
        if square[row+1][col-1] == 'w':
            return row+1, col-1
        elif square[row+1][col+1] == 'w':
            return row+1,col+1


def play_game(player_w, player_b, square):
    current_player, other_player = player_w, player_b
    white_pawn_row, white_pawn_col, black_pawn_row, black_pawn_col = get_pawns_positions(square)
    current_row, current_col, other_row, other_col = white_pawn_row, white_pawn_col, black_pawn_row, black_pawn_col

    while True:

        if captured(current_player, current_row, current_col, square):
            win_row, win_col = get_capture_position(current_player, current_row, current_col, square)
            print(f"Game over! {'White' if current_player == 'w' else 'Black'} win, capture on {draw_a_chessboard(size)[win_row][win_col]}.")
            break

        next_row, next_col = get_next_position(current_player, current_row, current_col, square)
        square[next_row][next_col] = current_player
        square[current_row][current_col] = '-'

        if current_player == 'w' and next_row == 0 or current_player == 'b' and next_row == 7:
            print(f"Game over! {'White' if current_player == 'w' else 'Black'} pawn is promoted to a queen at {draw_a_chessboard(size)[next_row][next_col]}.")
            break

        current_row, current_col = next_row, next_col
        current_player, other_player = other_player, current_player
        current_row, current_col, other_row, other_col = other_row, other_col, current_row, current_col


size = 8
square = create_square(size)
player_w = 'w'
player_b = 'b'
play_game(player_w, player_b, square)
