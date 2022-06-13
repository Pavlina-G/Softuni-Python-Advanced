import numpy as np


def create_field(rows, cols):
    return [[None] * cols for row in range(rows)]


def get_cell_value(cell):
    return cell if cell else 0


def print_field(field):
    [print([get_cell_value(x) for x in row]) for row in field]


def print_winner(player):
    print(f'Player {player} wins!')


def get_player_move(player, cols, all_rows_moves):
    while True:

        start_move_str = input(f'Player {player}, please choose a column\n')
        player_move = int(start_move_str) - 1
        if player_move in range(cols) and all_rows_moves[player_move] != 0:
            all_rows_moves[player_move] -= 1
            return all_rows_moves[player_move], player_move
        else:
            print(f'The column is not valid. Try again in range 1-{cols}')
            continue


def is_win_condition(row, col, player):
    for i in range(0 if row <= 3 else row - 3, 3 if row >= 2 else row + 1):
        for j in range(0 if col <= 3 else col - 3, 4 if col >= 3 else col + 1):
            current_field = [[(get_cell_value(field[r][c])) for c in range(j, j + 4)] for r in range(i, i + 4)]

            for current_row in range(4):

                current_col = np.matrix(current_field).transpose()[current_row].getA()[0]

                if len(set(current_col)) == 1 and player in current_col or \
                        len(set(current_field[current_row])) == 1 and player in current_field[current_row]:
                    if sum(current_field[current_row]) == player * 4 or sum(current_col) == player * 4:
                        return True
            if len(set(np.diag(current_field))) == 1 and player in np.diag(current_field) or \
                    len(set(np.diag(current_field[::-1]))) == 1 and player in (np.diag(current_field[::-1])):
                if sum(np.diag(current_field)) == player * 4 or sum(np.diag(current_field[::-1])) == player * 4:
                    return True


def play(field):
    current_player, other_player = 1, 2

    rows_count = len(field)
    cols_count = len(field[0])
    all_possible_moves = [rows_count] * cols_count

    while True:
        player_row, player_move = get_player_move(current_player, cols_count, all_possible_moves)
        field[player_row][player_move] = current_player
        print_field(field)
        if is_win_condition(player_row, player_move, current_player):
            print_winner(current_player)
            break
        if sum(all_possible_moves) == 0:
            print('No more moves. The game is over!')
            break

        current_player, other_player = other_player, current_player


field = create_field(6, 7)
play(field)
