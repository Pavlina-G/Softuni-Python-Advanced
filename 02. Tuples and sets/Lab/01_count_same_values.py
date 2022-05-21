nums = tuple(map(float, input().split(' ')))

number_value = {}

for num in nums:
    if num not in number_value:
        number_value[num] = 0
    number_value[num] += 1

for num, count in number_value.items():
    print(f"{num} - {count} times")
