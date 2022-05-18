clothes = list(map(int, input().split(' ')))
rack_capacity = int(input())

rack_counter = 1
current_rack = rack_capacity

while clothes:
    current_item = clothes[-1]

    if current_item <= current_rack:
        clothes.pop()
        current_rack -= current_item
    else:
        rack_counter += 1
        current_rack = rack_capacity

print(rack_counter)
