from collections import deque
queue = deque()
while True:

    customer = input()

    if customer == 'Paid':
        while queue:
            print(queue.popleft())

    elif customer == 'End':
        print(f"{len(queue)} people remaining.")
        break

    else:
        queue.append(customer)