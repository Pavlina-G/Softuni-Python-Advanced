from collections import deque

def list_manipulator(numbers, *args):

    nums = numbers
    command = args[0]
    direction = args[1]
    command_nums = list(args[2:]) if len(args) > 2 else []

    if command == 'add':
        nums = command_nums + nums if direction == 'beginning' else nums + command_nums
    elif command == 'remove':
        if command_nums:
            count = int(command_nums[0])
            if direction == 'beginning':
                nums = nums[count:] if len(nums)-1 >= count else []
            elif direction == 'end':
                nums = nums[:-count] if len(nums) - 1 >= count else []
        else:
            nums = nums[1:] if direction == 'beginning' else nums[:-1]
    return nums


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
