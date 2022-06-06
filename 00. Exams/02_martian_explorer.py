from collections import deque


def next_position(row, col, command):
    if command == 'up':
        return row - 1, col
    elif command == 'down':
        return row + 1, col
    elif command == 'left':
        return row, col - 1
    elif command == 'right':
        return row, col + 1


def new_position(row, col, size, command):
    if command == 'up':
        return size - 1, col
    elif command == 'down':
        return 0, col
    elif command == 'left':
        return row, size - 1
    elif command == 'right':
        return row, 0


def collect_deposits(deposits_dict, row, col, deposit_type):
    if deposit_type not in deposits_dict:
        deposits_dict[deposit_type] = [(row, col)]
    else:
        deposits_dict[deposit_type].append((row, col))
    return deposits_dict


size = 6
matrix = []
rover_row = 0
rover_col = 0

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(size):
        if matrix[row][col] == 'E':
            rover_row = row
            rover_col = col

commands = deque(input().split(', '))
deposits = {}
colony = False

while commands:

    command = commands.popleft()

    next_row, next_col = next_position(rover_row, rover_col, command)

    if next_row not in range(size) or next_col not in range(size):
        rover_row, rover_col = new_position(next_row, next_col, size, command)
    else:
        rover_row, rover_col = next_row, next_col

    if matrix[rover_row][rover_col] == 'R':
        print(f"Rover got broken at {rover_row, rover_col}")
        break

    elif matrix[rover_row][rover_col] == '-':
        continue

    elif matrix[rover_row][rover_col] == 'W':
        water = 'W'
        deposits = collect_deposits(deposits, rover_row, rover_col, water)
        print(f'Water deposit found at {rover_row, rover_col}')

    elif matrix[rover_row][rover_col] == 'M':
        metal = 'M'
        deposits = collect_deposits(deposits, rover_row, rover_col, metal)
        print(f'Metal deposit found at {rover_row, rover_col}')

    elif matrix[rover_row][rover_col] == 'C':
        concrete = 'C'
        deposits = collect_deposits(deposits, rover_row, rover_col, concrete)
        print(f'Concrete deposit found at {rover_row, rover_col}')

    matrix[rover_row][rover_col] = '-'

if len(deposits) == 3:
    print(f'Area suitable to start the colony.')
else:
    print(f'Area not suitable to start the colony.')
