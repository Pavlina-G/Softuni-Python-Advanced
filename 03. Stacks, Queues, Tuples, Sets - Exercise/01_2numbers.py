def extract_numbers(line):
    nums = set(map(int, command.split()[2:]))
    # nums = set([int(x) for x in command.split() if x.isdigit()])

    return nums


set1 = set([int(x) for x in input().split(' ')])
set2 = set([int(x) for x in input().split(' ')])
n = int(input())

while n > 0:
    n -= 1
    command = input()
    numbers = extract_numbers(command)

    if command.startswith('Add First'):
        set1 = set1.union(numbers)
    elif command.startswith('Add Second'):
        set2 = set2.union(numbers)
    elif command.startswith('Remove First'):
        set1.difference_update(numbers)
    elif command.startswith('Remove Second'):
        set2.difference_update(numbers)
    elif command.startswith('Check Subset'):
        print(set1.issubset(set2) or set2.issubset(set1))

print(*sorted(set1), sep=', ')
print(*sorted(set2), sep=', ')
