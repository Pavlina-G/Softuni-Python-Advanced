from collections import deque
from datetime import timedelta


def time_to_seconds(time):
    h, m, s = time.split(':')
    start_time_seconds = int(h) * 3600 + int(m) * 60 + float(s)

    return start_time_seconds


def seconds_to_time(sec):
    sec %= 24 * 60 * 60
    td = str(timedelta(seconds=sec)).zfill(8)

    # hours = sec // (60 * 60)
    # sec %= (60 * 60)
    # minutes = sec // 60
    # sec %= 60
    # return f'{hours:02d}:{minutes:02d}:{sec:02d}'

    return td


robots_data = deque(input().split(';'))
process_time_robots = {}
busy_time_robots = {}

starting_time = time_to_seconds(input())

for data in robots_data:
    name, process_time = data.split('-')
    process_time_robots[name] = int(process_time)
    busy_time_robots[name] = 0
    
products = deque()

while True:
    product = input()
    if product == 'End':
        break
    products.append(product)

while products:
    starting_time += 1
    item = products.popleft()

    for name, busy_until in busy_time_robots.items():
        if starting_time >= busy_until:
            busy_time_robots[name] = starting_time + process_time_robots[name]
            print(f"{name} - {item} [{seconds_to_time(starting_time)}]")
            break
    else:
        products.append(item)
