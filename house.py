
height = 5
width = 9

for i in range(height):
    print(' ' * (height - i - 1) + '*' * (2 * i + 1))

for i in range(height):
    print('*' + ' ' * (width - 2) + '*')

print('*' * width)
