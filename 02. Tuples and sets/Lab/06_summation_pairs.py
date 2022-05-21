from collections import deque

numbers = deque(map(int, input().split(' ')))
target = int(input())
iterations = 0
unique_combinations = set()

while numbers:
    current_number = numbers.popleft()
    if numbers:
        for num in numbers:
            iterations += 1
            if current_number + num == target:
                print(f"{current_number} + {num} = {target}")
                unique_combinations.add(f'({current_number}, {num})')

print(f"Iterations done: {iterations}")
for combination in unique_combinations:
    print(combination)
