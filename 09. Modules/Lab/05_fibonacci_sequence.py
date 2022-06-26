import fibonacci_module as fm
from fibonacci_module.while_input import while_input,parse_by_space

commands = while_input('Stop')

for command in commands:
    action, number  = parse_by_space(command)

    if action == 'Create':
        print(fm.create_fibonacci_up_to_number(number))

    elif action == 'Locate':
        index = fm.locate_number(number)

        if index is not None:
            print(f'The number - {number} is at index {index}')
        else:
            print(f'The number {number} is not in the sequence')






