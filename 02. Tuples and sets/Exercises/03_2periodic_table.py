def periodic_table():
    n = int(input())
    elements = set()

    for i in range(n):
        element = input().split(' ')
        for el in element:
            elements.add(el)

    print("\n".join(elements))


periodic_table()