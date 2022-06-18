from collections import deque


def replace_char(char, word):
    return word.replace(char, '')


def print_vowels_consonants_left(vowels, consonants):
    if vowels:
        print(f"Vowels left: {' '.join(x for x in vowels)}")
    if consonants:
        print(f"Consonants left: {' '.join(x for x in consonants)}")


vowels = deque(input().split(' '))
consonants = input().split(' ')
words = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil"
}
word_found = False

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for word in words:

        if current_vowel in word:
            words[word] = replace_char(current_vowel, words[word])
        if current_consonant in word:
            words[word] = replace_char(current_consonant, words[word])
        if words[word] == '':
            print(f"Word found: {word}")
            print_vowels_consonants_left(vowels, consonants)
            word_found = True
            break

    if word_found:
        break

if not word_found:
    print("Cannot find any word!")
    print_vowels_consonants_left(vowels, consonants)
