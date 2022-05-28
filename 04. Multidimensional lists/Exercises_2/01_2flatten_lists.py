main_list = input().split('|')
result = []

for i in range(len(main_list) - 1, -1, -1):
    sub_list = main_list[i].strip().split()
    result.extend(sub_list)

print(' '.join(result))
