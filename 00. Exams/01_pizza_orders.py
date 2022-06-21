from collections import deque

def is_valid_order(pizza):
    return 0 < pizza < 11

pizza_orders = deque(int(x) for x in input().split(', '))
employees = [int(x) for x in input().split(', ')]
pizzas_made = 0

while pizza_orders and employees:

    current_pizza = pizza_orders.popleft()
    current_employee = employees.pop()

    if not is_valid_order(current_pizza):
        employees.append(current_employee)
        continue
    if current_pizza > current_employee:
        pizza_orders.appendleft(current_pizza - current_employee)
        pizzas_made += current_employee
        continue
    pizzas_made += current_pizza


if not pizza_orders:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_made}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")
else:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")
