def numbers_searching(*args):
    duplicate_numbers = set()
    for arg in args:
        if args.count(arg) > 1:
            duplicate_numbers.add(arg)

    sorted_numbers = sorted(set(args))
    start_num = sorted_numbers[0]
    end_num = sorted_numbers[-1]
    full_list = []

    for i in range(start_num, end_num + 1):
        full_list.append(i)
        for j in sorted_numbers:
            full_list.append(j)

    result = []
    for num in full_list:
        if full_list.count(num) == 1:
            result.append(num)
            break

    result.append(sorted(duplicate_numbers))
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
