from collections import deque


def fast_food():
    food = int(input())
    order_food = deque(map(int, input().split()))
    print(max(order_food))

    while order_food:
        current_order = order_food[0]

        if current_order > food:
            break
        else:
            served_food = int(order_food.popleft())
            food -= served_food

    if len(order_food) == 0:
        print("Orders complete")
    else:
        print(f"Orders left: {' '.join(map(str, order_food))}")


fast_food()
