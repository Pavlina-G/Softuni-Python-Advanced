from collections import deque


def is_valid(num):
    return num > 0


def divisible_by_25(num):
    return num % 25 == 0


def match(male, female):
    return male == female


males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())
matches = 0
empty_list = False

while males and females:
    current_male = males[-1]
    current_female = females[0]

    if not is_valid(current_male) and is_valid(current_female):
        males.pop()
        continue
    elif is_valid(current_male) and not is_valid(current_female):
        females.popleft()
        continue
    elif not is_valid(current_male) and not is_valid(current_female):
        males.pop()
        females.popleft()
        continue

    if divisible_by_25(current_male):
        males.pop()
        if males:
            males.pop()
        else:
            break
        continue

    if divisible_by_25(current_female):
        females.popleft()
        if females:
            females.popleft()
        else:
            break
        continue

    if match(current_male, current_female):
        matches += 1
        males.pop()
        females.popleft()
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")
print(f"Males left: {'none' if not males else ', '.join(str(x) for x in reversed(males))}")
print(f"Females left: {'none' if not females else ', '.join(str(x) for x in females)}")
