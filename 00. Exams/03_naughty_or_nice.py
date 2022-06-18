def naughty_or_nice_list(kids, *args, **kwargs):
    santa_lists = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }
    kids_nums = [int(x[0]) for x in kids]

    for command in args:
        num, kind = command.split('-')
        num = int(num)

        for kid_num, kid_name in kids:
            if num == kid_num and kids_nums.count(num) == 1:
                santa_lists[kind].append(kid_name)
                kids.remove((kid_num, kid_name))

    for name, kind in kwargs.items():
        for kid_num, kid_name in kids:
            kids_names = [x[1] for x in kids]
            if name == kid_name and kids_names.count(name) == 1:
                santa_lists[kind].append(name)
                kids.remove((kid_num, kid_name))

    if kids:
        santa_lists['Not found'].extend([x[1] for x in kids])

    result = [f"{key}: {', '.join(value)}" for key, value in santa_lists.items() if len(value) > 0]
    return '\n'.join(result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
