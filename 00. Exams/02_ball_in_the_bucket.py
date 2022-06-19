def check_prizes(points):
    if points in range(100, 200):
        prize = 'Football'
        return f"Good job! You scored {points} points, and you've won {prize}."
    elif points in range(200, 300):
        prize = 'Teddy Bear'
        return f"Good job! You scored {points} points, and you've won {prize}."
    elif points >= 300:
        prize = 'Lego Construction Set'
        return f"Good job! You scored {points} points, and you've won {prize}."
    else:
        return f"Sorry! You need {100 - points} points more to win a prize."


def is_valid(row, col, size):
    return row in range(size) and col in range(size)


size = 6
board = [[int(x) if x.isdigit() else x for x in input().split(' ')] for row in range(size)]
points = 0

for _ in range(3):
    row, column = eval(input())
    if not is_valid(row, column, size):
        continue
    if isinstance(board[row][column], int):
        continue
    if board[row][column] == "B":
        points += sum(board[i][column] if not isinstance(board[i][column], str) else 0 for i in range(size))
        board[row][column] = 'x'

print(check_prizes(points))
