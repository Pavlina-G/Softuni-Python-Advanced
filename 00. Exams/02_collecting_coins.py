from math import floor

def find_player(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'P':
                return row, col


def start_from_opposite_side(size, row, col, direction):
    directions = {
        'up': lambda r, c: (size - 1, c),
        'down': lambda r, c: (0, c),
        'left': lambda r, c: (r, size - 1),
        'right': lambda r, c: (r, 0)
    }
    return directions[direction](row, col)


def is_valid(row, col, size):
    return row in range(size) and col in range(size)


def play_game(matrix):
    current_row, current_col = find_player(matrix)
    matrix[current_row][current_col] = 0
    path = []
    path.append([current_row, current_col])
    total_coins = 0

    directions = {
        'up': lambda r, c: (r - 1, c),
        'down': lambda r, c: (r + 1, c),
        'left': lambda r, c: (r, c - 1),
        'right': lambda r, c: (r, c + 1)
    }

    while True:
        direction = input()
        if direction not in directions:
            continue
        next_row, next_col = directions[direction](current_row, current_col)
        if not is_valid(next_row, next_col, size):
            next_row, next_col = start_from_opposite_side(size, next_row, next_col, direction)

        current_row, current_col = next_row, next_col
        path.append([current_row, current_col])

        if isinstance(matrix[current_row][current_col], int) and path.count([current_row, current_col]) <= 1:
            total_coins += matrix[current_row][current_col]
            if total_coins >= 100:
                print(f"You won! You've collected {total_coins} coins.")
                break
        elif matrix[current_row][current_col] == 'X':
            total_coins = floor(total_coins * 0.50)
            print(f"Game over! You've collected {total_coins} coins.")
            break

    print("Your path:")
    [print(f"{pair}") for pair in path]


size = int(input())
field = [[int(x) if x.isdigit() else x for x in input().split(' ')] for _ in range(size)]
play_game(field)
