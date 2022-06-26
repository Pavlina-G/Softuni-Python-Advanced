def play_game(maze, first_player, second_player):
    current_player, other_player = first_player, second_player
    winner = False
    rest = {}

    while True:

        position = eval(input())
        if current_player in rest:
            rest.pop(current_player)
            current_player, other_player = other_player, current_player
            continue

        current_row, current_column = position[0], position[1]

        maze_position = maze[current_row][current_column]
        if maze_position == 'T':
            winner = False
            break

        elif maze_position == 'E':
            winner = True
            break

        elif maze_position == 'W':
            print(f"{current_player} hits a wall and needs to rest.")
            if current_player not in rest:
                rest[current_player] = 1
            current_player, other_player = other_player, current_player
            continue
        else:
            pass
        current_player, other_player = other_player, current_player

    if not winner:
        print(
            f"{current_player} is out of the game! The winner is {second_player if current_player == first_player else first_player}.")
        return
    else:
        print(f"{current_player} found the Exit and wins the game!")
        return


first_player, second_player = input().split(', ')
size = 6
maze = [[x for x in input().split(' ')] for _ in range(size)]
play_game(maze, first_player, second_player)
