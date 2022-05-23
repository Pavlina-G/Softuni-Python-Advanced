from collections import deque


def mix_shakes(current_chocolate, current_cup, chocolates, cups_of_milk, milkshakes):
    if current_chocolate == current_cup:
        chocolates.pop()
        cups_of_milk.popleft()
        milkshakes += 1
    else:
        cups_of_milk.append(cups_of_milk.popleft())
        chocolates.pop()
        chocolates.append(current_chocolate - 5)

    return chocolates, cups_of_milk, milkshakes


def print_func(condition, chocolates, cups_of_milk, milkshakes):
    if condition:
        if milkshakes == 5:
            print("Great! You made all the chocolate milkshakes needed!")
        else:
            print("Not enough milkshakes.")

    if chocolates:
        print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
    else:
        print("Chocolate: empty")

    if cups_of_milk:
        print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")
    else:
        print("Milk: empty")


def milkshakes():
    chocolates = [int(x) for x in input().split(', ')]
    cups_of_milk = deque([int(x) for x in input().split(', ')])
    milkshakes = 0
    condition = False

    while True:
        if milkshakes == 5:
            condition = True
            break

        if chocolates:
            current_chocolate = chocolates[-1]
        else:
            condition = True
            break

        if cups_of_milk:
            current_cup = cups_of_milk[0]
        else:
            condition = True
            break

        if current_chocolate <= 0 and current_cup <= 0:
            chocolates.pop()
            cups_of_milk.popleft()
            continue

        if current_chocolate <= 0:
            chocolates.pop()
            continue

        if current_cup <= 0:
            cups_of_milk.popleft()
            continue

        chocolates, cups_of_milk, milkshakes = mix_shakes(current_chocolate, current_cup, chocolates, cups_of_milk,
                                                          milkshakes)

    print_func(condition, chocolates, cups_of_milk, milkshakes)


milkshakes()
