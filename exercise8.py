#example1

for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')

#example2

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)
print('Done!')

#example3

count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)

average = sum / count

print('After', count, sum, average)
