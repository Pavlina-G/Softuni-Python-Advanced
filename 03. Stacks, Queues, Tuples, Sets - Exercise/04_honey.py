from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
honey_operations = deque(input().split())
honey = 0

operations = {
    '+': lambda a,b: a + b,
    '-': lambda a,b: a - b,
    '*': lambda a,b: a * b,
    '/': lambda a,b: a / b
}

while working_bees and nectar:

    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar < current_bee:
        working_bees.appendleft(current_bee)
        continue
    if current_nectar != 0:
        current_symbol = honey_operations.popleft()
        honey += abs(operations[current_symbol](current_bee, current_nectar))

print(f"Total honey made: {honey}")

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
