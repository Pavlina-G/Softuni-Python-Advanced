from collections import deque


def make_bombs(bombs_types, bomb_effects, bomb_casing):
    current_effect = bomb_effects[0]
    current_casing = bomb_casing[-1]
    current_sum = current_casing + current_effect

    for bomb, values in bombs_types.items():
        if current_sum == values[0]:
            bombs_types[bomb][1] += 1
            bomb_effects.popleft()
            bomb_casing.pop()
            return

    bomb_casing[-1] -= 5
    return


bomb_effects = deque(int(x) for x in input().split(', '))
bomb_casing = [int(x) for x in input().split(', ')]

bomb_1 = 'Datura Bombs'
bomb_2 = 'Cherry Bombs'
bomb_3 = 'Smoke Decoy Bombs'

bombs_types = {
    bomb_1: [40, 0],
    bomb_2: [60, 0],
    bomb_3: [120, 0],
}
successful_condition = False

while bomb_effects and bomb_casing:
    bomb_made = make_bombs(bombs_types, bomb_effects, bomb_casing)
    if bombs_types[bomb_1][1] >= 3 and bombs_types[bomb_2][1] >= 3 and \
            bombs_types[bomb_3][1] >= 3:
        successful_condition = True
        break

if successful_condition:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}" if bomb_effects else f"Bomb Effects: empty")
print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casing)}" if bomb_casing else f"Bomb Casings: empty")

[print(f"{bomb}: {values[1]}") for bomb, values in sorted(bombs_types.items())]
