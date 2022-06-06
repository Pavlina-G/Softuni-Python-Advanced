from collections import deque

bowls = [int(x) for x in input().split(', ')]
customers = deque(int(x) for x in input().split(', '))

while bowls and customers:
    current_bowl = bowls.pop()
    customer = customers.popleft()

    if current_bowl > customer:
        bowls.append(current_bowl - customer)
    elif current_bowl < customer:
        customers.appendleft(customer - current_bowl)

if customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
else:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")
