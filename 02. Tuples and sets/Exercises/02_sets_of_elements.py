def sets_of_elements(n, m):
    set1 = set()
    set2 = set()

    for i in range(n):
        set1.add(int(input()))
    for i in range(m):
        set2.add(int(input()))
    common_numbers = set1.intersection(set2)

    for num in common_numbers:
        print(num)


n_num, m_num = list(map(int, input().split(' ')))
# n_num, m_num = [int(x) for x in input().split(' ')]
sets_of_elements(n_num, m_num)
