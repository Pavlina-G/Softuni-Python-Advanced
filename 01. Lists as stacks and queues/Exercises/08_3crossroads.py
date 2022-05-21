from collections import deque

green_light_sec = int(input())
free_window_sec = int(input())

cars = deque()
crash = False
car_counter = 0

while not crash:
    command = input()

    if command == 'END':
        break
    elif command != 'green':
        cars.append(command)
    else:
        green_light = green_light_sec

        while cars and green_light > 0:
            current_car = cars.popleft()

            if green_light + free_window_sec >= len(current_car):
                car_counter += 1
            else:
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[green_light + free_window_sec]}.")
                crash = True
                break
            green_light -= len(current_car)


if not crash:
    print("Everyone is safe.")
    print(f"{car_counter} total cars passed the crossroads.")



