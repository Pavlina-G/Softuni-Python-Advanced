from collections import deque

def best_list_pureness(numbers, k):
    nums = deque(numbers)
    pureness_sum = 0
    index = 0
    rotation_info = {}

    for i in range(k + 1):
        index = 0
        for num in nums:
            pureness_sum += num * index
            index += 1
        rotation_info[i] = pureness_sum
        pureness_sum = 0
        nums.rotate()

    (min_rotation, max_pureness) = max(rotation_info.items(), key=lambda x: (x[1], -x[0]))
    return f"Best pureness {max_pureness} after {min_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
