from math import sqrt
x1, y1 = input('Give the first point x,y: ').split(',')
x2, y2 = input('GIve the second point x,y: ').split(',')

lenght = sqrt((int(x2) - int(x1)) ** 2 + (int(y2) - int(y1)) ** 2)
print(f'The lenght between your points is {lenght: .2f}.')
