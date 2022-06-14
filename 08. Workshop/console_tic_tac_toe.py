import numpy as np

def players_signs(player_one):
    player1_sign = input(f"{player_one} would you like to play with 'X' or 'O'? ").upper()
    player2_sign = 'X' if player1_sign != 'X' else 'O'

    while not sign_is_valid(player1_sign):
        player1_sign = input(f"{player_one} would you like to play with 'X' or 'O'? ").upper()

    return player1_sign, player2_sign


def sign_is_valid(sign):
    return sign in ['X', 'O']


def create_board(size):
    board = []
    for r in range(size):
        board.append(['None'] * size)
    return board


def print_board_numbers(board):
    print('This is the numeration of the board')
    for i in range(1, 10, 3):
        print(f"|  {i}  |  {i + 1}  |  {i + 2}  |")

def possible_moves(board):
    positions_mapping = {}
    i = 1
    for r in range(len(board)):
        for c in range(len(board)):
            positions_mapping[i] = (r, c)
            i += 1

    return positions_mapping


def get_cell_value(cell):
    return cell if cell != 'None' else ' '


def draw_board(board):
    for r in board:
        print("|  ", end='')
        print('  |  '.join([str(get_cell_value(x)) for x in r]), end='')
        print('  |')


def is_winner(board, sign):
    for r in board:
        if len(set(r)) == 1 and sign in r:
            return True
    col_board = np.array(board)
    for c in col_board.transpose():
        if len(set(c)) == 1 and sign in c:
            return True
    if len(set(np.diag(board))) == 1 and sign in np.diag(board) or len(set(np.diag(board[::-1]))) == 1 and sign in np.diag(board[::-1]):
        return True
    return False


def play_game(player1, player2, player1_sign, player2_sign, board):
    current_player, other_player = player1, player2
    current_sign, other_sign = player1_sign,player2_sign
    all_moves = possible_moves(board)

    while True:
        if len(all_moves) == 0:
            print('Game over!')
            break
        choice = int(input(f"{current_player} choose a free position [1-9]:\n"))

        if choice in all_moves:
            current_row, current_col = all_moves[choice]
            del all_moves[choice]
            board[current_row][current_col] = current_sign
            draw_board(board)

            if is_winner(board, current_sign):
                print(f'{current_player} won!')
                break
        else:
            print(f'Position {choice} is not available.')
            continue

        current_player, other_player = other_player, current_player
        current_sign, other_sign =  other_sign,current_sign


player_one_name = input('Player one name: ')
player_two_name = input('Player two name: ')
player_one_sign, player_two_sign = players_signs(player_one_name)
board_size = 3
board = create_board(board_size)
print_board_numbers(board)
play_game(player_one_name, player_two_name, player_one_sign, player_two_sign, board)
