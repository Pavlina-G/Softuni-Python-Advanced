def stock_availability(boxes, command, *args):
    if command == 'delivery':
        for arg in args:
            boxes.append(arg)
    elif command == 'sell':
        if args:
            for arg in args:
                if isinstance(arg, int):
                    boxes = boxes[arg:]
                else:
                    if arg in boxes:
                        count_arg = boxes.count(arg)
                        [boxes.remove(arg) for _ in range(count_arg)]
        else:
            boxes = boxes[1:] if len(boxes) > 1 else []
    return boxes


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
