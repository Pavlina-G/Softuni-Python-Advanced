import string

rows, columns = [int(x) for x in input().split(' ')]
letters = string.ascii_lowercase

first_last_letters = letters[:rows]
middle_letters = letters[:rows+columns]

for row in range(rows):
    for col in range(columns):
        print(f'{first_last_letters[0 + row]}{middle_letters[0 + row + col]}{first_last_letters[0 + row]}', end=' ')
    print()