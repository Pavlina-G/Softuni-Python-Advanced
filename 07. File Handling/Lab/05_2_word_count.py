import re


def searched_words(file_path):
    with open(file_path, 'r') as file:
        s_words = file.read().split()

    return s_words


def find_words_count(s_words, file_path):
    words_count = {}
    with open(file_path, 'r') as file:
        text = file.read()
        for word in s_words:
            pattern = fr'\b{word}\b'
            counter = len(re.findall(pattern, text, re.IGNORECASE))
            words_count[word] = counter
    return words_count


def store_result(found_words, file_path):
    sorted_result =  sorted(found_words.items(), key=lambda kvpt: -kvpt[1])
    with open(file_path, 'w') as file:
        for k, v in sorted_result:
            file.writelines(f'{k} - {v}\n')


words_to_find = searched_words('./words_count_files/words.txt')
count_words = find_words_count(words_to_find, './words_count_files/input.txt')
result = store_result(count_words, './output.txt')


