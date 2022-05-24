from collections import deque

box_materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

crafting_table = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

crafted_presents = dict()

while box_materials and magic_level:
    material = box_materials.pop()
    magic = magic_level.popleft()

    if material == 0 and magic == 0:
        continue

    if material == 0:
        magic_level.appendleft(magic)
        continue

    if magic == 0:
        box_materials.append(material)
        continue

    result = material * magic

    if result in crafting_table:
        toy = crafting_table[result]
        if toy in crafted_presents:
            crafted_presents[toy] += 1
        else:
            crafted_presents[toy] = 1
        continue

    if result < 0:
        box_materials.append(material + magic)
    else:
        box_materials.append(material + 15)

if ('Doll' in crafted_presents and 'Wooden train' in crafted_presents) or \
    ('Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")
    
if box_materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(box_materials)])}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")
    
for toy, value in sorted(crafted_presents.items()):
    print(f"{toy}: {value}")