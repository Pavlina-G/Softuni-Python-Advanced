from collections import deque

n = int(input())
petrol_pumps = deque()

for i in range(n):
    pumps_data = list(map(int, input().split(' ')))
    petrol_pumps.append(pumps_data)

for attempt in range(n):
    tank = 0
    failed = False

    for fuel, distance in petrol_pumps:
        tank += fuel

        if distance > tank:
            failed = True
            break
        else:
            tank -= distance

    if failed:
        petrol_pumps.rotate(-1)
        # petrol_pumps.append(petrol_pumps.popleft())
    else:
        print(attempt)
        break


