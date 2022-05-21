guests_num = int(input())
vip_codes = set()
regular_codes = set()

for i in range(guests_num):
    current_code = input()
    if len(current_code) == 8:
        if current_code[0].isdigit():
            vip_codes.add(current_code)
        else:
            regular_codes.add(current_code)

all_guests = vip_codes.union(regular_codes)

while True:
    guest = input()
    if guest == 'END':
        break
    if guest in all_guests:
        all_guests.discard(guest)

print(len(all_guests))
for guest in sorted(all_guests):
    print(guest)
