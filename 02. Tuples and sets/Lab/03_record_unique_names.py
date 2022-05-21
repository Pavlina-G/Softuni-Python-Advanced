n = int(input())
unique_names = set()

for i in range(n):
    unique_names.add(input())

for name in unique_names:
    print(name)

# 2

# n = int(input())
# unique_names = {input() for _ in range(n)} # set()
# [print(name) for name in unique_names]