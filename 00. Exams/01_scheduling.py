tasks = [int(x) for x in input().split(', ')]
special_task = int(input())
clock_cycles = 0

ordered_tasks = {}
for i, task in enumerate(tasks):
    ordered_tasks[i] = task

for index, task in sorted(ordered_tasks.items(), key=lambda x: (x[1], x[0])):
    clock_cycles += task

    if index == special_task:
        break

print(clock_cycles)
