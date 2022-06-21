def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for i in range(2, n):
        triangle.append([1, ])

    for row in range(1, n - 1):
        for j in range(len(triangle[row]) - 1):
            current_num = triangle[row][j] + triangle[row][j + 1]
            triangle[row + 1].append(current_num)
        triangle[row + 1].append(1)

    return triangle


print(get_magic_triangle(5))
# output = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
