from collections import deque


def cups_and_bottles():
    cups = deque(list(map(int,input().split(' '))))
    bottles = list(map(int,input().split(' ')))
    wasted_water = 0

    while True:
        if not cups:
            break
        if not bottles:
            break

        current_cup = cups[0]
        current_bottle = bottles.pop()

        if current_bottle >= current_cup:
            current_bottle -= cups.popleft()
            wasted_water += current_bottle
        else:
            current_cup -= current_bottle
            cups.popleft()
            cups.appendleft(current_cup)
            continue

    if not cups:
        print(f"Bottles: {' '.join(map(str, bottles[::-1]))}")
    else:
        print(f"Cups: {' '.join(map(str, cups))}")
    print(f"Wasted litters of water: {wasted_water}")


cups_and_bottles()
