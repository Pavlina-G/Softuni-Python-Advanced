def get_next_move(command, miner_position):
    row, col = miner_position[0], miner_position[1]
    if command == 'up':
        return (row - 1, col)
    elif command == 'down':
        return (row + 1, col)
    elif command == 'left':
        return (row, col - 1)
    elif command == 'right':
        return (row, col + 1)


size = int(input())
commands = input().split()

matrix = []

miner_position = (0, 0)
total_coal = 0

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(size):
        element = row_elements[col]
        if element == 's':
            miner_position = (row, col)
        elif element == 'c':
            total_coal += 1

condition = False
for command in commands:
    next_position = get_next_move(command, miner_position)
    next_row,next_col = next_position[0], next_position[1]

    if next_row not in range(size) or next_col not in range(size):
        continue

    miner_position = next_position
    if matrix[next_row][next_col] == 'c':
        total_coal -= 1
        matrix[next_row][next_col] = '*'
        if total_coal == 0:
            break
    elif matrix[next_row][next_col] == 'e':
        condition = True
        break

if total_coal == 0:
    print(f"You collected all coal! {miner_position}")
elif condition:
    print(f"Game over! {miner_position}")
else:
    print(f"{total_coal} pieces of coal left. {miner_position}")
