from collections import deque


def is_valid(value):
    return value > 0


fireworks_effects = deque(int(x) for x in input().split(', '))
explosive_power = [int(x) for x in input().split(', ')]

firework_types = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0,
}
successfully_prepared = False

while fireworks_effects and explosive_power:
    effect = fireworks_effects.popleft()
    power = explosive_power.pop()

    if not is_valid(effect) and is_valid(power):
        explosive_power.append(power)
        continue
    elif is_valid(effect) and not is_valid(power):
        fireworks_effects.appendleft(effect)
        continue
    elif not is_valid(effect) and not is_valid(power):
        continue

    sum_mix = effect + power
    if sum_mix % 3 == 0 and sum_mix % 5 == 0:
        firework_types['Crossette Fireworks'] += 1
    elif sum_mix % 3 == 0 and sum_mix % 5 != 0:
        firework_types['Palm Fireworks'] += 1
    elif sum_mix % 5 == 0 and sum_mix % 3 != 0:
        firework_types['Willow Fireworks'] += 1
    else:
        fireworks_effects.append(effect - 1)
        explosive_power.append(power)

    if firework_types['Crossette Fireworks'] >= 3 and \
            firework_types['Palm Fireworks'] >= 3 and \
            firework_types['Willow Fireworks'] >= 3:
        successfully_prepared = True
        break

if successfully_prepared:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")
if fireworks_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in fireworks_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

for key, value in firework_types.items():
    print(f"{key}: {value}")
