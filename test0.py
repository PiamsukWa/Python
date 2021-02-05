numbers = [10, 20, 30, 40, 50, 60, 70]
sum = 0
for x in numbers:
    print(x, end =' ')
    sum += x

print('sum = ', sum)

names = ['Mateo', 'Danny', 'James', 'Thomas', 'Luke']
for i in range(0, len(names)):
    print(names[i].upper(), end =' ')