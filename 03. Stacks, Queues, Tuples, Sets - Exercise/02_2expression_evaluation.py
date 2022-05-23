from collections import deque

expression = input().split(' ')
nums = deque()

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}

for ch in expression:
    if ch not in '+-*/':
        nums.append(int(ch))
    else:
        while len(nums) > 1:
            first = nums.popleft()
            second = nums.popleft()
            result = operations[ch](first, second)
            nums.appendleft(result)

print(nums.popleft())