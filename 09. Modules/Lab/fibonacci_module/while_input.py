def while_input(command, map_func=None):
    result = []
    while True:
        line = input()
        if line == command:
            break
        result.append(line)

    if map_func is None:
        return result

    return [map_func(x) for x in result]


def parse_by_space(list_of_commands):
    info = list_of_commands.split(' ')
    if info[0] == 'Create':
        return info[0], int(info[-1])
    elif info[0] == 'Locate':
        return info[0], int(info[-1])
