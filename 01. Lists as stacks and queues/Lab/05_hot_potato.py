from collections import deque

kids = deque(input().split(' '))
n = int(input())

while len(kids) > 1:
    kids.rotate(-n)
    print(f'Removed {kids.pop()}')

print(f'Last is {kids.popleft()}')


# 2 way

# kids = deque(input().split(' '))
# n = int(input())
#
# current_count = 0
# while len(kids) > 1:
#     current_count += 1
#     kid = kids.popleft()
#
#     if current_count < n:
#         kids.append(kid)
#     else:
#         print(f'Removed {kid}')
#         current_count = 0
#
# print(f'Last is {kids.popleft()}')

