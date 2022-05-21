guests_num = int(input())
reservation_codes = set()

for i in range(guests_num):
    current_code = input()
    if len(current_code) == 8:
        reservation_codes.add(current_code)

while True:
    guest = input()
    if guest == 'END':
        break
    if guest in reservation_codes:
        reservation_codes.discard(guest)

print(len(reservation_codes))
for guest in sorted(reservation_codes):
    print(guest)
# [print(guest) for guest in sorted(reservation_codes)]