def create_matrix(rows):
    matrix = [input().split(" ") for _ in range(rows)]
    return matrix


def get_Y_position(matrix):
    for row_index, row in enumerate(matrix):
        if 'Y' in row:
            return row_index, row.index('Y')
    return None, None


def count_all_items(workshop):
    decoration = 0
    gifts = 0
    cookies = 0
    for row in workshop:
        decoration += row.count('D')
        gifts += row.count('G')
        cookies += row.count('C')
    return decoration, gifts, cookies


def is_valid(row, col, matrix):
    return row in range(len(matrix)) and col in range(len(matrix[0]))


rows, columns = [int(x) for x in input().split(', ')]
workshop = create_matrix(rows)
y_position = get_Y_position(workshop)
collected_decoration = 0
collected_gifts = 0
collected_cookies = 0
all_items = sum(count_all_items(workshop))

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

start_from_the_oposite_side = {
    'up': lambda r, c: (rows - 1, c),
    'down': lambda r, c: (0, c),
    'left': lambda r, c: (r, columns - 1),
    'right': lambda r, c: (r, 0)
}
all_collected = False

while True:
    command = input()

    if command == 'End':
        break

    direction, steps = command.split('-')
    steps = int(steps)
    current_row, current_col = get_Y_position(workshop)

    for i in range(steps):


        next_row, next_col = directions[direction](current_row, current_col)
        if not is_valid(next_row, next_col, workshop):
            next_row, next_col = start_from_the_oposite_side[direction](current_row, current_col)

        workshop[current_row][current_col] = 'x'
        current_row, current_col = next_row, next_col
        if workshop[next_row][next_col] == 'D':
            collected_decoration += 1
            all_items -= 1
        elif workshop[next_row][next_col] == 'G':
            collected_gifts += 1
            all_items -= 1
        elif workshop[next_row][next_col] == 'C':
            collected_cookies += 1
            all_items -= 1
        workshop[current_row][current_col] = 'Y'
        if all_items == 0:
            all_collected = True
            break

    if all_collected:
        print('Merry Christmas!')
        break

print(f"You've collected:")
print(f'- {collected_decoration} Christmas decorations')
print(f'- {collected_gifts} Gifts')
print(f'- {collected_cookies} Cookies')

for row in workshop:
    print(*row, sep=' ')
