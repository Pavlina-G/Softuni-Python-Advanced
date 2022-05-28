def next_position(command, row, col):
    if command == 'U':
        return row - 1, col
    elif command == 'D':
        return row + 1, col
    elif command == 'L':
        return row, col - 1
    elif command == 'R':
        return row, col + 1


def is_outside(next_row, next_col, rows, cols):
    return next_row not in range(rows) or next_col not in range(cols)


def get_children(row, col, rows, cols):
    possible_children = [
        [row - 1, col],
        [row + 1, col],
        [row, col - 1],
        [row, col + 1]
    ]

    result = []
    for child_row, child_col in possible_children:
        if not is_outside(child_row, child_col, rows, cols):
            result.append([child_row, child_col])

    return result


rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]

player_row = 0
player_col = 0
bunnies = set()

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == 'P':
            player_row = row
            player_col = col
        elif matrix[row][col] == 'B':
            bunnies.add(f'{row} {col}')

commands = input()

won = False
dead = False

for command in commands:
    next_row, next_col = next_position(command, player_row, player_col)
    matrix[player_row][player_col] = '.'

    if is_outside(next_row, next_col, rows, cols):
        won = True
    elif matrix[next_row][next_col] == 'B':
        dead = True
        player_row, player_col = next_row, next_col
    else:
        matrix[next_row][next_col] = 'P'
        player_row, player_col = next_row, next_col

    new_bunnies = set()
    for bunny in bunnies:
        bunny_row, bunny_col = [int(x) for x in bunny.split()]

        children = get_children(bunny_row, bunny_col, rows, cols)
        for child_row, child_col in children:
            new_bunnies.add(f'{child_row} {child_col}')
            matrix[child_row][child_col] = 'B'

            if child_row == player_row and child_col == player_col:
                dead = True

    bunnies = bunnies.union(new_bunnies)

    if won or dead:
        break

[print(''.join(x)) for x in matrix]
if won:
    print(f'won: {player_row} {player_col}')
else:
    print(f'dead: {player_row} {player_col}')
