size = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(size)]

primary_diagonal = []
secondary_diagonal = []

for row_index in range(size):
    primary_diagonal.append(matrix[row_index][row_index])
    secondary_diagonal.append(matrix[row_index][size - 1 - row_index])
    
primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {secondary_sum}")
