def unique_usernames(n):
    names = set()
    for i in range(n):
        names.add(input())

    for name in names:
        print(name)


num = int(input())
unique_usernames(num)
