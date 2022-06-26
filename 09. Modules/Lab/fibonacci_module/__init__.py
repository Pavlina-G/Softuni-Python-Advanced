result = []

def create_fibonacci_up_to_number(n):
    if result:
        result.clear()

    result.append(0)
    result.append(1)

    for i in range(n - 2):
        result.append(result[-1] + result[-2])
    return ' '.join(str(x) for x in result)

create_fibonacci_up_to_number(5)
def locate_number(n):
    if n in result:
        return result.index(n)

    return None

locate_number(3)
create_fibonacci_up_to_number(4)
locate_number(5)


