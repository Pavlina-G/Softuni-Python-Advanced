from string import punctuation, ascii_letters


def count_words_and_symbols(line):
    punctuation_marks = set(list(punctuation))
    letter_count = 0
    symbol_count = 0

    for ch in line:
        if ch in ascii_letters:
            letter_count += 1
        elif ch in punctuation_marks:
            symbol_count += 1
    return letter_count, symbol_count


with open('02_text.txt', 'r') as file, open('./output.txt', 'w') as result:
    for i, line in enumerate(file):
        letters, symbols = count_words_and_symbols(line)
        result.write(f'Line {i + 1}: {line.strip()} ({letters})({symbols})\n')
