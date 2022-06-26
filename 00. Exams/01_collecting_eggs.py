def egg_not_fresh(egg):
    return egg <= 0


def wrapped_egg(sum, box):
    return sum <= box


from collections import deque

eggs = deque(int(x) for x in input().split(', '))
paper = [int(x) for x in input().split(', ')]
filled_box = 0
box_size = 50

while eggs and paper:
    current_egg = eggs.popleft()
    current_paper = paper[-1]
    current_sum = current_egg + current_paper

    if egg_not_fresh(current_egg):
        continue
    if current_egg == 13:
        paper[0], paper[-1] = paper[-1], paper[0]
        continue
    if wrapped_egg(current_sum, box_size):
        filled_box += 1
        paper.pop()
    else:
        paper.pop()

print(f"Great! You filled {filled_box} boxes." if filled_box > 0 else "Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if paper:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper)}")
