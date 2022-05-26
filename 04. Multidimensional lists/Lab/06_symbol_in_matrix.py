size = int(input())

matrix = [[str(x) for x in input()] for _ in range(size)]
symbol = input()
symbol_found = False
# location = ()

for row_index in range(size):
    for col_index in range(size):
        current_char = matrix[row_index][col_index]
        if symbol == current_char:
            # location = (row_index, col_index)
            print(f"({row_index}, {col_index})")
            symbol_found = True
            break
    if symbol_found:
        break

if not symbol_found:
    print(f"{symbol} does not occur in the matrix")
