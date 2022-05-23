def is_even_odd(num, even, odd):
    if num % 2 == 0:
        even.add(num)
    else:
        odd.add(num)

    return even, odd


def operations(odd, even):

    if sum(odd) == sum(even):
        output = odd.union(even)
    elif sum(even) < sum(odd):
        output = odd.difference(even)
    else:
        output = odd.symmetric_difference(even)

    return output


n = int(input())
even = set()
odd = set()

for row in range(1, n + 1):
    name = input()
    sum_name = sum([ord(ch) for ch in name]) // row

    is_even_odd(sum_name, even, odd)

output = operations(odd, even)

print(*output, sep=', ')
