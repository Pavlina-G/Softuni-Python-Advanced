from collections import deque

elf_energies = deque(int(x) for x in input().split(' '))
boxes = [int(x) for x in input().split(' ')]

total_used_energy = 0
total_crafted_toys = 0
counter = 0

while boxes and elf_energies:
    current_energy = elf_energies.popleft()
    if current_energy < 5:
        continue

    counter += 1
    current_material = boxes.pop()

    energy_needed = current_material
    crafted_toys = 1
    cookie = 1
    chocolate = 2

    if counter % 3 == 0:
        crafted_toys = 2
        energy_needed *= 2

    if counter % 5 == 0:
        crafted_toys = 0
        cookie = 0

    if current_energy >= energy_needed:
        total_crafted_toys += crafted_toys
        total_used_energy += energy_needed
        elf_energies.append(current_energy - energy_needed + cookie)
    else:
        boxes.append(current_material)
        elf_energies.append(current_energy * chocolate)

print(f"Toys: {total_crafted_toys}")
print(f"Energy: {total_used_energy}")

if elf_energies:
    print(f"Elves left: {', '.join(str(x) for x in elf_energies)}")
if boxes:
    print(f"Boxes left: {', '.join(str(x) for x in boxes)}")
