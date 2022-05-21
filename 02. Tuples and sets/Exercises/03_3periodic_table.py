n = int(input())
elements = set()

for i in range(n):
    current_set = set(input().split(' '))
    elements = elements.union(current_set)

# {print(el) for el in elements}
print(*elements, sep='\n')