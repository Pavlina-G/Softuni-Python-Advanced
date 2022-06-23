from collections import deque

customers = deque(int(x) for x in input().split(', '))
taxis = [int(x) for x in input().split(', ')]
total_time = 0

while customers and taxis:
    current_customer = customers.popleft()
    current_taxi = taxis.pop()

    if current_taxi >= current_customer:
        total_time += current_customer
        continue
    else:
        customers.appendleft(current_customer)

if not customers:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print(f"Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
