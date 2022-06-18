from string import ascii_lowercase, digits


def create_square(size):
    matrix = [input().split(' ') for _ in range(size)]
    return matrix


def get_chessboard_position(row, col):
    column_names = ascii_lowercase[:8]
    row_names = digits[1:9]
    row_names = row_names[::-1]

    return column_names[col], row_names[row]


def find_player(player, square):
    for row_index, row in enumerate(square):
        if player in row:
            return (row_index, row.index(player))

    return None, None


def play_game(current_player, other_player, square):
    current_player_position = find_player(current_player, square)
    other_player_position = find_player(other_player, square)
    current_delta = -1
    other_delta = +1

    while True:
        (current_player_row, current_player_column) = current_player_position
        (other_player_row, other_player_column) = other_player_position

        current_player_row += current_delta
        current_player_position = (current_player_row, current_player_column)

        if current_player_row == other_player_row and abs(current_player_column - other_player_column) == 1:

            current_player_column = other_player_column
            print(
                f"Game over! {'White' if current_player == 'w' else 'Black'} win, capture on {''.join(get_chessboard_position(current_player_row, current_player_column))}.")
            break

        elif current_player_row in (0, size - 1):
            print(
                f"Game over! {'White' if current_player == 'w' else 'Black'} pawn is promoted to a queen at {''.join(get_chessboard_position(current_player_row, current_player_column))}.")
            break

        else:
            current_player, other_player = other_player, current_player
            current_player_position, other_player_position = other_player_position, current_player_position
            current_delta, other_delta = other_delta, current_delta


size = 8
square = create_square(size)
current_player = 'w'
other_player = 'b'
play_game(current_player, other_player, square)
