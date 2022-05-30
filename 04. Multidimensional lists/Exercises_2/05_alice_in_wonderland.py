def not_valid(row, col, matrix):
    return row not in range(len(matrix)) or col not in range(len(matrix))


def next_position(command, row, col):
    if command == 'left':
        return row, col - 1
    elif command == 'right':
        return row, col + 1
    elif command == 'up':
        return row - 1, col
    elif command == 'down':
        return row + 1, col


n = int(input())
wonderland = []
alice_row = 0
alice_col = 0

for row in range(n):
    row_elements = input().split()
    wonderland.append(row_elements)
    for col in range(n):
        if wonderland[row][col] == 'A':
            alice_row = row
            alice_col = col

tea_bags = 0
collected = False

while True:
    command = input()

    next_row, next_col = next_position(command, alice_row, alice_col)
    wonderland[alice_row][alice_col] = '*'

    if not_valid(next_row, next_col, wonderland):
        break

    alice_row, alice_col = next_row, next_col

    if wonderland[alice_row][alice_col] == 'R':
        wonderland[alice_row][alice_col] = '*'
        break

    elif wonderland[alice_row][alice_col] == '.' or wonderland[alice_row][alice_col] == '*':
        wonderland[alice_row][alice_col] = '*'
        continue

    else:
        tea_bags += int(wonderland[alice_row][alice_col])
        wonderland[alice_row][alice_col] = '*'

    if tea_bags >= 10:
        collected = True
        break

if collected:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for row in wonderland:
    print(*row, sep=' ')
