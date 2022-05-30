def is_valid(row, col, matrix):
    return row in range(len(matrix)) and col in range(len(matrix))


def next_position(row, col, direction, step):
    if direction == 'right':
        return row, col + step
    elif direction == 'left':
        return row, col - step
    elif direction == 'up':
        return row - step, col
    elif direction == 'down':
        return row + step, col


shooting_target = []
row_position = 0
col_position = 0
total_targets = 0

for row in range(5):
    row_elements = input().split()
    shooting_target.append(row_elements)
    for col in range(5):
        if shooting_target[row][col] == 'A':
            row_position = row
            col_position = col
        elif shooting_target[row][col] == 'x':
            total_targets += 1

shooting_target[row_position][col_position] = '.'

n = int(input())
shot_targets = []
all_shot = False
current_targets = 0

for i in range(n):
    command_info = input().split()
    action = command_info[0]
    direction = command_info[1]

    if action == "move":
        steps = int(command_info[2])
        next_row, next_col = next_position(row_position, col_position, direction, steps)

        if is_valid(next_row, next_col, shooting_target) and shooting_target[next_row][next_col] == '.':
            row_position, col_position = next_row, next_col

    if action == "shoot":
        target_row, target_col = next_position(row_position, col_position, direction, 1)

        while is_valid(target_row, target_col, shooting_target):

            if shooting_target[target_row][target_col] == 'x':
                shot_targets.append([target_row, target_col])
                current_targets += 1
                shooting_target[target_row][target_col] = '.'
                break
            target_row, target_col = next_position(target_row, target_col, direction, 1)

    if total_targets == current_targets:
        all_shot = True
        break

if all_shot:
    print(f"Training completed! All {current_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets - current_targets} targets left.")
if shot_targets:
    [print(target) for target in shot_targets]

