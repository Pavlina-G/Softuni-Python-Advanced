# n = int(input())
# cars = set()
#
# for i in range(n):
#     direction, number = input().split(', ')
#     if direction == 'IN':
#         cars.add(number)
#     elif direction == 'OUT' and number in cars:
#         cars.discard(number)
#
# if cars:
#     for car in cars:
#         print(car)
# else:
#     print('Parking Lot is Empty')

# 2

n = int(input())

parking_lot_logs = [input().split(', ') for _ in range(n)]

parking_lot = set()

for direction, car_number in parking_lot_logs:
    if direction == 'IN':
        parking_lot.add(car_number)
    else:
        parking_lot.remove(car_number)

if parking_lot:
    [print(car_number) for car_number in parking_lot]
else:
    print('Parking Lot is Empty')