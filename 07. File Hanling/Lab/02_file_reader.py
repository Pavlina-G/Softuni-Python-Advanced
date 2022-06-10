numbers = open('./numbers.txt', 'r')
sum = 0

for line in numbers:
    sum += int(line)

print(sum)