from collections import deque


def check_for_a_gift(points):
    if 100 <= points <= 199:
        return 'Gemstone'
    elif 200 <= points <= 299:
        return 'Porcelain Sculpture'
    elif 300 <= points <= 399:
        return 'Gold'
    elif 400 <= points <= 499:
        return 'Diamond Jewellery'
    return None


materials = [int(x) for x in input().split(' ')]
magic = deque(int(x) for x in input().split(' '))

gifts = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

while materials and magic:

    current_material = materials.pop()
    current_magic = magic.popleft()

    magic_sum = current_material + current_magic
    if magic_sum < 100 and magic_sum % 2 == 0:
        magic_sum = current_material * 2 + current_magic * 3

    if magic_sum < 100 and magic_sum % 2 != 0:
        magic_sum = current_material * 2 + current_magic * 2

    if magic_sum > 499:
        magic_sum /= 2

    current_gift = check_for_a_gift(magic_sum)

    if current_gift is not None:
        gifts[current_gift] += 1
    else:
        continue


if (gifts['Gemstone'] > 0 and gifts['Porcelain Sculpture'] > 0) or \
        (gifts['Gold'] > 0 and gifts['Diamond Jewellery'] > 0):
    print(f"The wedding presents are made!")
else:
    print(f"Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for gift, value in sorted(gifts.items()):
    if value != 0:
        print(f"{gift}: {value}")
