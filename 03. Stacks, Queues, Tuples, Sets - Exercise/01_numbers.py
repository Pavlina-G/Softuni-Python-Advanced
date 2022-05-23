def extract_numbers(line):
    nums = set(map(int, command.split()[2:]))

    return nums


set1 = set([int(x) for x in input().split(' ')])
set2 = set([int(x) for x in input().split(' ')])
n = int(input())

for _ in range(n):
    command = input()
    numbers = extract_numbers(command)

    if command.startswith('Add First'):
        [set1.add(int(x)) for x in numbers]
    elif command.startswith('Add Second'):
        [set2.add(int(x)) for x in numbers]
    elif command.startswith('Remove First'):
        set1 = set1.difference(numbers)
    elif command.startswith('Remove Second'):
        set2 = set2.difference(numbers)
    elif command.startswith('Check Subset'):
        print(set1.issubset(set2) or set2.issubset(set1))

print(*sorted(set1), sep=', ')
print(*sorted(set2), sep=', ')
