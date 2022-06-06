numbers_dictionary = {}

while True:
    line = input()

    if line == "Search":
        break
    try:
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")

while True:
    searched_num = input()

    if searched_num == "Remove":
        break

    if searched_num in numbers_dictionary:
        print(numbers_dictionary[searched_num])

while True:

    num_to_delete = input()
    if num_to_delete == "End":
        break
    try:
        del numbers_dictionary[num_to_delete]
    except KeyError:
        print('Number does not exist in dictionary')


print(numbers_dictionary)
