def find_player(field):
    for row_index, row in enumerate(field):
        if 'P' in row:
            return row_index, row.index('P')


def is_valid_position(row, col, matrix):
    return row in range(len(matrix)) and col in range(len(matrix))


def play_game(field, player_row, player_col, text):
    current_row, current_col = player_row, player_col
    field[current_row][current_col] = '-'
    directions = {
        "up": lambda r, c: (r - 1, c),
        "down": lambda r, c: (r + 1, c),
        "left": lambda r, c: (r, c - 1),
        "right": lambda r, c: (r, c + 1),
    }
    commands = int(input())
    for _ in range(commands):
        command = input()
        next_row, next_col = directions[command](current_row, current_col)
        if not is_valid_position(next_row, next_col, field):
            text = text[:-1]
            continue
        if field[next_row][next_col] == '-':
            current_row, current_col = next_row, next_col
            continue
        elif isinstance(field[next_row][next_col], str):
            text = text + field[next_row][next_col]
            field[next_row][next_col] = '-'
            current_row, current_col = next_row, next_col

    field[current_row][current_col] = 'P'
    print(text)

    for row in field:
        print(*row, sep='')


text = input()
size = int(input())
field = [[x for x in list(input())] for row in range(size)]
player_row, player_col = find_player(field)
play_game(field, player_row, player_col, text)
