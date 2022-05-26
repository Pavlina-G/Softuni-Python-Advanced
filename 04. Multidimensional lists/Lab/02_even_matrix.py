# Comprehension solution:

# rows = int(input())
# matrix = [[int(x) for x in input().split(', ') if int(x) % 2 == 0] for i in range(rows)]
# print(matrix)


rows = int(input())
matrix = []

for _ in range(rows):
    nums = [int(el) for el in input().split(', ') if int(el) % 2 == 0]
    matrix.append(nums)

print(matrix)