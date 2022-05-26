def extract_coordinates(command):
    numbers = [int(x) for x in command.split(' ') if x.isdigit()]
    return numbers


def coordinates_validation(coordinates, matrix, rows, columns):
    valid_coordinates = []
    valid = True
    if len(coordinates) == 4:
        for num in range(len(coordinates)):
            if num % 2 == 0 and coordinates[num] in range(rows):
                valid_coordinates.append(coordinates[num])
            elif num % 2 != 0 and coordinates[num] in range(columns):
                valid_coordinates.append(coordinates[num])
            else:
                valid = False
                print('Invalid input!')
                break
    else:
        print('Invalid input!')
    if valid:
        return valid_coordinates


def print_func(matrix):
    for row in range(len(matrix)):
        print(' '.join(matrix[row]))


rows, columns = [int(x) for x in input().split(' ')]
matrix = [input().split(' ') for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        break

    if command.startswith('swap'):
        coordinates = extract_coordinates(command)
        valid_coordinates = coordinates_validation(coordinates, matrix, rows, columns)

        if valid_coordinates:
            row1 = valid_coordinates[0]
            col1 = valid_coordinates[1]
            row2 = valid_coordinates[2]
            col2 = valid_coordinates[3]

            first_num = matrix[row1][col1]
            matrix[row1][col1] = matrix[row2][col2]
            matrix[row2][col2] = first_num

            print_func(matrix)
    else:
        print('Invalid input!')
