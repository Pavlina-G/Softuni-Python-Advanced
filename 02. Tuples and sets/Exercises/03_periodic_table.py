def periodic_table():
    n = int(input())
    elements = list()

    for i in range(n):
        elements.extend(input().split(' '))

    for i in set(elements):
        print(i)


periodic_table()