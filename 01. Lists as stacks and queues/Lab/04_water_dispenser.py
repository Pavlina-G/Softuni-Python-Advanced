from collections import deque

queue = deque()
water = int(input())

name = input()

while name != 'Start':
    queue.append(name)
    name = input()

while True:
    command = input()

    if command == 'End':
        print(f"{water} liters left")
        break
    # elif 'refill' in command:
    elif command.startswith('refill'):
        stack = command.split(' ') # _, water_to_refill = command.split(' ')
        water += int(stack.pop()) # water += int(water_to_refill)
    else:
        if (water - int(command)) >= 0:
            print(f"{queue.popleft()} got water")
            water -= int(command)
        else:
            print(f"{queue.popleft()} must wait")