from collections import deque


green_light_sec = int(input())
free_window_sec = int(input())

cars = deque()
crash = False
car_counter = 0
green_light = green_light_sec

while True:
    command = input()

    if command == 'END':
        break
    elif command != 'green':
        cars.append(command)
    else:
        if cars:
            green_light = green_light_sec
            while True:

                if cars:
                    current_car = cars.popleft()
                    current_car_time = len(current_car)

                    if current_car_time < green_light:
                        green_light -= current_car_time
                        car_counter += 1
                    elif current_car_time == green_light:
                        green_light -= current_car_time
                        car_counter += 1
                        crash = False
                        break
                    else:
                        if current_car_time <= green_light + free_window_sec and green_light != 0:
                            car_counter += 1
                            green_light = 0
                        elif current_car_time <= green_light + free_window_sec and green_light == 0:
                            break
                        else:
                            crash = True
                            crash_index = green_light + free_window_sec
                            break
                    if crash:
                        break
                else:
                    break
        if crash:
            break


if crash:
    print("A crash happened!")
    print(f"{current_car} was hit at {current_car[crash_index]}.")
else:
    print("Everyone is safe.")
    print(f"{car_counter} total cars passed the crossroads.")



