def next_position(row, col, direction):
    if direction == 'up':
        return row - 1, col
    elif direction == 'down':
        return row + 1, col
    elif direction == 'left':
        return row, col - 1
    elif direction == 'right':
        return row, col + 1


def is_valid(row, col, matrix):
    return row in range(len(matrix)) and col in range(len(matrix))


def give_presents(row, col, matrix, presents, kids):
    possible_presents = [
        [row + 1, col],
        [row - 1, col],
        [row, col + 1],
        [row, col - 1],
    ]

    for present_row, present_col in possible_presents:
        if is_valid(present_row, present_col, matrix):

            if matrix[present_row][present_col] == 'V':
                presents -= 1
                kids += 1
                matrix[present_row][present_col] = '-'

            elif matrix[present_row][present_col] == 'X':
                matrix[present_row][present_col] = '-'
                presents -= 1

    return presents, kids


presents = int(input())
n = int(input())

neighborhood = []
santa_row = 0
santa_col = 0
nice_kids = 0

for row in range(n):
    row_elements = input().split()
    neighborhood.append(row_elements)
    for col in range(n):
        if neighborhood[row][col] == 'S':
            santa_row = row
            santa_col = col
        elif neighborhood[row][col] == 'V':
            nice_kids += 1

neighborhood[santa_row][santa_col] = '-'
current_nice_kids = 0

while True:
    command = input()
    neighborhood[santa_row][santa_col] = '-'

    if command == 'Christmas morning':
        break

    next_row, next_col = next_position(santa_row, santa_col, command)
    if not is_valid(next_row, next_col, neighborhood):
        continue

    santa_row, santa_col = next_row, next_col

    if neighborhood[santa_row][santa_col] == 'V':
        presents -= 1
        current_nice_kids += 1
    elif neighborhood[santa_row][santa_col] == 'X' or neighborhood[santa_row][santa_col] == '-':
        continue
    elif neighborhood[santa_row][santa_col] == 'C':
        presents, current_nice_kids = give_presents(santa_row, santa_col, neighborhood, presents, current_nice_kids)

    if presents <= 0:
        break

neighborhood[santa_row][santa_col] = 'S'

if presents <= 0 and current_nice_kids < nice_kids:
    print("Santa ran out of presents!")
for row in neighborhood:
    print(*row, sep=' ')

if current_nice_kids == nice_kids:
    print(f"Good job, Santa! {current_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - current_nice_kids} nice kid/s.")
