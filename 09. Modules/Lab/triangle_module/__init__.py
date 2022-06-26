from printing_line import print_line

def print_triangle(size):
    for i in range(size):
        print_line(i+1)
    for i in range(size-1, -1, -1):
        print_line(i)
