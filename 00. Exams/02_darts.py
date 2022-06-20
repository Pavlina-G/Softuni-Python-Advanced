def is_valid(row, col, matrix):
    return row in range(len(matrix)) and col in range(len(matrix[0]))


def print_winner(player, turns):
    print(f"{player} won the game with {turns} throws!")


def sum_outside_numbers(throw_row, throw_col, size):
    return dartboard[0][throw_col] + dartboard[size - 1][throw_col] + dartboard[throw_row][0] + dartboard[throw_row][
        size - 1]


def play_game(first_player, second_player, dartboard):
    current_player, other_player = first_player, second_player
    current_score = 501
    other_score = 501
    current_turns = 0
    other_turns = 0

    while True:
        throw_row, throw_col = eval(input())
        current_turns += 1

        if is_valid(throw_row, throw_col, dartboard):
            current_hit = dartboard[throw_row][throw_col]
            if current_hit == 'B':
                print_winner(current_player, current_turns)
                break
            elif isinstance(current_hit, int):
                current_score -= current_hit
            elif current_hit == 'D':
                current_score -= sum_outside_numbers(throw_row, throw_col, size) * 2
            elif current_hit == 'T':
                current_score -= sum_outside_numbers(throw_row, throw_col, size) * 3

            if current_score <= 0:
                print_winner(current_player, current_turns)
                break

        current_player, other_player = other_player, current_player
        current_score, other_score = other_score, current_score
        current_turns, other_turns = other_turns, current_turns


size = 7
first_player, second_player = input().split(', ')
dartboard = [[int(x) if x.isdigit() else x for x in input().split(' ')] for row in range(size)]
play_game(first_player, second_player, dartboard)
