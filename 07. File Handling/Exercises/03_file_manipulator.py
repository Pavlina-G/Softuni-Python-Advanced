from os import remove
from os.path import exists


def create_file(file_path):
    file = open(file_path, 'w')
    file.close()


def add_content(file_path, content):
    if exists(file_path):
        with open(file_path, 'a') as file:
            file.write(f'{content}\n')
    else:
        with open(file_path, 'w') as file:
            file.write(f'{content}\n')
    file.close()


def replace_func(file_path, old, new):
    if not exists(file_path):
        print("An error occurred")
    else:
        with open(file_path, 'r') as file:
            text = '\n'.join([line.strip() for line in file.readlines()])

        with open(file_path, 'w') as new_text:
            new_text.write(text.replace(old, new))

        file.close()
        new_text.close()


def delete_file(file_path):
    if exists(file_path):
        remove(file_path)
    else:
        print("An error occurred")


while True:
    command = input().split('-')

    if command[0] == 'End':
        break

    action = command[0]
    file_name = command[1]
    file_path = f'./{file_name}'

    if action == 'Create':
        create_file(file_name)

    elif action == 'Add':
        content = command[2]
        add_content(file_path, content)

    elif action == 'Replace':
        old_string = command[2]
        new_string = command[3]
        replace_func(file_path, old_string, new_string)

    elif action == 'Delete':
        delete_file(file_path)
