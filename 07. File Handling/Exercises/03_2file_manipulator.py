from os.path import exists
from os import remove

while True:
    command = input().split('-')

    if command[0] == 'End':
        break

    action, file_name = command[0], command[1]
    file_path = f'./{file_name}'

    if action == 'Create':
        with open(file_path, 'w') as file:
            pass

    elif action == 'Add':
        content = command[2]
        with open(file_path, 'a') as file:
            file.write(content + '\n')

    elif action == 'Replace':
        if not exists(file_path):
            print("An error occurred")
            continue

        old_string = command[2]
        new_string = command[3]

        with open(file_path, 'r+') as file:
            file_content = file.read().replace(old_string, new_string)
            file.seek(0) # move the pointer at the beginning
            file.truncate() # delete the content from the beginning
            file.write(file_content)

    elif action == 'Delete':
        if not exists(file_path):
            print("An error occurred")
            continue

        remove(file_path)

