from collections import deque


def green_command(green, yellow, cars, counter, crash_index):
    green_light = green
    free_window = yellow
    crash = False

    while True:
        if cars:

            current_car = cars.popleft()
            current_time_car = len(current_car)

            if green_light > current_time_car:
                counter += 1
                green_light -= current_time_car
            elif green_light == current_time_car:
                counter += 1
                green_light -= current_time_car
                crash = False
                break
            else:
                if current_time_car <= green_light + free_window and green_light != 0:
                    counter += 1
                    green_light = 0
                elif current_time_car <= green_light + free_window and green_light == 0:
                    break
                else:
                    crash = True
                    crash_index = green_light + free_window
                    break
            if crash:
                break
        else:
            break

    return crash, current_car, crash_index, counter


def crossroad():
    green_light_sec = int(input())
    free_window_sec = int(input())

    cars = deque()
    crash = False
    car_counter = 0
    crash_index = 0

    command = input()
    while command != 'END':

        if command != 'green':
            cars.append(command)
        else:
            if cars:
                crash, current_car, crash_index, car_counter = green_command(green_light_sec, free_window_sec, cars,
                                                                             car_counter, crash_index)
            if crash:
                break

        command = input()

    if crash:
        print("A crash happened!")
        print(f"{current_car} was hit at {current_car[crash_index]}.")
    else:
        print("Everyone is safe.")
        print(f"{car_counter} total cars passed the crossroads.")


crossroad()
