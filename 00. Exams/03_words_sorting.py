def words_sorting(*args):
    words_dict = {}

    for word in args:
        if word not in words_dict:
            words_dict[word] = sum([ord(x) for x in word])

    sorted_dict = [f'{key} - {value}' for key, value in
                   sorted(words_dict.items(), key=lambda x: (-x[1] if sum(words_dict.values()) % 2 != 0 else x[0]))]
    return '\n'.join(sorted_dict)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
